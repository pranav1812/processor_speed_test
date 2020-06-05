import os, hashlib, time
from itertools import permutations

startTime=time.time()
answer= "you are doing great but take care of the order"
toMatch= hashlib.md5(answer.encode()).hexdigest()


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


print(found)
matched= False
count =0
for perm in permutations(found):
    permStr= ' '.join(perm)
    permHash= hashlib.md5(permStr.encode()).hexdigest()

    if toMatch==permHash or permStr=="":
        print('matched answer: '+permStr)
        matched= True
        break
    else:
        count+=1
        # print(count,'perms checked')


if not matched:
    print('nothing matched, check the code ')

endTime=time.time()
print(endTime-startTime,'seconds elapsed')