import streamlit as st
import pandas as pd

# Load the preprocessed dataset
data = pd.read_csv('preprocessed.csv')

# Sidebar
st.sidebar.header("Recipe Recommendation System")

# Get user inputs
ingredients = st.sidebar.text_input("Enter the ingredients you have, separated by commas")
recipe_type = st.sidebar.selectbox("Select recipe type", data['group'].unique())
dietary_restrictions = st.sidebar.multiselect("Select dietary restrictions", ["Vegetarian", "Vegan", "Gluten-free", "Dairy-free", "Low-carb"])

# Filter recipes based on user inputs
filtered_data = data[data['group'] == recipe_type]
if dietary_restrictions:
    for restriction in dietary_restrictions:
        filtered_data = filtered_data[filtered_data['process'].str.contains(restriction, case=False)]

if ingredients:
    ingredient_list = [x.strip() for x in ingredients.split(',')]
    for ingredient in ingredient_list:
        filtered_data = filtered_data[filtered_data['ingredient'].str.contains(ingredient, case=False)]

# Display recommended recipes
st.subheader("Recommended Recipes")
if filtered_data.empty:
    st.warning("No recipes found for your search criteria. Please try again.")
else:
    for idx, row in filtered_data.head(5).iterrows():
        st.write(f"{row['name']} ({row['rating']}/5)")
        st.write(f"Ingredients: {row['ingredient']}")
        st.write(f"Process: {row['process']}")
        st.write("")
