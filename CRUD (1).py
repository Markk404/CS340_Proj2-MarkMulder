from pymongo import MongoClient

from bson.objectid import ObjectId

from bson.json_util import dumps

from ipywidgets import IntSlider

from ipywidgets.embed import embed_minimal_html

from bson.objectid import ObjectId

import json

slider = IntSlider(value=40)

embed_minimal_html('export.html', views=[slider], title='Widgets export')

client=MongoClient('mongodb://localhost:51721')

animal_data=client.AAC.animals.find({})


class AnimalShelter(object):

    def __init__ (self, username, password):
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:51721/AAC' %(username, password))
        
        self.database = self.client['AAC']

    def create (self,data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
        else: raise Exception("Nothing to save: data empty")
            

    def read(self, criteria):
        if criteria is not None:
            data=self.database.animals.find(criteria,{"_id":False})
        else:
            data=self.database.animals.find({},{"_id":False})
        return data
    
    def update(self, save):
        if save is not None:
            if save:
                saveResult = self.database.animals.insert_one(save)
            return saveResult
        else:
            exception = "Error: Nothing to Update"
        
    def delete(self, remove):
        if remove is not None:
            if remove:
                removeResult = self.database.animals.delete_one(remove)
        else:
            exception: "Error: Nothing to Delete"
