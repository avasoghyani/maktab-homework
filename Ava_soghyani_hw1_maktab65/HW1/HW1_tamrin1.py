
def add(key,value):
    if key in dict.keys():
        print('you enter the wrong key!')
    else:
        dict.update({key:value})
        print('added successfully.')
    return dict

def remove(key,value):
    if key in dict.keys():
        if value==dict.get(key):
            dict.pop(key)
            print('removed successfully')
        else:
             print('enter the wrong value!')

    return dict


dict = {}

for i in range (5):
    action = input('please entet the action most be done:')
    key=input('enter the key:')
    value=input('enter the value:')
    if action == 'add':
         add(key,value)
    if action == 'remove':
        remove(key,value)
print(dict)



