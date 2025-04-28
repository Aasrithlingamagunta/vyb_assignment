import pandas as pd

class QuantityConverter:
    def __init__(self, measurement_file_path):
        self.measurements = pd.read_excel(measurement_file_path, sheet_name='Unit of measurements')
        self.unit_to_grams = {
            'pieces count': 100,
            '150ml cup or katori': 150,
            '250ml glass': 250,
            '5ml teaspoon': 5,
            '15ml tablespoon': 15
        }

    def standardize_quantity(self, quantity_text):
        quantity_text = quantity_text.lower()
        quantity_value = 1

        if any(char.isdigit() for char in quantity_text):
            parts = quantity_text.split()
            for part in parts:
                if part.replace('.', '', 1).isdigit():
                    quantity_value = float(part)
                    break

        for unit, grams in self.unit_to_grams.items():
            if any(word in quantity_text for word in unit.split()):
                return quantity_value * grams

        return None
