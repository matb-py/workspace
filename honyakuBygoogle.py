#pip install googletrans　⇒　NG
#pip3 install googletrans　⇒　OK
#googletrans 3.0.0
#from <module> import <method>, from <module> import <variable> 
from googletrans import Translator
translator  = Translator()
word1 = input("翻訳する言葉を入力して：")
word2 = translator.translate(word1)
print(word2.text)

