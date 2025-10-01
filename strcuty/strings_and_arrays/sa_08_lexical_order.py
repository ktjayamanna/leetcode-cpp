# Lexical Order
# Sort strings in lexicographical order

"""
PROBLEM DESCRIPTION:
================================================================================

Write a function, lexical_order, that takes in 2 words and an alphabet string as an argument. The function should return True if the first word should appear before the second word if lexically-ordered according to the given alphabet order. If the second word should appear first, then return False.

Note that the alphabet string may be any arbitrary string.

Intuitively, Lexical Order is like "dictionary" order:

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

(In lexical studies, shorter string is always before a longer string if all else is equal).

EXAMPLES:
================================================================================
alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("apple", "dock", alphabet) # -> True

alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("apple", "ample", alphabet) # -> False

alphabet = "abcdefghijklmnopqrstuvwxyz"
lexical_order("backs", "backdoor", alphabet) # -> False

alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("zoo", "dinner", alphabet) # -> True

alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("leaper", "leap", alphabet) # -> False

alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("backs", "backdoor", alphabet) # -> True

alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("semper", "semper", alphabet) # -> True

alphabet = "ghzstijbacdopnfklmeqrxyuvw"
lexical_order("semper", "semper", alphabet) # -> True


COMPLEXITY:
================================================================================
n = length of shorter string
Time: O(n)
Space: O(1)

"""

# SOLUTION:
# ================================================================================
def lexical_order(word_1, word_2, alphabet):
  length = max(len(word_1), len(word_2))
  for i in range(length): 
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
    if value_1 < value_2:
      return True
    elif value_2 < value_1:
      return False
  return True
