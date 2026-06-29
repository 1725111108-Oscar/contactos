import web

db = web.database(dbn='sqlite', db='agenda.db')
render = web.template.render('views/', base='layout')

class ListaContactos:
    def GET(self):
        contactos = db.select('contactos')
        return render.lista_contactos(contactos)