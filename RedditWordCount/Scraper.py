import praw
import pandas as pd
import numpy as np

class Scraper:

    def __init__(self, subreddit, depth, feed):
        self.reddit = praw.Reddit(client_id='a6uX27rHUe4D5y9cpLZ2WQ', client_secret='_ylxW5EjPRbVE44pXgWLISQflxXU-A', user_agent='CommentSearcher')
        if feed == "hot":
            self.posts = self.reddit.subreddit(subreddit).hot(limit=depth)
        elif feed == "top":
            self.posts = self.reddit.subreddit(subreddit).top(limit=depth)
        elif feed == "new":
            self.posts = self.reddit.subreddit(subreddit).new(limit=depth)



    # gets words to search for from input string 
    # - seperated by spaces except when in quotation marks
    def getKeywords(self, wordbank):
        words = []

        wordbank = wordbank.strip()
        word = ""
        quoteMode = False
        for i in wordbank:
            if quoteMode:
                if i == "\"":
                    if word != "":
                        words.append(word)
                        word = ""
                    quoteMode = False
                else:
                    word += i
            else:
                if i == "\"":
                    quoteMode = True
                    continue
                if i == " ":
                    if word != "":
                        words.append(word)
                        word = ""
                else:
                    word += i
        if(word != ""):
            words.append(word)
            

        return words

    def countInstances(self, baseStr, strToFind):
        baseStr = baseStr.lower()
        strToFind = strToFind.lower()
        index = 0
        count = 0
        while baseStr.find(strToFind, index) >= 0:
            index = baseStr.find(strToFind, index+1)
            count += 1
        return count


    def commentWordCount(self, keywordBank):
        keywords = self.getKeywords(keywordBank)
        stats = pd.Series(np.zeros(len(keywords)), index=keywords, dtype=int)

        for post in self.posts:
            print(len(post.comments))
            for comment in post.comments:
                for i in stats:
                    stats[i] = self.countInstances(comment, i)


        print(stats)



