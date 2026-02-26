# books = [
#     {"id": "101", "title": "Python Basics", "is_available": True},
#     {"id": "102", "title": "Data Structures", "is_available": True},
#     {"id": "103", "title": "Machine Learning", "is_available": False}
# ]
# members = [
#     {"member_id": "M1", "name": "Alice", "borrowed_books": []},
#     {"member_id": "M2", "name": "Bob", "borrowed_books": []}
# ]
# class library:
#     def lend_book(self,id, mem_id):
#         member = None
#         for m in members:
#             if m["member_id"] == mem_id:
#                 member = m
#                 break
                
#         if member is None:
#             print("Member not found")
#             return
            
#         book = None
#         for b in books:
#             if b["id"] == id and b["is_available"] == True:
#                 book = b
#                 break
#         if book is None:
#             print("book not found")
#             return
#         if not book["is_available"]:
#             print("Book is currently unavailable.")
#             return

#         # Update State
#         book["is_available"] = False
#         member["borrowed_books"].append(id)
#         print(f"Book '{book['title']}' is borrowed by {member['name']}")
# obj = library()   
# obj.lend_book("102", "M2")
# print(members)



class Library:

    def __init__(self, books, members):
        self.books = books
        self.members = members

    def lend_book(self, book_id, mem_id):

        # ----- Find Member -----
        member = None
        for m in self.members:
            if m["member_id"] == mem_id:
                member = m
                break

        if member is None:
            print("Member not found.")
            return

        # ----- Find Book (by ID only) -----
        book = None
        for b in self.books:
            if b["id"] == book_id:
                book = b
                break

        if book is None:
            print("Book not found.")
            return

        # ----- Check Availability -----
        if not book["is_available"]:
            print("Book is currently unavailable.")
            return

        # ----- Prevent Double Borrowing -----
        if book_id in member["borrowed_books"]:
            print("Member already borrowed this book.")
            return

        # ----- Update State -----
        book["is_available"] = False
        member["borrowed_books"].append(book_id)

        print(f"Book '{book['title']}' is borrowed by {member['name']}")
        
books = [
    {"id": "101", "title": "Python Basics", "is_available": True},
    {"id": "102", "title": "Data Structures", "is_available": True},
    {"id": "103", "title": "Machine Learning", "is_available": False}
]

members = [
    {"member_id": "M1", "name": "Alice", "borrowed_books": []},
    {"member_id": "M2", "name": "Bob", "borrowed_books": []}
]

library = Library(books, members)

library.lend_book("102", "M2")
library.lend_book("103", "M2")
library.lend_book("999", "M2")
library.lend_book("101", "M9")

print(members)