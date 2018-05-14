#!usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import re
import enchant
from nltk.corpus import wordnet
from random import randint
import nltk as nltk




"""
  Requires:
    *Running setup1.py in linux (&&) and in your python3 virtual env will set all this up for you*
  	Manual setup:
  	install - nltk
  	install - python3
  	install - PyEnchant
  	In your python3 shell type these to download needed data sets:
  	>>>import nltk
  	>>>nltk.download('wordnet')
  	>>>nltk.download('punkt')
  	>>>nltk.download('averaged_perceptron_tagger')
  	noun responses -- requires script1 as sys.argv
  	verb responses -- requires script2 as sys.argv
  	yes responses -- requires script3
    questionable -- script4
"""





class Wiwa(object):
	def __init__(self):
		self.nounscript = sys.argv[1]
		self.verbscript = sys.argv[2]
		self.simplescript = sys.argv[3]
		self.questionable = sys.argv[4]
		self.dictionary = enchant.Dict("en_US")

	def run_wiwa(self):
		intro = """ Welcome to the whispering wall, Wiwa is here to respond
		and question your perspective. She is just a program, and
		will respond according to her script.
		If you wish to stop program, type EXIT or QUIT.
		Have fun! """
		print(intro)
		make = input("..>>")
		while make not in ['EXIT', 'QUIT']:
			make = make.lower()
			nouns, verbs, adj, adv, errors = self.make_tag_lists(make)
			n = len(nouns)
			v = len(verbs)
			aj = len(adj)
			av = len(adv)
			er = len(errors)
			question = self.check_question(make)
			if question:
				# Maybe use simple script for these too?
				print("Wiwa:")
				discusanswer = self.get_script_line(self.questionable)
				print(discusanswer)
			elif make in ['yes', 'no', 'maybe']:
				response = self.get_script_line(self.simplescript)
				print("Wiwa:")
				print(response)
			elif n < 1 and v < 1 and er > 0:
				print(f" I do not know this: {errors[0]}, is the cat on the keyboard?")
			elif n > 0:
				response = self.get_script_line(self.nounscript)
				print("Wiwa:")
				print(response % nouns[0])
			elif v > 0:
				response = self.get_script_line(self.verbscript)
				print("Wiwa:")
				print(response % verbs[0])
			elif aj > 0:
				print("Wiwa:")
				print(f"Is being {adj[0]} a good thing?")
			elif av > 0:
				print("Wiwa:")
				print(f"I wish I could do it {adv[0]}")
			else:
				print("Wiwa: I do not comprehend")
			make = input("...>>")

	def get_script_line(self, arg):
		with open(arg) as f:
			for i, l in enumerate(f):
				pass
			count = i
		if count != None:
			with open(arg) as f:
				lines = f.readlines()
				x = randint(0, count)
				return lines[x]

	def strip_stop_words(self, arg):
		stops = ['the', 'of', 'he', 'she', 'it', 'some', 'all', 'a', 'lot',
				'have', 'about', 'been', 'to', 'too', 'from', 'an', 'at',
				'above', 'before', 'across', 'against', 'almost', 'along', 'aslo',
				'although', 'always', 'am', 'among', 'amongst', 'amount', 'and',
				'another', 'any', 'anyhow', 'anyone', 'anything', 'around', 'as',
				'be', 'maybe', 'being', 'beside', 'besides', 'between', 'beyond', 'both',
				'but', 'by', 'can', 'could', 'done', 'during', 'each', 'either',
				'else', 'even', 'every', 'everyone', 'everything', 'everywhere',
				'except', 'few', 'for', 'had', 'has', 'hence', 'here', 'in', 'into', 'is',
				'it', 'its', 'keep', 'last', 'latter', 'many', 'may', 'more', 'most',
				'much', 'name', 'next', 'none', 'not', 'nothing', 'now', 'nowhere',
				'often', 'other', 'others', 'over', 'rather', 'perhaps', 'seems', 'then',
				'there', 'these', 'they', 'though', 'thru', 'too', 'under', 'until',
				'upon', 'very', 'was', 'were' 'which', 'while', 'will', 'with', 'ill', 'lets']
		new_arg = []
		for item in arg:
			if item in stops:
				pass
			else:
				new_arg.append(item)
		#print(new_arg)
		return new_arg

	def make_tag_lists(self, arg):
	#With string as arg, return lists of Adj, adv, noun, verb
	#    Empty lists mean no found type-noun(verb, adv, adj)
		clean_arg, errors = self.clean_string(arg)
		tokens = nltk.word_tokenize(clean_arg)
		tags = nltk.pos_tag(tokens)
		nouns = []
		verbs = []
		adj = []
		adv = []
		for item in tags:
			x = item[1]
			#print(item)
			if x == ("VB"):
				verbs.append(item[0])
			elif x.startswith("NN"):
				nouns.append(item[0])
			elif x.startswith("JJ"):
				adj.append(item[0])
			elif x.startswith("RB"):
				adv.append(item[0])
			else:
				pass
		nouns = self.strip_stop_words(nouns)
		verbs = self.strip_stop_words(verbs)
		adj = self.strip_stop_words(adj)
		adv = self.strip_stop_words(adv)
		return nouns, verbs, adj, adv, errors

	def clean_string(self, astring):
		""" Take the string and clear out all irrelevant data.
		Goal: to identify main verbs and nouns, any adjectives, adverbs
		Only tag words that are in the PyEnchant English dictionary. """
		astring = str(astring)
		#astring = astring.lower() put in main _run_wiwa loop
		#print(astring)
		newstring = re.sub("[^a-zA-Z| |]+", "", astring)
		stringlist = newstring.split()
		cleaned = ""
		errors = []
		for word in stringlist:
			if self.enchant_check(word) == True:
				cleaned = cleaned + word + " "
			else:
				#print(f"word not found {word}")
				errors.append(word)

		return cleaned, errors

	def enchant_check(self, arg):
		""" using the PyEnchant English dictionary to check validity of a word."""
		x = self.dictionary.check(arg)
		return x

	def check_question(self, arg):
		questions = ['why', '?']
		if questions[0] in arg or questions[1] in arg:
			return True
		else:
			return False





new_wiwa = Wiwa()
new_wiwa.run_wiwa()
