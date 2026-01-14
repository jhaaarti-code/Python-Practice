# p = open(r'File_handling.py')
# print(p.read())

# r = open("Superman.txt", 'w')
# r.write("Hello this is aarti and i am writing inside this")
# r.close()

# r = open("Superman.txt", 'a')
# r.write("and now i am appending some content inside the file")
# r.close()

# file models in r,w,a,x

# r -: is used to read the file
#   -: file must already exist
#   -: if file not found error

# f = open("Superman.txt","r")
# print(f.read())
# f.close()

# w -: used to write new data in file
#   -: if file already exist old content gets deleted
#   -: if file doesn't exist new file will be created

# f = open("Superman.txt","w")
# f.write("Hello Aarti")
# f.close()

# a -: used to add new data at the end of the file
#   -: file exist add content at the end
#   -: file doesn't exist creates new file

# f = open("Superman.txt" , "a")
# f.write("/n this is a python program")
# f.close()

# x -: used to create a new file only
    # -: if file doesn't exist file will be created
    # -: if file already exist error
    
# f = open("file.txt","w")
# f.write("this is a new file")
# f.close()

#  now lets create a bsic file andling project