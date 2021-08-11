#print ('Guess Im getting starting in this  bitch') 
#x = 7
#if x< 8:
# print('x isnt legal')
#else:
#    print('x is legal')


#x = input('Have you heard of our lord and saviour Aqua?')

#with open('Aquasbelievers.txt', 'r') as beliverList:
 # x =  beliverList.read()
#  print(x)

#with open( 'file4.txt', 'r') as myVar:


#with open('Padlist.txt', 'r') as padList:
 #   x = padList.readlines()
   # print(x)

with open('Ava Tar.txt', 'r') as myAva:
    lines = myAva.readlines()
    for attribute in lines:
        num = attribute.split(' ')[1]
        print(num)




