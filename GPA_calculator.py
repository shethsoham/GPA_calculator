"GPA CALCULATOR "
"""
Your final score will determine your letter grade. The score is calculated by dividing the number of points you
have earned divided by the total number of points available in the course.
Grade Percentage Range
A 100% to 92.0%
AB < 92.0% to 88.0%
B < 88.0% to 80.0%
BC < 80.0% to 78.0%
C < 78.0% to 70.0%
CD < 70.0% to 68.0%
D < 68.0% to 60.0%
F < 60.0%
"""

def Gpa_calculator() :

    percentage = float(input("How much percentage you are getting ?"))

    if (percentage >= 92 ):
        print("You have got a A grade and your pointer is 4")
        subject_pointer = 4.00
        return subject_pointer

    elif (percentage>=88):
        print("You have got a grade AB and your pointer is 3.5 ")
        subject_pointer = 3.50
        return subject_pointer

    elif(percentage>= 80):
        print("You have got a grade B and your pointer is 3")
        subject_pointer = 3.00
        return subject_pointer

    elif(percentage>=78):
        print("you have got a grade BC and your pointer is 2.5")
        subject_pointer = 2.50
        return subject_pointer
    elif (percentage >= 70):
        print("you have got a grade C and your pointer is 2.0")
        subject_pointer = 2.00
        return subject_pointer
    elif (percentage >= 68):
        print("you have got a grade CD and your pointer is 1.5")
        subject_pointer = 1.50
        return subject_pointer
    elif (percentage >= 60):
        print("you have got a grade D and your pointer is 1.0")
        subject_pointer = 1.00
        return subject_pointer
    else:
        print("Your grade is F and you have failed ")
        subject_pointer = 0.00
        return subject_pointer

    return subject_pointer



subjects_taken = int(input("how many subjects have you taken?"))

addition_subject_pointer=0
for subject_taken in range (1,subjects_taken+1):
    subject = input("enter the subject name : ")
    print(subject)
    subject_pointer= Gpa_calculator()
    addition_subject_pointer = addition_subject_pointer + subject_pointer

print("additional subject pointer is ",addition_subject_pointer)


GPA = addition_subject_pointer/subjects_taken
print("Your overall GPA is",GPA)












