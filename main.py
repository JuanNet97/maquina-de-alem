import streamlit as st
import pandas as pd
import random
from openai import OpenAI

# --- CONFIGURACIÓN DE LA INTERFAZ ---
st.set_page_config(page_title="La Máquina de Alem", page_icon="🇦🇷", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f4f4f4; border-top: 20px solid #D32F2F; }
    h1, h2, h3 { color: #D32F2F; font-family: 'Courier New', Courier, monospace; font-weight: 900; letter-spacing: -1px; }
    .stButton>button { background-color: #D32F2F; color: white; border: 2px solid #B71C1C; font-family: 'Courier New'; font-weight: bold; width: 100%; transition: all 0.3s; }
    .stButton>button:hover { background-color: white; color: #D32F2F; border-color: #D32F2F; }
    
    /* Cajas de Texto */
    .machine-output { background-color: #1a1a1a; color: #00FF00; padding: 20px; font-family: 'Courier New'; border-left: 10px solid #D32F2F; margin-bottom: 20px; }
    .logic-box { background-color: #e3f2fd; border-left: 5px solid #2196f3; padding: 15px; margin-bottom: 20px; color: #0d47a1; }
    .quote-box { background-color: #ffffff; padding: 20px; border: 1px solid #ddd; font-style: italic; font-family: 'Georgia'; font-size: 1.1em; margin-bottom: 20px; border-right: 5px solid #D32F2F; }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("/// LA MÁQUINA DE ALEM_")
st.markdown("**Sistema de Procesamiento de Identidad Discursiva (V 3.1)**")
st.write("Base de datos: *Archivo Unificado*")

# --- CONEXIÓN IA ---
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    client = None

# --- CARGA DEL CEREBRO ---
try:
    df = pd.read_csv("matriz.csv", sep=';')
    
    st.write("---")
    coyuntura = st.text_input(">> INGRESAR COYUNTURA / CRISIS:", placeholder="Ej: Avance contra la justicia...")

    if st.button("EJECUTAR ANÁLISIS"):
        if coyuntura:
            with st.spinner("Consultando Archivo Unificado (1890-2025)..."):
                fila = df.sample(n=1).iloc[0]
                
                # 1. EL DIAGNÓSTICO (Output de Terminal)
                st.markdown(f"""
                <div class="machine-output">
                > INPUT: "{coyuntura}"<br>
                > PROTOCOLO ACTIVADO: {fila['Significante'].upper()}<br>
                > ESTADO: PROCESANDO LÓGICA DE SELECCIÓN...
                </div>
                """, unsafe_allow_html=True)

                # 2. LA EXPLICACIÓN (El Por qué)
                st.markdown("### ⚙️ Lógica de Selección:")
                st.markdown(f"""
                <div class="logic-box">
                <b>¿Por qué eligió la máquina este significante?</b><br>
                {fila['Logica_Maquina']}
                </div>
                """, unsafe_allow_html=True)

                # 3. LA EVIDENCIA (La Cita)
                st.markdown("### 📜 Evidencia del Archivo:")
                st.write(f"El sistema basa esta decisión en el precedente sentado por **{fila['Frecuencia_Historica']}**, quien estableció:")
                st.markdown(f"<div class='quote-box'>«{fila['Fragmento_Crudo']}»</div>", unsafe_allow_html=True)
                
                # 4. PROYECCIÓN VISUAL (Meme + Fallback)
                st.markdown("### 👁️ Proyección Visual (Meme):")
                
                imagen_generada = False
                if client:
                    try:
                        prompt_final = f"Political poster art, {fila['Prompt_Visual']}, colors red and white, high quality."
                        response = client.images.generate(model="dall-e-3", prompt=prompt_final, n=1)
                        st.image(response.data[0].url, caption=f"Generación IA: {fila['Significante']}")
                        imagen_generada = True
                    except Exception:
                        pass 

                if not imagen_generada:
                    st.image(fila['Imagen_Backup'], caption=f"Archivo Histórico: {fila['Frecuencia_Historica']}")
                    st.caption("⚠️ Visualizando archivo histórico (Modo Fallback).")

        else:
            st.error("Error: Input vacío.")

except Exception as e:
    st.error(f"Error del sistema: {e}")
