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

# queuelist = []
# finallist = []

# def evaluate(queuelist, finallist, input):
#     if(len(queuelist) == 0):
#         queuelist.append(input)
#         return queuelist, finallist

#     if(similar(queuelist[-1], input) > 0.5):
#         queuelist.append(input)
#         return queuelist, finallist
#     else:
#         finallist.append(common(queuelist))
#         queuelist.clear()
#         queuelist.append(input)
#         return queuelist, finallist

# # print(evaluate(queuelist, "123"))

# while True:
#     user_input = input("Input: ")
#     if(user_input == "exit"):
#         break
#     else:
#         print(evaluate(queuelist, finallist, user_input))


# queuelist = []
# finallist = []

# def evaluate(queuelist, finallist, input):
#     if(len(queuelist) == 0):
#         queuelist.append(input)
#         return queuelist, finallist

#     if(similar(queuelist[-1], input) > 0.5):
#         queuelist.append(input)
#         return queuelist, finallist
#     else:
#         finallist.append(common(queuelist))
#         queuelist.clear()
#         queuelist.append(input)
#         return queuelist, finallist

# # print(evaluate(queuelist, "123"))

# while True:
#     user_input = input("Input: ")
#     if(user_input == "exit"):
#         break
#     else:
#         print(evaluate(queuelist, finallist, user_input))

###
mainlist = []


def eval(mainlist, input):
    if(len(mainlist) == 0):
        mainlist.append(input)
        return mainlist

    if(type(mainlist[-1]) == list and similar(mainlist[-1][-1], input) > 0.5):
        mainlist[-1].append(input)
        return mainlist

    if(similar(mainlist[-1], input) < 0.5):
        if(type(mainlist[-1]) == list):
            last_element = mainlist.pop()
            mainlist.append(common(last_element))
        mainlist.append(input)
        return mainlist

    if(type(mainlist[-1]) != list and similar(mainlist[-1], input) > 0.5):
        last_element = mainlist.pop()
        innerlist = []
        innerlist.append(last_element)
        innerlist.append(input)
        mainlist.append(innerlist)
        return mainlist


def eval_exit(mainlist):
    if(type(mainlist[-1]) == list):
        last_element = mainlist.pop()
        mainlist.append(common(last_element))
        return mainlist
    else:
        return mainlist

while True:
    user_input = input("Input: ")
    if(user_input == "exit"):
        print(eval_exit(mainlist))
        break
    else:
        print(eval(mainlist, user_input))
