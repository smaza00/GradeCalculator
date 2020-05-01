'''
logan_faulstich_final_project:
This program will let the user input their quarter grades and the semestar grade
they want, and will calulate the final grade that they need to get for their
finals.
'''

from tkinter import *

root = Tk()


Q1Grade = DoubleVar() #This is the variable for the first quarter grade
Q2Grade = DoubleVar() #This is the variable for the second quarter grade
FinalGrade = DoubleVar() #This is the variable for the final quarter grade when the user says yes to taking the final
FinalGrade_no = DoubleVar() #This is the variable for the final quarter grade when the user says no the taking the final
letter = " " #This stores the letter grade for later use
F_Grade = 0 #This sets the final grade to 0 so it will be set as an integer.
welcomeText = Text(root, width = 60, height = 2) 

def final_grade(): #Goes to the 'final_grade' function and preforms that code
    global F_Grade
    F_Grade = (.4*Q1Grade.get())+(.4*Q2Grade.get())+(.2*FinalGrade.get()) #This is the math used in order to calculate the final grade overall
    print(F_Grade)
    letter_grade() #Goes to the 'letter_grade' function and preforms that code

def final_grade_no():
    global F_Grade
    F_Grade = ((FinalGrade_no.get()-((Q1Grade.get()*.4)+(Q2Grade.get()*.4)))/20)*100 #This is the math used in order to calculate what you need on your final in order to get the grade you want
    if F_Grade <= 0:
        F_Grade = 0
    letter_grade_no() #Goes to the 'letter_grade' function and preforms that code

def letter_grade(): #Goes to the 'letter_grade' function and preforms that code
    global letter
    
    if F_Grade <= 59: #The program checks if the number is less then 59.99 or equal to it and if it is it'll do the following code
        letter = 'F' #Changes letter to an F
    if F_Grade <= 69 and F_Grade >= 60: #The program checks if the number is between 60 and 69.99 or equal to them and if it is it'll do the following code
        letter = 'D' #Changes letter to a D
    if F_Grade <= 79 and F_Grade >= 70: #The program checks if the number is between 70 and 79.99 or equal to them and if it is it'll do the following code
        letter = 'C' #Changes letter to a C
    if F_Grade <= 89 and F_Grade >= 80: #The program checks if the number is between 80 and 89.99 or equal to them and if it is it'll do the following code
        letter = 'B' #Changes letter to a B
    if F_Grade >= 90: #The program checks if the number is more then 90 or equal to it and if it is it'll do the following code
        letter = 'A' #Changes letter to an A
    print(letter)
    show_grade()

def letter_grade_no(): #Goes to the 'letter_grade' function and preforms that code
    global letter
    
    if F_Grade <= 59: #The program checks if the number is less then 59.99 or equal to it and if it is it'll do the following code
        letter = 'F' #Changes letter to an F
    if F_Grade <= 69 and F_Grade >= 60: #The program checks if the number is between 60 and 69.99 or equal to them and if it is it'll do the following code
        letter = 'D' #Changes letter to a D
    if F_Grade <= 79 and F_Grade >= 70: #The program checks if the number is between 70 and 79.99 or equal to them and if it is it'll do the following code
        letter = 'C' #Changes letter to a C
    if F_Grade <= 89 and F_Grade >= 80: #The program checks if the number is between 80 and 89.99 or equal to them and if it is it'll do the following code
        letter = 'B' #Changes letter to a B
    if F_Grade >= 90: #The program checks if the number is more then 90 or equal to it and if it is it'll do the following code
        letter = 'A' #Changes letter to an A
    print(letter)
    show_grade_no()

