#!usr/bin/python3
# -*- coding: utf-8 -*-

import enchant
import re
import nltk as nltk
from nltk.corpus import wordnet
import random







"""

    Manual setup:
    install - nltk
    install - python3
    !!! GitHub version of Whispering wall does not use enchant.
    !!! python's Enchant did not pip install properly with Windows.
    install - PyEnchant
    In your python3 shell type these to download needed data sets:
    >>>import nltk
    >>>nltk.download('wordnet')
    >>>nltk.download('punkt')
    >>>nltk.download('averaged_perceptron_tagger')
    noun responses -- nouns.txt
    verb responses -- verbs.txt
    yes responses -- yes_no.txt
    questionable -- queries.txt
    adjectives -- adjectives.txt
    Interject -- interjections.txt <-- not used yet
    Adverbs -- adverbs.txt
    script8 -- about Nellie
    script9 -- about Wiwa

    Testing
        >>> import WW_online
        >>> WW_test()
"""


class Wiwa(object):
    def __init__(self): # added a initiated value for session to access (line_numb) 1-9-18
      #Personal CPU path: /home/nellie/MYSITE/my-first-blog-master/wiwa
      #Website path to files:"/home/NelliesNoodles/nelliesnoodles_mysite/WIWA"
      # script file path is also in the  ~~~~~get_script_line()~~~~~


        self.nounscript = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/nouns.txt"
        self.verbscript = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/verbs.txt"
        self.simplescript = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/yes_no.txt"
        self.questionable = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/queries.txt"
        self.adjectives = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/adjectives.txt"
        self.error_script ="/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/to_err.txt"
        self.adverbs = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/adverbs.txt"
        self.aboutNellie = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/script8.txt"
        self.aboutWiwa = "/home/NelliesNoodles/nelliesnoodles_mysite/WIWA/script9.txt"
        self.about_index = 0
        self.about_list = []
        self.about_W_index = 0
        self.about_W_list = []

##  GitHub version of Whispering wall does not use enchant.
##  python's Enchant did not pip install properly with Windows.

        self.dictionary = enchant.Dict("en_US")
        self.line_get = 1

##--------------------------------------##
##        Main run                      ##
##--------------------------------------##

    def run_wiwa(self, user_input):
        """intro = Welcome to the whispering wall, Wiwa is here to respond
        and question your perspective. She is just a program, and
        will respond according to her script.
        If you wish to stop program, type EXIT or QUIT.
        Have fun! *Used in bash run*"""

        make = user_input
        stripped = make.lower()
        newstring = re.sub("[^a-zA-Z| |]+", "", stripped)
        self.create_about_list()
        self.create_about_W_list()

        if make in ['QUIT', 'EXIT', 'exit', 'quit', 'q']:
            self.about_index = 0
            self.about_W_index = 0
            return "Goodbye, thanks for stopping in!"
        else:


            reject = self.unacceptable(make)
            question = self.check_question(make)
            about_me = self.check_for_name(make)
            about_wiwa = self.check_for_name_wiwa(make)
            greet = self.is_greeting(make)


            if reject:
                response = "That language is not acceptable here."
                return response

            elif about_me != False:
                response = self.get_about_line()
                return response

            elif greet:
                return 'Greetings human!'

            elif question:
                discusanswer = self.get_script_line(self.questionable)
                return discusanswer

            elif newstring in ['yes', 'no', 'maybe']:
                response = self.get_script_line(self.simplescript)
                return response

            else:
                choice = self.pick_response(make)
                if choice[0] == 'noun':
                    response = self.get_script_line(self.nounscript)
                    return response.format(choice[1])
                elif choice[0] =='verb':
                    response = self.get_script_line(self.verbscript)
                    verbasity = response.format(choice[1])
                    return verbasity
                elif choice[0] == 'adv':
                    response = self.get_script_line(self.adverbs)
                    if '{}' in response:
                        adverb = response.format(choice[1])
                        return adverb
                    else:
                        return response
                elif choice[0] == 'adj':
                    response = self.get_script_line(self.adjectives)

                    if '{}' in response:
                        adjective = response.format(choice[1])
                        return adjective
                    else:
                        return response

                elif about_wiwa != False:
                    response = self.get_about_W_line()
                    return response

                elif choice[0] == 'err':

                    response = self.get_script_line(self.error_script)

                    if '{}' in response:
                        too_error = response.format(choice[1])
                        return too_error
                    else:
                        return response

                else:

                    intro = """Welcome to the Whispering Wall, Wiwa is here to give you an outlet for your words.
                    She is just a program, and will respond according to her script. It's slightly better than talking to a literal wall. """
                    return(intro)

