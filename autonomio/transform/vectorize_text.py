import spacy as sp
from ascify import Ascify


def vectorize_text(data, language='en', ascifying=True):

    '''Text Vectorizer
    
    INPUT: a SERIES with string values

    OUTPUT: a list of lists with the word vectors in lists

    USE EXAMPLE:  vectors = vectorize_text(list_with_strings)


    '''

    nlp = sp.load(language)
    nlp.parser.model  # to confirm that the parser loaded ok

    c = len(data)

    l = []

    for i in range(c):

        if ascifying == True:
            temp_string = Ascify(str(data[i:i+1])).ascify()
        else:
            temp_string = str(data[i:i+1])

        uni_string = unicode(temp_string)
        vec_obj = nlp(uni_string)
        vector = vec_obj.vector
        l.append(vector)

    return l

# Returns a list with 300 columns when succesful
