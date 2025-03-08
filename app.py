import streamlit as st
import json
import os

# Constants for file paths
DATA_FILE = "data.json"
FIELDS_FILE = "fields.json"

# Load fields from JSON file or use default
def load_fields():
    if os.path.exists(FIELDS_FILE):
        with open(FIELDS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return ["name", "email", "ethnicity", "religion", "age", "address", "country", "technical_skills", "soft_skills"]

# Save new fields to JSON file
def save_fields(fields):
    with open(FIELDS_FILE, "w") as file:
        json.dump(fields, file, indent=4)

# Load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Initialize session state
if "user_data" not in st.session_state:
    st.session_state.user_data = load_data()
    st.session_state.fields = load_fields()

if "technical_skills" not in st.session_state.user_data:
    st.session_state.user_data["technical_skills"] = []

if "soft_skills" not in st.session_state.user_data:
    st.session_state.user_data["soft_skills"] = []

# Title and Introduction
st.title("AutoForm Data Manager")
st.write("Enter your personal details to autofill forms.")

# Dynamic fields rendering
for field in st.session_state.fields:
    # Dynamically generate input fields for each field in the list
    if field not in st.session_state.user_data:
        st.session_state.user_data[field] = ""
    st.session_state.user_data[field] = st.text_input(field.capitalize(), st.session_state.user_data.get(field, ""))

# Skills Section
st.subheader("Technical Skills")
technical_skill = st.text_input("Add a Technical Skill")
if st.button("Add Technical Skill"):
    if technical_skill and technical_skill not in st.session_state.user_data["technical_skills"]:
        st.session_state.user_data["technical_skills"].append(technical_skill)
        save_data(st.session_state.user_data)
        st.success("Technical skill added successfully!")

st.write("Your Technical Skills:", ", ".join(st.session_state.user_data["technical_skills"]))

st.subheader("Soft Skills")
soft_skill = st.text_input("Add a Soft Skill")
if st.button("Add Soft Skill"):
    if soft_skill and soft_skill not in st.session_state.user_data["soft_skills"]:
        st.session_state.user_data["soft_skills"].append(soft_skill)
        save_data(st.session_state.user_data)
        st.success("Soft skill added successfully!")

st.write("Your Soft Skills:", ", ".join(st.session_state.user_data["soft_skills"]))

# Allow user to add a new field dynamically
new_field_name = st.text_input("Enter new field name")
new_field_value = st.text_input("Enter value for the new field")

if st.button("Add New Field"):
    if new_field_name and new_field_name not in st.session_state.fields:
        st.session_state.fields.append(new_field_name)
        st.session_state.user_data[new_field_name] = new_field_value
        save_fields(st.session_state.fields)  # Save updated fields list
        save_data(st.session_state.user_data)  # Save updated user data
        st.success(f"New field '{new_field_name}' added successfully!")

# Save the details
if st.button("Save Details"):
    save_data(st.session_state.user_data)
    st.success("Details saved successfully!")

# Show stored data
if st.button("Show Stored Data"):
    st.json(st.session_state.user_data)
