from sys import argv

#unpacks the argument variable
script, filename = argv

#the variable "txt" is set to open the filename "ex_sample.txt"
txt = open(filename)

#prints the name of the file the user typed in
print "Here's your file %r:" % filename
# prints out the content of the file. txt holds the content. ".read()" reads it out
print txt.read()

print "Type the filename again:"
#file_again is set to the input from the user after ">"
file_again = raw_input("> ")

#txt_again is set to open the "file_again", which is the file the user typed in
txt_again = open(file_again)

#txt now holds the content of the file and ".read()" reads it out now 
print txt_again.read()
