import shutil, os

for i in range(200):
    path= './randomBox'+str(i)
    os.mkdir(path)
    os.chdir('./'+path)
    for j in range(200):
        fileName='flag'+str(j)+'.c'
        file= open(fileName,'w')
        file.write('#include<stdio.h> \n int main(){ \nprintf("this is flag: '+str(j)+' "); \n} '   )
        file.close()
    os.chdir('..')
print(os.path.abspath(path))


































