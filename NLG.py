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

def makestring(start, dictionary, length):
    startword = make_dictionary(start, 1)
    reference_words = random.choice(list(startword.keys())).split(' ') #random starting words
    string = ' '.join(reference_words) + ' '

 
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

def input_check():
    date = input("What date is the event? (N/A if it doesnt apply)")
    print("The event is in "+ date)
    date = ' ' + date + ' '
    return date

def interface(date):
    words = read.read_file()
    startingWords = read.readStarting()
    rule = make_dictionary(words, 1)
    string = makestring(startingWords, rule, 14)
    if date != ' N/A ':
        if '[date]' not in string:
            interface(date)
        else:
            string = string.replace(' [date] ', str(date))
            print(string)
    elif date == " N/A ":
        if '[date]' in string:
            interface(date)
        else:
            print(string)


if __name__ == '__main__':
    givenDate = input_check()
    interface(givenDate)