# Calculadora de propinas

print("Bienvenidos a la calculadora de propinas")
factura = float(input("\nCual es el importe de tu factura? : "))
propina = int(input("\nCual es el porcentaje de propinas que deseas dejar? : "))
personas = int(input("\nEntre cuántas personas hay que repartir la factura? : "))

importe_propina = (factura * propina)/100

print(importe_propina)

factura_total = factura+importe_propina

print(factura_total)

importe_por_persona = factura_total/personas

importe_redondeado = round(importe_por_persona,2)

print(importe_por_persona)


print("\n El importe a pagar por persona es de " + str(importe_redondeado))
