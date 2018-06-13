data = open('para.txt')
lis_line = []
for line in data:
    lis_line.append(line.upper().replace(",", "").replace("\"", "").replace(".", "").split(' '))
for split_words in lis_line:
    words = dict()
    for i in split_words:
        words[i] = words.get(i, 0) + 1
    for key in sorted(words.keys()):
        print("%s: %s" % (key, words[key]))
    print("-------------------Second Task----------------------")
    for key, value in sorted(words.items(), key=lambda item: (item[1], item[0])):
        print("%s: %s" % (value, key))
    # sorted_d = sorted((value, key) for (key, value) in words.items())
    # print(sorted_d)
