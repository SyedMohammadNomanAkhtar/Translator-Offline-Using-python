#!/usr/bin/env python
# coding: utf-8

# ## Translating Files into other language using python

# In[1]:


from translate import Translator
with open("test(input).txt", mode = "r") as myfile:
    text = myfile.read()
translator = Translator(to_lang="ja")
translation = translator.translate(text)
print(translation)
#myfile.close()

