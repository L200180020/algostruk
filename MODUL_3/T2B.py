def buatIdentitas(n):
    print("Membuat matriks Identitas dengan ordo"+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])

print("nomer 2b")
buatIdentitas(7)
buatIdentitas(3)
