import os


try:
  import nltk
  nltk.download('wordnet')
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
except ImportError as e:
  os.system('pip3 install nltk')
  import nltk
  nltk.download('wordnet')
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')



try:
  import PyEnchant
except ImportError as e:
  os.system("pip3 install PyEnchant")
