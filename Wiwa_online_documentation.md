# Whispering Wall (name: Wiwa)

 
The inspiration for the code project came from seeing a JavaScript version of [Wickipedia: Eliza](https://en.wikipedia.org/wiki/ELIZA). 
Whispering Wall is intended for entertainment purposes and to explore the possiblities of chatbot interactions.

## NLTK 
On building the initial code, I realized that it would be much more responsive to user input if it could identify parts of speech.
This way the bot could capture and feed back the users word in dialog.  
Example:  
<div style="display: flex; width: 100%;">
<img src="https://github.com/nelliesnoodles/Whispering-Wall/blob/master/Wiwa_5-16-2021.JPG" alt="Screenshot, User input: I have a dog.  Wiwa ouput: May I see dog?"></img>
</div>

In the example, the NLTK has parsed the initial user text, and found the word 'dog' and labeled it correctly as a Noun.
The user input is first made into lowercase letters, then stripped of punctuation.  _This approach needs to be made better as punctuation and capitalization, while not critical,
does play a role in the stop word identifier, and NLTK's proper tagging of the Parts of Speech._


After NLTK has returned the parts of speech with the class method: make_tags_lists(user_input), called inside the class method: pick_response(user_input), the different lists are put into an object.
code:
<pre><code>
options = {'noun': [], 'verb': [], 'adj': [], 'adv': [], 'err': []}
</code></pre>

The error list 'err' is not created by NLTK.  The version and set of NLTK wiwa uses will not distinguish words it does not recognize as errors. Most times it will label the word as a 'NN' or Noun and send it back in the tags list.
To compensate, another parse happens to go through each of the tagged words and check with the python Enchant if that word exists in the libraries given dictionary.  Words that are identified by the dictionary are 
sent back and assigned.  Two lists are returned by this method: remove_bad_tags(tags).  
They are assigned as the variables 'errors' and 'clean_tags' inside  method make_tags_lists.

## Decision tree
The decision tree is the engine of Whispering Walls responses.  It runs all the code necessary to generate a response to the user text, and return it in a specific priority order. 
When none of the items of the tree, (if clauses) are true, it falls to the else method, which returns Wiwa's introduction text.  This is useful because on the initial startup, a new page load of the view in Django,
The introduction will be sent as the returned result of Wiwa's decision tree. 

Code reference: 
<pre><code>
            reject = self.unacceptable(make)
            question = self.check_question(make)
            about_me = self.check_for_name(make)
            about_wiwa = self.check_for_name_wiwa(make)
            greet = self.is_greeting(make)
</code></pre>

The tree runs in this order of priority:
<ol>
  <li> Check if user has used an 'Exit' term, not NLTK dependant </li>
  <li> Enter first (else clause) where the words of the user are checked to see if the user's words should be rejected, are a question, a greeting, or are include reference to myself, or Wiwa.</li>
  <li> order of priority in this branch:  reject, about myself, greetings, question, simple sentence </li>
  <li> Enter else clause where the random choice is made from the returned list of tags created by M: pick_response(self, raw_input)</li>
  <li> Enter next branch (else clause) </li>
  <li> Order of priority in last branch: Noun, Verb, Adverb, Adjective, About Wiwa, Error, final else clause (return Introduction text)</li>
 </ol>
 
 ### Why the priorities matter
 
 The best example of why these priorities matter is the 'unacceptable speech'.  One day while scrolling through Twitter, I encountered a post about a chatbot being fed racial slurs.
 The chatbot had then repeated, and stored those slurs into it's language.  So for these reasons, I went directly to Wiwa's code in Pythonanywhere, and created the 'reject' phase of the tree.
 It is the highest priority so that if people do enter hate speech words into the project, they are immediately told that the language will not be tolerated.  While Wiwa has no memory, and does not 
 store any information on the user's text other than for the JavaScript to access and append to the 'chat box' for the user to see, Wiwa was made for constructive purposes.  Hate speech is not tolerated. And is immediately rejected.

The reasons the NLTK parts of speech are addressed after questions, or greetings, is that the scripts are just random sentences put together in a silly manner to replicate conversation with a robot. 
While it is not intended that Wiwa seem real, it is also more engaging if the code recognizes a greeting, or a question when it is entered.  The choice that is returned at that point could be any one of the 
four parts, Noun, Verb, Adverb, Adjective, and the order in the if clauses (branch) here, is just merely a remnant of when I had originally had her responding to just tagged parts of speech.
The tree runs the 'about_wiwa' last, as it is also a failsafe for if no Parts of Speech were tagged. 'Wiwa' in an input is tagged as an error by the python dictionary.
The last elif before the final else, will check the 'errors' list.   This will not return an interactive sentence where the user's word can be injected, but will return a line from the error script which contains
a few of the memorable lines from the different 'Monty Python' movies.  

*note to self, create a branch for single entries, such as numbers and letters.  Wiwa could return the next in a sequence. See: Cleverbot*

## Tests

The tests are simple methods built into the WW_online.py.  
When the script is run in the shell, the test methods can be called.  
They simply check that the scripts are reachable, that Wiwa instantiation has been successful, and that different test sentences are processed by the tree. 

## Additional information

### Stop words 

Stop words are words like prepositions, and articles.   In first creating the Whispering Wall online version, I had stripped the stop words before the NLTK parsed the text. 
This was a mistake, because NLTK needed those words to determine parts of speech.  It would often tell me a word was a Noun that should not have been labeled a noun because, without stop words, 
it had been incorrectly identified as the 'subject' of the sentence. This is just my lamen's interpretation of why this was happening.  It is neither confirmed or denied by the NTLK content maintainers/creators.

### Scripts

Many of the script lines need the python 3+ formatting where a word can be injected with the curly brackets '{<word>}'. 
  Only the Parts of Speech scripts do this. The users word, identified by parsing through NLTK as one of 'noun', 'verb', 'adverb' or 'adjective' is plucked from the tuple to fill 
  in the script lines.  Script lines are not randomly chosen, as I have found that the different run's of Wiwa(), tend to follow the same random pattern, and her conversations become predictable. 
  
  _note: can seeding/unseeding fix this?_
  
  The other scripts are just lines of text meant to encourage the user to keep interacting to see what Wiwa will say.
  
  ## Fork / Use Whispering Wall
  
  I encourage the fork, and use of this code.  I ask only for (reference) credit if her code is used directly for your project.  
  With all the code I openly share, I encourage users to take it, break it, learn from it, and have fun. 
  
  
  
    










