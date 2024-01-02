# Define list of books with details 
allBooks = [
    ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
    ['9780134494166', "The Human Body", "Dave R", 1, []],
    ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
]

# Initalize empty list for borrowed ISBNs
borrowedISBNs = []

# Validate ISBNs 
def validISBN(isbn):

    # Ensure that ISBN is numeric  and has a length of 13
    while not isbn.isnumeric() or len(isbn) != 13: 
        print('Invalid ISBN')
        isbn= input('ISBN> ')

    # Calculate the ISBN checksum using weights
    weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    total = sum(int(digit) * weight for digit, weight in zip(isbn, weights))
    return total % 10 == 0

# Define addbook function so new books can be added to list 
def addBook(allBooks):

   # Input book details if details are invalid ask user to re-enter the correct details 
    bookName = input('Book name> ')
    while '*' in bookName or '%' in bookName:
        print('Invalid book name.')
        bookName= input('Book name> ')

    author = input('Author name> ')
    edition = input('Edition> ')
    while not edition.isdigit():
        print("Invalid edition.")
        edition = input('Edition> ')
    edition = int(edition)

    isbn = input('ISBN> ')
    if not validISBN(isbn):
        print('Invalid ISBN!')
        return
    
    # Check if the ISBN already exists in list 
    for book in allBooks:
        if isbn == book[0]:
            print('This book is found.')
            return
        
    # Create a new book entry, add it to list and inform user that the book is added sucessfully
    oneNewBook = [isbn, bookName, author, edition, []]
    allBooks.append(oneNewBook)
    print('A new book is added successfully.')

# Define borrowbook function so books can be borrowed 
def borrowBook(allBooks, borrowedISBNs):

    # input borrower name and serach details so book can be found 
    borrowerName = input("Enter the borrower name> ")
    searchTerm = input('Search term> ')
    searchMode = None

# Determine the search modes and serach terms to find book
# searchTerm ends with * it sets the searchMode variable to "Contains" and removes * from the end of searchTerm
    if searchTerm.endswith('*'):
        searchMode = "Contains"
        searchTerm = searchTerm[:-1]

# searchTerm ends with % it sets the searchMode variable to "starts with" and removes % from the end of searchTerm           
    elif searchTerm.endswith("%"):
        searchMode = "Starts with"
        searchTerm = searchTerm[:-1]

# If searchTerm doesn't end with either the search will be  an exact match with the book title
    else:
        searchMode = "Exact"

    searchResults = []

# Search for book based on search term and mode
    for book in allBooks:
        isbn, title, author, edition, borrowers = book  
        bookName = title.lower()  
        # Check if 'searchTerm' is contained in 'bookName'. If it is append it to searchResults list
        if searchMode == "Contains" and searchTerm.lower() in bookName:
            searchResults.append(book)
        elif searchMode == "Starts with" and bookName.startswith(searchTerm.lower()):
            searchResults.append(book)
        elif searchMode == "Exact" and searchTerm.lower() == bookName:
            searchResults.append(book)

# Inform the user if the book is found and if it is avaiable or not for borrowing
    if not searchResults:
        print("No books were found for the search term.")
    else:
        for book in searchResults:
            isbn, title, author, edition, borrowers = book
            if isbn in borrowedISBNs:
                print(f'-"{title}" is borrowed!')
            else:
                print(f'-"{title}" is available for borrowing.')

            # append the name of the current borrower to the borrowers list for the book
                borrowedISBNs.append(isbn)
                borrowers.append(borrowerName)

# Define the return book function to return a borrowed book
def returnBook(allBooks, borrowedISBNs, borrowerName): 
    # Check if ISBN of book is presnet in the 'borrowedISBNs'
    returnISBN = input('ISBN> ')
    if returnISBN in borrowedISBNs:

        # Indentify book index, remove ISBN from 'borrowedISBNs' list marking the book returned 
        idx = 0
        for row in allBooks:
            if returnISBN ==row[0]:
                bookIndex = idx
            else: 
                idx+=1
        returnedBook = allBooks[bookIndex]
        borrowedISBNs.remove(returnISBN)
        
        # Infrom user that the book has been returned 
        print(f"'{returnedBook[1]}' is returned.")
        return 
    
    # Inform the user that no borrowed book has been found
    else:
       print("No book is found!")

# Define list books function to list all books in system and their details
def listBooks(allBooks):

     # Check avaiablity of book by checking if the isbn of the book is in the 'borrowedISBNs' list
    for book in allBooks:
        isbn, title, author, edition, borrowers = book
        availability= "[Available]" if isbn not in borrowedISBNs else "[Unavailable]"

        # Infrom user of availability, title, author, edition, book ISBN and borrower
        print(f"{availability}")
        print(f"{title} - {author}")
        print(f"E: {edition} ISBN: {isbn}")
        if borrowers:
            formattedBorrowers = ', '.join([f"'{borrower}'" for borrower in borrowers])
            print(f"Borrowed by: [{formattedBorrowers}]")
        else: print ('[ ]')
       

# Define the exit function to exit the program and print the final list of books
def exitProgram(allBooks):

    # Infrom user of final list of books 
    print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
    print("---------------")

    # Infrom user of availability, title, author, edition, book ISBN and borrower
     # Check availabity of book by checking if ISBN of book is present in 'borrowedISBNs' list accessed with 'book[0]'
    for book in allBooks:   
        if book[0] in borrowedISBNs:
            status = "[Unavailable]"
        else:
            status = "[Available]"
        print(status)
        print(f'{book[1]} - {book[2]}')
        print(f'E: {book[3]} ISBN: {book[0]}')
        borrowers = book[4]
        if borrowers:
            formattedBorrowers = ', '.join([f"'{borrower}'" for borrower in borrowers])
            print(f"borrowed by: [{formattedBorrowers}]")
        else:
            print("borrowed by: [ ]")
        print("---------------")

# Define a menu function to print the menu options to for the user 
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row a book.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')

# Initialize the variable to store the current borrowers name 
borrowerName = ""

# Define the main program loop 
def start():

    # Initalize variable to 0 so the while loop continues until the value of choice becomes -1 and program ends
    choice=0
    while choice!=-1:
        printMenu()
        
        # Perform task based on user selection
        choice = input("Your selection> ").lower()
        if choice == '1' or choice == 'a':
            addBook(allBooks)
        elif choice == '2' or choice == 'r':
            borrowBook(allBooks, borrowedISBNs)
        elif choice == '3' or choice == 't':
            returnBook(allBooks, borrowedISBNs, borrowerName)
        elif choice == '4' or choice == 'l':
            listBooks(allBooks)
        elif choice == '5' or choice == 'x':
            exitProgram(allBooks)
            choice=-1
            break
        else:
            print("Wrong selection! Please select a valid option.")

# Start the program 
start()