import streamlit as st
from PIL import Image
import os

st.title("🔒 Payment Window")
st.subheader("Scan the QR Code below to complete your payment")

# Display QR code image
qr_path = r"C:\Users\lakshya\Documents\images\Qr.jpg"
if os.path.exists(qr_path):
    st.image(qr_path, caption="Scan to Pay", use_container_width=True)
else:
    st.error("QR scanner image not found.")

# Upload payment screenshot
screenshot = st.file_uploader("Upload your payment screenshot here", type=["jpg", "jpeg", "png"])

# Flag to check registration
if "registration_complete" not in st.session_state:
    st.session_state.registration_complete = False

if screenshot is not None:
    st.success("Screenshot uploaded successfully ✅")

    if st.button("Submit Payment"):
        st.success("🎉 Payment Verified! Your registration is complete.")
        st.session_state.registration_complete = True  # ✅ Mark registration as complete

        st.write("📌 Booking ID:", st.session_state.get("booking_id", "N/A"))
        st.write("👤 Name:", st.session_state.get("user_name", "N/A"))
        st.write("📧 Email:", st.session_state.get("email", "N/A"))
        st.write("📞 Phone:", st.session_state.get("phone", "N/A"))
        st.write("📅 Date:", st.session_state.get("date", "N/A"))
        st.write("🎟️ Tickets:", st.session_state.get("tickets", "N/A"))

        # WhatsApp link
        phone = st.session_state.get("phone", "")
        message = "🎉 Your registration is successful for the Musical Festival!"
        encoded_message = message.replace(" ", "%20")
        if phone:
            whatsapp_url = f"https://wa.me/91{phone}?text={encoded_message}"
            st.markdown(f"[📲 Click here to send WhatsApp Confirmation]({whatsapp_url})", unsafe_allow_html=True)
        else:
            st.warning("Phone number not found in session. Cannot generate WhatsApp link.")

# Voice message section
if st.button("Click here!!"):
    import pyttsx3
    speaker = pyttsx3.init()

    if st.session_state.registration_complete:
        speaker.say("Congratulations! You have completed your registration.")
    else:
        speaker.say("Your registration is not done. Please complete it first.")

    speaker.runAndWait()


# Navigation
st.markdown("---")
if st.button("🏠 Back to Home Page"):
    st.switch_page("pages/6_frontpage.py")

