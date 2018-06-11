# TODO: Find word Frequency and most common word

data = open('para.txt')
lis_line = []
for line in data:
    lis_line.append(line.upper().replace(",", "").replace("\"", "").replace(".", "").split(' '))

for split1 in lis_line:
    print("WORD COUNT " + str(len(split1)))
    wordarray = []
    countarray = []
    for i in split1:
        if i in wordarray:
            continue
        else:
            wordarray.append(i)
            countarray.append(split1.count(i))

    most_frequent_count = max(countarray)
    max_index = countarray.index(most_frequent_count)

    for i in range(int(len(wordarray) - 1)):
        print(" The count : " + str(countarray[i]) + " \t\tAnd Word : " + wordarray[i])

    print(wordarray[max_index])
