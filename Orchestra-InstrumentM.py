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
   Βήμα 1:
    Αρχικοποίηση της κλάσης με τις ιδιότητες ενός μουσικού οργάνου:
        name --> Όνομα μουσικού οργάνου, kind --> Τύπος οργάνου
        category --> Κατηγορία, year --> Έτος κατασκευής
        manufacturer --> Κατασκευαστής
    """
    def __init__(self, name, kind, category, year, manufacturer):
        self.name = name
        self.kind = kind
        self.category = category
        self.year = year
        self.manufacturer = manufacturer

    # def __str__(self):Επιστρέφει ένα μορφοποιημένο string με τις πληροφορίες του μουσικού οργάνου.
    def __str__(self):
        return (f"Instrument: {self.name}, Kind: {self.kind}, "
                f"Category: {self.category}, Year: {self.year}, "
                f"Manufacturer: {self.manufacturer}")
"""
    Βήμα 2: Δημιουργία των μουσικών οργάνων ως αντικείμενα της κλάσης Instrument
"""
grand_piano = Instrument("Grand Piano", "Piano", "έγχορδο", 2020, "Fazioli")
rhythm_guitar = Instrument("Rhythm Guitar", "Guitar", "έγχορδο", 2015, "Fender")
first_violin = Instrument("First Violin", "Violin", "έγχορδο", 1715, "Antonio Stradivari")
principal_flute = Instrument("Principal Flute", "Flute", "πνευστό", 2018, "Yamaha")

"""
Βήμα 3: Δημιουργία λίστας orchestra που περιέχει τα αντικείμενα 
