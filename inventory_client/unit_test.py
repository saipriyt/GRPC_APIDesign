import unittest
from unittest.mock import MagicMock
import get_book_titles
import inventory_client


mock_client_obj = inventory_client.inventory_client()
real_client_obj = inventory_client.inventory_client()
first_title = ['Greys Anatomy - The beginning']
second_third_title = ['Greys Anatomy - Covid','Greys Anatomy - The end']

class UnitTest(unittest.TestCase):

    def testsstep5(self):
        mock_client_obj.get_book_titles = MagicMock(return_value = first_title) 
        mock_client_obj.get_book_titles(['1'], key = 'value')
        self.assertEqual(first_title,mock_client_obj.get_book_titles())


    def testsstep6(self):
        self.assertEqual(get_book_titles.get_book_titles(['2','3'],real_client_obj),second_third_title)

if __name__=="__main__":
    unittest.main()