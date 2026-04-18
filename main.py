import datetime
import json
import requests

fecha=((datetime.date.today()).strftime('%d-%m-%Y'))
cache={"fecha":'12-31-2000',
       "dolar":420}

def obtener_tasa_bcv():
    url = "https://ve.dolarapi.com/v1/dolares/oficial"
    try:
        response = requests.get(url)
        data = response.json()

        tasa = data['promedio']
        dolar=round(tasa, 2)
        return dolar
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
        return None

def calculo(carrito):
    usd=0
    for n in carrito:
        usd+=combos[n]["dolar"]
        
    return usd

try:
    with open("tasa_dolar.json", "r") as archivo:
        datos_guardados=json.load(archivo)
        if (datos_guardados["fecha"]==fecha):
            dolar=datos_guardados["dolar"]
            print(f"dolar={dolar}bs y es el {fecha}")
        else:
            with open("tasa_dolar.json", "w") as archivo:
                print(f"Actualizando la antigua fecha {datos_guardados["fecha"]} a la actual {fecha}")
                datos_guardados["dolar"] = obtener_tasa_bcv()
                datos_guardados["fecha"] = fecha
                dolar=datos_guardados["dolar"]
                json.dump(datos_guardados, archivo)
        
except FileNotFoundError:
    with open("tasa_dolar.json", "w") as archivo:
        print("creando archivo")
        dolar=obtener_tasa_bcv()
        cache["dolar"]=dolar
        json.dump(cache, archivo)
        

     

combos={"cmbduog":{"desc":"Combo Duo Grande","dolar":12.50,"bs":(12.50*dolar)},
        "cmbduom":{"desc":"Combo Duo Mediano","dolar":10.50,"bs":(10.50*dolar)},
        "cmbindiv":{"desc":"Combo Individual","dolar":5,"bs":(5*dolar)},
        "cmbpop":{"desc":"Combo POP","dolar":4.75,"bs":(4.75*dolar)},
        "cmbenamorado":{"desc":"Combo Enamorados","dolar":16,"bs":(16*dolar)}
        }

carrito=[]

while True:
    print('cmbduog||cmbduom||cmbindiv||cmbpop||cmbenamorado')
    seleccion=str(input("\nSeleccione un combo:")).lower()
    
    if seleccion in combos:
        cantidad=int(input(f"Indiquie la cantidad de {combos[seleccion]["desc"]} que desa:"))
        for i in range(cantidad):
            carrito.append(seleccion)
        print(f"Añadido {cantidad}x {combos[seleccion]["desc"]} al carrito exitosamente")
            
        
    else:
        print("el combo no se encuentra")

    continuar=str(input("\n desea continuar?:"))
    if continuar.lower() == "no":
        
        break

usdt=calculo(carrito)
print(f"\n{"-"*13}" "Imprimiendo factura" f"{"-"*15}")
bst=0
carrito_unico=set(carrito)
for n in carrito_unico:
    cant=carrito.count(n)
    bst+=combos[n]["bs"]*cant
    print(f"x{cant}")
    print(f"{combos[n]["desc"]:<30}  bs{combos[n]["bs"]:>8.2f}")
    print("")

print("-"*46)
print(f"{"Monto total:":<32} Bs{bst:>8.2f}")
print(f"{"-"*36}$ {usdt}")

import facturas
facturas.registro_de_facturas(usdt=usdt,bst=bst, carrito=carrito)
