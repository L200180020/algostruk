 #1A
#def cekMatrix(matrix) :
#    panjang = len(matrix)
#    hasil = True
#    for x in matrix :
#        lebar = len(x)
#        if lebar != panjang:
#            hasil = False
#            break

#        for i in x:
#            if type(i) != int:
#                hasil = False
#               break
#    return hasil

#m1 = [[2,3],[4,5]]
#m2 = [[10,20],[5,6]]
#m3 = [[4,8,3],[2,"8",4],[3,6,9]]
#m4 = [[6,2,7],[2,8]]

#print("m1 =", cekMatrix(m1))
#print("m2 =", cekMatrix(m2))
#print("m3 =", cekMatrix(m3))
#print("m4 =", cekMatrix(m4))

 #1B
def Ukuran(matrix):
    return("Ukuran Matrix = "+ str(len(matrix))+ " x "+ str(len(matrix[0])))

m1 = [[2,3],[4,5]]
m2 = [[10,20,7],[5,6,3]]

print(Ukuran(m1))
print(Ukuran(m2))
