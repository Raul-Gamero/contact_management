import re
import os

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"

class GestionContactos:
    def __init__(self, archivo="contactos.txt"):
        self.contactos = []
        self.archivo = archivo
        self.cargar_contactos()

    def agregar_contacto(self, contacto):
        if not self.validar_correo(contacto.correo):
            print("❌ Correo electrónico inválido.")
            return
        self.contactos.append(contacto)
        self.guardar_contactos()
        print("✅ Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("⚠️ No hay contactos registrados.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            for contacto in encontrados:
                print(contacto)
        else:
            print("❌ Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                self.guardar_contactos()
                print("🗑️ Contacto eliminado.")
                return
        print("❌ No se encontró el contacto a eliminar.")

    def guardar_contactos(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for c in self.contactos:
                    f.write(f"{c.nombre},{c.telefono},{c.correo}\n")
        except Exception as e:
            print(f"⚠️ Error al guardar los contactos: {e}")

    def cargar_contactos(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split(",")
                    if len(partes) == 3:
                        nombre, telefono, correo = partes
                        self.contactos.append(Contacto(nombre, telefono, correo))
        except Exception as e:
            print(f"⚠️ Error al cargar los contactos: {e}")

    def validar_correo(self, correo):
        patron = r"[^@]+@[^@]+\.[^@]+"
        return re.match(patron, correo) is not None

def mostrar_menu():
    print("\n📇 Menú de Gestión de Contactos")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    gestor = GestionContactos()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            correo = input("Correo electrónico: ").strip()
            if nombre and telefono and correo:
                contacto = Contacto(nombre, telefono, correo)
                gestor.agregar_contacto(contacto)
            else:
                print("❌ Todos los campos son obligatorios.")
        elif opcion == "2":
            gestor.mostrar_contactos()
        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            gestor.buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ").strip()
            gestor.eliminar_contacto(nombre)
        elif opcion == "5":
            print("👋 Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
