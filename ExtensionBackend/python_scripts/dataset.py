import os
import glob
import pandas as pd
from fetch import main as fetch
from tdqm import tdqm
import argparse

def main(urllist):
    # making a dataset from youtube videos
    dataset = pd.DataFrame()    

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-u', '--url', type=__path__, nargs='+', help='url list')
    args = parser.parse_args()

    if args.url:
        for i, url in enumerate(tdqm(urllist)): # urllist is a list of urls
            df = fetch(url)
            dataset = pd.concat(dataset, pd.read_csv(df))
    pd.save_csv(dataset, 'dataset/comments.csv')

if __name__ == '__main__':
    main()
