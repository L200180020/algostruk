def swap(A,p,q):
    tmp=A[p]
    A[p]=A[q]
    A[q]=tmp
    
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil=i
    return posisiTerkecil
