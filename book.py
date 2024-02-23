# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 03:04:27 2023

@author: yekta
"""

import sqlite3                                                                     # for sql
import datetime                                                                    # for date, time for books infromation

class Book:                                                                        # book part
    def __init__(self, title, authors, publisher, count=2):
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.count = count

    def __repr__(self):
        pass
    
    
    @staticmethod
    def getBook(isbn):                                                            # get book 
        conn = sqlite3.connect("regbookinfoac.db")                                 # connect with db
        c = conn.cursor()                                                          # we need to use it every time when we use sql
        
        
        c.execute("""
                  select bookID 
                  from books
                  where isbn = :is          
                  """,{'is':isbn})
        result = c.fetchone()                                                      # its for retrieves the next row in slq 
        
        conn.commit()                                                              # we need to us this part as well for sql
        conn.close()                                                               # db connection closed
        return result[0]
        
    def checkAvailableBook(bookId):                                              # available books
        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()

        c.execute("""SELECT available 
                  from books
                  WHERE bookID = :bid          
                  """,{'bid':bookId})

        avabl = c.fetchone()[0]                                                    # if available value is null it gonna be available 
        conn.close()                                                               # db connection closed
        return avabl
    
    
    def updateAvailable(number, bookId):                                         # update available
        import sqlite3  
                                                         # import sql
        conn = sqlite3.connect("regbookinfoac.db")                                 # connect db
        c = conn.cursor()                                                       
        c.execute("""Update books set
                      available = :navabl
                      WHERE bookID = :bid
                      """ , {'navabl' : number, 'bid':bookId})
        conn.commit()
        conn.close()     
                                                                                   # db connection closed
        
    def reserveBook(std_id, isbn):                                                # reserve book part
        print(std_id)
        print(isbn)
        
        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()

        bookId = Book.getBook(isbn)

        
        avabl2 = Book.checkAvailableBook(bookId)                                    # available book check
        if avabl2 == 0:
            print("Not available book")
            return
        
        
        
        if c.fetchone() is not None:
            print("You already have it")
            return

        date  = datetime.date.today()
        date_str = date.strftime("%d/%m/%Y")    

                                                                                    # Add the reservation to the database
        c.execute("""INSERT INTO reservation (id,bookID,resDate)                 
                  VALUES (:id, :bookID, :resDate)""",
                  {'id': std_id, 'bookID': bookId, 'resDate': date_str})
        conn.commit()

        
        Book.updateAvailable(avabl2 - 1, bookId)                                    # available book count updated 
        print("Already reserved")

        
        conn.close()                                                                # db connection closed 