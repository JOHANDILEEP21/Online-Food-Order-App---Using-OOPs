# Online-Food-Ordering-App---Using-OOPs

## Overview

The **Online Food Ordering App** is a Python-based console application that allows users to interact with various restaurants and food items. Users can search for restaurants, explore available food items, and view details of specific dishes. The app provides a simple and intuitive interface for a seamless user experience.

## Features

- **Show Restaurants**: Display a list of available restaurants with their details such as name, rating, location, and offers.
- **Show Food Items**: List all available food items along with their details such as name, rating, price, and description.
- **Search Restaurant**: Search for a specific restaurant by name.
- **Search Food Item**: Search for a specific food item by name.
- **Logout**: Exit the application.

## Project Structure

```plaintext
OnlineFoodApp/
│
├── Controllers/
│   ├── FoodManager.py       # Main controller that manages food items and restaurants.
│
├── Models/
│   ├── AbstractItem.py      # Abstract class for common properties of food items and restaurants.
│   ├── FoodItem.py          # Class representing individual food items.
│   ├── FoodMenu.py          # Class representing a food menu which includes multiple food items.
│   ├── Restaurant.py        # Class representing a restaurant.
│
├── main.py                  # Entry point of the application.
└── README.md                # Documentation of the project.
```

## Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/OnlineFoodApp.git
   cd OnlineFoodApp
   ```

2. Install the required dependencies (if any). There are no external dependencies for this project, so you can proceed directly to running the application.

### Running the Application

To run the application, execute the following command:

```bash
python main.py
```

### Application Flow

Upon running the application, you will be presented with a menu:

```plaintext
<< Welcome to Online Food Ordering App >>

1. Show Restaurants
2. Show FoodItems
3. Search Restaurant
4. Search FoodItem
5. Logout
```

You can choose any of the options by entering the corresponding number. For example:

- **Option 1**: Lists all available restaurants.
- **Option 2**: Lists all available food items.
- **Option 3**: Prompts you to enter a restaurant name to search.
- **Option 4**: Prompts you to enter a food item name to search.
- **Option 5**: Exits the application.

### Example Interaction

```plaintext
1. Show Restaurants
2. Show FoodItems
3. Search Restaurant
4. Search FoodItem
5. Logout
Please enter your choice: 4
-----------------------------------------------------------
Your choice is: -- SearchFoodItem --
-----------------------------------------------------------
Enter Food Name: Dosa
Food Item Found...
Name: Dosa, Rating: 4.4, Price: 60, Description: *****
```

In this example, the user chooses to search for a food item by selecting option 4 and entering "Dosa". The app returns the details of the "Dosa" food item.

## Class Descriptions

### `FoodItem` Class

Represents an individual food item with the following attributes:

- `name`: Name of the food item.
- `rating`: Rating of the food item.
- `price`: Price of the food item.
- `description`: Description of the food item.

### `FoodMenu` Class

Represents a menu that includes multiple food items. It has the following attributes:

- `type`: Type of menu (e.g., Veg, Non-Veg, Chinese).
- `FoodItems`: A list of `FoodItem` objects.

### `Restaurant` Class

Represents a restaurant with the following attributes:

- `name`: Name of the restaurant.
- `rating`: Rating of the restaurant.
- `location`: Location of the restaurant.
- `offer`: Current offer at the restaurant.
- `FoodMenus`: A list of `FoodMenu` objects.

### `FoodManager` Class

Handles the creation and management of restaurants, food items, and food menus. It provides methods to prepare food items, menus, and restaurants, and to perform search operations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to improve the application.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README file provides a comprehensive guide to understanding, setting up, and using the **Online Food Ordering App**. If you have any questions or need further assistance, please feel free to reach out.

## Find my Contact in my Portfolio: https://johandileep21.github.io/Dileepkumar.github.io/
