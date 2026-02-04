import streamlit as st
import pandas as pd
import random
from openai import OpenAI

# --- CONFIGURACIÓN DE LA INTERFAZ ---
st.set_page_config(page_title="La Máquina de Alem", page_icon="🇦🇷", layout="centered")

st.markdown("""
    <style>
    /* Estética General */
    .stApp { background-color: #f4f4f4; border-top: 20px solid #D32F2F; }
    
    /* Tipografía Radical */
    h1, h2, h3 { color: #D32F2F; font-family: 'Courier New', Courier, monospace; font-weight: 900; letter-spacing: -1px; }
    .stButton>button { background-color: #D32F2F; color: white; border: 2px solid #B71C1C; font-family: 'Courier New'; font-weight: bold; width: 100%; transition: all 0.3s; }
    .stButton>button:hover { background-color: white; color: #D32F2F; border-color: #D32F2F; }
    
    /* Cajas de Texto */
    .machine-output { background-color: #1a1a1a; color: #00FF00; padding: 20px; font-family: 'Courier New'; border-left: 10px solid #D32F2F; margin-bottom: 20px; }
    .quote-box { background-color: #ffffff; padding: 20px; border: 1px solid #ddd; font-style: italic; font-family: 'Georgia'; font-size: 1.1em; margin-bottom: 20px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("/// LA MÁQUINA DE ALEM_")
st.markdown("**Sistema de Procesamiento de Identidad Discursiva (V 2.1)**")
st.write("Base de datos: *Archivo Unificado*")

# --- CONEXIÓN IA (DALL-E) ---
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    client = None
    st.sidebar.warning("⚠️ MODO TEXTO: API Key no detectada.")

# --- CARGA DEL CEREBRO (CSV) ---
try:
    # AQUÍ ESTÁ EL CAMBIO CLAVE: sep=';'
    df = pd.read_csv("matriz.csv", sep=';')
    
    # Input del Usuario
    st.write("---")
    coyuntura = st.text_input(">> INGRESAR COYUNTURA / CRISIS:", placeholder="Ej: Corrupción en la obra pública...")

    if st.button("EJECUTAR ANÁLISIS"):
        if coyuntura:
            with st.spinner("Buscando en el Código Fuente (1890-2025)..."):
                
                # Selección aleatoria
                fila = df.sample(n=1).iloc[0]
                
                # --- SALIDA VISUAL ---
                # 1. El Diagnóstico
                st.markdown(f"""
                <div class="machine-output">
                > INPUT DETECTADO: "{coyuntura}"<br>
                > SIGNIFICANTE ACTIVADO: {fila['Significante'].upper()}<br>
                > FRECUENCIA: {fila['Frecuencia_Historica']}<br>
                > ESTADO: LATENCIA ACTIVA -> EJECUTANDO
                </div>
                """, unsafe_allow_html=True)

                # 2. El Discurso Crudo
                st.markdown("### 📜 Archivo Histórico (Fragmento Crudo):")
                st.markdown(f"<div class='quote-box'>«{fila['Fragmento_Crudo']}»</div>", unsafe_allow_html=True)

                # 3. La Lógica de la Tesis
                st.markdown("### 🧠 Lógica del Software:")
                st.info(f"{fila['Logica_Maquina']}")
                
                # 4. Generación de Meme
                st.markdown("### 🎨 Generador de Contenido Visual:")
                if client:
                    prompt_final = f"Political poster art, {fila['Prompt_Visual']}, colors red and white, high quality, propaganda style."
                    try:
                        response = client.images.generate(model="dall-e-3", prompt=prompt_final, n=1)
                        st.image(response.data[0].url, caption=f"Concepto Visual: {fila['Significante']}")
                    except Exception as e:
                        st.error(f"Error generando imagen: {e}")
                else:
                    st.warning(f"**Idea para Diseño Gráfico:** {fila['Prompt_Visual']}")
        else:
            st.error("Error: Input vacío.")

except FileNotFoundError:
    st.error("CRÍTICO: No se encuentra 'matriz.csv'.")
except Exception as e:
    st.error(f"Error del sistema: {e}")

# --- PIE DE PÁGINA ---
st.sidebar.markdown("### Sobre la Máquina")
st.sidebar.info("Operacionalización de la tesis 'El funcionamiento de la máquina de Alem'.")
