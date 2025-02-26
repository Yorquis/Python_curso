from abc import ABC, abstractmethod

class procesoDePago(ABC):
    @abstractmethod
    def procesoDePago(self, cantidad: float) -> None:
        pass

    @abstractmethod
    def reembolsoPago(self, transaccionId: str) -> None:
        pass

class Paypal(procesoDePago):

    def procesoDePago(self, cantidad: float) -> None:
        print(f"Procesando pago de {cantidad} por Paypal")

    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando id transaccion numero {transaccionId} por Paypal" )

class Stripe(procesoDePago):

    def procesoDePago(self, cantidad: float) -> None:
        print(f"Procesando pago de {cantidad} por Stripe")

    def reembolsoPago(self, transaccionId: str) -> None:
        print(f"Reembolsando id transaccion numero {transaccionId} por Stripe")

if __name__ == "__main__":

    procesoPaypal = Paypal()
    procesoStripe = Stripe()

    procesoPaypal.procesoDePago(500.0)
    procesoPaypal.reembolsoPago("EDRFTGYH")

    procesoStripe.procesoDePago(1000.0)
    procesoStripe.reembolsoPago("EDRFTGYH")