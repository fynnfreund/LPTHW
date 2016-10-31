#two arguments
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#two arguments different form
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#no argument
def print_none():
    print "I got nothing."


print_two("Fynn","Freund")
print_two_again("Fynn","Freund")
print_one("First!")
print_none() 
