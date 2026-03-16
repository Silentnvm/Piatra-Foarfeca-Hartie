import streamlit as st
import random

st.markdown("<h1 style='text-align: center;'>Piatra foarfeca hartie!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Alege una dintre optiuni</p>", unsafe_allow_html=True)

optiuni = ["Piatra", "Foarfeca", "Hartie"]

alegere_jucator = None

if "scor_player" not in st.session_state:
    st.session_state.scor_player = 0

if "scor_pc" not in st.session_state:
    st.session_state.scor_pc = 0

alegere_pc = random.choice(optiuni)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Piatra"):
        alegere_jucator = "Piatra"

with col2:
    if st.button("Foarfeca"):
        alegere_jucator = "Foarfeca"
        
with col3:
    if st.button("Hartie"):
        alegere_jucator = "Hartie"
        
if alegere_jucator == None:
    st.warning("Alege una dintre optiuni")
else:
    if alegere_jucator == alegere_pc:
        st.info("Egalitate")
    elif (alegere_jucator == "Piatra" and alegere_pc == "Hartie") or (alegere_jucator == "Hartie" and alegere_pc == "Foarfeca") or (alegere_jucator == "Foarfeca" and alegere_pc == "Piatra"):
        st.warning("Pc-ul a castigat")
        st.session_state.scor_pc += 1
    else:
        st.success("Felicitari, ai castigat!")
        st.session_state.scor_player += 1
    st.info(f"(Player) {st.session_state.scor_player} - {st.session_state.scor_pc} (PC)")