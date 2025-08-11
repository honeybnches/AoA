import os
from os import listdir,makedirs,rename
from os.path import splitext, isfile,join
wipe=False
if wipe:
    for folder in [x for x in listdir() if not isfile(x) and x.startswith("spr")]:
        print(folder)
        for image in [x for x in listdir(folder)]:
            print("|----"+image)
            rename(join(folder,image),image)
for img in [x for x in listdir() if x.endswith((".png",".jpg","jpeg")) and isfile(x) and x.startswith("sprite")]:  
    os.rename(img, img.removeprefix("sprite"))   

with open("renamed","a+") as log:
    s="_"
    for img in [x for x in listdir() if x.endswith((".png",".jpg","jpeg")) and isfile(x) and x.startswith("spr_")]:
        img2=None
        split=splitext(img)
        ext=split[-1]
        points=split[0].split(s)
        folder=points[1]
        action=points[2]
        for point in points:
            ind=points.index(point)
            if len(point)==2:
                point.translate({"lu":"nw","ld":"sw","ru":"ne","rd":"se"})
                points[ind]=point
        pDirect=True
        if len(points)==5:
            direction=points[3]
            slide=points[4]
            img2=action+s+direction+s+slide+ext
        else:
            for point in points:
                if point in ["nw","sw","ne","se"]:
                    pDirect=False
        if pDirect:
            points.insert(-1,"sw")
            img2= points[2]
            for point in points[3:]:
                img2=img2+s+point   
            img2=img2+ext         
        if len(points)==2:print("["+img+","+folder+"\\"+img2+"]")
        if img2!=None:
            None
            os.makedirs(folder,exist_ok=True)
            print("["+img+","+folder+"\\"+img2+"]")
            os.rename(img,points[1]+"\\"+img2)
            log.write("["+img+","+folder+"\\"+img2+"]")


