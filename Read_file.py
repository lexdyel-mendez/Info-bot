import keras

def read_file():
    text=(open("Dataset/Labeled_Dataset.txt", encoding = "utf-8-sig").read().lower())
    #text=(open("Dataset/Labeled_Dataset.txt", encoding = "utf-8-sig").read().lower())
    text = text.replace('.',' .')
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-/:;<=>?@\\^_`{|}~\t\n', lower=True, split=' ')
    return words

def readStarting():
    text=(open("Dataset/Greetings.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    return words
