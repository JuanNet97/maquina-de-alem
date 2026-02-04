import streamlit as st
import pandas as pd
import random
from openai import OpenAI

# 1. ESTÉTICA RADICAL
st.set_page_config(page_title="La Máquina de Alem", page_icon="🇦🇷")
st.markdown("""
    <style>
    .stApp { background-color: white; border-top: 15px solid #D32F2F; }
    h1 { color: #D32F2F; font-family: 'Helvetica'; font-weight: 800; text-transform: uppercase; }
    .stButton>button { background-color: #D32F2F; color: white; border: none; font-weight: bold; width: 100%; }
    .black-box { background-color: #1a1a1a; color: #fdfdfd; padding: 25px; border-left: 10px solid #D32F2F; font-family: 'Courier New'; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 LA MÁQUINA DE ALEM")
st.subheader("Caja Negra de Resiliencia Discursiva")

# 2. CONFIGURACIÓN
with st.sidebar:
    st.header("⚙️ Configuración")
    api_key = st.text_input("Introduce tu OpenAI API Key:", type="password")

# 3. PROCESAMIENTO
try:
    df = pd.read_csv("matriz.csv")
    
    coyuntura = st.text_area("💬 Ingresa la crisis o coyuntura actual:", placeholder="Ej: Crisis de confianza en las instituciones...")

    if st.button("PROCESAR EN CAJA NEGRA"):
        if coyuntura:
            fila = df.sample(n=1).iloc[0]
            
            st.markdown(f"""
            <div class="black-box">
            <h2 style='color:#00ff00'> > CAJA NEGRA: RESULTADO </h2>
            <strong>SIGNIFICANTE:</strong> {fila['Significante']}<br>
            <strong>INDICADOR ACADÉMICO:</strong> {fila['Indicador']}<br>
            <strong>SISTEMA OPERATIVO:</strong> {fila['Concepto_Tesis']}<br>
            <hr>
            <strong>TRADUCCIÓN NARRATIVA:</strong><br>
            "Ante la crisis de '{coyuntura}', la Máquina de Alem activa el protocolo de {fila['Significante']}. 
            Como indica el {fila['Discurso_Fuente']}, el radicalismo entra en modo de Reparación Nacional."
            </div>
            """, unsafe_allow_html=True)

            if api_key:
                client = OpenAI(api_key=api_key)
                with st.spinner("Generando meme..."):
                    prompt_dalle = f"A political meme about {fila['Significante']} in Argentina, style: {fila['Meme_Visual']}. High contrast red and white colors."
                    response = client.images.generate(model="dall-e-3", prompt=prompt_dalle, n=1)
                    st.image(response.data[0].url)
            else:
                st.warning(f"Sugerencia visual: {fila['Meme_Visual']}")
        else:
            st.error("Ingresa una coyuntura.")
except Exception as e:
    st.error(f"Error de sistema: {e}")


