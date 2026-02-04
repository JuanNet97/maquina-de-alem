import streamlit as st
import pandas as pd
import random
from openai import OpenAI

# 1. ESTÉTICA RADICAL (Rojo y Blanco)
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
st.subheader("la app para radicalizarlo todo")

# 2. CONFIGURACIÓN DE IA (DALL-E)
with st.sidebar:
    st.header("⚙️ Configuración")
    api_key = st.text_input("Introduce tu OpenAI API Key:", type="password")
    st.info("Esta clave permite que la máquina 'dibuje' los memes usando DALL-E.")

# 3. LÓGICA DE LA CAJA NEGRA
df = pd.read_csv("matriz.csv")

coyuntura = st.text_area("💬 Ingresa la crisis o coyuntura actual:", placeholder="Ej: Crisis de confianza en las instituciones...")

if st.button("PROCESAR DISCURSO Y GENERAR MEME"):
    if coyuntura:
        # Selección aleatoria basada en la matriz de la tesis
        fila = df.sample(n=1).iloc[0]
        
        st.markdown("### 📤 Resultado de la Caja Negra")
        st.markdown(f"""
        <div class="black-box">
        <strong>SIGNIFICANTE:</strong> {fila['Significante']}<br>
        <strong>INDICADOR:</strong> {fila['Indicador']} ({fila['Atributo']})<br><br>
        <strong>NARRATIVA DE REPARACIÓN:</strong><br>
        "Ante {coyuntura}, el radicalismo activa su software de {fila['Concepto_Tesis']}. 
        La tradición no es repetición, es resiliencia."
        </div>
        """, unsafe_allow_html=True)

        # 4. GENERACIÓN DE IMAGEN CON DALLE
        if api_key:
            client = OpenAI(api_key=api_key)
            with st.spinner("La Máquina de Alem está dibujando el meme..."):
                try:
                    # Construimos el prompt usando los datos de la tesis
                    prompt_dalle = f"A political meme about {fila['Significante']} in Argentina, style: {fila['Meme_Base']}. High contrast red and white colors. Professional graphic design."
                    
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt_dalle,
                        size="1024x1024",
                        quality="standard",
                        n=1,
                    )
                    image_url = response.data[0].url
                    st.image(image_url, caption=f"Meme generado: {fila['Significante']}")
                    st.success("Meme generado exitosamente.")
                except Exception as e:
                    st.error(f"Error con DALL-E: {e}")
        else:
            st.warning("⚠️ Sin API Key no puedo generar la imagen, pero aquí está la idea: " + fila['Meme_Base'])
    else:

        st.error("Debes ingresar una coyuntura para que la máquina pueda narrar.")

