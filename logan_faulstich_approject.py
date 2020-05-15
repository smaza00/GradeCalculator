'''
This program will let the user input their quarter grades and the semestar grade
they want, and will calulate the final grade that they need to get for their
finals.
'''

from tkinter import * #imports tkinter for window building

root = Tk() #Sets root to a Tkinter window
root.title("Semestar Grade Calculator") #Sets the title to Grade Calculator
root.geometry("400x300") #Sets the geometry of the Tkinter window



Q1Grade = DoubleVar() #This is the variable for the first quarter grade
Q2Grade = DoubleVar() #This is the variable for the second quarter grade
FinalGrade = DoubleVar() #This is the variable for the final quarter grade when the user says yes to taking the final
letter = " " #This stores the letter grade for later use
F_Grade = 0 #This sets the final grade to 0 so it will be set as an integer.
welcomeText = Text(root, width = 40, height = 2) #This sets the welcome text which is for the start of the program
FinalQuestion = " " #Sets a blank space for the answer to the final question

def Welcome(): #This is the welcome window when you start the program
    global welcomeText #Uses the global welcomeText
    welcomeText.insert(INSERT, "Welcome to the Grade Calculator\nPress Start to Continue") #Inserts the welcome text
    welcomeText.config(state=DISABLED) #Disables the user from interacting with the textbox
    welcomeText.pack(side=TOP) #Packs the welcome text into the window
    startButton = Button(root, text="Start", command=lambda:[buttons_delete(), ask_final()]) #Button to start the program
    startButton.pack(side=TOP) #Packs the start button into the window
    quitButton = Button(root, text="Quit", command=quit) #Button to quit the program
    quitButton.pack(side=TOP) #Packs the quit button into the window
    def buttons_delete(): #Deletes the un-needed buttons
        startButton.destroy() #Delete the start button
        quitButton.destroy() #Delete the quit button

def ask_final(): #Asks if the user has taken their final
    welcomeText.config(state=NORMAL) #Sets the welcome text to the normal state
    welcomeText.delete('1.0', END) #Deletes the previous message in welcome text
    welcomeText.insert(INSERT, "Have you taken your final?") #Inserts the new text
    welcomeText.config(state=DISABLED) #Disables the user from interacting with the textbox
    yesButtonfinal = Button(root, text="Yes", command=lambda:[wipe_ask_final(), final_questions_yes()]) #Button if the user says yes to taking their final
    yesButtonfinal.pack(side=TOP) #Packs the yes button into the window
    noButtonfinal = Button(root, text="No", command=lambda:[wipe_ask_final(), final_questions_no()]) #Button if the user says no to taking their final
    noButtonfinal.pack(side=TOP) #Packs the no button into the window
    def wipe_ask_final(): #Wipes the un-needed buttons 
        yesButtonfinal.destroy() #Destroys the yes button
        noButtonfinal.destroy() #Destroys the no button
    def final_questions_yes(): #Activates if the user says yes
        global FinalQuestion #Uses the global FinalQuestion
        FinalQuestion = "Y" #Sets FinalQuestion to yes if the user has taken the final
        print(FinalQuestion) #Prints FinalQuestion for developer use
        final_questions_Q1() #Activates the first question
    def final_questions_no(): #Activates if the user says no
        global FinalQuestion #Uses the global FinalQuestion
        FinalQuestion = "N" #Sets Finalquestion to no if the user has not taken the final
        print(FinalQuestion) #Prints FinalQuestion for developer use
        final_questions_Q1() #Activates the first question

def final_questions_Q1(): #Asks the user what their first quarter grade was
    global welcomeText #Uses the gloabl welcomeText
    welcomeText.destroy() #Destroys the welomce text
    questionTextQ1 = Text(root, width = 60, height = 2) #Questiontext is built to reset word size
    questionTextQ1.insert(INSERT, "What is your first quarter grade?\nPlease only use the percent grade. Do not include %")  #Inserts user's first question
    questionTextQ1.config(state=DISABLED) #Disables the user from interacting with the textbox
    questionTextQ1.pack() #PAcks the question text into the window
    Q1Text = Entry(root, width = 40, textvariable = Q1Grade) #Sets an entry for the first quarter grade
    Q1Text.pack() #PAcks the first quarter entry into the window
    nextButton_Q1 = Button(root, text="Next", command = lambda:[wipe_Q1(), final_questions_Q2()]) #Nextbutton is to continue the program
    nextButton_Q1.pack(side=TOP) #Packs the next button into the window
    def wipe_Q1(): #Wipes the first quarter question 
        print(Q1Grade.get()) #Prints the first quarter grade for developer use
        questionTextQ1.destroy() #Destroys the first question text
        Q1Text.destroy() #Destroys the first question entry
        nextButton_Q1.destroy() #Destroys the next button

def final_questions_Q2(): #Asks the user what their second quarter was
    questionTextQ2 = Text(root, width = 60, height = 2) #Questiontext is built
    questionTextQ2.insert(INSERT, "What is your second quarter grade?\nPlease only use the percent grade. Do not include %") #Inserts user's second question
    questionTextQ2.config(state=DISABLED) #Disables the user from interacting with the textbox
    questionTextQ2.pack() #Packs the second question into the window
    Q2Text = Entry(root, width = 40, textvariable = Q2Grade) #Sets the entry for the second quarter grade
    Q2Text.pack() #Packs the second quarter entry into the window
    nextButton_Q2 = Button(root, text="Next", command = lambda:[wipe_Q2(), final_questions_final()]) #Inserts the next button to continue to the next question
    nextButton_Q2.pack(side=TOP) #Packs the next question button into the window
    def wipe_Q2(): #Wipes the second question's un-needed functions
        print(Q2Grade.get()) #Prints the second quarter for developer use
        questionTextQ2.destroy() #Destroys the second question textbox
        Q2Text.destroy() #Destroys the second question entry
        nextButton_Q2.destroy() #Destroys the next button

