#Create a class Library with your choice of definitions
#creating the PublicLibrary class
class PublicLibrary: 
    #initialising method with reader_name and has_books properties
    def __init__(self, reader_name, has_books):
        self.reader_name= reader_name
        self.has_books= list(has_books) # a list of the books already issued
    #method for adding a book in the list of books
    def issuebook(self, name):
        #checks if the book is already issued
        if name in self.has_books: #self here is used to refer to the particular has_books list 
            print(f"Book is already issued under {self.reader_name}")
        else:
            self.has_books.append(name)
            print(f"'{name}' has been issued under {self.reader_name}. \nUpdated list is: " ,self.has_books)
    #method for returning a book
    def returnbook(self,name):
        try:
            # Attempting the removal
            self.has_books.remove(name)
            print(f"{self.reader_name} has returned '{name}'. Updated list is: {self.has_books}")
        except ValueError:
            # This is the error that happens if the name is not in the list
            print(f"'{name}' cannot be returned because it wasn't issued.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
        finally:
            # This block runs with or without an exception
            print("All modifications are complete")

#creating an object for the class PublicLibrary as pb
pb= PublicLibrary("Srestha", {"Intermezzo", "Normal people", "1984", "Blue sisters"})
#calling the issuebook
pb.issuebook("Metamorphosis")
pb.issuebook("1984")
#calling the returnbook
pb.returnbook("1984")
pb.returnbook("Animal Farm")