import shutil
import os
print()
print("\t\t\tWelcome to files manager!")
print()
print("____________________________________________________")
print("Example of folder path and extension")
print(r"1)FOLDER ------->  D:\newfolder\documents")
print(r"2)EXTENSION ----->  png ,pdf,docx,jpg,txt and others")
print("____________________________________________________")
def files_handler(folder1,extension,folder2):
    l=os.listdir(folder1)
    for i in l:
        if '.' in i:
            index=i.index(".")
            if i[index+1:]==extension:
                shutil.move(rf'{folder1}\{i}',folder2)
def main():
    folder1=input("Enter the path from where you want to move:")
    folder2=input("Enter the path of folder where you would be  moving:")
    extension=input("Enter the extension of file (like pdf or png):").lower()
    files_handler(folder1,extension,folder2)

main()