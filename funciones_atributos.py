class Persona:
    edad = 27
    nombre = "Claudio"
    pais = "Argentina"

doctor = Persona()

print("la edad es: " ,doctor.edad)
print(doctor.nombre)
print("la edad es: ",getattr(doctor,"edad"))
print("el doctor tiene una edad?",hasattr(doctor,"edad"))

setattr(doctor,"nombre","hector")
print(doctor.nombre)

delattr(Persona,"pais")
print(doctor.nombre)
print(doctor.pais)