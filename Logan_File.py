'''
logan_faulstich_final_project:
This program will let the user input their quarter grades and the semestar grade
they want, and will calulate the final grade that they need to get for their
finals.
'''

from tkinter import *
top = Tk()

first_grade = Label(top, text="Enter your first grade here:")
second_grade = Label(top, text="Enter your second grade here:")

first_entry = Entry(top)
second_entry = Entry(top)

first_grade.grid(row=0, sticky=E)
second_grade.grid(row=1, sticky=E)

first_entry = Entry(row=0, column=1)
second_entry = Entry(row=1, column=1)




top.mainloop()


'''
Yes = ('Yes', 'yes', 'Y', 'YES', 'y', 'ya', 'YA', 'Ya')
No = ('No', 'no', 'N', 'NO', 'n', 'Nah', 'nah', 'NAH')


def Final():
    print('Welcome to The Final Grade Calculator. Please follow the necessary instructions to calculate to the Final grade that you will need.')
    Class = raw_input('Please enter the class name: ')
    
    Q1 = input('Please enter your Quarter 1 Grade: ')
    Q2 = input('Please enter your Quarter 2 Grade: ')
    Sem = input('Please enter your Semestar grade that you want: ')
    Final = (((Sem - ((Q1 * 0.4) + (Q2 * 0.4)))/20)*100)
    print(Final)
  
'''  
