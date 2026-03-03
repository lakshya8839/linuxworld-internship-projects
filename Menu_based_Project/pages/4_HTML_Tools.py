import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="HTML + JS Viewer", layout="centered")
st.title("🌐 HTML + JavaScript Interface")

st.markdown("This page displays your custom HTML tool with a styled background.")

# Load HTML content from file
with open("menu_project_JS.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Inject CSS to set background image
background_css = """
<style>
body {
    background-image: url("https://media.istockphoto.com/id/1680372201/photo/flowing-lines-abstract-background-image-waves-copy-space-dark.jpg?s=612x612&w=0&k=20&c=Kb4aCMrhBWYZHpSQ523HS3vm0Vu3AOt0vU3qszJWhik=");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    color: white;
}
</style>
"""

# Combine background + HTML content
full_html = background_css + html_code

# Render with background
components.html(full_html, height=600, scrolling=True)
