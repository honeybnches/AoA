from PIL import Image
from os import listdir,remove,getcwd
from os.path import join,exists
dih={}
cwd=join(getcwd(),"data","sprites","char")
for folder in listdir(cwd):
    for x in[x for x in listdir(join(cwd,folder)) if x.endswith(".png") and not x.startswith("xia") and not x.endswith("Atlas.png")]:
        dih[x]=Image.open(join(cwd,folder,x))

    w=32;h=64

    if exists(join(cwd,folder,folder+"Atlas.png")):remove(join(cwd,folder,folder+"Atlas.png"))
    if exists(join(cwd,folder,"Atlas.png")):remove(join(cwd,folder,"Atlas.png"))

    for i in dih:
        if dih[i].width!=w or dih[i].height!=h:
            print(dih[i])
            del dih[i]
    new_im = Image.new('RGBA',(288,2048),(255, 0, 0, 0))
    x_offset = 0;y_offset = 0;x_total=0
    tag=list(dih.keys())[0].split("_")[0]
    side=list(dih.keys())[0].split("_")[1]
    for i in dih:
        if i.split("_")[0] != tag or i.split("_")[1] != side:
            tag=i.split("_")[0]
            side=i.split("_")[1]

            y_offset+=h*2
            x_offset=0

        new_im.paste(dih[i], (x_offset,y_offset))
        new_im.paste(dih[i].transpose(Image.FLIP_LEFT_RIGHT), (x_offset,y_offset+h))
        x_offset += w

        if x_offset>x_total:
            x_total=x_offset
    y_total=y_offset
    new_im.save(join(cwd,folder,"Atlas.png"))
    dih={}