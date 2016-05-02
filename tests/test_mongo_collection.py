import unittest
from tests.config import config
from smappdragon import MongoCollection

class TestMongoCollection(unittest.TestCase):

	def test_iterator_returns_tweets(self):
		collection = MongoCollection(     \
			config['mongo']['host'],      \
			config['mongo']['port'],      \
			config['mongo']['user'],      \
			config['mongo']['password'],  \
			config['mongo']['database'],  \
			config['mongo']['collection'] \
		)
		self.assertTrue(len(list(collection.set_limit(10).get_iterator())) > 0)

	# special test because custom logic is different on mongo
	def test_mongo_collection_custom_filter_filters(self):
		collectionone = MongoCollection(
			config['mongo']['host'],
			config['mongo']['port'],
			config['mongo']['user'],
			config['mongo']['password'],
			config['mongo']['database'],
			config['mongo']['collection']
		)
		full_collection_len = len(list(collectionone.get_iterator()))
		def is_tweet_a_retweet(tweet):
			if 'retweeted' in tweet and tweet['retweeted']:
				return True
			else:
				return False
		num_retweets = len(list(collectionone.set_custom_filter(is_tweet_a_retweet).get_iterator()))

		collectiontwo = MongoCollection(
			config['mongo']['host'],
			config['mongo']['port'],
			config['mongo']['user'],
			config['mongo']['password'],
			config['mongo']['database'],
			config['mongo']['collection']
		)
		def is_not_a_retweet(tweet):
			if 'retweeted' in tweet and tweet['retweeted']:
				return False
			else:
				return True
		num_non_retweets = len(list(collectiontwo.set_custom_filter(is_not_a_retweet).get_iterator()))

		#the number of retweets and non retweets should add up to the whole collection
		self.assertEqual(num_retweets + num_non_retweets, full_collection_len)

	def test_strip_tweets_keeps_fields(self):
		collection = MongoCollection(os.path.dirname(os.path.realpath(__file__)) +'/'+ config['bson']['valid'])
		self.maxDiff = None
		it = collection.strip_tweets(['id', 'entities.user_mentions', 'user.profile_image_url_https']).get_iterator()
		def tweets_have_right_keys(iterator, fields):
			for tweet in iterator:
				keys = [key for key in tweet]
				print(keys)
				if not fields  == keys:
					return False
			return True		
		self.assertTrue(tweets_have_right_keys(it, ['id', 'entities.user_mentions', 'user.profile_image_url_https']))

if __name__ == '__main__':
	unittest.main()

'''
read about twitter entities here:
https://dev.twitter.com/overview/api/entities-in-twitter-objects
'''

