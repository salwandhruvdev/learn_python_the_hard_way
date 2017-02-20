from sys import argv
from os.path import exists

script, filename, to_file = argv

print "Copying from %s to %s" %(filename, to_file)

data_from_file = open(filename).read()

print "The input file is %d bytes long." % len(data_from_file)

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue or CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w').write(data_from_file)

print "Alright, all done."
