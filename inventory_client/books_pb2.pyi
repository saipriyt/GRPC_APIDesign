from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AVAILABLE: STATUS
COMEDY: GENRE
CRIME: GENRE
DESCRIPTOR: _descriptor.FileDescriptor
DRAMA: GENRE
FANTASY: GENRE
TAKEN: STATUS

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishing_year", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: GENRE
    isbn: str
    publishing_year: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[GENRE, str]] = ..., publishing_year: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["bookObject", "invNumber", "status"]
    BOOKOBJECT_FIELD_NUMBER: _ClassVar[int]
    INVNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bookObject: Book
    invNumber: str
    status: STATUS
    def __init__(self, invNumber: _Optional[str] = ..., bookObject: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[STATUS, str]] = ...) -> None: ...

class createBookRequest(_message.Message):
    __slots__ = ["books"]
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    books: Book
    def __init__(self, books: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class createBookResponse(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class getBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class getBookResponse(_message.Message):
    __slots__ = ["books"]
    BOOKS_FIELD_NUMBER: _ClassVar[int]
    books: Book
    def __init__(self, books: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class GENRE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
