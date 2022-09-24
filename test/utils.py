from difflib import SequenceMatcher
from collections import Counter

a = "LWE41298"
b = "HIV09090"

listA = [a, b]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

listB = [b, a, a, b]

def common(list):
    data = Counter(list)
    return data.most_common(1)[0][0]

listC = [1, 2, 3]

# print(listC[-1])

queuelist = []
finallist = []

def evaluate(queuelist, finallist, input):
    if(len(queuelist) == 0):
        queuelist.append(input)
        return queuelist, finallist

    if(similar(queuelist[-1], input) > 0.5):
        queuelist.append(input)
        return queuelist, finallist
    else:
        finallist.append(common(queuelist))
        queuelist.clear()
        queuelist.append(input)
        return queuelist, finallist

# print(evaluate(queuelist, "123"))

while True:
    user_input = input("Input: ")
    if(user_input == "exit"):
        break
    else:
        print(evaluate(queuelist, finallist, user_input))