#!usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import re
import enchant
from nltk.corpus import wordnet
import nltk as nltk
import random
import os



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
      Scripts for responses should be in same directory as wiwa_class.py
"""





class Wiwa(object):
    def __init__(self):
        self.fileDirectory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.nounscript = os.path.join(self.fileDirectory, 'script1.txt')
        self.verbscript = os.path.join(self.fileDirectory, 'script2.txt')
        self.simplescript = os.path.join(self.fileDirectory, 'script3.txt')
        self.questionable = os.path.join(self.fileDirectory, 'script4.txt')
        self.adjectives = os.path.join(self.fileDirectory, 'script5.txt')
        self.adverbs = os.path.join(self.fileDirectory, 'script7.txt')
        self.dictionary = enchant.Dict("en_US")
        self.noun_script_order = create_script_line_order(self.nounscript)
        self.verb_script_order = create_script_line_order(self.verbscript)
        self.simple_script_order = create_script_line_order(self.simplescript)
        self.question_script_order = create_script_line_order(self.questionable)
        self.adj_script_order = create_script_line_order(self.adjectives)
        self.adv_script_order = create_script_line_order(self.adverbs)
        self.scripts_list = [self.nounscript, self.verbscript, self.simplescript, self.questionable, self.adjectives, self.adverbs]
        self.line_get = 0

    def test_filePath(self):
        #files_list = [self.nounscript, self.verbscript, self.simplescript, self.questionable, self.adjectives, self.adverbs]
        for script in self.scripts_list:
            try:
                with open(script) as f:
                    printable = str(script)
                    print(printable)
                    print("SUCCESS")
            except Exception as e:
                print(e)

    def test_variables(self):
        print("collection of script orders:")
        print("--------- nouns ---------")
        print(self.noun_script_order)
        print("--------- verbs ---------")
        print(self.verb_script_order)
        print("---------simple----------")
        print(self.simple_script_order)
        print("--------questions--------")
        print(self.question_script_order)
        print("-------adjectives--------")
        print(self.adj_script_order)
        print("--------adverbs----------")
        print(self.adv_script_order)
        print("line_get, integer:")
        print(self.line_get)

    def test_responses(self):
        for script in self.scripts_list:
            result = self.get_script_line(script)
            string_result = str(result)
            print(result)

    def run_wiwa(self):
        intro = """ Welcome to the whispering wall, Wiwa is here to respond
        and question your perspective. She is just a program, and
        will respond according to her script.
        If you wish to stop program, type EXIT or QUIT.
        Have fun! """
        print(intro)
        make = input("..>>")
        while make not in ['EXIT', 'QUIT']:

            choice = self.pick_response(make)
            #print(choice)
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
            else:
                if choice[0] == 'noun':
                    response = self.get_script_line(self.nounscript)
                    print("Wiwa:")
                    if '%' in response:
                        print(response % choice[1])
                    else:
                        print(response)
                elif choice[0] =='verb':
                    response = self.get_script_line(self.verbscript)
                    print("Wiwa:")
                    if '%' in response:
                        print(response % choice[1])
                    else:
                        print(response)
                elif choice[0] == 'adv':
                    response = self.get_script_line(self.adverbs)
                    print("Wiwa:")
                    if '%' in response:
                        print(response % choice[1])
                    else:
                        print(response)

                elif choice[0] == 'adj':
                    response = self.get_script_line(self.adjectives)
                    print("Wiwa:")
                    if '%' in response:
                        print(response % choice[1])
                    else:
                        print(response)
                else:

                    print("Wiwa:  ... ... ")
            make = input("...>>")


    def get_script_line(self, arg):
        """ Chooses a random script line to give back to user """
        # is often not random *sad face*
        #print(self.line_get)
        order = None
        for script in self.scripts_list:
            if script == arg:
                if arg.endswith('script1.txt'):
                    order = self.noun_script_order
                    break
                elif arg.endswith('script4.txt'):
                    order = self.question_script_order
                    break
                elif arg.endswith('script2.txt'):
                    order = self.verb_script_order
                    break
                elif arg.endswith('script3.txt'):
                    order = self.simple_script_order
                    break
                elif arg.endswith('script5.txt'):
                    order = self.adj_script_order
                    break
                elif arg.endswith('script7.txt'):
                    order = self.adv_script_order
                    break
            else:
                pass

        else:
            order = None
        if order != None:
            if self.line_get >= len(order):
                self.line_get = 0
            get_line = order[self.line_get]
            with open(arg) as f:
                lines = f.readlines()
                x = int(get_line)
                #print(lines[x])
                self.line_get += 1
                return lines[x]

        else:
            message = """
            script file could not be located:
            Original text file names should be one of the following:
            script1.txt, script2.txt, script3.txt, script4.txt, script5.txt, script7.txt
            """
            print(message)
            return None

    def pick_response(self, raw_input):
        """ Create lists of possible valid words for response mechanism,
            Then uses random to choose one to send back to run_wiwa() """
        make = raw_input.lower()
        nouns, verbs, adj, adv, errors = self.make_tag_lists(make)
        n = len(nouns)
        v = len(verbs)
        aj = len(adj)
        av = len(adv)
        er = len(errors)
        words_found = False
        options = {'noun': [], 'verb': [], 'adj': [], 'adv': [], 'err': []}
        if n > 0:
            words_found = True
            for item in nouns:
                options['noun'].append(item)
        if v > 0:
            words_found = True
            for item in verbs:
                options['verb'].append(item)
        if aj > 0:
            words_found = True
            for item in adj:
                options['adj'].append(item)
        if av > 0:
            words_found = True
            for item in adv:
                options['adv'].append(item)
        if er > 0:
            words_found = True
            for item in errors:
                options['err'].append(item)
        done = False
        if words_found == True:
            while not done:
                word_type = random.choice(list(options.keys()))
                word_list = options[word_type]
                if len(word_list) > 0:
                    choice_tup = (word_type, word_list[0])
                    done = True
                    return choice_tup
        else:
            return ('error', 'not identified')

    def strip_stop_words(self, arg):
        stops = ['i','the', 'of', 'he', 'she', 'it', 'some', 'all', 'a', 'lot',
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
        """ Use nltk to tag words for Wiwa to recycle and or respond too """
        # Now that this is working I'll have to make her an adjective and adverb script!
        errors = self.check_errors(arg)
        tokens = nltk.word_tokenize(arg)
        tags = nltk.pos_tag(tokens)
        clean_tags = self.remove_bad_tags(tags)
        #print("cleaned tags=", clean_tags)
        nouns = []
        verbs = []
        adj = []
        adv = []
        errors = []
        for item in clean_tags:
            x = item[1]
            #print(item)
            if x.startswith("VB"):
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

    def check_errors(self, arg):
        """ Make a list of words that are not found with pyEnchant"""
        errors = []
        for item in arg:
            if self.enchant_check(arg):
                pass
            else:
                errors.append(item)
        return errors


    def remove_bad_tags(self, tags_list):
        """ Use pyEnchant to remove unidentifiable words from tags list"""
        new_tags = []
        for item in tags_list:
            word = item[0]

            if self.enchant_check(word):
                new_tags.append(item)
            else:
                pass
                #print("word is not found:", word)

        return new_tags

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


def create_script_line_order(somescript):
    """ make a list with randomized order of line numbers from script
        not sure if this is worth all the work yet. Must be a better way."""
    # get count:
    count = None
    #print(somescript)
    if somescript.endswith('.txt'):
        try:
            with open(somescript) as f:
                for i, l in enumerate(f):
                    pass
                    count = i
        except:
            print("file is Empty.")
            raise ValueError
    else:
        print("***file is not a txt file***")
        print("\t file=", somescript)
        raise ValueError
    if count != None:
        first_list = []
        # create a list with all line numbers in it
        for x in range(1, i):
            first_list.append(x)
        # shuffle those items:
        random.shuffle(first_list)
    return first_list




new_wiwa = Wiwa()
new_wiwa.run_wiwa()


#########  tests #########
#### check if filePaths are being created properly
#new_wiwa.test_filePath()
#### check that all self.attributes are being created successfully
#new_wiwa.test_variables()
#### check that responses are being generated from the files:
#new_wiwa.test_responses()
