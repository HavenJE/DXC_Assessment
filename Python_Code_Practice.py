
import re
import random
from collections import Counter


def changeWord():
    # word = input("Write a word of your choice here...\n")
    word = input()
    result = []

    counter = Counter(word)
    # print(word)
    for elem in counter.elements():
        if counter[elem] == 1:
            # print(elem, counter[elem])
            word = re.sub(elem, 'x', word, flags=re.IGNORECASE)
        else:
            word = re.sub(elem, 'y', word, flags=re.IGNORECASE)
    result.append(word)
    print(result[-1])


changeWord()


# def changeWord():
#     # word = input("Write a word of your choice here...\n")
#     words = ['please', 'case', 'Times']
#     result = []
#     # word = random.choice(words)

#     for elem in words:
#         word = elem
#         counter = Counter(elem)
#         for letter in counter.elements():
#             if counter[letter] == 1:
#                 word = re.sub(letter, 'x', word, flags=re.IGNORECASE)
#             else:
#                 word = re.sub(letter, 'y', word, flags=re.IGNORECASE)
#         result.append(word)
#     print(result[-1])


# changeWord()

# def changeWord():
#     # word = input("Write a word of your choice here...\n")
#     words = ['please', 'case', 'Times']

#     word = random.choice(words)

#     # print(word)

#     counter = Counter(word)
#     # print(counter)
#     # print(counter.elements())
#     for elem in counter.elements():
#         if counter[elem] == 1:
#             # print(elem, counter[elem])
#             word = re.sub(elem, 'x', word, flags=re.IGNORECASE)
#         else:
#             word = re.sub(elem, 'y', word, flags=re.IGNORECASE)
#         print(word)
#         # word2 = ''.join(word)
#         # for index, elem in enumerate(word2):
#         #     if index == len(word2) - 1:
#         #         print(elem)


# changeWord()
