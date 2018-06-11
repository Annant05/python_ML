# TODO: Find word Frequency and most common word

data = open('para.txt')
lis_line = []
for line in data:
    lis_line.append(line.upper().replace(",", "").replace("\"", "").replace(".", "").split(' '))

for split1 in lis_line:
    print("WORD COUNT " + str(len(split1)))
    word_array = []
    count_array = []
    for i in split1:
        if i in word_array:
            continue
        else:
            word_array.append(i)
            count_array.append(split1.count(i))

    most_frequent_count = max(count_array)
    max_index = count_array.index(most_frequent_count)

    for i in range(int(len(word_array) - 1)):
        print(" The count : " + str(count_array[i]) + " \t\tAnd Word : " + word_array[i])

    print(word_array[max_index])
