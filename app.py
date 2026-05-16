import streamlit as st
import random

st.set_page_config(layout="wide")
st.header("🎰 APLIKACJA LOTTO DUŻY LOTEK")
st.subheader("🎯 Wpisz swoje 6 liczb:")
liczby = list(range(1, 50))

# Górne kolumny na wpisywanie liczb
kol1, kol2, kol3, kol4, kol5, kol6 = st.columns(6)
with kol1:
    liczba1 = st.number_input("Liczba 1:", label_visibility="collapsed", min_value=1, max_value=49, value=None, placeholder="1-49", key="n1")
with kol2:
    liczba2 = st.number_input("Liczba 2:", label_visibility="collapsed", min_value=1, max_value=49, value=None, placeholder="1-49", key="n2")
with kol3: 
    liczba3 = st.number_input("Liczba 3:", label_visibility="collapsed", min_value=1, max_value=49, value=None, placeholder="1-49", key="n3")
with kol4:
    liczba4 = st.number_input("Liczba 4:", label_visibility="collapsed", min_value=1, max_value=49, value=None, placeholder="1-49", key="n4")
with kol5:
    liczba5 = st.number_input("Liczba 5:", label_visibility="collapsed", min_value=1, max_value=49, value=None, placeholder="1-49", key="n5")
with kol6:
    liczba6 = st.number_input("Liczba 6:", label_visibility="collapsed", min_value=1, max_value=49, value=None, placeholder="1-49", key="n6")

liczby_wybrane = [liczba1, liczba2, liczba3, liczba4, liczba5, liczba6]
losuj = st.button("Losuj", use_container_width=True)

if losuj:
    if None in liczby_wybrane:
        st.warning("Proszę wybrać wszystkie 6 liczb.")
    elif len(set(liczby_wybrane)) != 6:
        st.warning("Proszę wybrać 6 różnych liczb.")
    else:
        wylosowane_liczby = random.sample(liczby, 6)
        trafione_liczby = set(liczby_wybrane) & set(wylosowane_liczby)
        
        st.divider()
        
        # GŁÓWNA SEKCJA WYNIKÓW (Zamykamy wszystko w dedykowany kontener)
        with st.container(border=True):
            st.markdown("### 📊 PODSUMOWANIE LOSOWANIA")
            
            # Dzielimy dół na 3 równe kolumny zamiast rozrzucać tekst po ekranie
            wynik_kol1, wynik_kol2, wynik_kol3 = st.columns(3)
            
            with wynik_kol1:
                st.info(f"📋 **Twój kupon:**\n\n`{liczby_wybrane}`")
                
            with wynik_kol2:
                st.success(f"🎰 **Wylosowane liczby:**\n\n`{wylosowane_liczby}`")
                
            with wynik_kol3:
                # Metric i trafione liczby lądują obok kuponów, eliminując gigantyczny margines
                st.metric(label="🎯 Trafione liczby:", value=f"{len(trafione_liczby)} / 6")
                
                if trafione_liczby:
                    tekst_trafień = " ".join([f"🟢 **{liczba}**" for liczba in sorted(trafione_liczby)])
                    st.markdown(f"**Trafiłeś:** {tekst_trafień}")
                else:
                    st.markdown("❌ *Brak trafień tym razem.*")