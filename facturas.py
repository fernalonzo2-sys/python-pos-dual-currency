import json
import datetime



def registro_de_facturas(usdt, bst, carrito):
    fecha=((datetime.datetime.today()).strftime("%d-%m-%Y %I:%M:%S"))

    facturas={"fecha":fecha,
              "MontoDolar":usdt,
              "Montobs":bst,
              "Objetos":f"{carrito}"
              }
    
    print(f"{facturas}")
    try:
        with open("registro_ventas.json", "r") as archivo:
            historial=json.load(archivo)
        
        historial.append(facturas)
        with open("registro_ventas.json", "w") as archivo:
                json.dump(historial, archivo, indent=4)
                print("modificado")

    except FileNotFoundError:

        historial=[facturas]

        print("creando archivo")
        
        with open("registro_ventas.json", "w") as archivo:
            json.dump(historial, archivo, indent=4)


