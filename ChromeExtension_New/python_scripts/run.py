from fetch import main as fetch
import TextBlob
import pandas as pd
import numpy as np
import re
import os
#import sys

#def main(url=sys.argv[1], output_filename='temp/comments.csv'):
def run(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ', output_filename='temp/comments.csv'):
    sentiment_score = 0
    comments = fetch(url, output_filename)
    df = pd.read_csv(comments)
    df['sentiment'] = df['comment'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['subjectivity'] = df['comment'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    sentiment_score = (df['sentiment']*df['subjectivity']).mean()
    os.remove(output_filename)
    print(sentiment_score)
    #return sentiment_score

if __name__ == '__main__':
    #main()
    run()
