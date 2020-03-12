def letter_grade():
    word = 'Y'
    while word == 'Y':
        q1 = input('What was your quarter 1 grade? ')
        q2 = input('What was your quarter 2 grade? ')
        q3 = raw_input('Did you take your final yet? ')
        if q3 == 'yes':
            final = input('What did you get on you final? ')
            answer = (.4*q1)+(.4*q2)+(.2*final)
            letter = 0
            if answer <= 59:
                letter = 'F'
            elif answer <= 69:
                letter = 'D'
            elif answer <= 79:
                letter = 'C'
            elif answer <= 89:
                letter = 'B'
            elif answer >= 90:
                letter = 'A'
            
            print(str('You will have' + ' ' + str(answer) + '%' + ' ' + 'or' + ' ' + str(letter)))
            
            
            
            word = raw_input('Would you like to do another? Y/N ')
        elif q3 == 'no':
            whole = input('What do you want your final grade to be? ')
            final1 = ((whole-((q1*.4)+(q2*.4)))/20)*100
            print(str('You will need' + ' ' + str(final1) + '%'))
            word = raw_input('Would you like to do another? Y/N ')