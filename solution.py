import os, hashlib, time
from itertools import permutations

startTime=time.time()
toMatch='611d6663e938213f9643144650180a8d'

toCheck="here's one key :"

found=[]
for i in range(200):
    os.chdir('./randomBox'+str(i))

    for j in range(200):
        with open('flag'+str(j)+'.c', 'r') as file:
            data= file.readlines()
            for line in data:
                lineAsList= line.split()
                if ':' in lineAsList:
                    found.append(lineAsList[-1])
    os.chdir('..')


print(len(found))
matched= False
count =0
for perm in permutations(found):
    permStr= ' '.join(perm)
    permHash= hashlib.md5(permStr.encode()).hexdigest()

    if toMatch==permHash:
        print('matched answer: '+permStr)
        matched= True
        break
    else:
        count+=1
        print(count,'perms checked')


if not matched:
    print('nothing matched, check the code ')

endTime=time.time()
print(endTime-startTime,'seconds elapsed')