```
                                     _                             
 ___ _ __ ___   __ _ _ __  _ __   __| |_ __ __ _  __ _  ___  _ __  
/ __| '_ ` _ \ / _` | '_ \| '_ \ / _` | '__/ _` |/ _` |/ _ \| '_ \ 
\__ \ | | | | | (_| | |_) | |_) | (_| | | | (_| | (_| | (_) | | | |
|___/_| |_| |_|\__,_| .__/| .__/ \__,_|_|  \__,_|\__, |\___/|_| |_|
                    |_|   |_|                    |___/             
```

smappdragon is a rebuild of the old [smapp-toolkit](https://github.com/SMAPPNYU/smapp-toolkit). It is a low level set of tools for programmers to use, it’s the low level part of the toolkit. There will be a separate piece of software called `smapptoolbox` that will import smapp dragon and buid the high level interface. Plotting figures, aggregating, and other non standard data operations will be in the new `smapptoolbox`.

##testing 

You absolutely need to write unit tests for any methods you add to smappdragon, this software needs to stay as stable as porssible as it will be the basis for other software.

This folder contains tests for smappdragon.

The `bson` folder contains two bson files on which to run tests. One if a valid.bson file with tweets that have properly formatted fields. Another is an sketchy.bson file that has tweets with strange fields, missing fields, etc.

##collection

classes for interfacing with a mongodb database of tweets

##basecollection

this is the base class for all collection objects. methods taht all collection objects use are found here. this is actually the most important class.

##mongocollection

this allows you to plug into a running live mongodb database and run smappdragon methods on the resulting collection object. 

abstract:
```python
	from smappdragon import MongoCollection

	collection = MongoCollection('HOST', PORT, 'USER_NAME', 'PASSWORD', 'DB_NAME', 'COLLECTION_NAME')
```

practical:
```python
	from smappdragon import MongoCollection
	
	collection = MongoCollection('superhost.bio.nyu.edu', 27574, smappReadWriteUserName, 'PASSWORD', 'GERMANY_ELECTION_2015_Nagler', 'tweet_collection_name')
```

*returns* a collection object that can have methods called on it

test: `python -m unittest tests.test_mongo_collection`

you should create a `config.py` file in the `tests` directory structured like so:

```python
config = {
	'mongo':{
		'host': 'HOSTNAME',
		'port': PORT,
		'user': 'DB_USER',
		'password': 'DB_PASS'
		'database': 'DB_NAME'
		'collection': 'COLLECTION_NAME'
	},
	'blah':{
		.
		.
		.
	}
}
```

this config is used for testing.

##top_entities

returns the top twitter entites from a tweet object, you can [read about twitter entities here](https://dev.twitter.com/overview/api/entities-in-twitter-objects)

abstract:
```python
```

practical:
```python
```

*returns* a dictionary containing tho requested entities and the counts for each entity

input:
```python
print MongoCollection('superhost.bio.nyu.edu', 27574, smappReadWriteUserName, 'PASSWORD', 'Jade_Helm_1', 'tweet_collection_name').top_entities({'user_mentions':5, 'media':3, 'hashtags':5})
```

output:
```
{
    "hashtags": {
        "JadeHelm": 118, 
        "pjnet": 26, 
        "jadehelm": 111, 
        "falseflag": 32, 
        "2a": 26
    },
    "user_mentions": {
        "1619936671": 41, 
        "27234909": 56, 
        "733417892": 121, 
        "10228272": 75, 
        "233498836": 58
    }, 
    "media": {
        "https://t.co/ORaTXOM2oX": 55, 
        "https://t.co/pAfigDPcNc": 27, 
        "https://t.co/TH8TmGuYww": 24
    }
}
```

*returns* a dictionary filled with the top terms you requested

note: no support for extended entities, retweet entities, user entites, or direct message entities.

note: if not enough entity objects are returned they get filled into the dictionary with null like so:

```
{
	"symbols": {
	    "0": null, 
	    "1": null, 
	    "hould": 1
	}
}
```
 





