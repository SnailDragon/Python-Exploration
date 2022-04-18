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
        f.close()
    else:
        continue

    subreddit = input("Enter subreddit: ")
    count = int(input("Number of Posts: "))
    feed = input("top/new/hot: ")
 
    scraper = Scraper(subreddit, count, feed)

    print("Looking for: " + str(scraper.getKeywords(keywords)) + " in r/" + scraper.subreddit)
    
    output = scraper.commentWordCount(keywords)

    fwrite = open("./output.txt", "a")
    fwrite.write(output)
    fwrite.close()





