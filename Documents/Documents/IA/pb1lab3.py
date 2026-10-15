import math

a=[-0.4, 0, 0.2, 0.2,0.4]
def softmax(a):
    rezultat=[]
    for i in range(len(a)):
        exp_val=math.exp(a[i])
        sum_exp=0
        for j in range(len(a)):
            exp_val_j=math.exp(a[j])
            sum_exp+=exp_val_j
        rezultat.append(exp_val/sum_exp)

    return rezultat

print(softmax(a))