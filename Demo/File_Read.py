f = open ('word_list.txt','r')
line=" "
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
#
