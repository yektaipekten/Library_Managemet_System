# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 03:22:42 2023

@author: yekta
"""

import sqlite3                                                                    # for sql

class Librarian:                                                                 # librarian part
    def __init__(self,f_name):
        self.f_name = f_name

    def menu(self):                                                               # menu for librarian
        print(f"""Librarian homepage
1. Option 1 ~ Add Book
2. Option 2 ~ Delete Book
3. Option 3 ~ Update User 
4. Option 4 ~ Search
5. Option 5 ~ User Record
q. Return

""")
        while True:
            c = input("\nSelect Option (1-5|q): ")
            choice = {"1" :self.f_opt1,
                  "2" :self.f_opt2,
                  "3" :self.f_opt3,
                  "4" :self.f_opt4,
                  "5" :self.f_opt5,
                  "q" :"q"}.get(c,"invalid")        
            if choice == "q":
                print('Take care...')
                break
            elif choice != "invalid":
                choice()
            else:
                print("Try again")

    def f_opt1(self):                                                            # add book part a bit long because librarian has to 
        print("1 - Add Book")                                                     # enter every info about books
        conn = sqlite3.connect('regbookinfoac.db')                                # connect to db
        c= conn.cursor()                                                          # we need to use this part every time whenever we use sql folder
       
        bookID = input("BookID")                                                  # enter values for each book
        title = input("Title")
        authors = input("Authors name ")
        average_rating = input("Average rating ")
        isbn = input("ISBN ")
        isbn13 = input("ISBN 13 ")
        language_code = input("Language_code ")
        num_pages = input("Num_pages")
        ratings_count = input("Ratings_count ")
        text_reviews_count = input("Text_reviews_count ")
        publication_date = input("Publication_date ")
        publisher = input("Publisher ")
        available = input("Available ")
                                                                                  # sql main part for add book
        c.execute(
        """INSERT INTO books(bookID,title,authors,average_rating,isbn,isbn13,language_code,num_pages,ratings_count,
        text_reviews_count,publication_date,publisher,available)
        VALUES(:bid,:title,:authors,:average_rating,:isbn,:isbn13,:language_code,:num_pages,:ratings_count,
        :text_reviews_count,:publication_date,:publisher,:available)""",
        {'bid': bookID, 'title':title,'authors':authors,'average_rating':average_rating, 'isbn':isbn,'isbn13':isbn13
        ,'language_code':language_code,'num_pages':num_pages,'ratings_count':ratings_count,
        'text_reviews_count':text_reviews_count,
        'publication_date':publication_date,'publisher':publisher,'available':available})
       
        conn.commit()                                                             # we need to use this part every time whenever we use sql folder
        conn.close()                                                              # its for invalid data from sql part
        print("Successfully added")
        
    def f_opt2(self):                                                            # remove book part
        print("2 - Delete Book")
                
        conn = sqlite3.connect('regbookinfoac.db')                                #connect bd
        c= conn.cursor()
        
        isbn = input("Enter the isbn of the book you want to remove: ")           # remove with isbn
        
        c.execute("DELETE FROM books WHERE isbn = :isbn",{'isbn':isbn})
            
        conn.commit()
        conn.close()
        print("Deleted")
        
    def f_opt3(self):                                                            # user account updating
        print("3 - Update User ")
        
        userid = input("Enter user id ")                                          # with user id
        
        conn = sqlite3.connect("regbookinfoac.db")                                # connect bd
        c = conn.cursor() 
        c.execute(""" 
                  select password 
                  from register
                  where id = :id
                  """,{'id':userid})
      
                  
        details = c.fetchone()                                                    # its for retrieves the next row in slq 
        print(details)
        
        newpassword = input("New password: ")
        
        c.execute("UPDATE register SET password = :password WHERE id = :id", {'password': newpassword,'id': userid})
        conn.commit()
        conn.close()
        print("Updated")
        
        
    def f_opt4(self):                                                            # search book part
        print("4 - Search")
        
        isbn3 = input("Search with isbn ")                                        # search with isbn

        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()
        
        c.execute(""" 
                  select bookID, title, authors 
                  from books
                  where isbn = :isbn
                  """,{'isbn':isbn3})
                  
        books = c.fetchone()
        print(books)
        
        
    def f_opt5(self):                                                            # user record
        print("5 - User Record")
        
        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()
        ID = input("Enter userid: ")
        c.execute(""" 
                  select borrowID,id,bookID,borrowDate,lastDate,returnDate 
                  from borrow
                  where id = :id
                  """,{'id':ID})
                  
        record = c.fetchall()                                                     # for show every informations in same row from sql
        print(record)
    
    def __repr__(self):
        pass