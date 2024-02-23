# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 02:43:12 2023

@author: yekta
"""


from librarian import Librarian                                                       # from librarianpy find librarian class
from user import User                                                                 # from userpy find user
from student import Student                                                           # from studentpy find student

class LibManSystem:                                                                  # main system 
    def __init__(self):
        while True:
            LibManSystem.login()   
    
    @classmethod       
    def login(cls):                                                                  # login part with classmethot because we can use this feature
                                                                                      # more than 1 time thats why i choose it
        print("Welcome Library System")
        req = input("Select (l) or (r) for Login or Register :")                      # register and login part
        if (req == 'l'):
            uid = input("Enter user id: ")
           
            try:
                if uid != '':
                    pass
                else:
                    raise TypeError
                    
            except TypeError:                                                         # we cant pass here with type error
                print('Enter Username')
                return cls.login();
            password = input("Enter password: ")
           
            try:
                if password != '':
                    pass
                else:
                    raise TypeError
            except TypeError:
                print('Enter Password ')
                return cls.login();
            
            try:
                result = User.authenticate(uid, password)                             # connect authenticate part for userpy
             
                if result['IsExist'] == True:                                         # if everything fine it gonna show id
                    print(f"Welcome {result['f_name']}....")
                    print(result['std_id']) 
                                                                                      # it gonna show menu by user type
                    if result['usrType'] == 'Student':
                        print("Student")
                        m = Student(result['std_id'],result['clsNumber'])
                        m.menu()
                  
                    elif result['usrType'] == 'Librarian':
                        print('Librarian')
                        m = Librarian(result['std_id'])
                        m.menu()
                   
                    elif result['usrType'] == 'Staff':
                        print('Staff')
                        m = Student(result['std_id'],None,result['dep'])
                        m.menu()
                   
                    else:
                        print("Wrong")
                
                else:
                    print("Wrong data")
          
            except ValueError:
                print("Try again")
      
        elif (req == 'r'):
            print("Registration")
            User.registration();
      
        else:
            print("Logged out")                                                        # if we text wrong in first process we gonna logout
            raise SystemExit

s = LibManSystem()


