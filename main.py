import streamlit as st
import pandas as pd
import random
from openai import OpenAI

# Estética basada en la Tradición Argentina (Blanco y Rojo)
st.set_page_config(page_title="La Máquina de Alem", page_icon="🇦🇷")

st.markdown("""
    <style>
    .stApp { background-color: white; border-top: 20px solid #D32F2F; }
    h1 { color: #D32F2F; font-family: 'Helvetica'; font-weight: 900; }
    .stButton>button { background-color: #D32F2F; color: white; border-radius: 0px; font-weight: bold; width: 100%; }
    .software-box { background-color: #f8f9fa; border: 1px solid #D32F2F; padding: 20px; font-family: 'Courier New'; }
    .quote-box { background-color: #ffffff; border-left: 5px solid #D32F2F; padding: 15px; font-style: italic; color: #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 LA MÁQUINA DE ALEM")
st.write("#### Herramienta de Mantenimiento del Software Político")

# Conexión con OpenAI mediante Secrets
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    client = None
    st.sidebar.warning("API Key no detectada. Generación de imágenes desactivada.")

# Cargar Matriz basada en el Archivo Unificado
try:
    df = pd.read_csv("matriz.csv")
    
    st.write("---")
    coyuntura = st.text_input("Ingrese la crisis o conflicto para procesar:", placeholder="Ej: Corrupción, Inestabilidad económica...")

    if st.button("CORRER SOFTWARE RADICAL"):
        if coyuntura:
            # Selección de significante estable
            fila = df.sample(n=1).iloc[0]
            
            st.markdown(f"""
            <div class="software-box">
            <strong>ESTADO DEL SOFTWARE:</strong> {fila['Estado_del_Software'].upper()}<br>
            <strong>SIGNIFICANTE DETECTADO:</strong> {fila['Significante']}<br>
            <strong>SEDIMENTO DISCURSIVO:</strong> {fila['Sedimento_Discursivo']}
            </div>
            """, unsafe_allow_html=True)
            
            st.write("---")
            st.markdown("#### 📜 Fragmento del Código Fuente (Discurso Crudo):")
            st.markdown(f"<div class='quote-box'>{fila['Fragmento_Crudo']}</div>", unsafe_allow_html=True)
            
            st.write(f"Ante '{coyuntura}', el sistema requiere ejecutar la actualización basada en **{fila['Significante']}**. El hardware partidario debe activarse para aplicar este sedimento discursivo.")

            if client:
                with st.spinner("Diseñando actualización memética..."):
                    prompt = f"Political graphic for Argentina, style: {fila['Actualizacion_Memetica']}, red and white palette, professional minimalist."
                    response = client.images.generate(model="dall-e-3", prompt=prompt, n=1)
                    st.image(response.data[0].url, caption=f"Actualización: {fila['Significante']}")
            else:
                st.info(f"💡 **Actualización Memética Sugerida:** {fila['Actualizacion_Memetica']}")
        else:
            st.error("Ingrese un input para activar la máquina.")

except Exception as e:
    st.error(f"Fallo en la carga del sistema: {e}")

st.sidebar.markdown("---")
st.sidebar.write("**Mantenimiento Técnico:** La UCR no desaparece, queda en latencia activa esperando el re-inicio del sistema nacional.")
