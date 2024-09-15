import random
from datetime import datetime, timedelta

class Book:
    """
    Represents a book in the library system.
    """

    def __init__(self, title, author, year, publisher, num_copies, publication_date):
        """
        Initialize a new Book instance.
        """
        self.book_id = self._generate_book_id()
        self.set_title(title)
        self.set_author(author)
        self.set_year(year)
        self.set_publisher(publisher)
        self.set_num_copies(num_copies)
        self.set_publication_date(publication_date)
        self.available_copies = num_copies

    def _generate_book_id(self):
        """Generate a random book ID."""
        return f"BK{random.randint(10000, 99999)}"

    def set_title(self, title):
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string")
        self.title = title

    def set_author(self, author):
        if not isinstance(author, str) or not author:
            raise ValueError("Author must be a non-empty string")
        self.author = author

    def set_year(self, year):
        if not isinstance(year, int) or year < 0:
            raise ValueError("Year must be a positive integer")
        self.year = year

    def set_publisher(self, publisher):
        if not isinstance(publisher, str) or not publisher:
            raise ValueError("Publisher must be a non-empty string")
        self.publisher = publisher

    def set_num_copies(self, num_copies):
        if not isinstance(num_copies, int) or num_copies < 0:
            raise ValueError("Number of copies must be a non-negative integer")
        self.num_copies = num_copies

    def set_publication_date(self, publication_date):
        if not isinstance(publication_date, datetime):
            raise ValueError("Publication date must be a datetime object")
        self.publication_date = publication_date

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_num_copies(self):
        return self.num_copies

    def get_available_copies(self):
        return self.available_copies

    def get_publication_date(self):
        return self.publication_date

class BookList:
    """
    Manages a collection of Book objects.
    """

    def __init__(self):
        """
        Initialize a new BookList instance.
        """
        self.books = {}

    def add_book(self, book):
        """
        Add a book to the collection.
        """
        if not isinstance(book, Book):
            raise ValueError("Only Book objects can be added to the collection")
        self.books[book.book_id] = book

    def search_book(self, query, search_type):
        """
        Search for a book by title, author, publisher, or publication date.
        """
        results = []
        for book in self.books.values():
            if search_type == "title" and query.lower() in book.get_title().lower():
                results.append(book)
            elif search_type == "author" and query.lower() in book.get_author().lower():
                results.append(book)
            elif search_type == "publisher" and query.lower() in book.get_publisher().lower():
                results.append(book)
            elif search_type == "publication_date" and query == book.get_publication_date().strftime("%Y-%m-%d"):
                results.append(book)
        return results

    def remove_book(self, title):
        """
        Remove a book from the collection by its title.
        """
        for book_id, book in list(self.books.items()):
            if book.get_title().lower() == title.lower():
                del self.books[book_id]
                return True
        raise ValueError(f"No book found with title: {title}")

    def get_total_books(self):
        """
        Return the total number of books in the collection.
        """
        return len(self.books)

class User:
    """
    Represents a user in the library system.
    """

    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, date_of_birth):
        """
        Initialize a new User instance.
        """
        self.username = username
        self.set_firstname(firstname)
        self.set_surname(surname)
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.set_email(email)
        self.set_date_of_birth(date_of_birth)

    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_house_number(self):
        return self.house_number

    def get_street_name(self):
        return self.street_name

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_firstname(self, firstname):
        if not isinstance(firstname, str) or not firstname:
            raise ValueError("First name must be a non-empty string")
        self.firstname = firstname

    def set_surname(self, surname):
        if not isinstance(surname, str) or not surname:
            raise ValueError("Surname must be a non-empty string")
        self.surname = surname

    def set_email(self, email):
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("Invalid email address")
        self.email = email

    def set_date_of_birth(self, date_of_birth):
        if not isinstance(date_of_birth, datetime):
            raise ValueError("Date of birth must be a datetime object")
        self.date_of_birth = date_of_birth

