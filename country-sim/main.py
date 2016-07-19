class Country:
    def __init__(self, name, ID):
        self.name = name
        self.iden = ID
    
    # scales from 1-5
    attk = 2
    defn = 1
    econ = 1
    morl = 3
    govt = 2
    terr = 3


country_A = Country("Country A", "0001")
print country_A.name
print country_A.iden
print country_A.govt
