
import keras
import random
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

def makestring(start, rule, length):    
    startword = make_dictionary(start, 1)
    oldwords = random.choice(list(startword.keys())).split(' ') #random starting words
    print(oldwords)
    string = ' '.join(oldwords) + ' '
 
    for i in range(length):
        try:
            key = ' '.join(reference_words)
            newword = random.choice(dictionary[key])
            string += newword + ' '
 
            for word in range(len(reference_words)):
                reference_words[word] = reference_words[(word + 1) % len(reference_words)]
            reference_words[-1] = newword
 
        except KeyError:
            return string
    return string



if __name__ == '__main__':
    words = read.read_file()
    startingWords = read.readStarting()
    rule = make_dictionary(words,1)
    string = makestring(startingWords, rule, 30)
    print(string)
