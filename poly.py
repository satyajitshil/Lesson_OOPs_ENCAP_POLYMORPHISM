class India:
    def language(self):
        print("Hindi is widely spoken in India.")
    def capital(self):
        print("The capital of India is New Dehli.")
    def type(self):
        print("India is developing.")
class USA:
    def language(self):
        print("English is widely spoken in the USA.")
    def capital(self):
        print("The capital of the USA is Washington, D.C.")
    def type(self):
        print("USA is developed.")

oUSA = USA()
oIndia = India()

for country in (oUSA, oIndia):
    country.capital()
    country.language()
    country.type()