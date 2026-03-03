import streamlit as st
import base64
import os

# Image path
image_path = "images/event_img.jpg"  # Update path if needed

# Convert image to base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Apply custom styles
if os.path.exists(image_path):
    img_base64 = get_base64_image(image_path)
    custom_css = f"""
    <style>
    /* Full background image */
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        padding-top: 0px !important;
    }}

    /* Remove white header box */
    [data-testid="stHeader"] {{
        background: transparent;
        height: 0rem;
        visibility: hidden;
    }}

    

    /* Main content block */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.3);
        padding: 2rem;
        border-radius: 12px;
    }}

    /* Make all text black */
    h1, h2, h3, h4, h5, h6, p {{
        color: #000000 !important;
    }}

    /* Button style */
    .stButton button {{
        background-color: white !important;
        color: black !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: 1px solid #ccc;
        transition: 0.3s;
    }}

    .stButton button:hover {{
        background-color: #f0f0f0 !important;
        border: 1px solid #888;
        cursor: pointer;
    }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
else:
    st.error("Image not found. Please check the path.")

# Main content inside styled container
st.markdown("<div class='block-container'>", unsafe_allow_html=True)

st.title("🎤 Event Pass")
st.write("A Concert Booking Platform.")
st.write("📍 JECC, Jaipur")
st.write("🕗 8:30 PM")

st.write("## What would you like to do?")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎟️ Book Ticket"):
        st.switch_page("pages/Registration_page.py")

with col2:
    if st.button("🔍 Check Your Ticket"):
        st.switch_page("pages/check_ticket.py")

st.markdown("</div>", unsafe_allow_html=True)
