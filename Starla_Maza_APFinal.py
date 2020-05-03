'''Starla Maza AP Final
This program uses nine different functions in order to calculate your final for 
a class. The first function is where you will tell the program about whether you 
had a final,  don't have a final, already took your final, or if you didn't take 
it. Most of the other functions are asking what your quarter 1 and quarter 2 
grades they'll also ask what your final grade was if you took one. The other 
majority of the functions is the actual math to find your final grade. The 
eighth function converts the grade they got into a letter. Finally, in the last 
function it will ask the user whether they want to do the program agian.
'''
def calculator(): #Starts the program
    global final, have_final #Makes the 'final' and 'have_final' variable in this function able to be used throughout the whole program 
    have_final = raw_input('Does your class have a final? ') #Asks whether your class has a final or not in order to decide which code to use
    if have_final.upper() == 'YES' or have_final.upper() == 'Y': #Preforms this code if you inpuy 'yes' or 'y'
        final = raw_input('Did you take your final yet? ') #Asks whether or not you took your final to decide what functions to use 
        if final.upper() == 'YES' or final.upper() == 'Y': #The function will change the 'yes' input of 'final' to captialize then do the following code
            taken_final() #Goes to the function 'taken_final' and does that code. Once done with all of it, this chunck of code will finish
            print(str('You will have' + ' ' + str(F_Grade) + '%' + ' ' + 'or' + ' ' + str(letter))) #Prints a sentence with the percent grade you will have along with the letter
            again() #Goes to the 'again' function and preforms that code
        elif final.upper() == 'NO' or final.upper() == 'N': #The function will change the 'no' input of 'final' to captialize then do the following code
            havent_taken_final() #Goes to the function 'havent_taken_final' and does that code. Once done with all of it, this chunck of code will finish
            print(str('You will need' + ' ' + str(F_Grade) + '%' + ' ' + 'or' + ' ' + str(letter))) #Prints a sentence with the percent grade you will need along with the letter
            again() #Goes to the 'again' function and preforms that code
        else: #If none of your responses are inputted correctly then this code will execute 
            print("Sorry that's an invalid response..") #If the inputted response doesn't work this meassage will print
    elif have_final.upper() == 'NO' or have_final.upper() == 'N': #Preforms this code if you inpuy 'no' or 'n'
        no_final() #Goes to the 'no_final' function and preforms that code
        print(str('You will have' + ' ' + str(F_Grade) + '%' + ' ' + 'or' + ' ' + str(letter))) #Prints a sentence with the percent grade you will get along with the letter
        again() #Goes to the 'again' function and preforms that code
    else: #If none of your responses are inputted correctly then this code will execute 
        print("Sorry that's an invalid response..") #If the inputted response doesn't work this meassage will print
        
def taken_final(): #When this function is called it preforms it's code 
    global q1, q2, final #Makes the 'q1', 'q2', and 'final' variables in this function able to be used throughout the whole program 
    q1 = input('What was your quarter 1 grade? ') #Asks you to input your quarter 1 grade in order to calculate your final grade
    q2 = input('What was your quarter 2 grade? ') #Asks you to input your quarter 2 grade in order to calculate your final grade
    final = input('What did you get on you final? ') #Asks you to input the grade you got on your final in order to calculate your final grade
    final_grade() #Goes to the 'final_grade' function and preforms that code
    
def final_grade(): #When this function is called it preforms it's code 
    global F_Grade #Makes the 'F_Grade' variable in this function able to be used throughout the whole program 
    F_Grade = (.4*q1)+(.4*q2)+(.2*final) #This is the math used in order to calculate the final grade overall
    letter_grade() #Goes to the 'letter_grade' function and preforms that code
    
def havent_taken_final(): #When this function is called it preforms it's code 
    global q1, q2, want #Makes the 'q1', 'q2', and 'want' variable in this function able to be used throughout the whole program 
    q1 = input('What was your quarter 1 grade? ') #Asks you to input your quarter 1 grade in order to calculate your final grade
    q2 = input('What was your quarter 2 grade? ') #Asks you to input your quarter 2 grade in order to calculate your final grade
    want = input('What do you want your final grade to be? ' ) #Asks you to input the grade you want to get on your final in order to calculate your final grade
    want_grade() #Goes to the 'want_grade' function and preforms that code
    
def want_grade(): #When this function is called it preforms it's code 
    global F_Grade #Makes the 'F_Grade' variable in this function able to be used throughout the whole program 
    F_Grade = ((want-((q1*.4)+(q2*.4)))/20)*100 #This is the math used in order to calculate what you need on your final in order to get the grade you want
    letter_grade() #Goes to the 'letter_grade' function and preforms that code
    
def no_final(): #When this function is called it preforms it's code 
    global q1, q2 #Makes the 'q1' and 'q2' variable in this function able to be used throughout the whole program
    q1 = input('What was you quarter 1 grade? ') #Asks you to input your quarter 1 grade in order to calculate your final grade
    q2 = input('What was you quarter 2 grade? ') #Asks you to input your quarter 2 grade in order to calculate your final grade
    no_final_grade() #Goes to the 'no_final_grade' function and preforms that code
    
def no_final_grade(): #When this function is called it preforms it's code 
    global F_Grade #Makes the 'F_Grade' variable in this function able to be used throughout the whole program 
    F_Grade = (q1+q2)/2 #This is the math used in order to calculate your final grade in a class if you don't take a final
    letter_grade() #Goes to the 'letter_grade' function and preforms that code
    
def letter_grade(): #When this function is called it preforms it's code 
    global letter #Makes the 'letter' variable in this function able to be used throughout the whole program 
    letter = '' #An empty variable used to be changed later on
    if F_Grade <= 59.99: #The program checks if the number is less then 59.99 or equal to it and if it is it'll do the following code
        letter = 'F' #Changes letter to an F
    elif F_Grade <= 69.99: #The program checks if the number is between 60 and 69.99 or equal to them and if it is it'll do the following code
        letter = 'D' #Changes letter to a D
    elif F_Grade <= 79.99: #The program checks if the number is between 70 and 79.99 or equal to them and if it is it'll do the following code
        letter = 'C' #Changes letter to a C
    elif F_Grade <= 89.99: #The program checks if the number is between 80 and 89.99 or equal to them and if it is it'll do the following code
        letter = 'B' #Changes letter to a B
    elif F_Grade >= 90: #The program checks if the number is more then 90 or equal to it and if it is it'll do the following code
        letter = 'A' #Changes letter to an A

def again(): #When this function is called it preforms it's code 
    global another #Makes the 'another' variable in this function able to be used throughout the whole program 
    another = raw_input('Would you like to do another? ') #Asks if you'd like to use the program again
    if another.upper() == 'YES' or another.upper() == 'Y': #The function will change the 'yes' input of 'final' to captialize then do the following code
        calculator() #Goes to the first function in order to do the program over again
    elif another.upper() == 'NO' or another.upper() == 'N': #The function will change the 'no' input of 'final' to captialize then do the following code
        print('Try again whenever!!') #Prints a message telling you that you can do the program over again if you want to
    else: #If none of your responses are inputted correctly then this code will execute 
        print("Sorry that's an invalid response..") #If the inputted response doesn't work this meassage will print