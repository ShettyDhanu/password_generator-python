import random
upper_char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'
            'V','W','X','Y','Z']
low_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'
            'v','w','x','y','z']
num=['1','2','3','4','5','6','7','8','9']
spl_char=['@','#','$','%','&','*']
password= random.choice(upper_char)+random.choice(low_char)+random.choice(num)+random.choice(spl_char)+ \
          random.choice(upper_char)+random.choice(low_char)+random.choice(num)+random.choice(spl_char)
print(password)