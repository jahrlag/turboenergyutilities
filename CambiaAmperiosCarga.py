#!/usr/bin/python3

############################################################################################
#
#    Modifica la corriente de carga máxima de inversores Turbo Energy / Deye / Sunsynk
#
#    Probado en un Turbo EnergY 5.5Kw
#
#    ¡ÚSALO BAJO TU PROPIA RESPONSABILIDAD!
#
#



from pymodbus.client.sync import ModbusSerialClient
import sys

##########################
# Devuelve al sistema:
#    0 Si se escribió el nuevo valor correctamente
#    1 Si no se exribió el nuevo valor por cualquier razón
#
valRet = 1

client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',
    baudrate=9600,
    timeout=3,
    parity='N',
    stopbits=1,
    bytesize=8
)

if len(sys.argv) == 2 and sys.argv[1].isnumeric():

    nuevoValordeCarga = int(sys.argv[1])
    print()
    print("Nuevo valor:", nuevoValordeCarga)
    print("Conectando al inversor...")
    if client.connect():
        print("Leyendo el valor de carga actual...")
        resultado = client.read_holding_registers(address=210, count=1, unit=1)
        if not resultado.isError():
            print("Valor Anterior: ",resultado.registers[0])
            print("Estableciendo nuevo valor de carga...")
            resultado = client.write_registers(address=210, values=nuevoValordeCarga, unit=1)
            if resultado.isError():
                print("No he podido escribir el nuevo valor!!")
            else:
                print("Nuevo Valor escrito correctamente:",nuevoValordeCarga)
                valRet = 0
                print()

            client.close()
        else:
            print('No puedo conectar al Inversor!!')

else:
    print()
    print("Uso: CambiaAmperiosCarga <nuevo valor en amperios>")
    print()
    print("Ejemplo: CambiaAmperiosCarga 80 --> Establece en 80A la corriente máxima de carga de la batería.")
    print()
    print("¡Úsalo bajo tu propia responsabilidad!")
    print()

sys.exit(valRet)


