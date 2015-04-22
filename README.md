Trie
=======

Introduction
------------
This is an implementation of a trie. The code is written in Python 2.7. The code too implements **word suggestion** and **spell check** which are one of the famous implementation of trie. Other implementations include **text-segmentation**, **word search**, etc...

Trie is an important data structure for storing a dictionary and performing related operations. The time complexity of searching a word in trie is O(k), where k is length of the word.

See https://www.topcoder.com/community/data-science/data-science-tutorials/using-tries/ for more information about Trie Implementation.

######Functions:
* `add_word_to_trie(word)` - adds word to trie.
* `search_prefix(prefix)` - returns the list of all the words with given prefix (suggestion of words).
* `search_word(word)` - return true if the word exists in the trie, else false
* `count_word_with_prefix(prefix)`- retunrs the total number of words with given prefix
* `check_spelling(word)`- returns correct if spelling is correct (and word exists in trie) else return the list of suggested words.

I have used **words.txt** file to add words in trie in **sample.py**.
