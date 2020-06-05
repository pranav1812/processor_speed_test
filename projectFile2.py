import os, random
from hashlib import md5

answer= "you are doing great but take care of the order"
hashval= md5(answer.encode()).hexdigest()
print(hashval)
keys=answer.split()

selected_folders=[]
for i in range(len(keys)):
    selected_folders.append(random.randrange(0,200,1))

for i in range(len(selected_folders)):
    os.chdir('./randomBox'+str(selected_folders[i]))
    selected_file= random.randrange(0,200,1)
    fileName='flag'+str(selected_file)+'.c'
    file=open(fileName,'a')
    file.write('//here\'s one key : '+keys[i])
    file.close()
    print('inserted a key in box number:'+str(selected_folders[i])+'\'s file number: '+str(selected_file))
    os.chdir('..')
print('done')