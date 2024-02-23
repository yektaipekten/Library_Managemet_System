# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 02:32:30 2023

@author: yekta
"""



import sqlite3                                                                     # for sql
import datetime                                                                    # date, time for informations in db


class Account:                                                                    # accont part
    
    def __init__(self,a_id, password, f_name,l_books_borrowed=[],l_books_reserved=[],    
                 history_return=None,l_lost_Books = None, acc_fine=None):
        self.a_id = a_id
        self.password = password
        self.f_name = f_name
        self.l_books_borrowed = l_books_borrowed
        self.l_books_reserved = l_books_reserved
        self.history_return = history_return
        self.l_lost_Books = l_lost_Books
        self.acc_fine = acc_fine      
    
    @staticmethod          
    def cal_fine(std_id, isbn):                                                   # calculating fine
        pass
 

    def printBorrowedBooks(userid):
        
        conn = sqlite3.connect("regbookinfoac.db")                                 # connect bd
        c = conn.cursor()
        c.execute(""" 
                  select borrow.id, borrow.bookID,  books.title, borrow.lastDate 
                  from borrow, books
                  where books.bookID = borrow.bookID 
                  and id = :id
                  """,{'id':userid})
      
                  
        details = c.fetchall()                                                     # its for retrieves the next row in slq 
        print(details)
        
    def __repr__(self):
        
            
        return f"""{'*'*20}
id: {self.a_id}
books_borrowed: {self.l_books_borrowed}
    """