from itertools import permutations
from PyDictionary import PyDictionary

def anagrams(word):
    d = PyDictionary()
    res = []
    for p in permutations(word):
        possibility = ''.join(p)
        
        if d.meaning(possibility, disable_errors=True):
            res.append(possibility)
    return res
        

if __name__ == '__main__':
    inp = input("Enter a string to find anagrams:\n")
    print(anagrams(inp))

