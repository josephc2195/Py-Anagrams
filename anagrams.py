from collections import defaultdict

class FindAnagrams:
    def __init__(self, words):
        webster = defaultdict(list)
        for word in words:
            webster[tuple(sorted(word))].append(word)
    def anagram(self, search):
        for ana in webster.values():
            if ana == search:
                print([x.decode() for x in ana])
