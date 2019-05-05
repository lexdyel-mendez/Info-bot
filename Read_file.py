import keras

def read_file():
    text=(open("/users/maria/github/ArtInt/Dataset/Dataset.txt", encoding = "utf-8-sig").read().lower())
    words = keras.preprocessing.text.text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\]^`{|}~\t\n', lower=True, split=' ')
    return words