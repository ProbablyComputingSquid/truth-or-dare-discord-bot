import random

t = []
d = []

with open("questions/t.txt") as f:
    t = f.read().split("\n")
with open("questions/d.txt") as f:
    d = f.read().split("\n")

#print(t)
#print(d)
def tr():
    return t[random.randint(0, len(t) - 1)] + "?"
def da():
    return d[random.randint(0,len(d) - 1)]
#print(tr())
#print(da())