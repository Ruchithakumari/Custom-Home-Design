import streamlit as st
from design_generator import generate_design_idea
from image_fetcher import fetch_image_from_lexica

st.title("🏡 Custom Home Design Assistant")

# User inputs
style = st.text_input("Enter home style (e.g., Modern, Rustic, Classic)")
size = st.text_input("Enter home size (e.g., 2500 sq ft)")
rooms = st.text_input("Enter number of rooms")

if st.button("Generate Design"):
    if style and size and rooms:
        # Generate home design
        design = generate_design_idea(style, size, rooms)
        st.markdown(design)
        
        # Fetch image
        image_url = fetch_image_from_lexica(style)
        if image_url:
            st.image(image_url, caption=f"{style} Home Design")
        else:
            st.warning("No image found for this style.")
    else:
        st.warning("Please fill in all fields.")
