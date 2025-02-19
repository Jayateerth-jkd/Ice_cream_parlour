import sqlite3
from database import conn

class IceCreamParlor:
    def __init__(self):
        self.conn = sqlite3.connect('ice_cream.db')
        self.cursor = self.conn.cursor()

    def add_seasonal_flavor(self, name, description):
        self.cursor.execute('''
        INSERT INTO seasonal_flavors (name, description) VALUES (?, ?)
        ''', (name, description))
        self.conn.commit()

    def search_flavors(self, keyword):
        self.cursor.execute('''
        SELECT * FROM seasonal_flavors WHERE name LIKE ? OR description LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        return self.cursor.fetchall()

    def add_allergen(self, name):
        self.cursor.execute('''
        INSERT OR IGNORE INTO allergens (name) VALUES (?)
        ''', (name,))
        self.conn.commit()

    def add_suggestion(self, flavor_name, allergy_concerns):
        self.cursor.execute('''
        INSERT INTO customer_suggestions (flavor_name, allergy_concerns) VALUES (?, ?)
        ''', (flavor_name, allergy_concerns))
        self.conn.commit()

    def view_cart(self):
        # Placeholder for cart functionality
        print("Cart functionality to be implemented.")

# Example usage
if __name__ == "__main__":
    parlor = IceCreamParlor()
    parlor.add_seasonal_flavor("Pumpkin Spice", "A seasonal favorite with cinnamon and nutmeg.")
    print(parlor.search_flavors("Pumpkin"))
    parlor.add_allergen("Nuts")
    parlor.add_suggestion("Mango", "None")
    parlor.view_cart()