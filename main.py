
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for i in word:
        if i in punctuation_chars:
            word = word.replace(i, "")
    return word


def get_neg(word):
    global negative_words
    word = word.split()
    positive_word = 0
    for i in word:
        k = strip_punctuation(str.lower(i))
        if k in negative_words:
            positive_word = positive_word + 1
    return positive_word


def get_pos(word):
    global positive_words
    word = word.split()
    positive_word = 0
    for i in word:
        k = strip_punctuation(str.lower(i))
        if k in positive_words:
            positive_word = positive_word + 1
    return positive_word


res = open("resulting_data.csv", "w")
tweets = list()

with open("project_twitter_data.csv") as pos_f:
    x = 0
    for i, line in enumerate(pos_f):
        if x == 0:
            x = x + 1
            res.write(
                "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score ""\n")
            continue
        temp_string_line = line.strip()
        temp_list_line = temp_string_line.split(",")
        pos = get_pos(temp_list_line[0])
        neg = get_neg(temp_list_line[0])
        num_tweets = temp_list_line[1]
        num_rep = temp_list_line[2]
        res.write(num_tweets+","+num_rep + "," +
                  str(pos)+","+str(neg)+","+str(pos-neg)+"\n")
