cnt = 0
user1 = input()
user2 = input()
user1_word_count = 0
user2_word_count = 0
user1_line_count = 0
user2_line_count = 0
with open ("template.txt",'r',encoding="utf-8") as read:
    temp = read.readlines()
    num = 0
    for line in temp:
        k = line.split('\t')
        for thing in k:
            if(thing == user1):
                num = 1
                user1_line_count += 1
                continue
            elif(thing == user2):
                num = 2
                user2_line_count += 1
                continue
            if(num == 1):
                num = 0
                user1_word_count += (len(thing)-1)
            if(num == 2):
                num = 0
                user2_word_count += (len(thing)-1)
print('user 1\'s word cnt is %d' %user1_word_count)
print('user 2\'s word cnt is %d' %user2_word_count)
print('user 1\'s line cnt is %d' %user1_line_count)
print('user 2\'s line cnt is %d' %user2_line_count)
