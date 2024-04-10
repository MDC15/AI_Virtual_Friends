import streamlit as st

# Set the title and subtitle of the web app
st.title("My First Streamlit App")
st.subheader("This is a simple Streamlit app to demonstrate its basic functionalities.")

# Create a text input field to get user input
user_input = st.text_input("Enter your name:")

# Display the user's input back to them
st.write("Hello, {}!".format(user_input))

# Create a button and a checkbox
if st.button("Click me!"):
    st.write("You clicked the button!")

checkbox = st.checkbox("Check me!")

# Display the state of the checkbox
if checkbox:
    st.write("The checkbox is checked!")

# Create a selectbox to get user input
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an option:", options)

# Display the selected option
st.write("You selected:", selected_option)

# Create a multiselect widget to get user input
selected_options = st.multiselect("Choose multiple options:", options)

# Display the selected options
st.write("You selected:", selected_options)

# Create a slider to get user input
number = st.slider("Choose a number:", 0, 100)

# Display the selected number
st.write("You chose the number:", number)

# Create a text area to get user input
text = st.text_area("Enter some text:")

# Display the entered text
st.write("You entered:", text)

# Create a file uploader to get user input
uploaded_file = st.file_uploader("Choose a file to upload:")

# Display the uploaded file
if uploaded_file is not None:
    st.write("You uploaded:", uploaded_file.name)
