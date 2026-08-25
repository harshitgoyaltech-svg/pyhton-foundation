class solar:
    def generate(self):
        print("electricity generated from solar")

class wind:
    def generate(self):
        print("electricity generated from wind")

class hydro:
    def generate(self):
        print("electricity generated from flowing water")

energies=[solar(),wind(),hydro()]
for energy in energies:
    energy.generate()