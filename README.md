# Library Management System

This Library Management System is a command-line application that allows you to manage books, users, and loans in a fictional library. The system is implemented in Python and follows an object-oriented programming approach.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Running the Program](#running-the-program)
4. [Using the System](#using-the-system)
   - [Managing Books](#managing-books)
   - [Managing Users](#managing-users)
   - [Managing Loans](#managing-loans)
5. [Class Structure](#class-structure)
6. [Error Handling](#error-handling)

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `book_management.py` file.
2. Ensure you have Python 3.6 or higher installed on your system.

## Running the Program

To run the Library Management System:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `book_management.py`.
3. Run the following command:

   ```
   python book_management.py.py
   ```

## Using the System

Upon running the program, you'll be presented with a main menu:

```
Library Management System
1. Manage Books
2. Manage Users
3. Manage Loans
4. Exit
```

Enter the number corresponding to your desired action.

### Managing Books

In the Book Management menu, you can:

1. Add a book: Enter book details such as title, author, year, publisher, number of copies, and publication date.
2. Modify a book: Update various attributes of an existing book.
3. Remove a book: Delete a book from the system by its title.
4. Search for a book: Find books by title, author, publisher, or publication date.

### Managing Users

In the User Management menu, you can:

1. Add a user: Enter user details such as username, name, address, email, and date of birth.
2. Modify a user: Update various attributes of an existing user.
3. Remove a user: Delete a user from the system by their first name.
4. View user details: Display all information about a specific user.

### Managing Loans

In the Loan Management menu, you can:

1. Borrow a book: Assign a book to a user.
2. Return a book: Process a book return.
3. View user's borrowed books: See all books currently borrowed by a specific user.
4. View overdue books: Display a list of all overdue books and the borrowers' information.

## Class Structure

The system consists of five main classes:

1. `Book`: Represents individual books.
2. `BookList`: Manages the collection of books.
3. `User`: Represents library users.
4. `UserList`: Manages the collection of users.
5. `Loans`: Handles book loans and returns.

## Error Handling

The system includes error checking and exception handling to manage invalid inputs or operations. Error messages will be displayed to guide you in case of incorrect actions or inputs.

Remember to follow the on-screen prompts and enter information as requested. If you encounter any issues or have questions about using the system, please refer back to this README or contact the system administrator.
