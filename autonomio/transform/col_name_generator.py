from string import ascii_lowercase
import itertools


def col_name_generator(data):

    '''Column Name Generator

    WHAT: A helper function that generates alphabetic
    column names automatically.

    HOW: col_name_generator(df)

    INPUT: A pandas dataframe

    OUTPUT: The input dataframe with alphabetical sequence
    column names.

    '''

    l = []

    for i in xrange(no_of_cols):

        l.append(prefix+str(i))

    data.columns = l

    return data
