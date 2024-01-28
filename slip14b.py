#Write a python program to fully reverse the contents of file and write it in another file

f=open("file1.txt","r")
f1=open("file2.txt","w")
data=f.read()
data=data[::-1]
f1.write(data)
f.close()
f1.close()

f=open("file2.txt","r")
print(f.read())
f.close()
