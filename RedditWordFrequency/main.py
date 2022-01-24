from Scraper import Scraper


subreddit = input("Subreddit to analyze: ")
depth = int(input("Number of posts: "))
feed = input("top/hot/new: ")

scraper = Scraper(subreddit, depth, feed)

scraper.commentWordAnalysis()

