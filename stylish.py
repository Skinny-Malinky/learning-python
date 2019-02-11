text = "Ahmed is a stylish man"

# enumarate(words) => [(0, 'Ahmed') (1, 'is') (2, 'a')]
def stylish(a):
    words = a.split()
    for i, word in enumerate(words):
        if i < len(words)-1:
            print word, words[i+1]
        else:
            return

stylish(text)