def show_grade():
    global letter
    global F_Grade
    global welcomeText
    showgrade = Text(root, width = 60, height = 3)
    showgrade.insert(INSERT, "Your final grade is " + str(int(F_Grade)) + "%.\nYour letter grade is " + letter + ".\nWould you like to use the program again?")        
    showgrade.config(state=DISABLED)
    showgrade.pack()
    continue_Button = Button(root, text="Continue", command = lambda:[wipe_show(), Welcome()])
    continue_Button.pack(side=LEFT)
    quitButton = Button(root, text="Quit", command=quit)
    quitButton.pack(side = LEFT)
    def wipe_show():
        global welcomeText
        showgrade.destroy()
        continue_Button.destroy()
        quitButton.destroy()
        welcomeText = Text(root, width = 60, height = 2)

def show_grade_no():
    global letter
    global F_Grade
    global welcomeText
    showgradeno = Text(root, width = 60, height = 3)
    if F_Grade <= 0:
        showgradeno.insert(INSERT, "Sorry, the grade you wanted can not be achieved.\nWould you like to use the program again?")
    else:
        showgradeno.insert(INSERT, "The grade you need on your final is " + str(int(F_Grade)) + "%.\nYour letter grade is " + letter + ".\nWould you like to use the program again?")        
    showgradeno.config(state=DISABLED)
    showgradeno.pack()
    continue_Button = Button(root, text="Continue", command = lambda:[wipe_show(), Welcome()])
    continue_Button.pack(side=LEFT)
    quitButton = Button(root, text="Quit", command=quit)
    quitButton.pack(side = LEFT)
    def wipe_show():
        global welcomeText
        showgradeno.destroy()
        continue_Button.destroy()
        quitButton.destroy()
        welcomeText = Text(root, width = 60, height = 2)

def calculator_1():
    global welcomeText
    welcomeText.config(state=NORMAL)
    welcomeText.delete('1.0', END)
    welcomeText.insert(INSERT, "Have you taken your final?")
    welcomeText.config(state=DISABLED)
    yesButtonfinal = Button(root, text="Yes", command=lambda:[wipe_calculator(), final_questions_Q1()])
    yesButtonfinal.pack(side=LEFT)
    noButtonfinal = Button(root, text="No", command=lambda:[wipe_calculator(), final_questions_Q1_no()])
    noButtonfinal.pack(side=LEFT)
    def wipe_calculator():
        yesButtonfinal.destroy()
        noButtonfinal.destroy()

  

def final_questions_Q1(): #When this function is called it performs it's code 
    global welcomeText
    welcomeText.destroy()
    questionTextQ1 = Text(root, width = 60, height = 2)
    questionTextQ1.insert(INSERT, "What is your first quarter grade?\n")
    questionTextQ1.insert(INSERT, "Please only use the percent grade. Do not include %")
    questionTextQ1.config(state=DISABLED)
    questionTextQ1.pack()
    Q1Text = Entry(root, width = 40, textvariable = Q1Grade)
    Q1Text.pack()
    nextButton_Q1 = Button(root, text="Next", command = lambda:[wipe_Q1(), final_questions_Q2()])
    nextButton_Q1.pack(side=LEFT)
    def wipe_Q1():
        print(Q1Grade.get())
        print(Q1Grade)
        questionTextQ1.destroy()
        Q1Text.destroy()
        nextButton_Q1.destroy()

def final_questions_Q1_no():
    global welcomeText
    welcomeText.destroy()
    questionTextQ1no = Text(root, width = 60, height = 2)
    questionTextQ1no.insert(INSERT, "What is your first quarter grade?\n")
    questionTextQ1no.insert(INSERT, "Please only use the percent grade. Do not include %")
    questionTextQ1no.config(state=DISABLED)
    questionTextQ1no.pack()
    Q1Textno = Entry(root, width = 40, textvariable = Q1Grade)
    Q1Textno.pack()
    nextButton_Q1no = Button(root, text="Next", command = lambda:[wipe_Q1_no(), final_questions_Q2_no()])
    nextButton_Q1no.pack(side=LEFT)
    def wipe_Q1_no():
        print(Q1Grade.get())
        print(Q1Grade)
        questionTextQ1no.destroy()
        Q1Textno.destroy()
        nextButton_Q1no.destroy()


