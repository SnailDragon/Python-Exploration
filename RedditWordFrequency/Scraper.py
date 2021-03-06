import praw
import pandas as pd
import numpy as np
from praw.models import MoreComments
import string

class Scraper:

    # ("memes", 10, "top")
    def __init__(self, subreddit, depth, feed):
        self.subreddit = subreddit
        self.reddit = praw.Reddit(client_id='a6uX27rHUe4D5y9cpLZ2WQ', client_secret='_ylxW5EjPRbVE44pXgWLISQflxXU-A', user_agent='CommentSearcher')
        if feed == "hot":
            self.posts = self.reddit.subreddit(subreddit).hot(limit=depth)
        elif feed == "top":
            self.posts = self.reddit.subreddit(subreddit).top(limit=depth)
        elif feed == "new":
            self.posts = self.reddit.subreddit(subreddit).new(limit=depth)

        self.frequencies = pd.Series(dtype=int)

    # gets words to search for from input string 
    # - seperated by spaces except when in quotation marks
    def getWords(self, wordbank):
        words = []

        wordbank = wordbank.strip()
        word = ""
        for i in wordbank:
            if i == "\n":
                continue
            if i == " ":
                if word != "":
                    word = word.lower()
                    word = word.translate(str.maketrans('','', string.punctuation))
                    words.append(word)
                    word = ""
            else:
                word += i
                
        if(word != ""):
            word = word.lower()
            word = word.translate(str.maketrans('','', string.punctuation))
            words.append(word)

        return words

    def countInstances(self, baseStr, strToFind):
        baseStr = baseStr.lower()
        strToFind = strToFind.lower()
        index = 0
        count = 0
        while baseStr.find(strToFind, index) >= 0:
            #print(index)
            count += 1
            index = baseStr.find(strToFind, index+len(strToFind))
        return count

    def addToSheet(self, word):
        word = str(word)
        for i in range(len(self.frequencies)):
            if self.frequencies.index[i] == word:
                self.frequencies[i] += 1
                return
        newRow = pd.Series(data=[1], index=[word])
        #print(newRow)
        #self.frequencies = self.frequencies.append(newRow, ignore_index = False)
        self.frequencies = pd.concat([self.frequencies, newRow])
        #print(self.frequencies)

    def commentWordAnalysis(self):
        total = 0
        it = 0
        f = open("WordFrequencies.csv", "w")
        f.close()
        for post in self.posts:
            print("post: " + str(it))
            it += 1
            # if(it % 10 == 0):
            #     self.frequencies.to_csv("WordFrequencies.csv")
            post.comments.replace_more(limit=10)
            print("expanded - comments: " + str(len(post.comments.list())))
            for comment in post.comments.list():
                print("next comment")
                if isinstance(comment, MoreComments):
                    continue
                words = self.getWords(comment.body)
                for i in words:
                    self.addToSheet(i)
                self.frequencies.to_csv("WordFrequencies.csv")
        
        print(self.frequencies)
