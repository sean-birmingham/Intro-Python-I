"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"


with open('./foo.txt', 'r') as myFile:
    readFile = myFile.read()
    print(readFile)

    # Open up a file called "bar.txt" (which doesn't exist yet) for
    # writing. Write three lines of arbitrary content to that file,
    # then close the file. Open up "bar.txt" and inspect it to make
    # sure that it contains what you expect it to contain


with open('bar.txt', 'w+') as newFile:
    newFile.write('Hello World! \nWelcome! \nHow are you?')
    newFile.close()

with open('./bar.txt', 'r') as myFile2:
    readFile2 = myFile2.read()
    print(readFile2)
