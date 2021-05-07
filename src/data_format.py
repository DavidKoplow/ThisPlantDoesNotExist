import shutil, glob, os


path="C:/Users/Administrator/Documents/GitHub/data"
saved={}
for root, dirs, files in os.walk(path):
    for file in files:
        #if(not (file.endswith(".jpg") or file.endswith(".txt"))):
        #    print(file)
        if(file.endswith(".jpg")):
            saved[file[:-4]]=True

#print(saved)
#delete extra txt files
for root, dirs, files in os.walk(path):
    for file in files:
        if(file.endswith(".txt")):
            n=file[:-4]
            if(not n in saved):
                #print("rm unmatched txt: "+file)
                os.remove(os.path.join(root,file))



#remove folders with no images in it
for root, dirs, files in os.walk(path, topdown=False):   
    for dir in dirs:
        if os.path.isdir(os.path.join(root, dir)):
            if (len(os.listdir(os.path.join(root, dir))) == 0):
                #print("rm empty dir: "+dir)
                os.rmdir(os.path.join(root, dir))

#Put all images and text files into dalle training folder

path2="C:/Users/Administrator/Documents/GitHub/data_train"
for root, dirs, files in os.walk(path):
    for file in files:
        #print("cp file to new dir: "+file)
        shutil.copy(os.path.join(root,file),path2)