import shutil
import os
path=input("Enter the path of the folder")
days=time.time(30)

if(os.path.exists(path))
    fileslist=os.walk(path)
    for file in fileslist:
        os.path.join(path,file)
        status = os.stat(path)

        if(status.st_ctime>days)
            if(os.path.isfile(path)
                os.remove(path)

            elif(os.path.isdir(path))
                shutil.rmtree(path)

             else:
                print("Path does not exist")

       
