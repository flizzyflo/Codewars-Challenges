def encode(st):
    d={"a":"1", "e":"2" , "i":"3" , "o":"4", "u":"5"}
    for i in st:
        if i in d:
            st=st.replace(i,d[i])
    return st

def decode(st):
    d={"1":"a", "2":"e" , "3":"i" , "4":"o", "5":"u"}
    for i in st:
        if i in d:
            st=st.replace(i,d[i])
    return st
