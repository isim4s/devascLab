class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

# Instancijos
loc1 = Location("Tomas", "Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
your_loc = Location("Simas", "Lithuania")

# Metodų kvietimas
loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()