class UserList:
    """
    Manages a collection of User objects.
    """

    def __init__(self):
        """
        Initialize a new UserList instance.
        """
        self.users = {}

    def add_user(self, user):
        """
        Add a user to the collection.
        """
        if not isinstance(user, User):
            raise ValueError("Only User objects can be added to the collection")
        self.users[user.get_username()] = user

    def remove_user(self, firstname):
        """
        Remove a user from the collection by first name.
        """
        matching_users = [user for user in self.users.values() if user.get_firstname().lower() == firstname.lower()]
        if len(matching_users) > 1:
            raise ValueError(f"Multiple users found with first name: {firstname}. Please use a unique identifier.")
        elif len(matching_users) == 0:
            raise ValueError(f"No user found with first name: {firstname}")
        else:
            del self.users[matching_users[0].get_username()]

    def get_user_count(self):
        """
        Return the total number of users in the collection.
        """
        return len(self.users)

    def get_user_by_username(self, username):
        """
        Return a user's details by username.
        """
        if username not in self.users:
            raise ValueError(f"No user found with username: {username}")
        return self.users[username]

class Loans:
    """
    Manages book loans in the library system.
    """

    def __init__(self):
        """
        Initialize a new Loans instance.
        """
        self.loans = {}  # {username: {book_id: due_date}}

    def borrow_book(self, user, book, days=14):
        """
        Assign a book to a user.
        """
        if not isinstance(user, User) or not isinstance(book, Book):
            raise ValueError("Invalid user or book object")
        
        if book.get_available_copies() <= 0:
            raise ValueError("No available copies of this book")
        
        username = user.get_username()
        book_id = book.book_id
        
        if username not in self.loans:
            self.loans[username] = {}
        
        if book_id in self.loans[username]:
            raise ValueError("User already has this book on loan")
        
        due_date = datetime.now() + timedelta(days=days)
        self.loans[username][book_id] = due_date
        book.available_copies -= 1

    def return_book(self, user, book):
        """
        Un-assign a book previously assigned to a user.
        """
        username = user.get_username()
        book_id = book.book_id
        
        if username not in self.loans or book_id not in self.loans[username]:
            raise ValueError("This book is not on loan to this user")
        
        del self.loans[username][book_id]
        book.available_copies += 1

    def get_user_loan_count(self, user):
        """
        Count and return the total number of books a user is currently borrowing.
        """
        username = user.get_username()
        return len(self.loans.get(username, {}))

    def get_overdue_books(self, user_list):
        """
        Print out all overdue books along with the users' username and first name.
        """
        overdue_loans = []
        current_date = datetime.now()
        
        for username, books in self.loans.items():
            user = user_list.get_user_by_username(username)
            for book_id, due_date in books.items():
                if current_date > due_date:
                    overdue_loans.append({
                        'username': username,
                        'firstname': user.get_firstname(),
                        'book_id': book_id,
                        'due_date': due_date
                    })
        
        return overdue_loans

