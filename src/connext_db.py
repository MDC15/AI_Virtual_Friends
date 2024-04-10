import sqlite3
import streamlit as st


# Create a function to connect to the database
def get_connection():
    return sqlite3.connect("mydb.db")


# Create a function to execute a query
def execute_query(query):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()


# Get the data from the database
results = execute_query("SELECT * FROM mytable")

# Display the data in a table
st.table(results)