##---------------------------------##
##    modified for test main run   ##
##  does not include aboutWiwa,    ##
## or aboutNellie scripts yet.     ##
##---------------------------------##

    def _test_response_making(self, test_sentence):
        print('RUNNING TEST RESPONSE')
        make = test_sentence
        stripped = make.lower()
        newstring = re.sub("[^a-zA-Z| |]+", "", stripped)
        if make in ['QUIT', 'EXIT', 'exit', 'quit', 'q']:
            return "Goodbye, thanks for stopping in!"
        else:
            choice = self.pick_response(make)

            question = self.check_question(make)
            if question:
                discusanswer = self.get_script_line(self.questionable)
                return discusanswer
            elif newstring in ['yes', 'no', 'maybe']:
                response = self.get_script_line(self.simplescript)
                return response
            else:
                if choice[0] == 'noun':
                    response = self.get_script_line(self.nounscript)
                    return response.format(choice[1])
                elif choice[0] =='verb':
                    response = self.get_script_line(self.verbscript)
                    verbasity = response.format(choice[1])
                    return verbasity
                elif choice[0] == 'adv':
                    response = self.get_script_line(self.adverbs)
                    if '{}' in response:
                        adverb = response.format(choice[1])
                        return adverb
                    else:
                        return response
                elif choice[0] == 'adj':
                    response = self.get_script_line(self.adjectives)

                    if '{}' in response:
                        adjective = response.format(choice[1])
                        return adjective
                    else:
                        return response
                elif choice[0] == 'err':
                    response = self.get_script_line(self.error_script)

                    if '{}' in response:
                        too_error = response.format(choice[1])
                        return too_error
                    else:
                        return response

                else:

                    return("Wiwa:  ... ... ")

##---------------------------------##
##    added a simple greeting      ##
##---------------------------------##

    def is_greeting(self, user_input):
            greetings = [
            'hiya', 'howdy', 'hello', 'greetings',
            'aloha', 'yo', 'salutations', 'hi'
            ]
            loweruser = user_input.lower()
            if len(user_input) == 0:
                return True

            else:
                if type(user_input) == str:
                    alist = loweruser.split()
                    for word in alist:
                        if word in greetings:
                            return True
                        else:
                            pass
            return False

##----------------------------------------------------##
##    Creating a filter for words that shall not      ##
## be accepted or processed by Wiwa.                  ##
## This language is not acceptable.                   ##
## If I missed any feel free to let me know, I will   ##
## add it to her doNOTPARSE list.                     ##
##----------------------------------------------------##

    def unacceptable(self, astring):
        stripped = astring.lower()
        newstring = re.sub("[^a-zA-Z| |]+", "", stripped)
        checking_list = newstring.split(' ')
        #print(checking_list)
        doNOTPARSE = [
            'cunt', 'whore', 'chink', 'bootlip', 'coon', 'nigger', 'niger', 'niglet', 'slut',
             'retard', 'retarded']
        for word in checking_list:
            if word in doNOTPARSE:
                return True

        return False

