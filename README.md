# Whispering-Wall
Python chatbot 

It is also being modified and run online at nellietobey.pythonanywhere.com
The online version found in the WW_online.py file, is more advanced than the offline version.

No user text is stored inside the website. It is processed but not stored. 
Clear this data by using the clear button found next to the submit button.
Play with Wiwa here: [Whispering Wall](https://nelliestobey.pythonanywhere.com/wiwa)

This code needs NLTK installed along with a few packages downloaded.

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

5/11/2021 

Wiwa's code has a list of hateful words (slurs) she will not parse.  
I will add more words as I am informed of them.  
I do not want my chatbot engaging in conversation where these words are used. 
If you have words you think I should add, you can DM my twitter account and let me know.
[twitter: NelliesNoodles](https://twitter.com/NelliesNoodles)

