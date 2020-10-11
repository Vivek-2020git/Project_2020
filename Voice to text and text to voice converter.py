#!/usr/bin/env python
# coding: utf-8

# # Simple voice to text and text to voice converter

# ## 1. Voice to text converter

# In[17]:


## This code is for windows 10 version


# In[18]:


get_ipython().system('pip3 install SpeechRecognition pydub')


# In[19]:


get_ipython().system('pip3 install pyaudio')


# In[20]:


import speech_recognition as spre


# In[21]:


reg = spre.Recognizer()


# In[23]:


with spre.Microphone() as sigin:
    print("Please say somethong")
    audio=reg.record(sigin, duration=5)
try:    
    print(reg.recognize_google(audio),"\n")
except:
    print("Completed")


# ## 2. Text to voice converter

# In[24]:


## This code is for windows 10 version


# In[25]:


get_ipython().system('pip3 install SpeechRecognition pydub')


# In[26]:


get_ipython().system('pip3 install pyaudio')


# In[27]:


from win32com.client import constants, Dispatch


# In[28]:


Text = "Enter text which you want to convert into voice output and run this cell again Thank you" 
speaker = Dispatch("SAPI.SpVoice")
speaker.Speak(Text)
del speaker


# In[ ]:




