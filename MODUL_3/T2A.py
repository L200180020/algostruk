def buatNol(n,m=None):
    if(m==None):
        m=n
    print("Membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for x in range(m)] for y in range(n)])
print("nomer 2a")
buatNol(3)
buatNol(5,3)
