# turboenergyutilities

CambiaAmperiosCarga --> Modifica vía Modbus el registro 210 del inversor, que especifica la corriente máxima de carga de la bater

$ sudo ./CambiaAmperiosCarga.py

Uso: CambiaAmperiosCarga <nuevo valor en amperios>

Ejemplo: CambiaAmperiosCarga 80 --> Establece en 80A la corriente máxima de carga de la batería.

¡Úsalo bajo tu propia responsabilidad!

$ sudo ./CambiaAmperiosCarga.py 50

Nuevo valor: 50
Conectando al inversor...
Leyendo el valor de carga actual...
Valor Anterior:  50
Estableciendo nuevo valor de carga...
Nuevo Valor escrito correctamente: 50

