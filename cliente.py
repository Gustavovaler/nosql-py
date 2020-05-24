from nosqlite.nosqlite import Nosqlite 


database = Nosqlite("doctores")

database.newCollection("articulos")

database.insert("articulos", {"id":1,"nombre":"gustavo"})

database.show("articulos")

database.findOne("articulos", {"nombre": "pedro"})

database.findAll("articulos", {"nombre": "pedro"})

database.deleteOne("articulos",{"nombre": "pedro"} )

database.deleteAll("articulos", {"nombre": "pedro"})

database.deleteCollection("articulos")

database.close()



