import sys

if __name__=="__main__":
    print("files: {}  {}".format(sys.argv[1],sys.argv[2]))
    f1 = open(sys.argv[1]).read().split("\n")
    f2 = open(sys.argv[2]).read().split("\n")

    for line in range(0,len(f1)):
        print("line {} ".format(line+1))
        line1 = f1[line]
        line2 = f2[line]
        print("lens:  line1={}  line2={}".format(len(line1),len(line2)))
        fi1 = line1.split(",")
        fi2 = line2.split(",")
        print("fields: {} {}".format(len(fi1),len(fi2)))
        for n in range(len(fi1)):
            if fi1[n] != fi2[n]:
                print("    field {}   {}!={}".format(n,fi1[n],fi2[n]))
        print("")

