from concurrent import futures
import logging

import grpc
import books_pb2 
import books_pb2_grpc

libary = []
libary.append(
    books_pb2.Book(
        isbn='1',
        title='Greys Anatomy - The beginning',
        author='Elen pompeo',
        publishing_year=2016,
        genre='DRAMA'
    ))

libary.append(
    books_pb2.Book(
        isbn='2',
        title='Greys Anatomy - Covid',
        author='Elen pompeo',
        publishing_year=2018,
        genre='DRAMA'
    ))

libary.append(
    books_pb2.Book(
        isbn='3',
        title='Greys Anatomy - The end',
        author='Elen pompeo',
        publishing_year=2020,
        genre='DRAMA'
    ))

class Books(books_pb2_grpc.BooksServicer):

    def getBook(self, request, context):
        for book in libary: 
            if book.isbn == request.isbn:
                return books_pb2.getBookResponse(books = book)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Book not found")
        return books_pb2.getBookResponse()

    def setBook(self, request, context):
        for book in libary: 
            if book.isbn == request.books.isbn:
                return books_pb2.createBookResponse(isbn = "Book already exists in the libary")
        libary.append(request.books)
        return books_pb2.createBookResponse(isbn = "Book added to the libary")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BooksServicer_to_server(Books(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


#To make sure only run will start the server
if __name__ == '__main__':
    serve()

'''
{
    "isbn": "6"
}
{
    "books": {
        "author": "cillum dolore",
        "genre": 3,
        "isbn": "ullamco",
        "publishing_year": -1408571029,
        "title": "dolor mollit non adipisicing cupidatat"
    }
}

'''