class vin:
    Vehicles = []
    def __init__(self, Vehicles):
        self.Vehicles = Vehicles

class Vehicle:
    type1 = 'mobil'
    type2 = 'motor'
    def __init__(self, nama, n_pls):
        self.nama = nama
        self.n_pls = n_pls
        
        
        # Instance method
    def description(self):
        return self.nama, self.n_pls
    
class mobil(Vehicle):
    def run(self, speed):
        return "%s runs %s" % (self.nama, speed)
        
        # Child class 
class mobil2(Vehicle):
    def run(self, speed):
        return "%s runs %s" % (self.nama, speed)

   # Create instances 
my_Vehicles = [
    mobil("Deni", "B 890 A"), 
    mobil2("Dina", "AB 90 A"), 
    Vehicle("Agoy", "B 9 RI")
]

# Instantiate class
my_vin = vin(my_Vehicles)

# Output
print("Saya Mempunyai {} Kendaraan.".format(len(my_vin.Vehicles)))
for Vehicle in my_vin.Vehicles:
    print("Untuk {} nomor polisi {} .".format(Vehicle.nama, Vehicle.n_pls))
print("==================================================")
print("Dan itu semua adalah sebuah {}.".format(Vehicle.type1))

