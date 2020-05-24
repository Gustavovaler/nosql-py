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


    def showOne(self, collection_name, param=()):
        print("find into {} where {} value {}".format(collection_name, param[0], param[1]))

    def showAll(self, collection_name, param=()):
        print("find ALL into {} where {} value {}".format(collection_name, param[0], param[1]))

    def deleteOne(self, collection_name, param=()):
        print("delete into {} where {} value {}".format(collection_name, param[0], param[1]))

    def deleteAll(self, collection_name, param=()):
        print("delete  ALL into {} where {} value {}".format(collection_name, param[0], param[1]))





        

            





