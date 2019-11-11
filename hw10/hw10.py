# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:46:38 2019

@author: lydia
"""
class Complex:

#==========================================
# Purpose: 
#   A constructor that initializes a Complex object 
# Input Parameter(s): 
#   real is a numeric value that represents the real component of the complex number
#   imag is a numeric value that represents the imaginary component of the complex number    
# Return Value(s): 
#   None    
#==========================================

    def __init__(self, real, imag): 
        self.real = real
        self.imag = imag
    
#==========================================
# Purpose: 
#   A getter method to access the real component of the complex number     
# Input Parameter(s): 
#   None        
# Return Value(s):
#   A numeric value that represents the real component of the complex number        
#==========================================
    
    def get_real(self):
        return self.real

#==========================================
# Purpose: 
#   A getter method to access the imaginary component of the complex number     
# Input Parameter(s): 
#   None        
# Return Value(s):
#   A numeric value that represents the imaginary component of the complex number        
#==========================================

    def get_imag(self):
        return self.imag

#==========================================
# Purpose: 
#   A setter method to change the real component of the complex number        
# Input Parameter(s): 
#   new_real is a numeric value that represents the new real component of the
#    complex number        
# Return Value(s): 
#   None        
#==========================================
    
    def set_real(self, new_real):
        self.real = new_real
    
#==========================================
# Purpose: 
#   A setter method to change the imaginary component of the complex number        
# Input Parameter(s): 
#   new_imag is a numeric value that represents the new imaginary component of 
#    the complex number        
# Return Value(s): 
#   None        
#==========================================
    
    def set_imag(self, new_imag):
        self.imag = new_imag
    
#==========================================
# Purpose: 
#   Creates a string representation of the complex number        
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A string representation of the complex number        
#==========================================
    
    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + 'i'

#==========================================
# Purpose: 
#   Calculates the sum of two complex numbers        
# Input Parameter(s): 
#   other is a Complex object     
# Return Value(s): 
#   A new Complex object representing the sum of the complex numbers        
#==========================================

    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)
    
#==========================================
# Purpose:
#   Calculates the product of two complex numbers         
# Input Parameter(s): 
#   other is a Complex object     
# Return Value(s): 
#   A new Complex object representing the product of the complex numbers        
#==========================================
        
    def __mul__(self, other):
        ac = self.real*other.real
        bd = self.imag*other.imag
        ad = self.real*other.imag
        bc = self.imag*other.real
        return Complex(ac-bd, ad+bc)
    
#==========================================
# Purpose: 
#   Complares two Complex objects to see if they are equal, i.e., their 
#    real components are equal and their imaginary components are equal.          
# Input Parameter(s): 
#   other is a Complex object        
# Return Value(s): 
#   True if the two Complex objects are equal. False otherwise.         
#==========================================
        
    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False



class Employee:

#==========================================
# Purpose: 
#   A constructor that initializes an Employee object 
# Input Parameter(s): 
#   line is  a single string representing the line in the CSV file that 
#    contains the employee’s data    
# Return Value(s): 
#   None    
#==========================================

    def __init__(self, line): 
        lst = line.split(',')
        self.name = lst[0]
        self.position = lst[1]
        self.salary = float(lst[2])
        self.seniority = float(lst[3])
        self.value = float(lst[4])
        
#==========================================
# Purpose: 
#   Creates a string representation of the employee containing their name and position      
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A string containing the employee name and position        
#==========================================
    
    def __str__(self):
        return self.name + ', ' + self.position

#==========================================
# Purpose: 
#   Calculates an employee's net value, i.e., their value minus their salary     
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A floating point number which is the employee’s value minus their salary        
#==========================================

    def net_value(self):
        return self.value - self.salary

#==========================================
# Purpose: 
#   Complares two Employee objects to see if the left operand (self) has a lower
#    net_value than the right operand (other).          
# Input Parameter(s): 
#   other is an Employee object        
# Return Value(s): 
#   True if the left operand (self) has a lower net_value than the right operand (other). 
#   False otherwise.         
#==========================================

    def __lt__(self,other):
        if self.net_value() < other.net_value():
            return True
        else: 
            return False


class Branch:

#==========================================
# Purpose: 
#   A constructor that initializes a Branch object 
# Input Parameter(s): 
#   fname is a string representing the filename for the CSV where 
#    the branch information is stored.   
# Return Value(s): 
#   None    
#==========================================

    def __init__(self, fname):
        fp = open(fname)
        lines = fp.readlines()
        self.location = lines[0].split(',')[1]
        self.upkeep = float(lines[1].split(',')[1])
        self.team = []
        for i in range(3,len(lines)):
            self.team.append(Employee(lines[i]))
        fp.close()

#==========================================
# Purpose: 
#   Creates a string representation of the branch containing
#    the branch location and each employee        
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A string containing the location of the branch, 
#   followed by the string representation of each employee, 
#   separated by newlines         
#==========================================
    
    def __str__(self):
        emp_str=''
        for emp in self.team:
            emp_str += str(emp)
            emp_str += '\n'
        return self.location + '\n' + emp_str        

#==========================================
# Purpose: 
#   Calculates the branch profit, i.e., the sum of the net values of all 
#   the employees in the branch minus the upkeep of the branch.         
# Input Parameter(s): 
#   None   
# Return Value(s): 
#   A floating point number which is the sum of the net values 
#   of all the employees in the branch minus the upkeep of the branch.    
#==========================================

    def profit(self):
        total = 0
        for emp in self.team:
            total += emp.net_value()
        return total - self.upkeep    
  
#==========================================
# Purpose: 
#   Complares two branches to see if the left operand (self) has a lower profit
#   than the right operand (other).          
# Input Parameter(s): 
#   other is a Branch object        
# Return Value(s): 
#   True if the left operand (self) has a lower profit than the right operand (other). 
#   False otherwise.         
#==========================================

    def __lt__(self,other):
        if self.profit() < other.profit():
            return True
        else: 
            return False

#==========================================
# Purpose: 
#   Sorts the employees by their net value and removes 
#   the lowest num Employees from the team list          
# Input Parameter(s): 
#   num is an integer representing the number of employees that must be cut 
#   from the branch.      
# Return Value(s): 
#   None         
#==========================================
        
    def cut(self, num):
        self.team.sort()
        self.team = self.team[num:]

        
class Company:
    
#==========================================
# Purpose: 
#   A constructor that initializes a Company object 
# Input Parameter(s): 
#   name is a string representing the name of the company
#   branches is a list of Branch objects representing the branches of the company    
# Return Value(s): 
#   None    
#==========================================

    def __init__(self, name, branches):
        self.name = name
        self.branches = branches
        
#==========================================
# Purpose: 
#   Creates a string representation of the company including the company name,
#   all the branches, and the employees at each branch        
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   A string containing the company name, all the branches, and the employees
#   at each branch        
#==========================================
    
    def __str__(self):        
        br_str=''
        for branch in self.branches:
            br_str += str(branch)
            br_str += '\n' + '\n'
        return self.name + '\n' + '\n' + br_str
 
#==========================================
# Purpose: 
#   Finds the company branch with the lowest profit margin 
#   and cuts half (rounded down) of the employees from that branch.        
# Input Parameter(s): 
#   None        
# Return Value(s): 
#   None       
#==========================================    
    
    def synergize(self):
        low_branch = min(self.branches)
        low_branch.cut(len(low_branch.team)//2)
        

        