#!usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import re
#import enchant  #Remove enchant for windows, will not install easily
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
      install - PyEnchant (Windows 10 fails to load pyEnchant)
      *  if you can't use pyenchant, there is a nltk function to check words *
      Areas where enchant is removed are marked with ## !!!!!!!! lines
      In your python3 shell type these to download needed data sets:
      >>>import nltk
      >>>nltk.download('wordnet')
      >>>nltk.download('punkt')
      >>>nltk.download('averaged_perceptron_tagger')
      Scripts for responses should be in same directory as wiwa_class.py
"""





class Wiwa(object):
    def __init__(self):
        self.fileDirectory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.nounscript = os.path.join(self.fileDirectory, 'script1.txt')
        self.verbscript = os.path.join(self.fileDirectory, 'script2.txt')
        self.simplescript = os.path.join(self.fileDirectory, 'script3.txt')
        self.questionable = os.path.join(self.fileDirectory, 'script4.txt')
        self.adjectives = os.path.join(self.fileDirectory, 'script5.txt')
        self.errorscript = os.path.join(self.fileDirectory, 'script6.txt')
        self.adverbs = os.path.join(self.fileDirectory, 'script7.txt')
        ## NEW--
        self.aboutNellie = os.path.join(self.fileDirectory, 'script8.txt')
        self.about_index = 0
        self.about_list = []
        self.aboutWiwa = os.path.join(self.fileDirectory, 'script9.txt')
        self.about_W_index = 0
        self.about_W_list = []
        ## -----
## !!!!!!!!! ----
        #self.dictionary = enchant.Dict("en_US") #<-- Removed for windows
## !!!!!!!  ----

        self.noun_script_order = create_script_line_order(self.nounscript)
        self.verb_script_order = create_script_line_order(self.verbscript)
        self.simple_script_order = create_script_line_order(self.simplescript)
        self.question_script_order = create_script_line_order(self.questionable)
        self.adj_script_order = create_script_line_order(self.adjectives)
        self.err_script_order = create_script_line_order(self.errorscript)
        self.adv_script_order = create_script_line_order(self.adverbs)
        self.scripts_list = [self.nounscript, self.verbscript, self.simplescript, self.questionable, self.adjectives, self.errorscript, self.adverbs]
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
        print("------  errors  ---------")
        print(self.err_script_order)
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
        self.about_list = self.create_about_list()
        self.about_W_list = self.create_about_W_list()
        print(intro)
        
        make = input("..>>")
        while make not in ['EXIT', 'QUIT']:
            stripped = make.lower()
            make = re.sub("[^a-zA-Z| |]+", "", stripped)

            choice = self.pick_response(make)
            #print(choice)
            question = self.check_question(make)
            about_me = self.check_for_name(make)
            about_wiwa = self.check_for_name_wiwa(make)
            greet = self.is_greeting(make)
            if greet:
                print("Wiwa: Greetings human!")



            elif about_me != False:
                print("Wiwa:")
                response = self.get_about_line()
                print(response)


            elif question:
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

                elif choice[0] == 'err':
                    response = self.get_script_line(self.errorscript)
                    print("Wiwa:")
                    if '%' in response:
                        print(response % choice[1])
                    else:
                        print(response)

                elif about_wiwa != False:
                    print("Wiwa:")
                    response = self.get_about_W_line()
                    print(response)

                else:
                    print("Wiwa:  ... ... ")

            make = input("...>>")

    ## NEW Greetings---

    def is_greeting(self, user_input):
        greetings = [
        'hiya', 'howdy', 'hello', 'greetings',
        'aloha', 'yo', 'salutations', 'hi'
        ]
        if len(user_input) == 0:
            return True

        else:
            if type(user_input) == str:
                alist = user_input.split()
                for word in alist:
                    if word in greetings:
                        return True
                    else:
                        pass
        return False





    def create_about_list(self):
        """
        Get the lines in the text file to respond when input includes creator's name
        """
        about_list = []
        try:
            with open(self.aboutNellie) as f:
                lines = f.readlines()

                for line in lines:
                    #print(line)
                    self.about_list.append(line)
        except:
            print(f"file at : {self.aboutNellie} could not be opened.")

        finally:
            return self.about_list

    def create_about_W_list(self):
        """
        Get lines from script9 for input that includes reference to Wiwa.
        """
        about_list = []
        try:
            with open(self.aboutWiwa) as f:
                lines = f.readlines()

                for line in lines:
                    #print(line)
                    self.about_W_list.append(line)
        except:
            print(f"file at : {self.aboutWiwa} could not be opened.")

        finally:
            return self.about_W_list

    def get_about_line(self):
        """
        The about Nellie script is supposed to go in order.
        It is not randomized and responses are only dependant on the
        user refering to the words 'nellie', 'tobey' or 'creator' in an input.
        script lines are to be put in a list, and incremented through.
        Once the end of the list is reached, we start over.
        """
        max = len(self.about_list) - 1
        if self.about_index > max:
            self.about_index = 0

        line = self.about_list[self.about_index]
        self.about_index += 1
        return line

    def get_about_W_line(self):
        """
        The about Wiwa script is supposed to go in order.
        It is not randomized and responses are only dependant on the
        user refering to the words 'wiwa', 'you' in an input.
        script lines are to be put in a list, and incremented through.
        Once the end of the list is reached, we start over.
        """
        max = len(self.about_W_list) - 1
        if self.about_W_index > max:
            self.about_W_index = 0

        line = self.about_W_list[self.about_W_index]
        self.about_W_index += 1
        return line

    def check_for_name(self, arg):
        """
        check the user input for key words that trigger the about
        me script.  script8.txt.
        """
        if len(arg) == 0:
            return "I'm just a wall, you can talk to me."
        else:
            arg = arg.lower()
            me = ['nellie', 'creator', 'tobey']
            found = False
            for item in me:
                if item in arg:
                    #self.get_about_line()
                    found = True
                else:
                    pass
            return found

    def check_for_name_wiwa(self, arg):
        """
        check the user input for key words that trigger the about
        Wiwa script.  script9.txt.
        """
        if len(arg) == 0:
            return "I'm just a wall, you can talk to me."
        else:
            arg = arg.lower()
            me = ['wiwa', 'you', 'your']
            found = False
            for item in me:
                if item in arg:
                    #self.get_about_line()
                    found = True
                else:
                    pass
            return found
    ## END NEW -----
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
                elif arg.endswith('script2.txt'):
                    order = self.question_script_order
                    break
                elif arg.endswith('script3.txt'):
                    order = self.verb_script_order
                    break
                elif arg.endswith('script4.txt'):
                    order = self.simple_script_order
                    break
                elif arg.endswith('script5.txt'):
                    order = self.adj_script_order
                    break
                elif arg.endswith('script7.txt'):
                    order = self.adv_script_order
                    break
                elif arg.endswith('script6.txt'):
                    order = self.err_script_order
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
            script1.txt, script2.txt, script3.txt, script4.txt, script5.txt, script6.txt
            or script7.txt
            """
            print(message)
            return None

    def pick_response(self, raw_input):
        """ Create lists of possible valid words for response mechanism,
            Then uses random to choose one to send back to run_wiwa() """
        make = raw_input.lower()
        nouns, verbs, adj, adv, errors = self.make_tag_lists(make)
        print("nouns=", nouns)
        print("verbs=", verbs)
        print("adj=", adj)
        print("adv=", adv)
        print("errors=", errors)
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
                #print("word_type=", word_type)
                #print("word_list[0]=", options[word_type])
                if len(word_list) > 0:
                    choice_tup = (word_type, word_list[0])
                    done = True
                    return choice_tup
        else:
            return ('error', 'not identified')

    def strip_stop_words(self, arg):
        """
        arg is passed in as a list, and as a string.
        Once while checking for errors as a string, and once again
        as a list when removing stop words from the list.
        """

        stops = [' ', 'i','the', 'of', 'he', 'she', 'it', 'some', 'all', 'a', 'lot',
                'have', 'about', 'been', 'to', 'too', 'from', 'an', 'at', 'do', 'go'
                'above', 'are', 'before', 'across', 'against', 'almost', 'along', 'aslo',
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

        if type(arg) == str:
            arg = arg.split()
            for item in arg:
                if item in stops:
                    pass
                else:
                    new_arg.append(item)



        elif type(arg) == list:
            i = 0
            for item in arg:
                word = arg[i]
                if word in stops:
                    pass
                else:
                    new_arg.append(word)
                i += 1


        else:
            new_arg = ['ERRORinSTOPwordSTRIP']

        return new_arg


    def make_tag_lists(self, arg):
        """ Use nltk to tag words for Wiwa to recycle and or respond too """

## !!!!!!!!!!!!!

        errors = self.check_errors_W(arg)

## !!!!!!!!!!!!
        tokens = nltk.word_tokenize(arg)
        tags = nltk.pos_tag(tokens)

        print("tags=", tags)
        clean_tags = self.remove_bad_tags(tags)
        print("cleaned tags=", clean_tags)
        nouns = []
        verbs = []
        adj = []
        adv = []
        #print('clean_tags =', clean_tags)
        #!!!! if someone enters unfindable text, clean_tags will be empty !!!!
        if len(clean_tags) > 0:
            for item in clean_tags:
                x = item[1]
                #print(item)
                if x.startswith("V"):
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
        else:
            nouns = []
            verbs = []
            adj = []
            adv = []
            return nouns, verbs, adj, adv, errors


    def check_errors(self, arg):
        """
        Make a list of words that are not found with pyEnchant,
        Currently using NLTK in wiwa online.  This is an optional way.
        """
        errors = []
        #print("arg =", arg)
        for item in arg:
            if self.enchant_check(arg):
                pass
            else:
                errors.append(item)
        return errors
    ## NEW --- for windows users:
    def check_errors_W(self, arg):
        """
        arg is the user's input.  Must be split into words.
        """
        errors = []

        print('arg type in check_errors_W=', type(arg))
        stripped = self.strip_stop_words(arg)
        user_words = stripped
        print("user_words = ", user_words)


        for item in user_words:
            if wordnet.synsets(item):
                pass
            else:
                errors.append(item)
        return errors
    ### end validating word with wordnet

    def remove_bad_tags(self, tags_list):
        """ Use pyEnchant to remove unidentifiable words from tags list"""
        new_tags = []
        for item in tags_list:
            word = item[0]
## !!!!!!!!!!    windows vs non-windows change   !!!!!#
            # !!!   Use enchant_check_W for windows  !!!
            # !!!   enchant_check for non-windows    !!!
            if self.enchant_check_W(word):
                new_tags.append(item)
            else:
                pass
                #print("word is not found:", word)

        return new_tags

    def enchant_check(self, arg):
        """ using the PyEnchant English dictionary to check validity of a word."""
        x = self.dictionary.check(arg)
        return x
    ###  NEW check validity check for Windows:
    def enchant_check_W(self, arg):

        if wordnet.synsets(arg):
            return True
        else:
            return False
    ####  END NEW validity check for Windows


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