def final_questions_Q2():
    questionTextQ2 = Text(root, width = 60, height = 2)
    questionTextQ2.insert(INSERT, "What is your second quarter grade?\n")
    questionTextQ2.insert(INSERT, "Please only use the percent grade. Do not include %")
    questionTextQ2.config(state=DISABLED)
    questionTextQ2.pack()
    Q2Text = Entry(root, width = 40, textvariable = Q2Grade)
    Q2Text.pack()
    nextButton_Q2 = Button(root, text="Next", command = lambda:[wipe_Q2(), final_questions_final()])
    nextButton_Q2.pack(side=LEFT)
    def wipe_Q2():
        print(Q2Grade.get())
        questionTextQ2.destroy()
        Q2Text.destroy()
        nextButton_Q2.destroy()

def final_questions_Q2_no():
    questionTextQ2no = Text(root, width = 60, height = 2)
    questionTextQ2no.insert(INSERT, "What is your second quarter grade?\n")
    questionTextQ2no.insert(INSERT, "Please only use the percent grade. Do not include %")
    questionTextQ2no.config(state=DISABLED)
    questionTextQ2no.pack()
    Q2Textno = Entry(root, width = 40, textvariable = Q2Grade)
    Q2Textno.pack()
    nextButton_Q2no = Button(root, text="Next", command = lambda:[wipe_Q2_no(), final_questions_final_no()])
    nextButton_Q2no.pack(side=LEFT)
    def wipe_Q2_no():
        print(Q2Grade.get())
        questionTextQ2no.destroy()
        Q2Textno.destroy()
        nextButton_Q2no.destroy()

def final_questions_final():
    questionTextFinal = Text(root, width = 60, height = 2)
    questionTextFinal.insert(INSERT, "What is the grade you got on your final?\n")
    questionTextFinal.insert(INSERT, "Please only use the percent grade. Do not include %")
    questionTextFinal.config(state=DISABLED)
    questionTextFinal.pack()
    FinalText = Entry(root, width = 40, textvariable = FinalGrade)
    FinalText.pack()
    nextButton_Final = Button(root, text="Next", command = lambda:[wipe_Final(), final_grade()])
    nextButton_Final.pack(side=LEFT)
    def wipe_Final():
        print(FinalGrade.get())
        questionTextFinal.destroy()
        FinalText.destroy()
        nextButton_Final.destroy()

def final_questions_final_no():
    questionTextFinalno = Text(root, width = 60, height = 2)
    questionTextFinalno.insert(INSERT, "What would you like your final grade to be?\n")
    questionTextFinalno.insert(INSERT, "Please only use the percent grade. Do not include %")
    questionTextFinalno.config(state=DISABLED)
    questionTextFinalno.pack()
    FinalTextno = Entry(root, width = 40, textvariable = FinalGrade_no)
    FinalTextno.pack()
    nextButton_Finalno = Button(root, text="Next", command = lambda:[wipe_Final_no(), final_grade_no()])
    nextButton_Finalno.pack(side=LEFT)
    def wipe_Final_no():
        print(FinalGrade.get())
        questionTextFinalno.destroy()
        FinalTextno.destroy()
        nextButton_Finalno.destroy()


def Welcome():
    global welcomeText
    welcomeText.insert(INSERT, "Welcome to the Grade Calculator\n")
    welcomeText.insert(INSERT, "Press Start to Continue")
    welcomeText.config(state=DISABLED)
    welcomeText.pack()
    startButton = Button(root, text="Start", command=lambda:[buttons_delete(), calculator_1()])
    startButton.pack(side=LEFT)
    quitButton = Button(root, text="Quit")
    quitButton.pack(side=LEFT)
    def buttons_delete():
        startButton.destroy()
        quitButton.destroy()

 
Welcome()
root.mainloop()
