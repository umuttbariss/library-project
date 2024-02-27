class Library:

    def __init__(self):
        self.file = open("books.txt","a+")

    def __del__(self):
        self.file.close()
        
    def list_books(self):
        file = self.file
        file.seek(0)
        print("#"*20)
        
        #Looking for is list is empty
        if file.readline() == "":
            print("List is empty.")
        
        file.seek(0)
        count = 0
        while True:
            count += 1
            line = file.readline().strip().split(",")

            if len(line) == 1:
                break

            book_title = line[0]
            book_author = line[1]
            relase_year = line[2]
            nop = line[3]

            print(f'{count}) Book Title: {book_title} - Author: {book_author} - Relase Year: {relase_year} - Number of Pages: {nop}')
        
        print("#"*20)


    def add_book(self):
        book_title = input("Book Title: ").strip(",")
        book_author = input("Author: ").strip(",")
        relase_year = input("Relase Year: ").strip(",")
        nop = input("Number of Pages: ").strip(",")

        result = f'{book_title},{book_author},{relase_year},{nop}\n'

        self.file.writelines(result)
        print("-Book added successfully.")

    def remove_book(self):
        book_name = input("Book Title: ")
        count = 0

        file = self.file
        file.seek(0)
        lines = file.readlines()
        file.truncate(0) #deleting method
        for i in lines:
            line = i.strip().split(",")
            if line[0].lower() == book_name.lower():
                print("-Book removed successfully.")
                count = 1
            if line[0].lower() != book_name.lower():
                file.writelines(i)

        if count == 0:
            print("-Book is not in the list!")

#Program start
lib = Library()

while True:
    print("-"*20)
    print("#Choose an action#")
    print("1. List Books")
    print("2. Add Book")
    print("3. Remove Book")
    print('Type "q" for quit')
    print("-"*20)
    
    answer = input("Action: ")
    print("-"*20) 

    if answer == "q" or answer =="Q":
       break
   
    elif answer == "1":
       lib.list_books()

    elif answer == "2":
        lib.add_book()

    elif answer == "3":
        lib.remove_book()

    else:
        print("-Invalid input. Please enter a valid input!")
