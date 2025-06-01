import qrcode as qr
import streamlit as st
import io
import validators


st.set_page_config(page_title="QR Code Generator", page_icon="🔗",layout="centered")
st.title("QR Code Generator")
st.markdown("Easily turn any link into a QR code! Just paste your URL below and click the button to generate your QR code instantly.")


url = st.text_input("Enter the URL:", placeholder="https://example.com")

button = st.button("Generate QR code")

if button:
    if url and validators.url(url):
        qr_img = qr.make(url)

        img_bytes = io.BytesIO()
        qr_img.save(img_bytes , format="png")
        img_bytes.seek(0)

        st.image(img_bytes, caption="📷 Here is you QR code")

        st.download_button("Download QR code", data=img_bytes, file_name= "qr-code.png", mime="image/png")  

    else:
        st.warning("Please enter a valid url.")

    