def main():
    book_list = BookList()
    user_list = UserList()
    loans = Loans()

    while True:
        print("\nLibrary Management System")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Manage Loans")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manage_books(book_list)
        elif choice == '2':
            manage_users(user_list)
        elif choice == '3':
            manage_loans(loans, book_list, user_list)
        elif choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_books(book_list):
    while True:
        print("\nManage Books")
        print("1. Add a book")
        print("2. Modify a book")
        print("3. Remove a book")
        print("4. Search for a book")
        print("5. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(book_list)
        elif choice == '2':
            modify_book(book_list)
        elif choice == '3':
            remove_book(book_list)
        elif choice == '4':
            search_book(book_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book(book_list):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    publisher = input("Enter publisher name: ")
    num_copies = int(input("Enter number of copies: "))
    pub_date = input("Enter publication date (YYYY-MM-DD): ")
    publication_date = datetime.strptime(pub_date, "%Y-%m-%d")
    
    new_book = Book(title, author, year, publisher, num_copies, publication_date)
    book_list.add_book(new_book)
    print("Book added successfully.")

def modify_book(book_list):
    title = input("Enter the title of the book to modify: ")
    books = book_list.search_book(title, "title")
    
    if not books:
        print("No books found with that title.")
        return
    
    if len(books) > 1:
        print("Multiple books found. Please choose one:")
        for i, book in enumerate(books):
            print(f"{i+1}. {book.get_title()} by {book.get_author()}")
        choice = int(input("Enter the number of the book to modify: ")) - 1
        book = books[choice]
    else:
        book = books[0]
    
    print("\nModify Book")
    print("1. Modify title")
    print("2. Modify author")
    print("3. Modify year")
    print("4. Modify publisher")
    print("5. Modify number of copies")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        new_title = input("Enter new title: ")
        book.set_title(new_title)
    elif choice == '2':
        new_author = input("Enter new author: ")
        book.set_author(new_author)
    elif choice == '3':
        new_year = int(input("Enter new year: "))
        book.set_year(new_year)
    elif choice == '4':
        new_publisher = input("Enter new publisher: ")
        book.set_publisher(new_publisher)
    elif choice == '5':
        new_copies = int(input("Enter new number of copies: "))
        book.set_num_copies(new_copies)
    else:
        print("Invalid choice.")
        return
    
    print("Book modified successfully.")

def remove_book(book_list):
    title = input("Enter the title of the book to remove: ")
    try:
        book_list.remove_book(title)
        print("Book removed successfully.")
    except ValueError as e:
        print(str(e))

def search_book(book_list):
    print("\nSearch Book")
    print("1. Search by title")
    print("2. Search by author")
    print("3. Search by publisher")
    print("4. Search by publication date")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        query = input("Enter title to search: ")
        search_type = "title"
    elif choice == '2':
        query = input("Enter author to search: ")
        search_type = "author"
    elif choice == '3':
        query = input("Enter publisher to search: ")
        search_type = "publisher"
    elif choice == '4':
        query = input("Enter publication date (YYYY-MM-DD) to search: ")
        search_type = "publication_date"
    else:
        print("Invalid choice.")
        return
    
    results = book_list.search_book(query, search_type)
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}")
    else:
        print("No books found matching the search criteria.")


def manage_users(user_list):
    while True:
        print("\nManage Users")
        print("1. Add a user")
        print("2. Modify a user")
        print("3. Remove a user")
        print("4. View user details")
        print("5. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_user(user_list)
        elif choice == '2':
            modify_user(user_list)
        elif choice == '3':
            remove_user(user_list)
        elif choice == '4':
            view_user_details(user_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user(user_list):
    username = input("Enter username: ")
    firstname = input("Enter first name: ")
    surname = input("Enter surname: ")
    house_number = input("Enter house number: ")
    street_name = input("Enter street name: ")
    postcode = input("Enter postcode: ")
    email = input("Enter email address: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
    
    new_user = User(username, firstname, surname, house_number, street_name, postcode, email, date_of_birth)
    user_list.add_user(new_user)
    print("User added successfully.")

def modify_user(user_list):
    username = input("Enter the username of the user to modify: ")
    try:
        user = user_list.get_user_by_username(username)
    except ValueError:
        print("User not found.")
        return
    
    print("\nModify User")
    print("1. Modify first name")
    print("2. Modify surname")
    print("3. Modify house number")
    print("4. Modify street name")
    print("5. Modify postcode")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        new_firstname = input("Enter new first name: ")
        user.set_firstname(new_firstname)
    elif choice == '2':
        new_surname = input("Enter new surname: ")
        user.set_surname(new_surname)
    elif choice == '3':
        new_house_number = input("Enter new house number: ")
        user.house_number = new_house_number
    elif choice == '4':
        new_street_name = input("Enter new street name: ")
        user.street_name = new_street_name
    elif choice == '5':
        new_postcode = input("Enter new postcode: ")
        user.postcode = new_postcode
    else:
        print("Invalid choice.")
        return
    
    print("User modified successfully.")

def remove_user(user_list):
    firstname = input("Enter the first name of the user to remove: ")
    try:
        user_list.remove_user(firstname)
        print("User removed successfully.")
    except ValueError as e:
        print(str(e))

def view_user_details(user_list):
    username = input("Enter the username of the user to view: ")
    try:
        user = user_list.get_user_by_username(username)
        print(f"\nUser Details:")
        print(f"Username: {user.get_username()}")
        print(f"Name: {user.get_firstname()} {user.get_surname()}")
        print(f"Address: {user.get_house_number()} {user.get_street_name()}, {user.get_postcode()}")
        print(f"Email: {user.get_email()}")
        print(f"Date of Birth: {user.get_date_of_birth().strftime('%Y-%m-%d')}")
    except ValueError:
        print("User not found.")

def manage_loans(loans, book_list, user_list):
    while True:
        print("\nManage Loans")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View user's borrowed books")
        print("4. View overdue books")
        print("5. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            borrow_book(loans, book_list, user_list)
        elif choice == '2':
            return_book(loans, book_list, user_list)
        elif choice == '3':
            view_user_borrowed_books(loans, user_list)
        elif choice == '4':
            view_overdue_books(loans, user_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def borrow_book(loans, book_list, user_list):
    username = input("Enter the username of the borrower: ")
    try:
        user = user_list.get_user_by_username(username)
    except ValueError:
        print("User not found.")
        return
    
    book_title = input("Enter the title of the book to borrow: ")
    books = book_list.search_book(book_title, "title")
    
    if not books:
        print("No books found with that title.")
        return
    
    if len(books) > 1:
        print("Multiple books found. Please choose one:")
        for i, book in enumerate(books):
            print(f"{i+1}. {book.get_title()} by {book.get_author()}")
        choice = int(input("Enter the number of the book to borrow: ")) - 1
        book = books[choice]
    else:
        book = books[0]
    
    try:
        loans.borrow_book(user, book)
        print("Book borrowed successfully.")
    except ValueError as e:
        print(str(e))

def return_book(loans, book_list, user_list):
    username = input("Enter the username of the borrower: ")
    try:
        user = user_list.get_user_by_username(username)
    except ValueError:
        print("User not found.")
        return
    
    book_title = input("Enter the title of the book to return: ")
    books = book_list.search_book(book_title, "title")
    
    if not books:
        print("No books found with that title.")
        return
    
    if len(books) > 1:
        print("Multiple books found. Please choose one:")
        for i, book in enumerate(books):
            print(f"{i+1}. {book.get_title()} by {book.get_author()}")
        choice = int(input("Enter the number of the book to return: ")) - 1
        book = books[choice]
    else:
        book = books[0]
    
    try:
        loans.return_book(user, book)
        print("Book returned successfully.")
    except ValueError as e:
        print(str(e))

def view_user_borrowed_books(loans, user_list):
    username = input("Enter the username to view borrowed books: ")
    try:
        user = user_list.get_user_by_username(username)
        loan_count = loans.get_user_loan_count(user)
        print(f"\n{user.get_firstname()} {user.get_surname()} has borrowed {loan_count} book(s).")
        if username in loans.loans:
            print("Borrowed books:")
            for book_id, due_date in loans.loans[username].items():
                print(f"Book ID: {book_id}, Due Date: {due_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("User not found.")

def view_overdue_books(loans, user_list):
    overdue_loans = loans.get_overdue_books(user_list)
    if overdue_loans:
        print("\nOverdue Books:")
        for loan in overdue_loans:
            print(f"Username: {loan['username']}, First Name: {loan['firstname']}, "
                  f"Book ID: {loan['book_id']}, Due Date: {loan['due_date'].strftime('%Y-%m-%d')}")
    else:
        print("No overdue books found.")

if __name__ == "__main__":
    main()