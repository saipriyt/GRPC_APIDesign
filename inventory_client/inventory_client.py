import books_pb2
import books_pb2_grpc
import grpc

class inventory_client:
    def __init__(self,localhost='localhost',portnumber='50051'):
        self.channel = grpc.insecure_channel(localhost+':'+portnumber)
        self.stub = books_pb2_grpc.BooksStub(self.channel)
    
    def getBook(self, isbn):
        return self.stub.getBook(books_pb2.getBookRequest(isbn = isbn))

    def setBook(self, book):
        return self.stub.setBook(books_pb2.createBookRequest(book = book))
        