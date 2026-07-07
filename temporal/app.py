import web
import sqlite3

render = web.template.render('views', base='layout')

class Contactos:

    def obtenerContactos(self):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))  
            # Almacena cada registro en un diccionario
            row = cursor.fetchone()
            for row in cursor.fetchall():
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
        
            # Cierra la conexión a la base de datos
            conn.close()
            return contactos
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []
        finally:
            conn.close()

    def GET(self):
        contactos = self.buscarContactos()
        print(contactos)
        return render.lista_contactos(contactos)
        print(contacto)  