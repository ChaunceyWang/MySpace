#include <iostream>
#include <io.h>
#include <stdlib.h>
#include <string>
#include <vector>
/*
    Traverse a folder to get all speceifc type files!
    support any number of subfolders!


 **/
int  TraverseAllFiles(const std::string & OrigInputDir, const std::string &Type, std::vector<std::string> & AllFiles)
{
    string InputDir = OrigInputDir;
    if (InputDir.substr( InputDir.size()-1, 1) !="/" && InputDir.substr( InputDir.size()-1, 1 )!= "\\")
    {
        InputDir.append("/");
    }
     string ToFind = InputDir +"*";  //查找所有类型的
     struct _finddata_t  FindInfo;
     long handle = _findfirst(ToFind.c_str(), &FindInfo);
     if (-1 == handle) // empty ,nothing
     {
         return -1;
     }
     do 
     {
         //是一个目录
         if (_A_SUBDIR == FindInfo.attrib)
         {
             string Name =FindInfo.name;
             if (Name!="." && Name!="..") //不是本目录，也不是父目录
             {
                 string NextPath = InputDir +Name + "/";
                 //递归
                 RecursionAllFiles(NextPath, Type, AllFiles);
             }
         }
         else if (_A_ARCH == FindInfo.attrib || _A_NORMAL ==FindInfo.attrib || _A_RDONLY ==FindInfo.attrib)
         {
             string  ThisFileName =FindInfo.name;
             string FullName = InputDir +ThisFileName;
             int Loc=FullName.find_last_of(".");
             if (Type==FullName.substr(Loc+1, Type.size()))  //找到符合条件的目录，装入
             {
                 AllFiles.push_back(FullName);
             } 
         }
     } while (0 == _findnext(handle, &FindInfo));
     _findclose(handle);

    return 0;
}

int main(int argc, char *argv[])
{
    string  OrigInputDir = "D:/Pictures";
    string ImageTyep = ".tif" ; 
    vector<std::string>  RetFiles;
    TraverseAllFiles(OrigInputDir, ImageTyep, RetFiles);
    /*  next do something
        such as processing every image, Face Recognition!
    */
    
    return 0;
}