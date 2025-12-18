#basic functions of lists
#books is a set of all the books in a small bookstore
books= ["Harry Potter", "Percy Jackson", "Normal People", "Vegetarian","Intermezzo"]
print(books[0]) # Harry Potter
print(books[4]) # Intermezzo
books[0]= "Maidens"
print(books[0]) # changes Harry Potter ->  Maidens

books.append("Animal Farm")
print("after append: ", books)
books.remove("Percy Jackson")
print("after removing: ", books)
books.pop
books.pop(1)
print("after pop functions" , books)
books.insert(5, "Poirot")
print("after the insert function: ", books)
books.sort()

books.clear()

for i in books:
    print(i)