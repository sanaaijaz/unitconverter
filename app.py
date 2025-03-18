import streamlit as st

st.title("🐱‍🏍Unit Converter App✨")

st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a Category")

Category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return 0  # Properly aligned

if Category == "Length":
    unit = st.selectbox("Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif Category == "Weight":
    unit = st.selectbox("⚖⚖ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif Category == "Time":
    unit = st.selectbox("⏲ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter Your Value")  # Correct indentation

if st.button("Convert"):
    result = convert_units(Category, value, unit)
    st.success(f"The result is {result:.2f}")
