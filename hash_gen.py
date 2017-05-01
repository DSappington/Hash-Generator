from hashlib import md5


iname = 'data.txt'
oname = 'hashed.txt'

with open(iname, 'r') as ifile:
    with open(oname, 'w') as ofile:
        for line in ifile:
            line = line.rstrip()
            digest = md5(line).hexdigest()
            ofile.write(line+"\t"+digest+"\n")
    print"Brute.py Finished"

    print("----------------------------------")
    print"How many hashes are you looking for? \n"
    input = int(raw_input())
    print("----------------------------------")

    for x in range(0,input):
        print("----------------------------------")
        print"Enter the hash:  \n\n"
        finder = raw_input()
        print("----------------------------------")

        for line in open("data.txt"):
            if finder in line:
             print "Found! \n" + line
    ofile.close()
