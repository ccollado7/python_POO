#Clases y objetos II

class Persona:
    doctor = "claudio"

print(Persona.doctor)

class Jugadores_A:
    j1 = "messi"
    j2 = "c.ronaldo"

print(Jugadores_A.j2)

class Jugadores_B:
    j3 = "marcelo"
    j1 = "falcao"

print(Jugadores_B.j1)

class Equipo:
    e2 = "barcelona"
    e3 = "real madrid"

print(Equipo.e3)


class Nombre:
    pass

victor = Nombre()
maria = Nombre()

victor.edad = 30
victor.sexo = "Masculino"
victor.pais = "Argentina"

maria.edad = 25
maria.sexo = "Femenimo"
maria.pais = "Colombia"

print(victor.edad)
print(maria.edad)