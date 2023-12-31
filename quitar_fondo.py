# LLIBRERIES UTILITZADES

import streamlit as st
from PIL import Image
from rembg import remove
import io
import os


# DESENVOLUPAMANT DE LES FUNCIONS ENCARREGADES D'ELIMINAR EL FONS DE L'IMATGE

def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    processed_imagen = remove_background(image)
    return processed_imagen

def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    processed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(processed_image_bytes))


# DESENVOLUPAMENT DE LA PART GRÀFICA DEL SCRIPT

st.header("SUPRESSIÓ DEL FONS D'IMATGES")
st.text("""
Feu clic al botó de 'Browse Files' per cercar i seleccionar una imatge.
Posteriorment premeu el botó de 'ELIMINAR FONS' perquè s'executi l'acció.
""")
uploaded_image = st.file_uploader("TRIA UNA IMATGE", type=["jpg", "jpeg", "png"])


# DESENVOLUPAMENT DE L'EXECUCIÓ DE FUNCIONS I RETORN DE LA IMATGE
if uploaded_image is not None:

    st.image(uploaded_image, caption="IMATGE PUJADA AMB ÈXIT", use_column_width=True)

    eliminate_button = st.button(label="ELIMINAR EL FONS")

    if eliminate_button:

        processed_image = process_image(uploaded_image)

        st.image(processed_image, caption="FONS ELIMINAT AMB ÈXIT", use_column_width=True)

        processed_image.save("documents/processed_image.png")

        with open("documents/processed_image.png", "rb") as f:
            image_data = f.read()

        st.download_button("DESCARREGAR L'IMATGE FINAL", data=image_data, file_name="documents/processed_image.png")
        os.remove("documents/processed_image.png")

