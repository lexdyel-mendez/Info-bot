
import keras
import random
import re
import Read_file as read


def make_dictionary(words, context):
    """Creates a dictionary which will store all the words in the dataset and all the perceived next words
        Parameters: 
            words: an array of all (non unique) words  in the dataset
            context: quantity if words that the dictionary uses to create references"""
    dictionary = {}
    index = 0
 
    for word in words[index:]:
        key = ' '.join(words[index-context:index])
        if key in dictionary:
            dictionary[key].append(word)
        else:
            dictionary[key] = [word]
            
        index += 1
 
    return dictionary

def generate_text(dictionary, length):    
    oldwords = random.choice(list(dictionary.keys())).split(' ') #random starting words
    string = ' '.join(oldwords) + ' '
 
    for i in range(length):
        try:
            key = ' '.join(oldwords)
            newword = random.choice(dictionary[key])
            string += newword + ' '
 
            for word in range(len(oldwords)):
                oldwords[word] = oldwords[(word + 1) % len(oldwords)]
            oldwords[-1] = newword
 
        except KeyError:
            return string
    return string



if __name__ == '__main__':
    words = read.read_file()
    dictionary = make_dictionary(words,1)
    string = generate_text(dictionary, 30)
    print(string)
