from .core import main


class Nosqlite(main.DatabaseManager):
    
    def __init__(self, db_name):
        main.DatabaseManager.__init__(self,db_name)

    def close(self):
        try:
            main.DatabaseManager.close_db(self)
        except:
            pass


    def newCollection(self, collection_name):
        main.DatabaseManager.create_collection(self, collection_name)

    def insert(self, colection_name, register={}):
        print(colection_name)
        print(register)

    def show(self, collection_name):
        print("showing {}".format(collection_name))

    def deleteCollection(self, collection_name):
        print("deleted {}".format(collection_name))


    def findOne(self, collection_name, dat={}):
        print("find  ONe into {} where {} value {}".format(collection_name,list(dat)[0],dat[list(dat)[0]]))
       

    def findAll(self, collection_name,dat={}):
        print("find  ALL into {} where {} value {}".format(collection_name,list(dat)[0],dat[list(dat)[0]]))

    def deleteOne(self, collection_name,dat={}):
        print("delete into {} where {} value {}".format(collection_name,list(dat)[0],dat[list(dat)[0]]))

    def deleteAll(self, collection_name,dat={}):
        print("delete into {} where {} value {}".format(collection_name,list(dat)[0],dat[list(dat)[0]]))





        

            





