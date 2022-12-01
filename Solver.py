#Wordle Helper Edward Peng

#designate variables
words = []
wordsCopy=[]
incorrectWords=[]
correct=[]
incorrect=[]
final=["*", "*", "*", "*", "*",]
check=0
i=0

#open file with list of all 5 letter word possibilities
with open('/Users/eddiepeng/Desktop/Projects/WordleHelper/Answers.txt') as w:
  words = w.readlines()

for i in range(5):
    if final.count("*")==0:
        print("Congratulations on figuring out the word: " + guess + " !")
        quit()
    guess=input("What was the word? ")
    color=input("What were the colors (g for green, y for yellow, b for black/grey)? ")
    
    for x in range(0,len(guess)):
        #if color is g.. add to correct / adjust final
        if color[x] == 'g' or color[x] == 'G':
            final[x]=guess[x]
            if guess[x] in correct:
                continue
            correct+=guess[x]
        #if color is y.. add to correct 
        if color[x] == 'y' or color[x] == 'Y':        
            if guess[x] in correct:
                continue
            correct+=guess[x]
        #if color is b.. add to incorrect
        elif color[x] == 'b' or color[x] == 'B':
            if guess[x] in correct:
                continue 
            if guess[x] in incorrect: 
                continue     
            incorrect+=guess[x]
    # print(*words)
    # print("Correct letters: ")
    # print(correct)
    # print("Incorrect letters: ")
    # print(incorrect)
    # print("Final answer: ")
    print(final)

    #go through the list, 
    for word in words:
        check=0
        #if in incorrect -> don't add to wordCopy ... break
        for incorrectLetter in incorrect:
            if incorrectLetter in word:
                check=1
                continue

        #if word doesn't have correct letter -> don't add to wordCopy .. break
        for correctLetter in correct:
            if correctLetter not in word:
                check=1
                continue

        #if guess is different from final ->don't add to wordCopy .. break
        for x in range(0,5):
            if final[x] != "*":
                if final[x] != word[x]:
                    check=1
                    continue
        #TODO
        #remove words based on yellow letters

        #final step to remove words from list
        if(check==0):
            if word in wordsCopy:
                continue
            wordsCopy.append(word)

        
        
    words=wordsCopy.copy()
    wordsCopy=[]
        
    #print possible answers
    print(*words)
    print(len(words))