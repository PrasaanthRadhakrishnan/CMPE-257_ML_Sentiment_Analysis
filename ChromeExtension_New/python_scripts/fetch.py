import argparse
import json
import pandas as pd

# pip install google-api-python-client
from apiclient.discovery import build
from csv import writer
from urllib.parse import urlparse, parse_qs

def get_keys(filename='key.txt'):
    with open(filename) as f:
        key = f.readline()
    DEVELOPER_KEY = key
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return {'key': key, 'name': 'youtube', 'version': 'v3'}

def build_service(filename='key.txt'):
    with open(filename) as f:
        key = f.readline()

    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return build(YOUTUBE_API_SERVICE_NAME,
                 YOUTUBE_API_VERSION,
                 developerKey=key)

# https://stackoverflow.com/questions/45579306/get-youtube-video-url-or-youtube-video-id-from-a-string-using-regex
def get_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]

def get_comments(service, video_id, output_filename):
    """
    https://python.gotrained.com/youtube-api-extracting-comments/#Cache_Credentials
    https://www.pingshiuanchua.com/blog/post/using-youtube-api-to-analyse-youtube-comments-on-python
    """
    output_dict = {}
    for i, video in enumerate(video_id):
        comment_threads_response = service.commentThreads().list(
            part = "snippet",
            videoId = video,
            textFormat = "plainText",
            maxResults = 100,
            order = "relevance"
        ).execute()
        comments = []
        for item in comment_threads_response["items"]:
            comment = item["snippet"]["topLevelComment"]
            comments.append(comment["snippet"]["textDisplay"])
        output_dict[video] = comments
        if i % 100 == 0:
            save_to_csv(output_dict, video_id, output_filename)
    
def save_to_csv(output_dict, video_id, output_filename):
    output_df = pd.DataFrame(output_dict, columns = output_dict.keys())
    output_df.to_csv(f'{output_filename}.csv')

def main(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ', output_filename='temp/comments.csv'):
    service = build_service()
    video_id = get_id(url)
    get_comments(service, video_id, output_filename)
    return output_filename

if __name__ == '__main__':
    main()