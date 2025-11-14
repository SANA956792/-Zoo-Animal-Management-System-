import streamlit as st

# -------------------- CLASS DEFINITIONS --------------------

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species   

    def show_info(self):
        return f"Name: {self.name}, Species: {self.species}"


class Mammal(Animal):
    def __init__(self, food_type=None, **kwargs):
        self.food_type = food_type
        super().__init__(**kwargs)

    def show_info(self):
        info = super().show_info()
        return f"{info}, Food Type: {self.food_type}, Animal Type: Mammal"


class Reptile(Animal):
    def __init__(self, reptile_type=None, food=None, **kwargs):
        self.reptile_type = reptile_type
        self.food = food
        super().__init__(**kwargs)

    def show_info(self):
        info = super().show_info()
        return f"{info}, Reptile Type: {self.reptile_type}, Reptile Food: {self.food}, Animal Type: Reptile"


class Zoo(Mammal,Reptile):
    """Zoo dynamically creates Mammal or Reptile based on category"""
    def __init__(self, name, species, zoo_name=None, location=None,
                 category=None, food_type=None, reptile_type=None, food=None):
        self.name = name
        self.species = species
        self.zoo_name = zoo_name
        self.location = location
        self.category = category

        # Create the right object dynamically
        if category == "Mammal":
            self.animal = Mammal(name=name, species=species, food_type=food_type)
        elif category == "Reptile":
            self.animal = Reptile(name=name, species=species, reptile_type=reptile_type, food=food)
        # else:
        #     self.animal = Animal(name, species)

    def show_info(self):
        info = self.animal.show_info()
        return f"{info}, Zoo Name: {self.zoo_name}, Location: {self.location}"


st.title("🐾 Zoo Animal Management System")

# Basic Inputs
name = st.text_input("Enter Animal Name")
species = st.text_input("Enter Animal Species")
zoo_name = st.text_input("Enter Zoo Name")
location = st.text_input("Enter Zoo Location")

# Animal Type Selection
category = st.radio("Select Animal Type", ["Mammal", "Reptile"])

# Conditional Fields
food_type = None
reptile_type = None
food = None

if category == "Mammal":
    food_type = st.text_input("Enter Food Type (e.g., Carnivore, Herbivore)")
elif category == "Reptile":
    reptile_type = st.text_input("Enter Reptile Type (e.g., Venomous, Non-Venomous)")
    food = st.text_input("Enter Reptile Food Type (e.g., Insects, Meat)")

# Show Info Button
if st.button("Show Animal Info"):
    zoo_animal = Zoo(
        name=name,
        species=species,
        zoo_name=zoo_name,
        location=location,
        category=category,
        food_type=food_type,
        reptile_type=reptile_type,
        food=food
    )

    st.subheader("📋 Animal Information")
    st.success(zoo_animal.show_info())