def final_questions_final(): #Asks the user about their final/semestar grade depending on the FinalQuestion
    if FinalQuestion == "Y": #Activates if the user says yes to taking the final
        questionTextFinal = Text(root, width = 60, height = 2) #Inserts a textbox for asking questions
        questionTextFinal.insert(INSERT, "What is the grade you got on your final?\nPlease only use the percent grade. Do not include %") #Asks the user's final grade
        questionTextFinal.config(state=DISABLED) #Disables the user from interacting with the textbox
        questionTextFinal.pack() #Packs the textbox into the window
    if FinalQuestion == "N": #Activates if the user says no to taking the final
        questionTextFinal = Text(root, width = 60, height = 2) #Inserts a textbox for asking questions
        questionTextFinal.insert(INSERT, "What would you like your semestar grade to be?\nPlease only use the percent grade. Do not include %") #Asks the user what they want their semestar grade to be
        questionTextFinal.config(state=DISABLED) #Disables the user from interacting with the textbox
        questionTextFinal.pack() #Packs the textbox into the window
    FinalText = Entry(root, width = 40, textvariable = FinalGrade) #Maks an entry for the user's answer
    FinalText.pack() #Packs the entry into the window
    nextButton_Final = Button(root, text="Next", command = lambda:[wipe_Final(), final_grade_choose()]) #Inserts a next button to continue the program
    nextButton_Final.pack(side=TOP) #Packs the next button into the window
    def wipe_Final(): #Wipes the un-needed functinos
        print(FinalGrade.get()) #Prints the final grade for developer use
        questionTextFinal.destroy() #Destroys the textbox
        FinalText.destroy() #Destroys the entry
        nextButton_Final.destroy() #Destroys the next button
    def final_grade_choose(): #Activates the calculation program
        if FinalQuestion == "Y": #Activates if the user has taken their final
            final_grade() #Activates the final calculation program
        elif FinalQuestion == "N": #Activates if the user has not taken their final
            final_grade_no() #Activates the final calculation program

'''Starla Maza's Program'''

def final_grade(): #Goes to the 'final_grade' function and preforms that code
    global Q1Grade #Uses the global Quarter One grade
    global Q2Grade #Uses the global Quarter Two grade
    global F_Grade #Uses the global final grade 
    F_Grade = (.4*Q1Grade.get())+(.4*Q2Grade.get())+(.2*FinalGrade.get()) #This is the math used in order to calculate the final grade overall
    if F_Grade <= 0: #This if statement unallows the use of negative numbers
        F_Grade = 0 #Sets the Final Grade to 0 if number is negative
    print(F_Grade) #prints the Final grade for developer use
    letter_grade() #Goes to the 'letter_grade' function and preforms that code

def final_grade_no(): #Goes to the 'final_grade_no' function and preforms that code
    global Q1Grade #Uses the global Quarter One grade
    global Q2Grade #Uses the global Quarter Two grade
    global F_Grade #Uses the global final grade 
    F_Grade = ((FinalGrade.get()-((Q1Grade.get()*.4)+(Q2Grade.get()*.4)))/20)*100 #This is the math used in order to calculate what you need on your final in order to get the grade you want
    if F_Grade <= 0: #This if statement unallows the use of negative numbers
        F_Grade = 0 #Sets the Final Grade to 0 if number is negative
    letter_grade() #Goes to the 'letter_grade' function and preforms that code

def letter_grade(): #Goes to the 'letter_grade' function and preforms that code
    global F_Grade #Uses the global final grade 
    global letter #Uses the global letter grade
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
    print(letter) #Prints the letter grade for developer use
    show_grade() #Activates the show grade window

'''Logan Faulstich's Program'''

def show_grade(): #Goes to the 'show_grade' function and preforms that code
    global FinalQuestion #Uses the global FinalQuestion
    global F_Grade #Uses the global final grade 
    global letter #Uses the global letter grade
    if FinalQuestion == "Y": #Activates if the user has taken their final
        showgrade = Text(root, width = 60, height = 3) #Makes a text box to show the user's grade
        showgrade.insert(INSERT, "Your final grade is " + str(int(F_Grade)) + "%.\nYour letter grade is " + letter + ".\nWould you like to use the program again?") #Shows the grade to the user 
        showgrade.config(state=DISABLED) #Disables the user from interacting with the textbox
        showgrade.pack() #Packs the textbox into the window 
    elif FinalQuestion == "N": #Activates if the user has taken their final
        showgrade = Text(root, width = 60, height = 3) #Makes a text box to show the user's grade
        showgrade.insert(INSERT, "The grade you need on your final is " + str(int(F_Grade)) + "%.\nYour letter grade is " + letter + ".\nWould you like to use the program again?") 
        showgrade.config(state=DISABLED) #Disables the user from interacting with the textbox
        showgrade.pack() #Packs the textbox into the window
    continue_Button = Button(root, text="Continue", command = lambda:[wipe_show(), Welcome()]) #Creates the continue button
    continue_Button.pack(side=TOP) #Packs the continue button into the window
    quitButton = Button(root, text="Quit", command=quit) #Creates the quit button
    quitButton.pack(side = TOP) #Packs the quit button
    def wipe_show(): #Wipes the show grade window
        global welcomeText #Uses the global windowtext
        showgrade.destroy() #Destroys the textbox
        continue_Button.destroy() #Destroys the continue button
        quitButton.destroy() #Destroys the quit button
        welcomeText = Text(root, width = 60, height = 2) #Recreates the welcome text


 
Welcome() #Starts the program
root.mainloop()
