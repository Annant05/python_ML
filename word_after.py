data = open('para.txt')
lis_line = []
word_array = []
for line in data:
    line_filter = (line.upper()
                   .replace(",", "")
                   .replace("\"", "")
                   .replace(".", "")
                   .replace("(", "")
                   .replace(")", "")
                   .replace("\n", "")
                   .replace("-", " "))
    lis_line.append(line_filter.split(" "))

for split_words in lis_line:  # to prevent the exception of shallow copying
    for i in split_words:
        word_array.append(i)


# Consider the above code as declaration

def next_word_list(word):  # find the indexes of the given word
    count = 0
    indexes = []
    next_words = []

    while count != (len(word_array) - 1):
        if word.upper() == word_array[count]:
            indexes.append(count + 1)
        count += 1

    for i in indexes:
        next_words.append(word_array[i])
    return next_words  # return the list of next words


def no_of_times_in_list(lis):  # calculate the no of times a word appears after the given word
    word_ar = []
    count_array = []
    for i in lis:
        if i in word_ar:  # if word is already in list just skip it
            continue
        else:  # else the word is not in list so append it in the list with its corresponding
            # count using the list.count("Word") function
            word_ar.append(i)
            count_array.append(lis.count(i))
    return_lis = []  # return the list with its count attached to the word in this way
    #  {"Key" : ["word1__count", "word2__count","word3__count"]}
    for i in range(len(word_ar)):
        return_lis.append(word_ar[i] + "__" + str(count_array[i]))
    return return_lis


def no_of_times(dict_word):
    for key in dict_word.keys():
        # {"key" : [word1,word2,word3,word4 ]   to    {"Key" : ["word1__count", "word2__count","word3__count"]} }
        dict_word[key] = no_of_times_in_list(dict_word[key])
    return dict_word


word_dictionary = dict()
for i in word_array:
    word_dictionary[str(i)] = next_word_list(str(i))

new_dic = (no_of_times(word_dictionary.copy()))

for key in new_dic.keys():
    print("\n" + key)
    for elem in new_dic[key]:
        theword, count = elem.split("__")
        print(theword + "\t" + str(count))
