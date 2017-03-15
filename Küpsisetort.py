from math import ceil, floor

pikkus = input("Sisestage tordi pikkus küpsistes: ")
laius = input("Sisestage tordi laius küpsistes: ")
korgus= input("Sisestage tordi kõrgus küpsistes: ")
tkPakis = input("Sisestage mitu küpsist on pakis: ")

def pakke ():
    tkArv = int(pikkus)*int(laius)*int(korgus)
    pakid = tkArv/int(tkPakis)
   # print("Sul on vaja "+ str(round(pakid+0.49))+" pakki")
    print("Sul on vaja "+ str(ceil(pakid))+" pakki")

pakke()