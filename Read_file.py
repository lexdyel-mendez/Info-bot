import keras

def read_file():
    text=(open("/home/eduardo/github/AI_NLG/Info-bot/Dataset/Dataset.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_wordsequence(text, filters='!"#$%&()*+,-./:;<=>?@[\]^`{|}~\t\n', lower=True, split=' ')
    return words