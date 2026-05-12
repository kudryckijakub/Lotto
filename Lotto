import streamlit as st
import random

st.title("🎰 Symulator Lotto")

# Inicjalizacja "pamięci" programu (Session State)
if 'moje_liczby' not in st.session_state:
    st.session_state.moje_liczby = []
if 'wyniki' not in st.session_state:
    st.session_state.wyniki = []
if 'losowanie_odbyte' not in st.session_state:
    st.session_state.losowanie_odbyte = False

# --- SEKCA 1: Wybieranie liczb ---
st.subheader("Wybierz swoje 6 liczb")

# Formularz do wpisywania liczby
with st.form("dodaj_liczbe"):
    x = st.number_input("Podaj liczbę (1-49):", min_value=1, max_value=49, step=1)
    submit = st.form_submit_button("Dodaj liczbę")

    if submit:
        if x not in st.session_state.moje_liczby:
            if len(st.session_state.moje_liczby) < 6:
                st.session_state.moje_liczby.append(x)
            else:
                st.warning("Masz już 6 liczb!")
        else:
            st.error("Ta liczba została już wybrana!")

st.write(f"Twoje liczby: **{st.session_state.moje_liczby}**")

# Przycisk do resetowania
if st.button("Zacznij od nowa"):
    st.session_state.moje_liczby = []
    st.session_state.wyniki = []
    st.session_state.losowanie_odbyte = False
    st.rerun()

# --- SEKCJA 2: Losowanie ---
if len(st.session_state.moje_liczby) == 6:
    st.success("Wybrałeś wszystkie liczby! Możesz losować.")
    
    if st.button("Zwolnij blokadę maszyny losującej!"):
        pula = list(range(1, 50))
        st.session_state.wyniki = random.sample(pula, 6) # Szybszy sposób na 6 liczb
        st.session_state.losowanie_odbyte = True

# --- SEKCJA 3: Wyniki ---
if st.session_state.losowanie_odbyte:
    st.divider()
    st.subheader("Wyniki losowania:")
    st.info(f"Wylosowane liczby to: {st.session_state.wyniki}")
    
    trafione = [l for l in st.session_state.moje_liczby if l in st.session_state.wyniki]
    
    if trafione:
        st.write(f"Trafiłeś **{len(trafione)}** liczb: {trafione}")
    else:
        st.write("Niestety, tym razem nic nie trafiłeś.")

    if len(trafione) == 6:
        st.balloons() # Efekt wizualny przy 6 trafieniach!
