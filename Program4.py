#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 4
#
#  File Name:         Program4.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          09-26-2019
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapters # 1-3
#
#  Description:
#     This program is designed to calculate an employee's total net,gross,and overtime pay
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    BaseHours = 40
    OtMultiplier = 1.5

    IDnumber = int(input('Enter the employee ID number: '))
    PayRate = float(input('Enter the hourly pay rate: '))
    hours = float(input('Enter the number of hours worked: '))
    Parking = 25.00
    
    if hours > BaseHours:
        RegHours = 40.0
        OvertimeHours = hours - BaseHours
        OvertimePay = OvertimeHours * PayRate * OtMultiplier
        GrossPay = BaseHours * PayRate + OvertimePay
        RegPay = BaseHours * PayRate
    else:
        GrossPay = hours * PayRate
        OvertimeHours = 0.0
        RegPay = hours * PayRate
        OvertimePay = 0.0
        RegHours = hours
    if GrossPay > 600.00:
        IncomeTax = GrossPay * 0.105
        NetPay = GrossPay - IncomeTax - Parking
        Deductions = IncomeTax + Parking
    else:
        NetPay = GrossPay - Parking
        Deductions = Parking
    
    print('ID number is', IDnumber)
    print('The pay rate is', PayRate)
    print('The regular hours are', RegHours)
    print('The overtime hours are', OvertimeHours)
    print('The total hours are', hours)
    print('The regular pay is', RegPay)
    print('The overtime pay is', OvertimePay)
    print('The gross pay is', GrossPay)
    print('The deductions are', Deductions)
    print('The net pay is', NetPay)
    
    
        
    
    
    
    
    
    
    
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Course:   Programming Fundamentals I')
    print('Program:  Four')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
