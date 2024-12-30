
class Card:
    def __init__(self, players):
        self.turn = 0
        self.players = players
        empty = ["?" for i in range(len(players))]
        self.who = {
            "Green": empty.copy(),
            "Mustard": empty.copy(),
            "Peacock": empty.copy(),
            "Plum": empty.copy(),
            "Scarlet": empty.copy(),
            "Orchid": empty.copy()
        }
        self.what = {
            "Candlestick": empty.copy(),
            "Dagger": empty.copy(),
            "Revolver": empty.copy(),
            "Lead Pipe": empty.copy(),
            "Rope": empty.copy(),
            "Wrench": empty.copy()
        }
        self.where = {
            "Conservatory": empty.copy(),
            "Ballroom": empty.copy(),
            "Kitchen": empty.copy(),
            "Dining Room": empty.copy(),
            "Lounge": empty.copy(),
            "Hall": empty.copy(),
            "Study": empty.copy(),
            "Library": empty.copy(),
            "Billiard Room": empty.copy()
        }
    
    def getTurnPlayer(self):
        return self.players[self.turn]

    def addKnown(self, responder, key):
        if key in self.who: self.who[key] = ["X" if self.players[i] == responder else "O" for i in range(len(self.who[key]))]
        elif key in self.what: self.what[key] = ["X" if self.players[i] == responder else "O" for i in range(len(self.what[key]))]
        elif key in self.where: self.where[key] = ["X" if self.players[i] == responder else "O" for i in range(len(self.where[key]))]
        else: raise KeyError("Bad key")

    def addGuess(self, guess_who, guess_what, guess_where, responder):
        if responder not in self.players: 
            return False 
        index = self.turn + 1
        print("Guessing", guess_who, guess_what, guess_where, responder)
        while self.players[index] != responder: 
            self.who[guess_who][index] = "O"
            self.what[guess_what][index] = "O"
            self.where[guess_where][index] = "O"
            index += 1 
        
        

    def getBestGuess(self):

        def getBest(d):
            best_count = 0
            best = list(d.keys())[0]
            for k, v in d.items():
                if(v.count("O") > best_count):
                    best_count = v.count("O")
                    best = k
            if d[best].count("O") == len(d[best]):
                return f"Who: {best} (known)\n"
            else:
                return f"Who: {best} \n"

        return getBest(self.who) + getBest(self.what) + getBest(self.where)

    def __str__(self):
        ss = "\n"
        ss += "%-20s" % "Mansion"
        for p in self.players:
            ss += "%-10s" % p
        ss += "\n"

        def helper(d):
            table = ""
            for k in d:
                table += "%-20s" % k
                for v in d[k]:
                    table += "%-10s" % v
                table += "\n"
            return table

        ss += "\nWho?\n" 
        ss += helper(self.who)
        ss += "\nWhat?\n"
        ss += helper(self.what)
        ss += "\nWhere?\n"
        ss += helper(self.where)

        return ss

if __name__ == "__main__":
    user_input = input("Enter player names (including you) in order separated by a space \nstarting with whoever goes first: ").split()
    card = Card(user_input)
    print(card)
    while True: 
        user_input = input("Next turn (1) or input known (2) or quit (q): ")
        if user_input == "q": break
        elif user_input == "1":
            print(f"It is {card.getTurnPlayer()}\s turn, enter their guess: ")

            who = input("Who: ")
            what = input("What: ")
            where = input("Where: ")
            responder = input("Who gave a card: ")
            card.addGuess(who, what, where, responder)

        elif user_input == "2":
            known = input("What is known to not be the answer? ")
            responder = input("Who has the card: ")
            card.addKnown(responder, known)
        else:
            print("Invalid input")
            
        print(card)
        print("Best guess:", card.getBestGuess(), sep="\n")
        
    print()