# After using AntiDupl or TreeSize Duplicate remover, paste all dirs to this flat location. this will pack them into their original folders
import os
prog=[]
inhr=[]
delete=[]
for f0 in [ x for x in os.listdir() if os.path.isdir(x)]:
    prog.append(f0)
    for f1 in [ x for x in os.listdir(f0) if os.path.isdir(x)]:
        inhr.append(os.path.join(f0,f1))

for f0 in prog:
    for f1 in inhr:
        if f0==f1.split("\\")[-1]:
            for file in os.listdir(f0):
                os.rename(os.path.join(f0,file),os.path.join(f1,file))
            print(f0+" ---> "+f1)
    if len(os.listdir(f0))==0:
        delete.append(f0)

                
for d in delete:
    os.rmdir(d)