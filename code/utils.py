import re
import unicodedata

from sacremoses import MosesPunctNormalizer

# Utility functions
def delete_value_from_vector(vector, value):
    '''Delete a given value from a vector.

    To be used only when the value is in the vector.
    '''
    if value in vector:
        vector = [el for el in vector if el != value]
        # vector.remove(value)
        return vector
    else:
        raise ValueError('The asked value is not in the vector.')

def text_to_line(raw_text, empty=True):
    r'''Split a raw text into a list of sentences (string) according to '\n'.'''
    split_text = re.split('\n', raw_text)
    if ('' in split_text) and empty: # To remove empty lines
        return delete_value_from_vector(split_text, '')
    else:
        return split_text

def line_to_word(raw_line):
    '''Split a sentence into a list of words (string) according to whitespace.'''
    return re.split(' ', raw_line)

def deduplicate_list(original_list):
    '''Remove duplicates from a list, while keeping the original order.'''
    return list(dict.fromkeys(original_list))

def remove_excessive_whitespace(string):
    '''Remove excessive whitespace.'''
    return re.sub(' +', ' ', string)


# Handling text files
class Text:
    '''Basic processing of a text file.
    
    Parameters
    ----------
    file_path : string
        Path to the file
    empty : bool
        Empty lines are removed if True (default: True)

    Attributes
    ----------
    raw_file : string
        Text as a character string
    split_file : list of strings [string]
        Text converted into a list of sentences
    n_sent : integer
        Number of sentences in the text
    '''
    def __init__(self, file_path, empty=True):
        self.raw_file = open(file_path, 'r').read()
        self.pp_file = self.simple_preprocess()

        self.split_file = text_to_line(self.pp_file, empty=empty)
        self.n_sent = len(self.split_file)
        unique_sent = set(self.split_file)
        print(f'There are {self.n_sent} sentences ({len(unique_sent)} unique sentences).')
    
    def simple_preprocess(self):
        '''Applying Unicode normalisation and spliting sentences.'''
        normalised_text = unicodedata.normalize('NFC', self.raw_file)
        # Punctuation normalisation
        # normalised_text = punctuation_normalisation(normalised_text)
        return simple_preprocessing(normalised_text)

# Simple preprocessing
def simple_preprocessing(text):
    '''Apply preprocessing on the original text.'''
    new_text = punctuation_normalisation(text)
    new_text = remove_excessive_whitespace(new_text)
    return new_text.strip()

# Pre-processing punctuation
mpn = MosesPunctNormalizer(lang='en')
mpn.substitutions = [
    (re.compile(r), sub) for r, sub in mpn.substitutions
]

def punctuation_normalisation(sent):
    return mpn.normalize(sent).strip()

# Save text file
def save_file(text, path):
    '''Save a text file in the desired path.'''
    with open(path, 'w', encoding = 'utf8') as out_text:
        out_text.write(text)
