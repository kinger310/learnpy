import pandas as pd
import numpy as np
from collections import defaultdict
import sys


def find_frequent_itemsets(favorable_reviews_by_user, last_itemsets, min_support):
    counts = defaultdict(int)
    for user, reviews in favorable_reviews_by_user.items():
        for itemset in last_itemsets:
            if itemset.issubset(reviews):
                for other_reviewed_movie in reviews - itemset:
                    current_superset = itemset | frozenset((other_reviewed_movie, ))
                    counts[current_superset] += 1
        return dict([(itemset, frequency) for itemset, frequency in counts.items() if frequency >= min_support])


def main():
    df_ratings = pd.read_csv(r'D:\ProgramFiles\PycharmProjects\datamine\ml-latest-small\ratings.csv')
    df_movies = pd.read_csv(r'D:\ProgramFiles\PycharmProjects\datamine\ml-latest-small\movies.csv')

    df_ratings['timestamp'] = pd.to_datetime(df_ratings['timestamp'], unit='s')
    df_ratings['favorable'] = df_ratings['rating'] > 3

    favorable_ratings = df_ratings[df_ratings['favorable']]

    favorable_reviews_by_user = dict((k, frozenset(v.values))
                                     for k, v in favorable_ratings.groupby('userId')['movieId'])

    favorable_num_by_movie = df_ratings[['movieId', 'favorable']].groupby('movieId').sum().reset_index()

    frequent_itemsets = {}
    min_support = 2
    frequent_itemsets[1] = dict((frozenset((x.movieId,)), x.favorable) for x in favorable_num_by_movie.itertuples() if
                                x.favorable > min_support)
    for k in range(2, 20):
        cur_frequent_itemsets = find_frequent_itemsets(favorable_reviews_by_user, frequent_itemsets[k-1], min_support)
        frequent_itemsets[k] = cur_frequent_itemsets
        if len(cur_frequent_itemsets) == 0:
            print("Did not find any frequent itemsets of length {0}".format(k))
            sys.stdout.flush()
            break


if __name__ == '__main__':
    main()
