import streamlit as st
import random

st.title("Welcome to India's best Booking Platform")
st.header("🎵 Musical Festival Registration Form")

# Track registration status
if "registered" not in st.session_state:
    st.session_state.registered = False

if not st.session_state.registered:
    with st.form(key='registration_form'):
        first_name = st.text_input("First Name:")
        last_name = st.text_input("Last Name:")
        email = st.text_input("Email:")
        phone = st.text_input("Phone Number:")
        show_date = st.selectbox("Select an available date:", [
            '21 June 2025', '22 June 2025', '23 June 2025', '24 June 2025'
        ])
        tickets = st.number_input("Number of Tickets:", min_value=1, max_value=10, step=1)
        submit = st.form_submit_button("Proceed to Payment")

    if submit:
        if not first_name or not last_name or not email or not phone:
            st.error("❌ Please fill in all the details before proceeding.")
        else:
            # Save user data
            st.session_state.booking_id = random.randint(1000, 9999)
            st.session_state.user_name = f"{first_name} {last_name}"
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.date = show_date
            st.session_state.tickets = tickets
            st.session_state.registered = True
            st.rerun()  # ✅ rerun to show success page
else:
    # Display confirmation
    st.success("Registration Successful! 🎉")
    st.write("📌 Booking ID:", st.session_state.booking_id)
    st.write("👤 Name:", st.session_state.user_name)
    st.write("📧 Email:", st.session_state.email)
    st.write("📞 Phone:", st.session_state.phone)
    st.write("📅 Date:", st.session_state.date)
    st.write("🎟️ Tickets:", st.session_state.tickets)

    if st.button("Go to Payment Page"):
        st.switch_page("pages/8_Payment_window.py")
