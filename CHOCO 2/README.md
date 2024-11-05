# HOW TO RUN THE CODE 

1. CLONE THE GITHUB REPOSITORY OR DOWNLOAD THE ZIP FILE
2. Open the project folder (CHOCO 2) in VS Code using File > Open Folder.
3. OPEN APP.PY FILE, THEN RIGHT CLICK
4. RUN IN PYTHON TERMINAL
5. IN TERMINAL, TYPE python app.py 
6. THE FOLLOWING IS DISPALYED
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    Running on http://127.0.0.1:5000 
    
7. GO TO BROWSER, TYPE http://127.0.0.1:5000 TO GET THE OUTPUT.


 # Achieving the Key Criteria

1. Seasonal Flavor Offerings
How this project achieves it:


Add Seasonal Flavors: The admin can add a new flavor and mark it as seasonal. The form for adding a flavor includes fields like Flavor Name, Description, and Seasonal Availability.

View Seasonal Flavors: On the homepage, a list of seasonal flavors is displayed to the customers. These are pulled from the database, where the seasonal flag is set to True.

Database: The Flavors table has the following relevant fields:

id: Unique identifier for the flavor.
name: Name of the flavor (e.g., "Chocolate Mint").
description: A short description of the flavor.
seasonal: A boolean field indicating whether the flavor is seasonal or not.


2. Ingredient Inventory
How this project achieves it:

The ingredient inventory is managed through an Ingredients table in the SQLite database. Admins can add new ingredients to the inventory, view the current stock levels, and update the stock quantity when necessary.

Add Ingredients: Admins can add new ingredients by entering details such as the ingredient name (e.g., "Cocoa Powder") and its quantity (e.g., "500 grams").

Update Ingredient Stock: The admin can update the stock levels (e.g., from "500 grams" to "300 grams") to reflect changes in the inventory.

View Inventory: The admin can view all ingredients along with their stock levels.

Database Structure: The Ingredients table consists of the following fields:

id: Unique identifier for the ingredient.
name: Name of the ingredient (e.g., "Cocoa Powder").
quantity: Quantity of the ingredient in stock (e.g., "500 grams").


3. Customer Flavor Suggestions and Allergy Concerns
How this project achieves it:

The Customer Flavor Suggestions feature allows customers to submit suggestions for new flavors. Additionally, customers can flag potential allergens (such as "Nuts", "Dairy", etc.) when making their suggestions, ensuring that allergy concerns are properly addressed.

Submit Flavor Suggestions: Customers can visit the Customer Suggestions page, where they can input their new flavor ideas.

Allergy Concerns: Along with the flavor suggestion, customers can select any allergens they are concerned about (e.g., nuts, dairy). This helps the admin to evaluate and address these concerns when reviewing the suggestions.

Database: The Suggestions table stores customer flavor suggestions and allergy concerns. It includes the following fields:

id: Unique identifier for the suggestion.
flavor: The name of the suggested flavor.
allergens: A list of allergens associated with the suggested flavor.