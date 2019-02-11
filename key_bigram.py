# Key bigram i.e. Ahmed is. Value is pos in sentence
# Dict looks something like:
# Ahmed is: 1
# is a: 2
# a stylish: 3
# stylish man: 4

text = "Ahmed is a stylish man"
keyValue = {}

# enumarate(words) => [(0, 'Ahmed') (1, 'is') (2, 'a')]
def stylish(a):
    words = a.split()
    for i, word in enumerate(words):
        if i < len(words)-1:
            key = word + " " + words[i+1]
            keyValue[key] = i
        else:
            print keyValue
            return

stylish(text)