def word_occur(word):
    count = 0
    indexes = []
    while count != len(word_array):
        if word.upper() == word_array[count]:
            indexes.append(count)
        count += 1
    print(indexes)


data = open('para.txt')
lis_line = []
for line in data:
    lis_line.append(line.upper().replace(",", "").replace("\"", "").replace(".", "").split(' '))

word_array = []
for split_words in lis_line:
    for i in split_words:
        word_array.append(i)

word_occur("an")

# print("WORD COUNT " + str(len(split_words)))
# word_array = split_words.copy()
# word_after = []
# count = 1
# print(word_array[9])
# while count != len(split_words):
#     if word_array[]
#
#     count +=1
