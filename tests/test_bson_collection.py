import os
import unittest
from tests.config import config
from smappdragon import BsonCollection

class TestBsonCollection(unittest.TestCase):

	def test_iterator_returns_tweets(self):
		collection = BsonCollection(os.path.dirname(os.path.realpath(__file__)) +'/'+ config['bson']['valid'])
		self.assertTrue(len(list(collection.set_limit(10).get_iterator())) > 0)

if __name__ == '__main__':
    unittest.main()

'''
read about twitter entities here:
https://dev.twitter.com/overview/api/entities-in-twitter-objects
'''