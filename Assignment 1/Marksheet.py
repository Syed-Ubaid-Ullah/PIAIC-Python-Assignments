name = input('Enter Student Name : ')
father_name = input("Enter Father's Name : ")

sub1=float(input('Enter Marks of Subject 1 out of 100 : '))
sub2=float(input('Enter Marks of Subject 2 out of 100 : '))
sub3=float(input('Enter Marks of Subject 3 out of 100 : '))
sub4=float(input('Enter Marks of Subject 4 out of 100 : '))
sub5=float(input('Enter Marks of Subject 5 out of 100 : '))
sub6=float(input('Enter Marks of Subject 6 out of 100 : '))
sub7=float(input('Enter Marks of Subject 7 out of 50  : '))
total_marks=sub1+sub2+sub3+sub4+sub5+sub6+sub7
percentage=(total_marks*100)/650

print('-----------------------------------------')
print("Student Name     :"+name)
print("Father's Name    :"+father_name)
print('-----------------------------------------')
print('| Subjects   | Total  |   Obtained      |')
print('-----------------------------------------')
print('| Subject 1  '+'|  100   |    '+str(sub1)+'         |')
print('| Subject 2  '+'|  100   |    '+str(sub2)+'         |')
print('| Subject 3  '+'|  100   |    '+str(sub3)+'         |')
print('| Subject 4  '+'|  100   |    '+str(sub4)+'         |')
print('| Subject 5  '+'|  100   |    '+str(sub5)+'         |')
print('| Subject 6  '+'|  100   |    '+str(sub6)+'         |')
print('| Subject 7  '+'|  50    |    '+str(sub7)+'         |')
print('-----------------------------------------')
print('|Total Marks Obtained Out of 650 : '+str(total_marks)+'|')
print('-----------------------------------------')

if percentage>=88:
    print('Percentage: '+str(percentage))
    print('Grade     : A')
    print('Remarks   : Well Done')
elif percentage>=70 and percentage<=87:
    print('Percentage: '+str(percentage))
    print('Grade     : B')
    print('Remarks   : Good')
elif percentage>=55 and percentage<=69:
    print('Percentage: '+str(percentage))
    print('Grade     : C')
    print('Remarks   : Better Luck Next Time')
elif percentage>=40 and percentage<=54:
    print('Percentage: '+str(percentage))
    print('Grade     : D')
    print('Remarks   : Must Work Hard')
elif percentage<=39:
    print('Percentage: '+str(percentage))
    print('Grade     : F')
    print('Remarks   : Sorry You Have Failed!')

print('-----------------------------------------')