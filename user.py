# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 03:24:35 2023

@author: yekta
"""

import sqlite3

class User :
    def __init__(self,f,s,a=None):
        self.f = f
        self.s = s
        self.account = a
           
    def __rpr__(self):
        pass

    @staticmethod                   
    def authenticate(uid,password):                                                             # authenticate from DB system
        
        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()
                                                                                                  # its for check informations matching
        c.execute("""                                                                             
                  select password,f_name,std_id,usrType,clsNumber,department 
                  from register
                  where std_id = :userid
                  and password = :pass
                  """,{'userid':uid , 'pass':password})
        result = c.fetchone()
        
        if not result:
            return {'IsExist' : False}
        else:
            return {'IsExist' : True , 'password': result[0], 'f_name': result[1] , 'std_id': result[2], 
                    'usrType': result[3], 'clsNumber':result[4], 'dep' : result[5]}
        
        conn.commit()
        conn.close()
                    


    @staticmethod    
    def registration():                                                                         # register part for student 
    
        conn = sqlite3.connect('regbookinfoac.db')                                               # connect to register DB
        c= conn.cursor()
        
        std_id = input("Enter student id ")
        password = input("Enter password ")
        f_name = input("Enter name ")
        usrType = input("Enter userType ")
        
        c.execute(                                                                               # if informations not to match with any value registration gonna be okay
            """CREATE TABLE IF NOT EXISTS register(
            id text,
            password text,
            f_name text,
            std_id text,
            usrType text,
            l_books_borrowed text,
            l_books_reserved text,
            his_return text,
            l_lost_books text,
            acc_fine integer
            )"""
            )
    
        c.execute("""INSERT INTO register(password,f_name,std_id,usrType) 
                  VALUES(:pass,:fn,:si,:ut)""",
                  {'pass': password, 'fn':f_name, 'si':std_id, 'ut':usrType })
        
        conn.commit()
        conn.close()
        print("Registered")
