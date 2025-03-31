"""
|-------------------------------------------------------------------------------------------------------------------------------|
                    |-------> ΟΔΗΓΙΕΣ ΠΡΟΓΡΑΜΜΑΤΟΣ <-------|                                                                    |
---> Step 1: The Instrument class includes the properties of musical instruments.
---> Step 2: Create musical instrument objects using the Instrument class.
---> Step 3: Create an orchestra list containing the musical instrument objects.
---> Step 4: Implement the display_all(orchestra) function to display the characteristics of all instruments in the list.
---> Step 5: Implement the filter_by_category(orchestra, category) function to filter instruments by category
and display the characteristics of the filtered instruments.                                                       |
|-------------------------------------------------------------------------------------------------------------------------------|
"""

class Instrument:
    """
   Step 1:
          Initialization of the class with the properties of a musical instrument:
          name --> Instrument name, kind --> Type of instrument
          category --> Category, year --> Year of manufacture
          manufacturer --> Manufacturer
    """
    def __init__(self, name, kind, category, year, manufacturer):
        self.name = name
        self.kind = kind
        self.category = category
        self.year = year
        self.manufacturer = manufacturer

    # def __str__(self):Returns a formatted string with the musical instrument's information.
    def __str__(self):
        return (f"Instrument: {self.name}, Kind: {self.kind}, "
                f"Category: {self.category}, Year: {self.year}, "
                f"Manufacturer: {self.manufacturer}")
"""
    Step 2: Creation of musical instruments as objects of the Instrument class.
"""
grand_piano = Instrument("Grand Piano", "Piano", "έγχορδο", 2020, "Fazioli")
rhythm_guitar = Instrument("Rhythm Guitar", "Guitar", "έγχορδο", 2015, "Fender")
first_violin = Instrument("First Violin", "Violin", "έγχορδο", 1715, "Antonio Stradivari")
principal_flute = Instrument("Principal Flute", "Flute", "πνευστό", 2018, "Yamaha")

"""
Step 3: Creation of the orchestra list containing the objects.
orchestra = [grand_piano, rhythm_guitar, first_violin, principal_flute]

"""
orchestra = [grand_piano, rhythm_guitar, first_violin, principal_flute]

Βήμα 4: Implementation of the display_all function.
"""
def display_all(orchestra):
    # Displaying the characteristics of all the instruments in the list.
    for instrument in orchestra:
        print(instrument)

"""
Βήμα 5: Implementation of the filter_by_category function.
"""
def filter_by_category(orchestra, category):
    # Filtering the instruments in the list by category.
    #We created a new list filtered_instruments, which contains only the instruments that belong to the desired category.
    filtered_instruments = [instrument for instrument in orchestra if instrument.category == category]
    # Displaying the characteristics of the filtered instruments.
    display_all(filtered_instruments)

print("\nCharacteristics of the available instruments for the orchestra.:\n")
print("=" * 100)
#Displaying all instruments.
display_all(orchestra)
print("=" * 100)
print(" 🎼 End of the available orchestra instruments. 🎼 ")




# Filtering and displaying instruments by category "string"
print("\nFiltered instruments based on the category "string":")
print("=" * 100)
filter_by_category(orchestra, "έγχορδο")
print("=" * 100)
print(" 🎼 End of the available orchestra instruments. 🎼 ")



#---------------------------------> END OF PROGRAM  <-------------------------------------




