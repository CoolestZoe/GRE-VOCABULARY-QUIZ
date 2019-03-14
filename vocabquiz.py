import tkinter as tk
import random
import sys
class Category:
    def __init__(self,filein,fileout):#contains two parameters:input file and output file
        wordlist=filein.readlines()#read the document into a list of lines
        #instance variables include the output file, list of lines, dictionary of advance level difficulty, common level and basic level, and include a list containing wrong words
        self.fileout=fileout
        self.wordlist=wordlist
        self.advance={}
        self.common={}
        self.basic={}
        self.wrong=[]
        check1=False#create flag variable
        for item in self.wordlist:
            if item[:]=="Common Words\n":
                check1=True
            elif check1==True and item[:]!="\n":
                wordkey=item.split(" (")#split the item by "(" into the word and its meaning
                self.common[wordkey[0]]="("+wordkey[1]
            if item[:]=="\n":
                check1=False
        check2=False
        for item in self.wordlist:
            if item[:]=="Basic Words\n":
                check2=True
            elif check2==True and item[:]!="\n":
                wordkey=item.split(" (")
                self.basic[wordkey[0]]="("+wordkey[1]
            if item[:]=="\n":
                check2=False
        check3=False
        for item in self.wordlist:
            if item[:]=="Advanced Words\n":
                check3=True
            elif check3==True and item[:]!="\n":
                wordkey=item.split(" (")
                self.advance[wordkey[0]]="("+wordkey[1]
            elif item[:]=="\n":
                check3=False
        

    def spelling(self):#create spelling mode
        #interact with user let them choose differnt level
        print("Welcome to the GRE vocabulary spelling mode")
        n=input("Please choose a mode by typing 1,2 or 3 (1:common, 2:basic, 3:advance):")
        while(n!="1" and n!="2" and n!="3"):#make sure the unexpected answer won't go through
            print("I don't understand. Please type 1, 2 or 3.")
            n=input("Your pick:")


        while True:#check if the input is a valid positive integer in a while loop
            try:
                questionNum=int(input("please type a number that represents the questions you want to take:")) 
                assert(questionNum>0)
                break
            except:
                print("not valid")


        right=0#keep track of score 


        for i in range (questionNum):#start asking question
            if n=="1":
                answer=list(self.common.keys())[random.randint(0,len(self.common)-1)]
                meaning=self.common[answer]
            if n=="2":
                answer=list(self.basic.keys())[random.randint(0,len(self.basic)-1)]
                meaning=self.basic[answer]
            if n=="3":
                answer=list(self.advance.keys())[random.randint(0,len(self.advance)-1)]
                meaning=self.advance[answer]
            print("Question",i+1,meaning)
            userInput=input("Please spell the word of the meaning showing above:")
            if userInput != answer:#if wrong write the wrong words to a file
                print("You are wrong, the correct answer is:",answer)
                self.wrong.append(answer+meaning)
            else:
                print("You are right")
                right+=1#add one if correct


                
        print("Your score is",right,"/",questionNum)
        print("Thanks for studying with me!")
        self.writeWrong(self.fileout)


    def multipleChoice(self):#create multiple choice function

        print("Welcome to the GRE vocabulary multiple choice mode")

        n=input("Please choose a mode by typing 1,2 or 3 (1:common, 2:basic, 3:advance):")


        while(n!="1" and n!="2" and n!="3"):
            print("I don't understand. Please type 1, 2 or 3.")
            n=input("Your pick:")
        right=0


        while True:#also check if the number is a positive integer
            try:
                questionNum=int(input("please type a number that represents the questions you want to take:")) 
                assert(questionNum>0)
                break
            except:
                print("not valid")


        for num in range (questionNum):#start asking question
            if n=="1":
                answer=list(self.common.keys())[random.randint(0,len(self.common)-1)]#randomly choose a word from dictionary
                meaning=self.common[answer]
            if n=="2":
                answer=list(self.basic.keys())[random.randint(0,len(self.basic)-1)]
                meaning=self.basic[answer]
            if n=="3":
                answer=list(self.advance.keys())[random.randint(0,len(self.advance)-1)]
                meaning=self.advance[answer]
            print("Question",num+1,meaning)



            choices=[answer]#a list that contains the correct answer and other choices
            if n=="1":
                answerlist=list(self.common.keys())
            if n=="2":
                answerlist=list(self.basic.keys())
            if n=="3":
                answerlist=list(self.advance.keys())
            answerlist.remove(answer)#remove the correct answer from the list in case repetition



            if len(answerlist)>3:#randomly choose three words from the dictionary
                for i in range(3):
                    idx=random.randint(0,len(answerlist)-1)
                    choices.append(answerlist[idx])
                    answerlist.pop(idx)
            else:
                choices+=answerlist


            correctPos = random.randint(0, len(choices) - 1)#randomly generate the correct answer's positon
            tmp = choices[correctPos]
            choices[correctPos] = choices[0]
            choices[0] = tmp

            answerList = 'abcd'#start print the choices
            for i in range(len(choices)):
                print(answerList[i] + ") " + choices[i])
    
            userAnswer=input("Your answer: ")#ask user for their answer
            while(userAnswer!="a" and userAnswer!="b" and userAnswer!="c" and userAnswer!="d"):
                userAnswer=input("I don't understand. Please type a, b, c, or d.Your answer: ")
        

            if userAnswer==answerList[choices.index(answer)]:
                print("Correct!")
                right+=1

            else:
                print("Sorry, the correct answer was","'",answer,"'")
                self.wrong.append(answer+meaning)#add wrong words and its meaning to the list
                
        
        print("Your final score was: ",right, "/",questionNum)
        print("Thanks for studying with me!")
        self.writeWrong(self.fileout)


    def writeWrong(self,fileout):#create a write wrong method that takes wrong words to a output file with its meaning
        for item in self.wrong:
            fileout.write(item)
    def quit(self):
        self.root.destroy()


def main():
    fin=open(sys.argv[1],"r")#read input file
    fout=open(sys.argv[2],"w")#read output file

    c1=Category(fin,fout)#create a class object
    #create GUI
    root = tk.Tk()
    l1 = tk.Label(root, text="please click spelling or multiple choice mode")
    f1 = tk.Frame(root)
    l1.grid(row=0, column=1)
    f1.grid(row=1, column=1, sticky="nsew")
    

    b1 = tk.Button(f1, text="spelling",command=c1.spelling)
    b2 = tk.Button(f1, text="multiple choice", command=c1.multipleChoice)
    b1.pack(side="top")
    b2.pack(side="top")
    root.mainloop()


    fin.close()#close file
    fout.close()
main()

   
