#Write Python script to create two text files. Enter data in each file and merge the data in the third file. (using function).

def merge(file1,file2,file3):
    f1=open(file1,"r")
    f2=open(file2,"r")
    f3=open(file3,"w")
    f3.write(f1.read())
    f3.write(f2.read())
    f1.close()
    f2.close()
    f3.close()
    print("File merged successfully")

file1=input("Enter first file name: ")
file2=input("Enter second file name: ")
file3=input("Enter third file name: ")
merge(file1,file2,file3)

