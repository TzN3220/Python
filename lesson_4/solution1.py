import string
import os
import sys
homework= (sys.argv[0])
solution= (sys.argv[1])
hwFile = open("homework.txt","r")
with open("solution.txt", 'w') as file:
    file.write(" ")
exe=hwFile.readline()
exe=exe.split()
exe.reverse() 
while(exe!=[]):
    if len(exe)==3:
        if exe[0].isdigit() and exe[2].isdigit():
            num1=(int)(exe[0])
            num2=(int)(exe[2])
            operator=exe[1]
            exe.append('=')
            if operator == "+":
                exe.append((str)(num1+num2))
                exe.reverse() 
                
                with open("solution.txt", 'a') as file:
                    file.write(" ".join(exe)+"\n")
            elif operator == '-':
                if num1-num2 < 0:
                    exe.append("-")
                    exe.append(str(abs(num1-num2)))
                else:
                    exe.append((str)(num1-num2))
                exe.reverse() 
                with open("solution.txt", 'a') as file:
                    file.write(" ".join(exe)+"\n")
            elif operator == '*':
                if num1*num2 < 0:
                    exe.append("-")
                    exe.append(str(abs(num1*num2)))
                else:
                    exe.append((str)(num1*num2))
                exe.reverse() 
                with open("solution.txt", 'a') as file:
                    file.write(" ".join(exe)+"\n")
            elif operator == '/':
                if num2==0:
                    with open("solution.txt", 'a') as file:
                        file.write("divided by zero\n")
                else:   
                    line.append((str)(num1/num2))
                    line.reverse() 
                    with open("solution.txt", 'a') as file:
                        file.write(" ".join(exe)+"\n")
            else:
                with open("solution.txt", 'a') as file:
                    file.write("error! Invalid operator\n")
                   
        else:
             with open("solution.txt", 'a') as file:
                    file.write("Invalid parameter\n")
        with open("solution.txt", 'a') as file:
                    file.write("good\n")   
    else:
        with open("solution.txt", 'a') as file:
                    file.write("you are missing somthing---\n")
    exe=hwFile.readline()
    exe=exe.split()
    exe.reverse()        