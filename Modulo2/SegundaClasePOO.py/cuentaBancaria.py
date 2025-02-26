class cuentaBancaria:

    def __init__(self, titular, saldo, clave):
        self.titular = titular
        self._saldo = saldo
        self.__clave = clave
        
    def depositar(self, cantidadDeposito):
        self._saldo += cantidadDeposito
        return f"Deposito exitoso. El saldo actual es: {self._saldo}"

    def retirar(self, cantidadRetiro):
        if cantidadRetiro >= self._saldo:
            return "Fondos insuficientes"
        self._saldo -= cantidadRetiro
        return f"Retiro exitoso. El saldo actual es: {self._saldo}"

    def modificarClave(self, nuevaClave):
        self.__clave = nuevaClave
        return f"Clave modificada exitosamente. La nueva clave es: {self.__clave}"
        
cuentaBancaria1 = cuentaBancaria("Yorquis", 1000, "1234")
print(cuentaBancaria1.titular)
print(cuentaBancaria1._saldo)

print(cuentaBancaria1.depositar(500))
print(cuentaBancaria1.retirar(200))
print(cuentaBancaria1.modificarClave("5678"))
