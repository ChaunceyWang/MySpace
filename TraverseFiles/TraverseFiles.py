#coding=utf-8
import os
import sys
import os.path

'''
 Traverse a folder to get all speceifc type files!
    support any number of subfolders!
'''
def depthTraverse(root,*FileType):
#root: paraent path; FileType: file extension,such as 'jpg', 'png'
   if ''== root.strip() or 0 == len(FileType):
      print '--- Input parameter is invalid ---\n'
      os._exit(-1)
   FileList =[]
   for dirpath, dirnames, filenames in os.walk(root):
     # print (dirpath, dirnames, filenames)
     for filename in filenames:
      # if os.path.splitext(filename)[1] == goalType:
      for Type in FileType:
         if filename.endswith(Type):
            filepath = os.path.join(dirpath, filename) 
            FileList.append(filepath)
   return FileList

if __name__ == '__main__':
    BsicPath = r'D:/Pictures/';
    FileList =  depthTraverse(BsicPath, 'jpg','tif')
    print FileList
