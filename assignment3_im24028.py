import random

#trials
t=10000

#S be the sample space.
S=[['b','b'],['r','b'],['r','r']]

#counter
i=0
j=0

for z in range(t):
    a=random.randint(0,2)
    b=random.randint(0,1)
    if S[a][b]=='r':           #Randomly selecting the card
        i+=1
        if S[a]==['r','b']:    #Checking for the desired result
            j+=1

print("The Probability is ",j/i)

