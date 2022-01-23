from Scraper import Scraper

while True:
    print("\nComment analysis:")
    option = ""
    option = input("Use wordlist file? (y/n/quit): ")

    if option == "quit": 
        break
    elif option == "n":
        keywords = input("Enter words to look for (\"quit\" to exit): ")

        if keywords == "quit":
            break
    elif option == "y":
        path = input("Enter file path: ")
        f = open(path, "r")
        keywords = f.read()
    else:
        continue
        


    scraper = Scraper("memes", 100, "top")

    print("Looking for: " + str(scraper.getKeywords(keywords)) + " in r/" + scraper.subreddit)
    
    scraper.commentWordCount(keywords)



