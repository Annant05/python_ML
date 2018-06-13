data = open('para.txt')
lis_line = []
word_array = []
for line in data:
    lis_line.append(
        line.upper().replace(",", "")
            .replace("\"", "")
            .replace(".", "")
            .replace("(", "")
            .replace(")", "")
            .replace("\n", "").split(' '))

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


word_dictionary = dict()
for i in word_array:
    word_dictionary[str(i)] = next_word_list(str(i))
# print(word_dictionary)
for i in word_dictionary:
    print("Word is : " + i + "\tNext word :  " + str(word_dictionary[i]))
