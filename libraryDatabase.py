# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 02:51:29 2023

@author: yekta
"""

import sqlite3                                                                      # for sql
import datetime                                                                     # date, time for books informations
from book import Book                                                               # from bookpy find book class

class LibraryDatabase:                                                            # DB main part
    
    def __init__(self):
        pass
                          
    @staticmethod                                                                   # we dont need to use this part continually so we can use staticmethod
    def searchBook(data):
        conn = sqlite3.connect("regbookinfoac.db")                                  # connect to informationsDB
        c = conn.cursor()
        data = '%'+data+'%'                                                         # its for search book with any data
        c.execute("""SELECT title,authors,isbn 
                  from books
                  WHERE title like :d
                  or authors like :d
                  or ISBN like :d                  
                  """,{'d':data})
                  
        result = c.fetchall()                                                       # its for get a value from sql folder
        print('ISBN - Title - Authors')
        
        i = 1
        for book in result:
            print(f"{i} - {book[2]} - {book[0]} - {book[1]}")
            i = i +1
        conn.commit()                                                               # we need to use this part whenever we use sql 
        conn.close()                                                                # its for invalid data from sql part
        
    @staticmethod
    def borrowBook(userId,bookId):                                                 # borrow book part
        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()
        
        c.execute("""SELECT books.isbn, borrow.bookID, borrow.id
                  from books,borrow
                  WHERE borrow.bookID = books.bookID
                  and borrow.id = :uId
                  """,{'uId':userId})
                  
        books = c.fetchone()                                                        # its for retrieves the next row in slq 
        print(books)                                                                
        
        
        if not books:
            print('You can borrow this book')
        else:   
            print("You have already borrowed the books") 
                        
        
        avabl = Book.checkAvailableBook(bookId)                                      # check to available book
        date  = datetime.date.today()                                                
        date_str = date.strftime("%d/%m/%Y")                                         # date info
        exp = date + datetime.timedelta(days = 21)                                   # last day calculating 
        exp_str = exp.strftime("%d/%m/%Y")                                           # last date 
        
        if avabl > 0 :                                                               # if book is available user can borrow it
            c.execute("""INSERT into borrow(id,bookID, borrowDate, lastDate)
                      VALUES(:uid,:bid,:bdate,:lDate)              
                      """,{'uid':userId, 'bid':bookId, 'bdate':date_str, 'lDate':exp_str})
            conn.commit()
            conn.close()                      
            Book.updateAvailable(avabl-1,bookId)                                     # borrow book process successfull
            print('Borrowed successful')

        else:
            print('Not available')    