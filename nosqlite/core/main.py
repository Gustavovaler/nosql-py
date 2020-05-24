import json
from . import settings
import time
import os



class Manager:
    pass

class DataObject:
    pass

class DatacollectionManager(Manager):


    def __init__(self):
        pass


    def create_collection(self, collection_name):

        self.db.seek(0)
        # data = self.db.read()
        # datadic = json.loads(data)
            
        
        # datadic[1]["collections"][collection_name]=[]
        # print(datadic)

        # self.db.write(json.dumps(datadic))
        if settings.DEBUG:
            print("collection was created")


    def delete_collection(self):
        pass


    def update_collection(self):
        pass


    def rename_collection(self):
        pass


class DatabaseManager(DatacollectionManager):
   

    def __init__(self,db_name):
        DatacollectionManager.__init__(self)
        self.root = settings.ROOT
        self.db_name = db_name
        try:
            self.create_db(self.db_name)
        except:
            pass
        finally:
            self.open_db()
        
        


    def open_db(self):
        
        self.db = open('{}/databases/{}/{}.nql'.format(self.root,self.db_name,self.db_name) , "a+")

        if settings.DEBUG:
            print("opened")
            


    def create_db(self, name):

        self.__get_time()

        try:
            #crear la carpeta con el nombre de a db
            os.mkdir("{}/databases/{}".format(self.root,self.db_name))
            #crea el archivo header de la db
            self.db = open('{}/databases/{}/{}.nql'.format(self.root,name,name) , "w")
            
            headers = [
                        {'headers':{'created at':self.timef, "name":name}},
                         {"collections":{}}
                         ,
                         ]
            data = json.dumps(headers)
            self.db.write(data)
            if settings.DEBUG:
                print("created")
            return True
        except:
            return False


    def delete_db(self):
        pass


    def rename_db(self):
        pass

    def close_db(self):
        self.db.close()
        if settings.DEBUG:
            print("closed database")

    def __get_time(self):
        timer = time.localtime()
        self.timef = "{}/{}/{} - {}:{}:{}".format(timer.tm_mday,timer.tm_mon,
            timer.tm_year, timer.tm_hour, timer.tm_min, timer.tm_sec )
        if settings.DEBUG:
            print(self.timef)






