import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime, timedelta

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        
        self.library = Library()

        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.master, width=60, height=20)
        self.text_area.grid(row=0, column=0, columnspan=2)

        self.btn_members = tk.Button(self.master, text="Members", command=self.display_members)
        self.btn_members.grid(row=1, column=0, sticky="ew")

        self.btn_publications = tk.Button(self.master, text="Publications", command=self.display_publications)
        self.btn_publications.grid(row=1, column=1, sticky="ew")

        self.btn_books = tk.Button(self.master, text="Books", command=self.display_books)
        self.btn_books.grid(row=2, column=0, sticky="ew")

        self.btn_loans = tk.Button(self.master, text="Loans", command=self.display_loans)
        self.btn_loans.grid(row=2, column=1, sticky="ew")

        self.btn_popular_publications = tk.Button(self.master, text="Popular Publications", command=self.display_popular_publications)
        self.btn_popular_publications.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.btn_add_member = tk.Button(self.master, text="Add Member", command=self.add_member_to_library)
        self.btn_add_member.grid(row=4, column=0, sticky="ew")

        self.btn_add_book = tk.Button(self.master, text="Add Book", command=self.add_publication_to_library)
        self.btn_add_book.grid(row=4, column=1, sticky="ew")

        self.btn_add_book = tk.Button(self.master, text="Borrow Book", command=self.borrow_publication)
        self.btn_add_book.grid(row=5, column=0, sticky="ew")

        self.btn_add_book = tk.Button(self.master, text="Retuen Book", command=self.return_book)
        self.btn_add_book.grid(row=5, column=1, sticky="ew")


    def display_members(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "สมาชิกของห้องสมุด:\n")
        for member in self.library.members:
            self.text_area.insert(tk.END, f"ชื่อ: {member.name}, รหัส: {member.member_id}, อาชีพ: {member.details}\n")

    def display_publications(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "หนังสือในห้องสมุด(ตามชื่อ):\n")
        for publication in self.library.publications:
            self.text_area.insert(tk.END, f"ชื่อ: {publication.title}, นักเขียน: {publication.writer}, ปีที่พิมพ์: {publication.year}\n")

    def display_books(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "หนังสือในห้องสมุด(ตามรหัส):\n")
        for book in self.library.books:
            self.text_area.insert(tk.END, f"ISBN: {book.isbn}, ประเภทหนังสือ: {book.book_type}\n")

    def display_loans(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "หนังสือที่ถูกยืม:\n")
        for loan in self.library.loans:
            self.text_area.insert(tk.END, f"ผู้ยืม: {loan.member.name}, หนังสือ: {loan.publication.title}, วันที่ยืม: {loan.borrowing_date}, วันครบกำหนด: {loan.due_date}\n")

    def display_overdue_books(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "หนังสือที่ยังไม่ได้คืน:\n")
        today = datetime.today()
        for loan in self.library.loans:
            if loan.due_date < today:
                self.text_area.insert(tk.END, f"หนังสือ: {loan.publication.title}, วันครบกำหนด: {loan.due_date}\n")

    def display_popular_publications(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "สิ่งพิมพ์ยอดนิยม:\n")
        publication_count = {}
        for loan in self.library.loans:
            publication = loan.publication.title
            if publication in publication_count:
                publication_count[publication] += 1
            else:
                publication_count[publication] = 1
        
        sorted_publications = sorted(publication_count.items(), key=lambda x: x[1], reverse=True)[:5]
        for publication, count in sorted_publications:
            self.text_area.insert(tk.END, f"สิ่งตีพิมพ์: {publication}, จำนวนที่ถูกยืม: {count}\n")
    
    def display_publications(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "หนังสือในห้องสมุด(ตามชื่อ):\n")
        for publication in self.library.publications:
            self.text_area.insert(tk.END, f"ชื่อ: {publication.title}, นักเขียน: {publication.writer}, ปีที่พิมพ์: {publication.year}\n")

    def add_member_to_library(self):
        name = input("ชื่อของคุณ: ")
        member_id = input("รหัสของคุณ: ")
        details = input("อาชีพของคุณ: ")
        member = Member(name, member_id, details)
        self.library.add_member(member)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "สมัครเป็นสมาชิกชองห้องสมุดเรียบร้อย\n")
        self.display_members()

    def add_publication_to_library(self):
        title = input("ชื่อหนังสือที่ต้องการเพิ่ม: ")
        writer = input("ชื่อผู้เขียน: ")
        year = input("ปีที่ผลิต: ")
        publication = Publication(title, writer, year)
        self.library.add_publication(publication)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "เพิ่มหนังสือเสร็จสมบูรณ์\n")
        self.display_publications()
    
    def borrow_publication(self):
        member_name = input("ชื่อสมาชิก: ")
        publication_title = input("ชื่อหนังสือที่ต้องการยืม: ")

        # Search for member by name
        member = None
        for m in self.library.members:
            if m.name == member_name:
                member = m
                break

        if member is None:
            print("ไม่พบสมาชิก")
            return

        # Search for publication by title
        publication = None
        for p in self.library.publications:
            if p.title == publication_title:
                publication = p
                break

        if publication is None:
            print("ไม่พบหนังสือ")
            return

        # Get today's date and due date (assuming 14 days loan period)
        today = datetime.today()
        due_date = today + timedelta(days=14)

        # Create a loan object
        loan = Loan(member, publication, today, due_date)

        # Add the loan to the library
        self.library.add_loan(loan)

        # Update display
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"{member_name} ยืมหนังสือ {publication_title} สำเร็จ\n")
        self.display_loans()

    def return_book(self):
        member_name = input("ชื่อสมาชิก: ")
        publication_title = input("ชื่อหนังสือที่ต้องการยืม: ")

        # Search for the loan corresponding to the member and publication
        for loan in self.library.loans:
            if loan.member.name == member_name and loan.publication.title == publication_title:
                # Remove the loan from the library's loans list
                self.library.loans.remove(loan)
                # Update display
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f"{member_name} คืนหนังสือ {publication_title} สำเร็จ\n")
                self.display_loans()
                return

        # If the loan is not found
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "การยืมไม่สำเร็จ โปรดตรวจสอบชื่อสมาชิกหรือชื่อหนังสืออีกครั้ง\n")


