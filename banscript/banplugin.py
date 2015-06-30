#IP ban script

def returnState(ip):
    with open("banlist.txt","r"):
        for x in f.readlines():
            e = x.split("/")
            if e[0] == ip:
                return True

def Ban(ip):
    with open("banlist.txt", "a") as f:
        f.write(ip)
        f.close()

if argv[1] == "!ban":
    Ban(argv[2])
elif argv[2] == "check":
    if returnState(argv[2]) == True:
        return True
    else:
        return False
