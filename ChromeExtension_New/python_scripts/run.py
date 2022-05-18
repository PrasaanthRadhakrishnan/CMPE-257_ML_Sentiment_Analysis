# TextBlob installation needs 2 steps: 
# 1. pip install -U textblob
# 2. python3 -m textblob.download_corpora

from fetch import main as fetch
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import os
#import sys


#def main(url=sys.argv[1], output_filename='temp/comments.csv'):
def run(url='https://www.youtube.com/watch?v=YbJOTdZBX1g', output_filename='temp/comments.csv'):
    sentiment_score = 0
    comments = fetch(url, output_filename)

    df = pd.read_csv(comments)
    df['sentiment'] = df['comment'].apply(lambda x: TextBlob(x).sentiment.polarity)
    sentiment_score = df['sentiment'].mean()
    print(sentiment_score)
    # return sentiment_score

if __name__ == '__main__':
    #main()
    run()
