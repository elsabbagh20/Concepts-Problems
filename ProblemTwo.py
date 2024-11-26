def libraryBookBorrowingnAnalysis(records):
    

    bookDictionary = {}
    

    
    uniqueTitles = set()
    
    for record in records:
        title, days = record.split(' - ')
        days = int(days)
        uniqueTitles.add(title)
       
        if title in bookDictionary:
            bookDictionary[title] += days
        else:
            bookDictionary[title] = days
        
    
    mostBorrowedBook = max(bookDictionary, key=bookDictionary.get)
    leastBorrowedBook = min(bookDictionary, key=bookDictionary.get)
    
    
    averageDaysBorrowed = sum(bookDictionary.values()) / len(bookDictionary)
    
   
    sortedBooks = sorted(bookDictionary.items(), key=lambda x: x[1], reverse=True)
    
    
    print("Most borrowed book:", mostBorrowedBook)
    print("Least borrowed book:", leastBorrowedBook)
    print("Average days borrowed:", averageDaysBorrowed)
    print("Unique titles:", uniqueTitles)
    print("Sorted books by days borrowed (descending):", sortedBooks)


records = [
    "Book A - 3",
    "Book B - 5",
    "Book C - 2",
    "Book A - 5",
    "Book C - 1",
    "Book D - 7"
]

libraryBookBorrowingnAnalysis(records)