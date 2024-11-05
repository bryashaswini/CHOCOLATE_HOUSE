from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database (make sure this is your database initialization logic)
def initialize_db():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        flavor_id INTEGER PRIMARY KEY,
        flavor_name TEXT,
        season TEXT,
        available BOOLEAN
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        ingredient_id INTEGER PRIMARY KEY,
        ingredient_name TEXT,
        stock_quantity INTEGER,
        allergens TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_feedback (
        feedback_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        flavor_suggestion TEXT,
        allergy_concerns TEXT
    )
    ''')
    connection.commit()
    connection.close()

# Routes for managing seasonal flavors, ingredients, and customer feedback
@app.route('/')
def index():
    return render_template('index.html')

# Add a seasonal flavor
@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor_route():
    if request.method == 'POST':
        flavor_name = request.form['flavor_name']
        season = request.form['season']
        available = bool(request.form.get('available'))
        
        connection = sqlite3.connect("chocolate_house.db")
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO seasonal_flavors (flavor_name, season, available)
        VALUES (?, ?, ?)
        ''', (flavor_name, season, available))
        connection.commit()
        connection.close()
        
        return redirect(url_for('list_flavors_route'))
    return render_template('add_flavor.html')

# List all seasonal flavors
@app.route('/list_flavors')
def list_flavors_route():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()
    connection.close()
    return render_template('list_flavors.html', flavors=flavors)

# Add an ingredient
@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient_route():
    if request.method == 'POST':
        ingredient_name = request.form['ingredient_name']
        stock_quantity = int(request.form['stock_quantity'])
        allergens = request.form.get('allergens', '')
        
        connection = sqlite3.connect("chocolate_house.db")
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO ingredients (ingredient_name, stock_quantity, allergens)
        VALUES (?, ?, ?)
        ''', (ingredient_name, stock_quantity, allergens))
        connection.commit()
        connection.close()
        
        return redirect(url_for('list_ingredients_route'))
    return render_template('add_ingredient.html')

# List all ingredients
@app.route('/list_ingredients')
def list_ingredients_route():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ingredients')
    ingredients = cursor.fetchall()
    connection.close()
    return render_template('list_ingredients.html', ingredients=ingredients)

# Add customer feedback
@app.route('/add_feedback', methods=['GET', 'POST'])
def add_feedback_route():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_suggestion = request.form.get('flavor_suggestion', '')
        allergy_concerns = request.form.get('allergy_concerns', '')
        
        connection = sqlite3.connect("chocolate_house.db")
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO customer_feedback (customer_name, flavor_suggestion, allergy_concerns)
        VALUES (?, ?, ?)
        ''', (customer_name, flavor_suggestion, allergy_concerns))
        connection.commit()
        connection.close()
        
        return redirect(url_for('list_feedback_route'))
    return render_template('add_feedback.html')

# List all customer feedback
@app.route('/list_feedback')
def list_feedback_route():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM customer_feedback')
    feedbacks = cursor.fetchall()
    connection.close()
    return render_template('list_feedback.html', feedbacks=feedbacks)

# Search functionality
@app.route('/search', methods=['GET', 'POST'])
def search_route():
    if request.method == 'POST':
        query = request.form['query']
        # Search in ingredients and feedback (for simplicity)
        connection = sqlite3.connect("chocolate_house.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ingredients WHERE ingredient_name LIKE ?", ('%' + query + '%',))
        search_results_ingredients = cursor.fetchall()
        cursor.execute("SELECT * FROM customer_feedback WHERE flavor_suggestion LIKE ? OR allergy_concerns LIKE ?", ('%' + query + '%', '%' + query + '%'))
        search_results_feedback = cursor.fetchall()
        connection.close()
        
        return render_template('search_results.html', query=query, ingredients=search_results_ingredients, feedbacks=search_results_feedback)
    return render_template('search.html')

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
