from Scraper import Scraper

s = Scraper("memes", 10, "hot")
print(s.countInstances("asdf asdf adsf", "asdf"))


while False:
    print("\nComment analysis:")
    keywords = input("Enter words to look for (\"quit\" to exit): ")
    
    if keywords == "quit":
        break

    scraper = Scraper("memes", 10, "hot")

    print("Looking for: \n" + str(scraper.getKeywords(keywords)))
    
    #scraper.commentWordCount(keywords)



