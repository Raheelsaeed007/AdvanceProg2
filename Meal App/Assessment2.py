# The meal Database API

# Importing  necessary modules
import requests  # HTTP requests
import tkinter as tk  # GUI
from PIL import Image, ImageTk  # images
from io import BytesIO  # For handling binary data
import tkinter.messagebox  # For displaying message boxes

# Function to fetch a random meal from the API
def random_meal():
    url = "http://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    if response.status_code == 200:
        meal = response.json()["meals"][0]
        return meal
    else:
        return None

# clear the text
def clear_labels():
    for label in [meal_label, image_label, ingredients_label, measurements_label, area_label, category_label]:
        label.config(text="")

# Function to display information about a meal
def show_meal(meal_name):
    global meal_label, image_label, ingredients_label, measurements_label, area_label, category_label
    clear_labels()

    # Fetch meal data from  DB API
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meal = data["meals"][0]

        # Display meal name and image
        meal_label = tk.Label(root, text=meal["strMeal"], font=("Helvetica", 16))
        meal_label.place(x=350, y=250)

        image_url = meal["strMealThumb"]
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image = image.resize((352, 204), resample=Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            image_label = tk.Label(root, image=image)
            image_label.image = image
            image_label.place(x=592, y=250)

            # Display ingredients, measurements, area, and category
            ingredients = [meal[f"strIngredient{i}"] for i in range(1, 21) if meal[f"strIngredient{i}"]]
            measurements = [meal[f"strMeasure{i}"] for i in range(1, 21) if meal[f"strMeasure{i}"]]

            ingredients_label = tk.Label(root, text="Ingredient: " + ", ".join(ingredients), font=("Helvetica", 12), wraplength=800)
            ingredients_label.place(x=350, y=550)

            measurements_label = tk.Label(root, text="Measurement: " + ", ".join(measurements), font=("Helvetica", 12), wraplength=800)
            measurements_label.place(x=350, y=670)

            area_label = tk.Label(root, text="Area: " + meal["strArea"], font=("Helvetica", 16))
            area_label.place(x=350, y=777)

            category_label = tk.Label(root, text="Category: " + meal["strCategory"], font=("Helvetica", 16))
            category_label.place(x=350, y=807)

        else:
            meal_label = tk.Label(root, text="No meal found")
            meal_label.pack()
    else:
        meal_label = tk.Label(root, text="No meal found")
        meal_label.pack()

# create a GUI with tkinter
root = tk.Tk()
root.geometry("1500x1000+200+0")  # size and position of the window
root.maxsize(1500, 1000)  # maximum size of the window
root.minsize(1500, 1000)  # minimum size of the window


# Load the image file
bg_image = ImageTk.PhotoImage(Image.open("bg2.jpg"))  # background image
background_label = tk.Label(root, image=bg_image)  # Create a label to display the background image
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the background label, covering the entire window

# Get the width and height of the window
window_width = root.winfo_width()
window_height = root.winfo_height()


meal_label = tk.Label(root, text="")  # label for displaying meal information
image_label = tk.Label(root, text="")  # label for displaying images
ingredients_label = tk.Label(root, text="")  # label for displaying ingredients
measurements_label = tk.Label(root, text="")  # label for displaying measurements
area_label = tk.Label(root, text="")  # label for displaying the meal area
category_label = tk.Label(root, text="")  # label for displaying the meal category

def show_random_meal():
    clear_labels()
    meal = random_meal()  # Get a random meal from the API

    if meal:
        show_meal(meal["strMeal"])  # Display the details of the random meal
    else:
        meal_label = tk.Label(root, text="No meal found")  # Display a message if no meal is found
        meal_label.pack()

def show_info():
    tkinter.messagebox.showinfo(
        "Information",
        "Welcome to the Meal API! Explore random and top-rated delights with an option to search. Click the buttons to view recipes."
    )  

RandomButton = tk.Button(
    root,
    text="Random Meal",
    command=show_random_meal,
    fg="white",
    font=("Italiana", 18),
)  #  random meal
RandomButton.place(x=1180, y=80, relwidth=0.1, relheight=0.05)  # Place the random meal button

RandomButton.config(
    borderwidth=5,
    relief="flat",
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
    padx=0,
)  # appearance of the random meal button

#  button for displaying instructions
InstructionButton = tk.Button(
    root,
    text="Instruction",
    command=show_info,
    fg="white",
    font=("Italiana", 24),
)
InstructionButton.place(x=140, y=90, relwidth=0.1, relheight=0.05)

InstructionButton.config(
    borderwidth=5,
    relief="flat",
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
    padx=0,
)  # Configure the appearance of the instruction button

OmeletteButton = tk.Button(
    root,
    text="Omelette",
    command=lambda: show_meal("Bread omelette"),
    fg="white",
    font=("Italiana", 28),
)
OmeletteButton.place(x=300, y=185, relwidth=0.1, relheight=0.05)

OmeletteButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)

