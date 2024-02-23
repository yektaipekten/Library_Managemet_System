# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 02:12:43 2023

@author: yekta
"""

from user import User                                                                     # from userpy find user class
from book import Book                                                                     # from bookpy find book class
from account import Account                                                               # from accountpy find account class
from libraryDatabase import LibraryDatabase                                               # from libDB find libDB

class Student(User): 
    def __init__(self,std_id,clsNumber):                                                 # Student class values
        self.std_id = std_id
        self.clsNumber = clsNumber

    def menu(self):                                                                       # Menu for student users 
        print(f"""Student menu
                1. Option 1 ~ Return a book
                2. Option 2 ~ Borrowed books
                3. Option 3 ~ Add book
                4. Option 4 ~ User information
                5. Option 5 ~ Search Book
                6. Option 6 ~ Reservation 
                q. Return
                
                """)
        while True:                                                                       # When its going to be true we can choose a option
            c = input("\nSelect Option (1-6|q): ")
            choice = {"1" :self.f_opt1,
                  "2" :self.f_opt2,
                  "3" :self.f_opt3,
                  "4" :self.f_opt4,
                  "5": self.f_opt5,
                  "6": self.f_opt6,
                  "q" :"q"}.get(c,"invalid")        
            if choice == "q":                                                              # Quit part
                print('Bye..')
                break
            elif choice != "invalid":                                                      # If text something without options it gonna be invalid
                choice()
            else:
                print("Try again...")

    def f_opt1(self):
        print("Option 1 ~ Return a book")                                                  # It shows return a book
        try:
            isbn = str(input('Enter ISBN: '))                                              # Input isbn for check book
            if isbn == '':
                print("Please enter isbn ")
            else:
                if isbn in self.account.l_books_borrowed:                                  # it gonna check it from account.py because borrowed book part in there
                    self.account.l_books_borrowed.remove(isbn)
                else:
                    print("No borrowed book")
        except:
            print("Pleace try again")
            
    def f_opt2(self):
        print("Option 2 ~ Borrowed books")                                                 # It shows borrowed book from user
        Account.printBorrowedBooks(self.std_id)
        
    def f_opt3(self):                                                                     # it gonna connect to bookpy for get book
        print("Option 3 ~ Add book")
        isbn = input('Please enter isbn: ')
        bookID = Book.getBook(isbn)
        LibraryDatabase.borrowBook(self.std_id, bookID) 
                                                                                           # this part is main part for add book

    def f_opt4(self):                                                                     # find user info with sql
        
        print("Option 4 ~ User information")
        import sqlite3       
        conn = sqlite3.connect("regbookinfoac.db")
        c = conn.cursor()
        
        c.execute(""" 
                  select books.isbn,books.title, borrow.borrowDate,borrow.lastDate 
                  from books,borrow
                  where borrow.bookID = books.bookID
                  and borrow.id = :uId
                  """,{'uId':self.std_id})
                  
        books = c.fetchall()
        
        if not books:                                                                       # check borrowed books
            print('No book')
            print('')
        else:   
            print('')
            
            print('* List Of Borowed Book*')
            
            
            for book in books:
                print(f"{book[0]} - {book[1]} - {book[2]} - {book[3]}")
            print('...')
        
        conn.commit()
        conn.close()   
        
    def f_opt5(self):                                                                      # its for search books with any data
        print("Option 5 ~ Search Book")
        data = input('Enter book information: ')
        LibraryDatabase.searchBook(data)
        

    def f_opt6(self):                                                                      # reservation for book
        print("Option 7 ~ Reservation ")
        isbn = input('Enter isbn: ')

        Book.reserveBook(self.std_id, isbn)
        
    def __repr__(self):
        return f"{self.f}\n {self.account}"
    