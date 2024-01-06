from otrosIngresos import OtrosIngresos


# CREATE
# elemento = "venta de producto"
# valor = 20000
# fecha = "2024-01-06"

# ingreso = OtrosIngresos(elemento, valor, fecha)

# ingreso.guardar()

# READ
# Ejemplo de uso para consultar todos los registros
# if __name__ == "__main__":
#    OtrosIngresos.consultar_todos()

# UPDATE
# if __name__=="__main__":
#    #Creamos el objeto OtrosIngresos con los valores
#    actualizacion = OtrosIngresos("Proteina", 80000, "2019-01-20")

# actualizamos el registro
#    actualizacion.actualizar(1)

# DELETE
if __name__ == "__main__":

    OtrosIngresos.eliminar(1)
    OtrosIngresos.consultar_todos()
