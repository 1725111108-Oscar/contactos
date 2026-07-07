import web
import os

urls = (
    '/', 'controllers.index.Index',
    '/contactos', 'controllers.lista_contactos.ListaContactos',
    '/contacto/insertar', 'controllers.insertar_contacto.InsertarContacto',
    '/contacto/ver/(.+)', 'controllers.ver_contacto.VerContacto',
    '/contacto/borrar/(.+)', 'controllers.borrar_contacto.BorrarContacto',
    '/contacto/modificar/(\d+)', 'controllers.editar_contacto.EditarContacto',
)

app = web.application(urls, globals())

if not os.path.exists('agenda.db'):
    db = web.database(dbn='sqlite', db='agenda.db')
    with open('sql/script.sql', 'r') as f:
        for statement in f.read().split(';'):
            if statement.strip():
                db.query(statement)

if __name__ == "__main__":
    app.run()