##----------------------------------------------------##
##  New scripts for responses to my name, or wiwa     ##
##  script8 -- about me   script9 -- about wiwa       ##
##----------------------------------------------------##
    def create_about_list(self):
        """
        Get the lines in the text file to respond when input includes creator's name
        """
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
        Adding randomization to the about_me script
        It is not randomized and responses are only dependant on the
        user refering to the words 'nellie', 'tobey' or 'creator' in an input.
        script lines are to be put in a list, and incremented through.
        Once the end of the list is reached, we start over.
        """
        max = len(self.about_list) - 1
        line_choice = random.randint(0, max)

        line = self.about_list[line_choice]
        #testline = "about index =" + str(self.about_index)
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
        #testline = "about wiwa index =" + str(self.about_W_index)
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
            me = ["wiwa", "you", "your", "hello", "you're"]
            found = False
            for item in me:
                if item in arg:
                    found = True
                else:
                    pass
            return found



##----------------------------------------------------##
##   send back random choice of response tuples       ##
##----------------------------------------------------##

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
                # it might be bad to trust random.choice to not run idle while finding a choice in the list
                # the options dict is tiny so it shouldn't get stuck picking one
                dict_key_list =[]

                #print(list(options))
                word_type = random.choice(list(options))

                word_list = options[word_type]


                if len(word_list) > 0:
                    choice_tup = (word_type, word_list[0])
                    done = True
                    return choice_tup
        else:
            choice_tup = ('error', 'not identified')
            return choice_tup

##----------------------------------------------##
##       open script, return line from script   ##
##----------------------------------------------##

    def get_script_line(self, arg):
        """ Chooses a random script line to give back to user """
        # is often not random *sad face*
        #print(self.line_get)
        #return "getting line"
        if arg.startswith("/home/NelliesNoodles/nelliesnoodles_mysite/WIWA"):   ####   Script file path  ####
            if self.line_get > 22:
                self.line_get = 0
            with open(arg) as f:
                lines = f.readlines()
                x = int(self.line_get)
                #print(lines[x])
                #self.line_get += 1 ##  Views.py and sessions handles the line_get attribute
                return lines[x]

        else:
            return "script file could not be found"

##  ------------------------------------------- ##
##        input processing, cleaning            ##
##----------------------------------------------##


    def strip_stop_words(self, arg):
        """
        error fix: 02-26-2020
        arg is passed in as a list, and as a string.
        Once while checking for errors as a string, and once again
        as a list when removing stop words from the list.
        """

        stops = [' ', 'i','the', 'of', 'he', 'she', 'it', 'some', 'all', 'a', 'lot',
                'have', 'about', 'been', 'to', 'too', 'from', 'an', 'at', 'do', 'go'
                'above', 'are', 'before', 'across', 'against', 'almost', 'along', 'aslo',
                'although', 'again', 'always', 'am', 'among', 'amongst', 'amount', 'and',
                'another', 'any', 'anyhow', 'anyone', 'anything', 'around', 'as',
                'be', 'maybe', 'being', 'beside', 'besides', 'between', 'beyond', 'both',
                'but', 'by', 'can', 'could', 'done', 'during', 'each', 'either',
                'else', 'even', 'every', 'everyone', 'everything', 'everywhere',
                'except', 'few', 'for', 'had', 'has', 'hence', 'here', 'in', 'into', 'is',
                'it', 'its', 'keep', 'last', 'latter', 'many', 'may', 'more', 'most', "n't",
                'much', 'name', 'next', 'none', 'not', 'nothing', 'now', 'nowhere',
                'often', 'other', 'others', 'over', 'rather', 'perhaps', 'seems', 'then',
                'there', 'these', 'they', 'though', 'thru', 'too', 'under', 'until',
                'upon', 'very', 'was', 'were' 'which', 'while', 'will', 'with', 'ill', 'lets'
                'wo', 'would', 'b', 'c', 'd', 'e', 'f', 'g', 'x', 'y', 'z']
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
            new_arg = ['ERROR-stopwords']

        return new_arg

    def make_tag_lists(self, arg):
        """
           Use nltk to tag the input, then clean up the lists to return
           A mechanism that will chose one of the items at random to return to
           Whispering walls response loop.
           Change in remove_bad_tags => strip_stop_words
        """
        tokens = nltk.word_tokenize(arg)
        tags = nltk.pos_tag(tokens)
        errors, clean_tags = self.remove_bad_tags(tags)
        nouns = []
        verbs = []
        adj = []
        adv = []
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

    def remove_bad_tags(self, tags_list):
        """ Use pyEnchant to remove unidentifiable words from tags list"""
        new_tags = []
        errors = []
        for item in tags_list:
            word = item[0]

            if self.enchant_check(word):
                new_tags.append(item)
            else:
                errors.append(word)

        return errors, new_tags

    def enchant_check(self, arg):
        """ using the PyEnchant English dictionary to check validity of a word."""
        x = self.dictionary.check(arg)
        return x

    def check_question(self, arg):
        questions = ['why', '?', 'maybe']
        if questions[0] in arg or questions[1] in arg:
          return True
        else:
          return False

##----------------------------------##
##  testing WW class attributes     ##
##----------------------------------##

    def _test_attributes(self):
        scripts = [self.nounscript, self.verbscript, self.adjectives, self.simplescript, self.questionable, self.error_script, self.adverbs]
        index = 0
        for script in scripts:
            try:
                with open(script) as f:
                    #print('SUCCESS')
                    #print('script index: ', index)
                    index += 1
            except:
                message = "unable to open file at index {} in scripts of test_attributes"
                error_message = message.format(index)
                #print(error_message)
                index += 1

        index = 0
        for script in scripts:
            result = self.get_script_line(script)
            if result == "script file could not be found":
                message = "unable to open file at index {} in scripts of test_attributes"
                error_message = message.format(index)
                #print(error_message)
                index += 1
            else:
                print('get line success @ :', index)
                index += 1


## ***********************************  ##
##      WW python shell test run        ##
##  >>> import WW_online as ww          ##
##  >>> ww.WW_test()                    ##
##--------------------------------------##

def WW_test():
    test_sentences = [
        "Where are the goats?", #questionable.txt
        "The goats are jumping", #Noun, verb
        "The frog jumped.", #noun, verb
        "No", #simpleScript.txt
        "Tree.", #Noun
        "Kill it", # Verb
        "Pretty Octopus.", #Adjective
        "Edible button.", #adjective
        "Beautifully done.", #adverb
        "It is simply magnificent.", #adverb
        "fjskdflskjdflsjjslkfj", #error script
        ]
    WW = Wiwa()
    WW._test_attributes()
    ###  run testing of sentences  ###
    ### should produce any result except: "Wiwa:  ... ... " ###
    index = 0
    fails = ["Wiwa: ... ... ", "script file could not be found"]
    for data in test_sentences:
        #print('data loop through test sentences')
        try:
            response = WW._test_response_making(data)
            #print(response)
            if response not in fails:
                print("successful sentence response, index= ", index)
                index += 1
            else:
                print("Unsuccessful test sentence response, index= ", index)
                index += 1
        except:
            print(data)
            print("Whispering wall failed to process sentence at index= ", index)
            index += 1

def newtest():

    WW = Wiwa()
    try:
        WW.run_wiwa('new word')
        print('wiwa did not fail')
    except:
        print('wiwa failed to run.')

