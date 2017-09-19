This test suite consists of 3 test cases.
Allegro_TC1 uses Xpath to locate elements on a web service and checks if all the chosen product categories are displayed in breadcrumbs.
Allegro_TC2 uses CSS locators to find other product categories.
Allegro_TC3 focusses on adding a specific product to cart and verifying that the product is in the cart by returning to the main page and taking a screenshot as proof.
All the above-mentioned test cases inherit the set up and tear down functions from a common driver_creation module.
