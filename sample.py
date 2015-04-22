import trie
t=trie.Trie()
for word in file("words.txt"):
 	t.add_word_to_trie(word[:-1].lower())
print "suggestions for word starting with the - \n",t.search_prefix("the"),"\n"
print "total words starting with ind - ",t.count_word_with_prefix("the"),"\n"
print t.check_spelling("busnssmn"), "\n"
print t.search_word("businessman")