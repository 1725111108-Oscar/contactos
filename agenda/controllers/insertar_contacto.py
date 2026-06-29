import web

db = web.database(dbn='sqlite', db='agenda.db')
render = web.template.render('views/', base='layout')

class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()

    def POST(self):
        form = web.input()
        db.insert('contactos', nombre=form.nombre, telefono=form.telefono, email=form.email)
        raise web.seeother('/contactos')