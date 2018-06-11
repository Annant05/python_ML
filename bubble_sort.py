# Bubble Sort
listtt = [5, 4, 8, 9, 1, 2, 0, 3]


def bubble_sort(lis):
    counts = 0
    prevsum = 0
    for i in range(int(len(lis) - 1)):
        for i in range(int(len(lis) - 1)):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                counts = counts + 1
                prevsum = prevsum + lis[i + 1]
                if counts == 1:
                    sums2 = lis[i] + lis[i + 1]
                    prevsum = sums2
                avgr = prevsum / 2
                print("Sum : " + str(prevsum) + "\t Average  : " + str(avgr) + "\t count : " + str(
                    counts) + "\t List : " + str(lis) + "\t Print Elem : " + str(lis[i + 1]))
    return lis


res = bubble_sort(listtt)
print("Sorted List  : " + str(res))
# print("Count : " + str(count))
