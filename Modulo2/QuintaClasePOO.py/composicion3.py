class calcularImpuesto:

    def ejecutar(self, monto):
        return monto * 0.19

class aplicarDescuento:

    def ejecutar(self, monto, descuento):
        return monto - (descuento * descuento / 100)

class generarRecibo:
    def ejecutar(self, monto):
        return f"recibo generado por ${monto:.2f}"

class facturacion:
    def __init__(self):
        self.pasos = []

    def agregarPaso(self, paso):
        self.pasos.append(paso)

    def procesarFactura(self, monto, descuente=0):
        print("Procesando factura...")
        for paso in self.pasos:
            if isinstance(paso, calcularImpuesto):
                impuesto = paso.ejecutar(monto)
                print(f"Aplicando impuesto: ${impuesto:.2f}")
                monto += impuesto
            elif isinstance(paso, aplicarDescuento):
                monto = paso.ejecutar(monto, descuento)
                print(f"Aplicando descuento: ${descuento:.2f}")
            elif isinstance(paso, generarRecibo):
                print(paso.ejecutar(monto))

Facturacion = facturacion()
impuesto = calcularImpuesto()
descuento = aplicarDescuento()
recibo = generarRecibo()

facturacion.agregarPaso(impuesto)
facturacion.agregarPaso(descuento)
facturacion.agregarPaso(recibo)

facturacion.procesarFactura(100, descuento=10)

