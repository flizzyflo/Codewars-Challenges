def bouncing_ball(initial, proportion, n=0):
    if initial<1000 and initial>1 and proportion>0 and proportion<1:
        while initial>1:
                initial=initial*proportion
                n+=1
        return n
    else:
        return None

print(bouncing_ball(3,0.5))