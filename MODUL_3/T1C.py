k = [[4,7],[4,4]]
l = [[5,6],[7,8]]
m = [[1,3,9,9],[2,"x",4]]
n = [[3,24],[32,5],[31,5]]
o = [[2,3,3],[17,2,22]]
p = [[8,9,20],[1,2,3],[3,4,5]]

def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("ukuran beda")
        
print("nomer 1c")
jumlah(k,l)
jumlah(k,n)
