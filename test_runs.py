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
for i in lis_line:
    print(i)
