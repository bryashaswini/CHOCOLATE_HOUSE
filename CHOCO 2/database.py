import sqlite3

# Database connection setup
def get_db_connection():
    conn = sqlite3.connect('chocolate_house.db')
    conn.row_factory = sqlite3.Row  # allows for column name access
    return conn

# Function to fetch available seasonal flavors
def get_available_flavors(season):
    conn = get_db_connection()
    query = "SELECT * FROM flavors WHERE available = 1 AND season = ?"
    flavors = conn.execute(query, (season,)).fetchall()
    conn.close()
    return flavors

# Function to add a new seasonal flavor
def add_flavor(name, season):
    conn = get_db_connection()
    conn.execute("INSERT INTO flavors (name, season, available) VALUES (?, ?, 1)", (name, season))
    conn.commit()
    conn.close()

# Function to delete a flavor by its ID
def delete_flavor(flavor_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM flavors WHERE id = ?", (flavor_id,))
    conn.commit()
    conn.close()

# Function to fetch all ingredients
def get_all_ingredients():
    conn = get_db_connection()
    query = "SELECT * FROM ingredients"
    ingredients = conn.execute(query).fetchall()
    conn.close()
    return ingredients

# Function to add an ingredient
def add_ingredient(name, quantity):
    conn = get_db_connection()
    conn.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

# Function to fetch all customer feedback
def get_all_feedback():
    conn = get_db_connection()
    query = "SELECT * FROM feedback"
    feedback = conn.execute(query).fetchall()
    conn.close()
    return feedback

# Function to add customer feedback
def add_feedback(suggestion, allergy_concern):
    conn = get_db_connection()
    conn.execute("INSERT INTO feedback (suggestion, allergy_concern) VALUES (?, ?)", (suggestion, allergy_concern))
    conn.commit()
    conn.close()
