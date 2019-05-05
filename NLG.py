
import keras
import random
import re


def read_file():
    text=(open("/Users/maria/github/ArtInt/Dataset/Dataset.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    return words


def makerule(words, context):
    '''Make a rule dict for given data.'''
    rule = {}
    index = context
 
    for word in words[index:]:
        key = ' '.join(words[index-context:index])
        if key in rule:
            rule[key].append(word)
        else:
            rule[key] = [word]
        index += 1
 
    return rule

def makestring(rule, length):    
    '''Use a given rule to make a string.'''
    oldwords = random.choice(list(rule.keys())).split(' ') #random starting words
    string = ' '.join(oldwords) + ' '
 
    for i in range(length):
        try:
            key = ' '.join(oldwords)
            newword = random.choice(rule[key])
            string += newword + ' '
 
            for word in range(len(oldwords)):
                oldwords[word] = oldwords[(word + 1) % len(oldwords)]
            oldwords[-1] = newword
 
        except KeyError:
            return string
    return string



if __name__ == '__main__':
    words = read_file()
    rule = makerule(words,1)
    string = makestring(rule, 30)
    print(string)
