st.subheader("📩 Send SMS")

with st.form("sms_form"):
    twilio_sid = st.text_input("Twilio SID", type="password")
    twilio_token = st.text_input("Twilio Auth Token", type="password")
    twilio_number = st.text_input("Twilio Phone Number (with +country code)")
    recipient_number = st.text_input("Recipient Phone Number (with +country code)")
    sms_body = st.text_input("Message Text", value="Hello from Python, I am Lakshya!")
    sms_submit = st.form_submit_button("Send SMS")

    if sms_submit:
        try:
            client = Client(twilio_sid, twilio_token)
            message = client.messages.create(
                body=sms_body,
                from_=twilio_number,
                to=recipient_number
            )
            st.success(f"✅ SMS sent! SID: {message.sid}")
        except Exception as e:
            st.error(f"❌ SMS Error: {e}")