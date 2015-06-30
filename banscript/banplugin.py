#IP ban script

def returnState(ip):
    with open("banlist.txt","r"):
        for x in f.readlines():
            e = x.split("/")
            if e[0] == ip:
                return True
currentAccess =True
if returnState(argv[1]) == True:
    currentAccess = False

if currentAccess == True:
    return True
else:
    return False
