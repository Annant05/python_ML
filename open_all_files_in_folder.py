from glob import glob

files = glob('*.txt')

for i in files:
    print(i)
    data = open(str(i))
    for line in data:
        print(line)
