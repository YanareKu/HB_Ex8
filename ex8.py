"""
This is a program to read in 2 texts and create a markov chain. 
The data structures are a list as the value, a tuple as a key, and a dictionary
that they are nested in.
"""

from sys import argv
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    d = {}

    counter = 0

    while(counter != len(corpus) - 2):
        tup = ( corpus[counter], corpus[counter + 1] )
        val = corpus[counter + 2]
        if tup not in d:
            d[tup] = [val]
        else:
            d[tup].append(val)

        counter = counter + 1

    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    first_key = random.choice(chains.keys()) # original key selected randomly
    string_list = list(first_key)  
    key = first_key

    counter = 0

    while key in chains:

        #gives value. Value is a list
        value = chains[key]  

        #turns tuple into list
        key_to_list = list(key) 

        #picks random integer (for index) from 0 to length -1 uses it to
        #select an item from the list "value"
        value_from_list = value[random.randint(0, len(value)-1)]

        #takes list of keys and  merges with the randomly chosen value in a list.
        if counter == 0:
            string_list = [''] + string_list + [value_from_list]
        elif counter%11 == 0:
            string_list = string_list + ['\n']
        else:
            string_list = string_list + [value_from_list]

        #rebinds key to a tuple of the second item in list "key_to_list" and
        #item "value_from_list"
        key = (key_to_list[1], value_from_list)

        #limit output
        counter = counter + 1
        if counter > 300:
            break

    return string_list



def clean_string(filename):
    # Change this to read input_text from a file
    input_text = open(filename).read()
    split_corpus = input_text.split()
    return split_corpus


def main():
    script, filename = argv

    input_text = clean_string(filename)
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print ' '.join(random_text)

if __name__ == "__main__":
    main()