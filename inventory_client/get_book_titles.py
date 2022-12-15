import inventory_client

isbn_list = ['1','2']

def get_book_titles(isbn_list,inventory_client):
    title_names = []
    for number in isbn_list:
        book = inventory_client.getBook(number)
        title_names.append(book.books.title)
    return title_names

if __name__ == "__main__":
    list_books = get_book_titles(isbn_list,inventory_client.inventory_client())
    print(len(list_books))