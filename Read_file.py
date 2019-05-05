import keras

def read_file():
    text=(open("/users/maria/github/artint/Dataset/Dataset.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    return words

def readStarting():
    text=(open("/users/maria/github/artint/Dataset/Greetings.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    return words
