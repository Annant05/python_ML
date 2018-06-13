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

for split_words in lis_line:
    for i in split_words:
        word_array.append(i)

        # Consider the above code as declaration


def next_word_list(word):
    count = 0
    indexes = []
    next_words = []

    while count != (len(word_array) - 1):
        if word.upper() == word_array[count]:
            indexes.append(count + 1)
        count += 1

    for i in indexes:
        next_words.append(word_array[i])
    return next_words


def no_of_times_in_list(lis):
    word_ar = []
    count_array = []
    for i in lis:
        if i in word_ar:
            continue
        else:
            word_ar.append(i)
            count_array.append(lis.count(i))
    return_lis = []
    for i in range(len(word_ar)):
        return_lis.append(word_ar[i] + "__" + str(count_array[i]))
    return return_lis


def no_of_times(dict_word):
    for key in dict_word.keys():
        dict_word[key] = no_of_times_in_list(dict_word[key])
    return dict_word


word_dictionary = dict()
for i in word_array:
    word_dictionary[str(i)] = next_word_list(str(i))
# print(word_dictionary)
new_dic = (no_of_times(word_dictionary.copy()))
# for i in new_dic:
#     print("\nWord is : " + i + "\t" + str(new_dic[i]))

for key in new_dic.keys():
    print("\n" + key)
    for elem in new_dic[key]:
        theword, count = elem.split("__")
        print(theword + "\t" + str(count))

# print("Word is : " + "THE" + "\t Count" + str(new_dic))
