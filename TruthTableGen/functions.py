
def HasErrors(equation):
    #check characters
    goodChars = "&|! ABCDEFG"
    for i in equation:
        if(goodChars.index(i) == -1):
            return True
    #check parenthesis completion
    parenths = ""
    for i in equation:
        if i == "(" or i == ")":
            parenths += i
    if parenths % 2 != 0:
        return True
    newparenths = ""
    while(parenths != newparenths):
        newparenths = ""
        for i in range(len(equation), 2):
            if not (equation[i] == "(" and equation[i+1] == ")"):
                newparenths += equation[i:i+2]
    print(parenths + "\t" + newparenths)

            

    #check operation validity

    return False

def GenerateTruthTable(equation):
    # check errors
    print(equation)
    