# trie_no_prefix

There is a given list of strings where each string contains only lowercase letters from , inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

Note If two strings are identical, they are prefixes of each other.

## Function Description

Complete the noPrefix function which has the following parameter(s):
* string words[n]: an array of strings

As a result print string(s): either GOOD SET or BAD SET on one line followed by the word on the next line. No return value is expected.

## Input Format
* First line contains `n`, the size of `words[]`.
* Then next `n` lines each contain a string, `words[i]`.

## Constraints
* 1 <= n <= 10^5
* 1 <= the length of words[i] <= 60
* All letters in `words[i]` are in the range 'a' through 'j', inclusive.
