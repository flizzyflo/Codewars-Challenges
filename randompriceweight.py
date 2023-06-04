# n ist der rang desjenigen der gewinnen soll
# we ist die gewichtung der nummer eines einzelnen
# st sind die strings der vornamen
def rank(st, we, n, d_l=dict(), d_u=dict(), alph="abcdefghijklmnopqrstuvwxyz",sum=0):
    st=st.split(",")
    if len(st)==1:
        return "No participants"
    elif n>len(st) and len(st)>1:
        return "Not enough participants"
    elif len(we)>=len(st):
        alph_upper=alph.upper()
        for i,j in enumerate(alph):
            if j in d_l:
                continue
            else:
                d_l[j]=i+1
        for i,j in enumerate(alph_upper):
            if j in d_u:
                continue
            else:
                d_u[j]=i+1
        namelist=dict()
        for i in st:
            namelist[i]=0
            for j in i:
                if j in d_l:
                    namelist[i]+=d_l[j]+1
                elif j in d_u:
                    namelist[i]+=d_u[j]+1
            namelist[i]*=we[st.index(i)]
        return namelist
    else:
        return False


print(rank("Lagon,Lily", [1, 5], 1))