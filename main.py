import sys
import urllib.request
from anagrams import FindAnagrams

words = urllib.request.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
search = FindAnagrams(words)

if sys.argv[1] == 'scramble':
    search.anagram(sys.argv[2])