class Member:
    def __init__(self, name, member_id, details):
        self.name = name
        self.member_id = member_id
        self.details = details

class Publication:
    def __init__(self, title, writer, year):
        self.title = title
        self.writer = writer
        self.year = year

class Book:
    def __init__(self, isbn, book_type):
        self.isbn = isbn
        self.book_type = book_type

class Loan:
    def __init__(self, member, publication, borrowing_date, due_date):
        self.member = member
        self.publication = publication
        self.borrowing_date = borrowing_date
        self.due_date = due_date

class Library:
    def __init__(self):
        self.members = []
        self.publications = []
        self.books = []
        self.loans = []

        # Adding members
        member1 = Member("นฤกวินทร์", 101, "นักศึกษา")
        member2 = Member("พีรนัฐ", 102, "โปรแกรมเมอร์")
        self.add_member(member1)
        self.add_member(member2)

        # Adding publications
        publication1 = Publication("Python Programming", "Guido van Rossum", 2020)
        publication2 = Publication("Introduction to Algorithms", "Thomas H. Cormen", 2009)
        self.add_publication(publication1)
        self.add_publication(publication2)

        # Adding books
        book1 = Book("978-0134852836", "Textbook")
        book2 = Book("978-0262033848", "Technical")
        self.add_book(book1)
        self.add_book(book2)

        # Adding loans
        today = datetime.today()
        due_date = today + timedelta(days=14)  # Assuming 14 days loan period

        loan1 = Loan(member1, publication1, today, due_date)
        loan2 = Loan(member2, publication2, today, due_date)
        self.add_loan(loan1)
        self.add_loan(loan2)

    def add_member(self, member):
        self.members.append(member)

    def add_publication(self, publication):
        self.publications.append(publication)

    def add_book(self, book):
        self.books.append(book)

    def add_loan(self, loan):
        self.loans.append(loan)


def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
