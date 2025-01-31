import random

truths = []
dares = []


with open("questions/t.txt") as f:
    t = f.read().split("\n")
    i = 0
    rating = "PG"
    for text in t:
        temp = t[i].split("|")
        truths.append({})
        if len(temp) > 1:
            rating = temp[0]
            truths[i]["question"] = temp[1].strip()
        else:
            truths[i]["question"] = temp[0].strip()
        truths[i]["rating"] = rating
        i+=1

with open("questions/d.txt") as f:
    t = f.read().split("\n")
    i = 0
    rating = "PG"
    for text in t:
        temp = t[i].split("|")
        dares.append({})
        if len(temp) > 1:
            rating = temp[0]
            dares[i]["question"] = temp[1].strip()
        else:
            dares[i]["question"] = temp[0].strip()
        dares[i]["rating"] = rating
        i+=1

#print(t)
#print(d)
def truth():
    qID = random.randint(0, len(truths) - 1)
    return {
        "question": truths[qID]["question"],
        "id": qID,
        "rating": truths[qID]["rating"],
    }
def dare():
    qID = random.randint(0, len(dares) - 1)
    return {
        "question": dares[qID]["question"],
        "id": qID,
        "rating": dares[qID]["rating"],
    }
#print(tr())
#print(da())