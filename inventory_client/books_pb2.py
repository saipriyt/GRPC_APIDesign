# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: books.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62ooks.proto\x12\x05\x62ooks\"i\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1b\n\x05genre\x18\x04 \x01(\x0e\x32\x0c.books.GENRE\x12\x17\n\x0fpublishing_year\x18\x05 \x01(\x05\"\x1e\n\x0egetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"-\n\x0fgetBookResponse\x12\x1a\n\x05\x62ooks\x18\x01 \x01(\x0b\x32\x0b.books.Book\"/\n\x11\x63reateBookRequest\x12\x1a\n\x05\x62ooks\x18\x01 \x01(\x0b\x32\x0b.books.Book\"\"\n\x12\x63reateBookResponse\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"l\n\rInventoryItem\x12\x11\n\tinvNumber\x18\x06 \x01(\t\x12!\n\nbookObject\x18\x07 \x01(\x0b\x32\x0b.books.BookH\x00\x12\x1d\n\x06status\x18\x08 \x01(\x0e\x32\r.books.STATUSB\x06\n\x04\x62Obj*6\n\x05GENRE\x12\n\n\x06\x43OMEDY\x10\x00\x12\t\n\x05\x43RIME\x10\x01\x12\t\n\x05\x44RAMA\x10\x02\x12\x0b\n\x07\x46\x41NTASY\x10\x03*\"\n\x06STATUS\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x32\x81\x01\n\x05\x42ooks\x12\x38\n\x07getBook\x12\x15.books.getBookRequest\x1a\x16.books.getBookResponse\x12>\n\x07setBook\x12\x18.books.createBookRequest\x1a\x19.books.createBookResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'books_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=403
  _GENRE._serialized_end=457
  _STATUS._serialized_start=459
  _STATUS._serialized_end=493
  _BOOK._serialized_start=22
  _BOOK._serialized_end=127
  _GETBOOKREQUEST._serialized_start=129
  _GETBOOKREQUEST._serialized_end=159
  _GETBOOKRESPONSE._serialized_start=161
  _GETBOOKRESPONSE._serialized_end=206
  _CREATEBOOKREQUEST._serialized_start=208
  _CREATEBOOKREQUEST._serialized_end=255
  _CREATEBOOKRESPONSE._serialized_start=257
  _CREATEBOOKRESPONSE._serialized_end=291
  _INVENTORYITEM._serialized_start=293
  _INVENTORYITEM._serialized_end=401
  _BOOKS._serialized_start=496
  _BOOKS._serialized_end=625
# @@protoc_insertion_point(module_scope)