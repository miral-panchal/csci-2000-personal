def has_no_e(line):
    ePresent = False;
    for i in line:
        if (i == 'e'):
            ePresent = True
            break
    return ePresent


user_input = input("Enter a line.")
found=has_no_e(user_input)


if(found == True):
    print('An "e" was found')
else:
    print('There was no "e" found')
    

file= open('gadsby.txt','r')

for each_line in file:
    new_found=False
    new_found=has_no_e(each_line)
    if(new_found == True):
        break
    
if(new_found == True):
    print('An "e" was found in the file')
else:
    print('There was no "e" found in the file')