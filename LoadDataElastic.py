# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:51:31 2019

@author: mbacon
"""

from elasticsearch import Elasticsearch, helpers 
import uuid 

# create a new instance of the Elasticsearch client class 
es = Elasticsearch() 

 
def gendata(json_file, _index):
    with open('redout.json', encoding='UTF-8', errors='none', buffering=1) as f:
        for doc in f:
            if '{"index"' not in doc:
                yield {
                        "_index": _index,
                        "_id": uuid.uuid4(),
                        "_source": doc
                }

try:
    # make the bulk call, and get a response
    response = helpers.bulk(es, gendata("redout.json", "redcap1"))
    print ("\nbulk_json_data() RESPONSE:", response)
except Exception as e:
    print("\nERROR:", e)

#def gendata():
#    mywords = ['foo', 'bar', 'baz']
#    for word in mywords:
#        yield {
#            "_index": "mywords",
#            "_type": "document",
#            "doc": {"word": word},
#        }
#
#bulk(es, gendata())
#    yield {
#            "_index": _index,
#            "_id" : uuid.uuid4(),
#            "_source": doc