#!/usr/bin/env python
from string import punctuation
import operator
import pandas as pd


def WordCount(dataframe, country, column_str):
    '''
    This function do word count for a dataframe. It first group the dataframe
    based on the column with the country name, and then cat all the str stored
    in that country together, and perform a wordcount on the concatenated str.
    It returns a dictionary of all the word for each country.

    params: dataframe: the dataframe on which you want to perform wordcount
    params: country: the column on which the dataframe is grouped by
    params: column_name_str: the column in which the str is stored
    '''
    dic = {}
    UniqueNames = dataframe.country.unique()
    dic = {item: pd.DataFrame for item in UniqueNames}
    for key in dic.keys():
        dic[key] = dataframe[dataframe.country == key]
    dic2 = {}
    for p in dic.keys():
        dic2[p] = reduce(lambda x, y: x + y,
                         dic[p][column_str], '')
    wc = {}
    for k, v in dic2.iteritems():
        ls = dic2.get(k).lower().translate(None, punctuation).split(' ')
        freq = {}
        for word in ls:
            freq[word] = ls.count(word)
            sorted_freq = sorted(freq.items(), key=operator.itemgetter(1),
                                 reverse=True)
            wc[k] = sorted_freq
    return wc
