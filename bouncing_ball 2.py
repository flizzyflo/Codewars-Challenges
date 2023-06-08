def bouncing_ball(h, proportion, hwindow, n=1):
    if h>0 and proportion>0 and proportion<1 and hwindow<h:
        h=h*proportion
        while h>hwindow:
            h=h*proportion
            n+=2
        return n
    else:
        return -1

print(bouncing_ball(30, 0.66, 1.5))