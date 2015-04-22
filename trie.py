import sys
class Node(object):
	def __init__(self):
		self.char = ''
		self.word = ''
		self.is_end = False
		self.prefix_count = 0
		self.child = {}


class Trie(object):
	def __init__(self):
		self.root=Node()

	def get_all_words(self, current, words):
		if current.is_end:
			words.append(current.word)
		for i in current.child:
			self.get_all_words(current.child[i], words)
		return words

	def print_trie(self, current):
		print current.char, current.is_end, current.prefix_count
		if current.is_end:
			print current.word," "*2,"\\"
		for i in current.child:
			self.print_trie(current.child[i])
	
	def add_word_to_trie(self, word):
		current = self.root
		current.prefix_count+=1
		for key in word:
			try:
				if current.child[key]:
					pass
			except:
				current.child[key] = Node()
			current = current.child[key]
			current.char = key
			current.prefix_count+=1
		current.is_end = True
		current.word = word

	def search_word(self, pref):
		current = self.root
		for key in pref:
			try:
				current = current.child[key]
			except:
				return False
		if current.is_end:
			return True
		else:
			return False
	
	def search_prefix(self, pref):
		current = self.root
		for key in pref:
			try:
				current = current.child[key]
			except:
				return False
		return self.get_all_words(current,[])

	def count_word_with_prefix(self, pref):
		current = self.root
		for key in pref:
			try:
				current = current.child[key]
			except:
				return False
		return current.prefix_count

	def check_spelling(self, word):
		if self.search_word(word):
			return "correct"
		suggestions = self.search_prefix(word[:len(word)/3])
		if suggestions!=False:
			return suggestions
		else:
			return "No suggestions"
