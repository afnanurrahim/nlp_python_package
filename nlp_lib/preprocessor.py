import json
import pandas as pd
import emoji
import wordfreq
import string
import re

def replace_contraction(string):
    contractions_dict=contractions()
    string=string.lower()
    for s in string.split(' '):
        if s in contractions_dict.keys():
            string=string.replace(s,contractions_dict[s])
    return string

def replace_abbreviations(string):
    abbreviations_dict=abbreviations()
    string=string.lower()
    for s in string.split(' '):
        if s in abbreviations_dict.keys():
            string=string.replace(s,abbreviations_dict[s])
    return string

def remove_emoji(string):
    emoji_list=[c for c in string if c in emoji.EMOJI_DATA]
    for e in emoji_list:
        string=string.replace(e,'')
    return string

def replace_emoji(string):
    emoji_dict=emojis()
    emoji_list=[c for c in string if c in emoji.EMOJI_DATA]
    for e in emoji_list:
        if e in string and e in emoji_dict.keys():
            string=string.replace(e,emoji_dict[e])
    return string

def abbreviations():
    with open('data/abbreviations.json') as f:
        abb= json.load(f)
    return abb

def contractions():
    with open('data/contractions.json.json') as f:
        contrac = json.load(f)
    return contrac

def emojis():
    with open('data/emojis.json') as f:
        emoji_dict= json.load(f)
    return emoji_dict

def remove_special_char(sentence):
    st=''
    for ch in sentence:
        if ch.isalnum() or ch in string.whitespace:
            st+=ch
    return st

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

class WordSegment:
    def __init__(self,string):
        self.text=string.lower()
        self.english_words = wordfreq.get_frequency_dict("en")
        self.__P= self.__probability(self.english_words)
        self.__result=self.__segment(self.text)
    
    def __probability(self,counter):
        N = sum(counter.values())
        return lambda x: counter.get(x,0)/N


    def segment_list(self):
        return self.__result
    
    def __Pwords(self,words):
        result=1
        for w in words:
            result*= self.__P(w)
        return result

    def __tokens(text):
        return re.findall('[a-z]+', text.lower()) 

    def __memo(f):
        cache = {}
        def fmemo(*args):
            if args not in cache:
                cache[args] = f(*args)
            return cache[args]
        fmemo.cache = cache
        return fmemo

    def __get_length(self,string):
        count = 0
        for char in string:
            count += 1
        return count

        
    def __splits(self,text, start=0, L=20):
        return [(text[:i], text[i:]) 
                for i in range(start, min(self.__get_length(text), L)+1)]

    @__memo
    def __segment(self,text):
        if not text: 
            return []
        else:
            candidates = ([first] + self.__segment(rest) 
                        for (first, rest) in self.__splits(text, 1))
            return max(candidates, key=self.__Pwords)