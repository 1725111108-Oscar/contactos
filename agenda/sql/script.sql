CREATE TABLE contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL

);

INSERT INTO contactos(nombre,primer_apellido,segundo_apellido,email,telefono)
VALUES
('Dejah','Thoris','Barson','dejah@email.com','11111111111'),
('John','Carter','Earth','jonhcarter@email.com','2222222222');

SELECT * FROM contactos;