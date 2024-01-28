#Write a file handling program in python, which opens the file ‘report.txt’
#and write data into it. Use the seek() and tell() functions in python while
#reading the data from the file.

def write_data():
    with open('report.txt', 'w+') as f:
        f.write("Hello World")
        f.seek(0)
        print(f.tell())
        f.write("Hello World")
        f.seek(0)
        print(f.tell())
        f.write("Hello World")
        f.seek(0)
        print(f.tell())

def read_data():
    with open('report.txt', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    write_data()
    read_data()
