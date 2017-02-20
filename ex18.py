# this one is like your scripts with argv

def print_two(*argvs):
    arg1, arg2 = argvs
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# ok, that *argvs is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

# this one just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothing!"


print_two("Me", "You")
print_two_again("Me", "You")
print_one("Just me")
print_none()
