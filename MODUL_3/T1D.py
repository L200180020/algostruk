k = [[4,7],[4,4]]
l = [[5,6],[7,8]]
m = [[1,3,9,9],[2,"x",4]]
n = [[3,24],[32,5],[31,5]]
o = [[2,3,3],[17,2,22]]
p = [[8,9,20],[1,2,3],[3,4,5]]

def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("tidak memenuhi syarat")
print("nomer 1d")
zz = [[1,2,3],[1,2,3]]
zx = [[1],[2],[3]]
kali(zz,zx)
kali(k,l)
kali(k,o)
kali(k,zx)
