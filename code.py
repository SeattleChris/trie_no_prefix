#!/bin/python3

import math
import os
import random
import re
import sys

FAIL = "BAD SET"
GOOD = "GOOD SET"

class Node:
    def __init__(self):
        self.children = [None] * 10  # a through j
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def add_no_pre(self, key):
        curr = self.root
        at_beg = True
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Node()
                at_beg = False
            curr = curr.children[index]
            if at_beg and curr.isEndOfWord:
                return False
        curr.isEndOfWord = True
        return not at_beg
            
    def _search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False, curr
            curr = curr.children[index]
        return True, curr        

    def match(self, key):
        success, curr = self._search(key)
        return success and curr.isEndOfWord

    def is_prefix(self, key):
        success, curr = self._search(key)
        return success

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    tree = Trie()
    for word in words:
        if not tree.add_no_pre(word):
            return word
    return True
    
    
if __name__ == '__main__':
    n = int(input().strip())
    words = []
    for _ in range(n):
        words_item = input()
        words.append(words_item)
    result = noPrefix(words)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    if result is True:
        fptr.write(GOOD + '\n')
    else:
        fptr.write(FAIL + '\n')
        fptr.write(result + '\n')
    fptr.close()
