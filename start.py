import os,shutil,time
i=open(os.getcwd()+'//FilePath.txt','r',encoding='utf-8')
o=open(os.getcwd()+'//SavesPath.txt','r',encoding='utf-8')
inputting=i.read()
outputting=o.read()
a=True 
if os.path.exists(inputting):#判断文件是否存在
    pass
else:
    print('文件路径错误！请检查FilePath.txt内是否是正确且存在的路径！')
    a=False
if os.path.exists(outputting):
    pass
else:
    print('文件路径错误！请检查SavesPath.txt内是否是正确且存在的路径！')
    a=False
if a==False:
    input()
    exit()
else:
    outputting+='\\'+time.strftime("%Y_%m_%d %H.%M.%S")
    print('当前脚本运行的路径：'+str(os.getcwd())+'\n\n将文件夹：'+str(inputting)+'\n\n复制到：'+str(outputting)+'\n')
    print('确认后按下enter开始')
    input()
    print('拷贝开始\n')
    shutil.copytree(inputting,outputting)
    print('拷贝完成！')
    input()
