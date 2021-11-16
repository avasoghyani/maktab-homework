password=input('enter the passwords:').split(',')
def valid(item):
    c1, c2, c3, c4 = 0, 0, 0, 0
    for i in item:
        if (i.isalpha()):
           c1 +=1
        if (i.isupper()):
           c2 += 1
        if (i.isdigit()):
           c3 +=1
        if (i=='@' or i=='$' or i=='_'):
            c4 += 1
    if( c1>=1 and c2>=1 and c3>=1 and c4>=1):
        print(item)

for item in password:
    if (5<len(item)<12) :
           valid(item)

#ava9474Ava,ava,Ava,ava234567,aVa@1234A



