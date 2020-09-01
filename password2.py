import random

wordlist=[]
spl_char=['@','#','$','%','&','*']

with open('wiki.txt','r')as file:
    data=file.readlines()

    for line in data:
        word=line.split()

        for item in word:
            if len(item)>5:
                wordlist.append(item.capitalize())
word=random.choice(wordlist)
schr=random.choice(spl_char)
num=str(random.randint(10,100))
paswd=word+schr+num
print(paswd)