k = [[4,7],[4,4]]
l = [[5,6],[7,8]]
m = [[1,3,9,9],[2,"x",4]]
n = [[3,24],[32,5],[31,5]]
o = [[2,3,3],[17,2,22]]
p = [[8,9,20],[1,2,3],[3,4,5]]

def determinanHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determinanHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinannya, karena bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinannya, karena bukan matrix bujursangkar"
    return total


q = [[3,1],[2,5]]
r = [[1,2,1],[3,3,1],[2,1,2]]
s = [[1,-2,0,0],[3,2,-3,1],[4,0,5,1],[2,3,-1,4]]
t = [[10,23,45,12,13],[1,2,3,4,5],[1,2,3,4,6],[4,2,3,4,8],[1,4,5,6,10]]

print("nomer 1e")
print(determinanHitung(q))
print(determinanHitung(r))
print(determinanHitung(s))
print(determinanHitung(t))
print(determinanHitung(n))
print(determinanHitung(o))

