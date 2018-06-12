import operator

data = open('para.txt')

lis_line = []
for line in data:
    lis_line.append(line.upper().replace(",", "").replace("\"", "").replace(".", "").split(' '))

for split_words in lis_line:
    words = dict()
    for i in split_words:
        words[i] = words.get(i, 0) + 1
    sorted_d = sorted((value, key) for (key, value) in words.items())
    print(sorted_d)
