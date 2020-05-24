from nosqlite.nosqlite import Nosqlite 


database = Nosqlite("doctores")

database.newCollection("articulos")

database.insert("articulos", {"id":1,"nombre":"gustavo"})

database.show("articulos")

database.showOne("articulos", ("clave", "valor"))

database.showAll("articulos", ("clave", "valor"))

database.deleteOne("articulos", ("clave", "valor"))

database.deleteAll("articulos", ("clave", "valor"))

database.deleteCollection("articulos")

database.close()



