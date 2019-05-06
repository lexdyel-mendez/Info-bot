import keras

def read_file():
<<<<<<< HEAD
    text=(open("/home/eduardo/github/AI_NLG/Info-bot/Dataset/Labeled_Dataset.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
=======
    text=(open("Dataset/Labeled_Dataset.txt", encoding = "utf-8-sig").read().lower())
   #text=(open("Dataset/Labeled_Dataset.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@\\^_`{|}~\t\n', lower=True, split=' ')
>>>>>>> f26a2477a8f5880c4b9d21079b59087d9261a23f
    return words

def readStarting():
    text=(open("/home/eduardo/github/AI_NLG/Info-bot/Dataset/Greetings.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    return words