bistekButton = tk.Button(
    root,
    text="Bistek",
    command=lambda: show_meal("bistek"),
    fg="white",
    font=("Italiana", 28),
)  # Create a button for displaying information about Bistek
bistekButton.place(x=520, y=185, relwidth=0.1, relheight=0.05)  

bistekButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)  

burekButton = tk.Button(
    root,
    text="Burek",
    command=lambda: show_meal("burek"),
    fg="white",
    font=("Italiana", 28),
)  # Create a button for displaying information about Burek
burekButton.place(x=740, y=185, relwidth=0.1, relheight=0.05)  #  button

burekButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)  

PastaButton = tk.Button(
    root,
    text="Pasta",
    command=lambda: show_meal("Pasta"),
    fg="white",
    font=("Italiana", 28),
)
PastaButton.place(x=960, y=185, relwidth=0.1, relheight=0.05)

PastaButton.config(
    borderwidth=5,
    relief="flat",
    bg="#A94700",
    highlightcolor="#839b7f",
    activebackground="#B68558",
    highlightbackground="#B68558",
)

def top_rated_meals():
    # Fetch top-rated meals from the API
    top_rated_url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=Canadian"
    top_rated_response = requests.get(top_rated_url)

    if top_rated_response.status_code == 200:
        top_rated_data = top_rated_response.json()
        if top_rated_data["meals"]:
            show_meal(top_rated_data["meals"][0]["strMeal"])
        else:
            tkinter.messagebox.showinfo("Information", "No top-rated meals found.")
    else:
        tkinter.messagebox.showinfo("Information", "Failed to fetch top-rated meals. Please try again.")

top_rated_button = tk.Button(
    root,
    text="Show Top Rated Meals",
    command=top_rated_meals,
    fg="white",
    font=("Italiana", 16),
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
)
top_rated_button.place(x=400, y=80, relwidth=0.2, relheight=0.05)

# Fetch meal categories from the API
categories_url = "https://www.themealdb.com/api/json/v1/1/categories.php"
categories_response = requests.get(categories_url)

if categories_response.status_code == 200:
    categories_data = categories_response.json()
    meal_categories = [category["strCategory"] for category in categories_data["categories"]]
else:
    meal_categories = []

# Creating a dropdown for meal categories
category_var = tk.StringVar()
category_dropdown = tk.OptionMenu(root, category_var, *meal_categories)
category_dropdown.config(font=("Helvetica", 14), bg="#B68558", fg="white", activebackground="#936A54",
                         highlightbackground="#936A54")
category_dropdown.place(x=800, y=50)

def show_category_meals():
    selected_category = category_var.get()
    if selected_category:
        # Fetch meals based on the selected category and display them
        category_meals_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={selected_category}"
        category_meals_response = requests.get(category_meals_url)

        if category_meals_response.status_code == 200:
            category_meals_data = category_meals_response.json()
            if category_meals_data["meals"]:
                show_meal(category_meals_data["meals"][0]["strMeal"])
            else:
                tkinter.messagebox.showinfo("Information", f"No meals found in the {selected_category} category.")
        else:
            tkinter.messagebox.showinfo("Information", "Failed to fetch meals. Please try again.")

category_button = tk.Button(
    root,
    text="Show Category Meals",
    command=show_category_meals,
    fg="white",
    font=("Italiana", 16),
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
)
category_button.place(x=800, y=80, relwidth=0.2, relheight=0.05)

search_entry = tk.Entry(root, font=("Helvetica", 14))
search_entry.place(x=1100, y=150, width=200)

def search_meal():
    search_text = search_entry.get()
    if search_text:
        show_meal(search_text)

search_button = tk.Button(
    root,
    text="Search",
    command=search_meal,
    fg="white",
    font=("Italiana", 16),
    bg="#B68558",
    highlightcolor="#936A54",
    activebackground="#936A54",
    highlightbackground="#936A54",
)
search_button.place(x=1010, y=150, width=80, height=30)


# run the main loop
root.mainloop()
