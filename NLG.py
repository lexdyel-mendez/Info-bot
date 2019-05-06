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
        key = ' '.join(words[index - context:index])
        if key in dictionary:
            dictionary[key].append(word)
        else:
            dictionary[key] = [word]

        index += 1
    return dictionary


def makestring(start, dictionary, length):
    startword = make_dictionary(start, 1)
    reference_words = random.choice(list(startword.keys())).split(' ')  # random starting words
    string = ' '.join(reference_words) + ' '

    for i in range(length):
        try:
            key = ' '.join(reference_words)
            newword = random.choice(dictionary[key])
            string += newword + ' '
            if (newword == '.'): break
            for word in range(len(reference_words)):
                reference_words[word] = reference_words[(word + 1) % len(reference_words)]
            reference_words[-1] = newword

        except KeyError:
            return string
    return string


def data_saver(eventDate, eventName, givenString):
    '''
    Saves the data into the textfile Saved_data for record keeping.
    :param eventDate: the given input as the date of the event
    :param eventName: the given input as the name of the event
    :param givenString: the string generated by the AI
    :return: None
    '''
    filepath = open('Saved_data.txt', 'a+')
    filepath.write('The date of the event is: ' + str(eventDate) +
                   '\nThe name of the event is: ' + str(eventName) +
                   '\nThe given string is: ' + str(givenString) + '\n\n'
                   )
    filepath.close()


def input_checker(question, valueName):
    '''
    Method that gets a question and return the value of the question
    If the value is N/A, it does not print anything.
    :param question: String holding the question that is going to be asked
    :param valueName: String holding the name of the value
    :return: value
    '''
    value = input(str(question) + ' (N/A if it does no apply) ')
    if value.upper() != 'N/A':
        print("The " + valueName + " is: " + value)
    return value


def input_date():
    '''
    Method that asks the user for the date of the event.
    :return: The event's date, only if its not N/A
    '''
    date = input_checker("What date is the event?", 'day of the event')
    return date

def input_event():
    '''
    Method in charge of asking the user for the topic of the event
    :return: The event
    '''
    event = input_checker("What's the name of the event?", "event")
    return  event


stringToOutput = ''         # Global variable that holds the string generated by the AI.


def interface(date):
    '''
    This method works with what happens with each
    input that is asked to the user.
    :param date: The input date given by the user.
    :return:None
    '''
    global stringToOutput
    words = read.read_file()
    startingWords = read.readStarting()
    rule = make_dictionary(words, 1)
    string = makestring(startingWords, rule, 30)
    if date != 'N/A':
        if '[date]' not in string:
            interface(date)
        else:
            string = string.replace('[date]', str(date))
            stringToOutput = string
            print(string)
    elif date.upper() == "N/A":
        if '[date]' in string:
            interface(date)
        else:
            stringToOutput = string
            print(string)


if __name__ == '__main__':
    givenDate = input_date()
    eventName = input_event()
    interface(givenDate)

    data_saver(givenDate, 'To be implemented', stringToOutput)
