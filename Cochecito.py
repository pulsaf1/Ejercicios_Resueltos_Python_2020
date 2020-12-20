class Coche:

    def __init__(self, matricula, marca):
        self.matricula = matricula
        self.marca = marca
        self.kilometros_recorridos = 0
        self.gasolina = 0

    def repostar(self, litros):
        # self.gasolina = self.gasolina + litros
        self.gasolina += litros
        
    
    def avanzar(self, kms):       
        if (self.gasolina >= kms * 0.1):
            self.kilometros_recorridos += kms 
            self.gasolina -= kms * 0.1
        else: 
            print(f"Es necesario repostar para recorrer {kms} Km.")    
    
    def imprimir(self):
        print("Matricula: ", self.matricula)
        print("Marca: ", self.marca)
        print("Kms: ", self.kilometros_recorridos)
        print("Gasolina: ", self.gasolina)
        print("--------------------------")

micoche = Coche("1234JKL","Ford")
micoche.repostar(50)
micoche.avanzar(100)
micoche.avanzar(50)

micoche2= Coche("1111AAA", "Honda")

parking = []
parking.append(micoche)
parking.append(micoche2)

for cochecito in parking:
    cochecito.imprimir()

