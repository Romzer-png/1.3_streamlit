import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

csv = pd.read_csv('Dictionnaire.csv', sep = ";")
df = pd.DataFrame(csv)
dict_user = df.to_dict('records')

# 1. Construction du dict usernames
usernames = {}

for user in dict_user:
    usernames[user["name"]] = user

# 2. Création du dictionnaire final
final_dict = {
    "usernames": usernames
}

authenticator = Authenticate(

    final_dict,  # Les données des comptes

    "cookie name",         # Le nom du cookie, un str quelconque

    "cookie key",          # La clé du cookie, un str quelconque

    30,                    # Le nombre de jours avant que le cookie expire

)
authenticator.login()



if st.session_state["authentication_status"]:

    # ----- MENU -----
    with st.sidebar:
        st.write(f'Bienvenue {st.session_state["name"]}')
        selection = option_menu(
        menu_title=None,
        options=["😍​ Accueil", "😺​ Les photos de mon chat"])
            # Bouton de déconnexion
        authenticator.logout("Déconnexion")

    # ----- ROUTING -----
    if selection == "😍​ Accueil":
            st.title("Bienvenue sur ma page !")
            st.image("https://www.shutterstock.com/image-photo/applause-support-success-business-team-600nw-2312975429.jpg")

    elif selection == "😺​ Les photos de mon chat":
        st.audio(r"C:\Users\mosca\Desktop\Wild Code School\Streamlit_quêtes\cute-cat-meow-song-429568.mp3")
        st.write("Bienvenue sur mon album photo !")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Mon chat en mode felin")
            st.image("https://static.streamlit.io/examples/cat.jpg")
# Contenu de la deuxième colonne :
        with col2:
            st.header("Mon chat le plus heureux ")
            st.image("https://t4.ftcdn.net/jpg/00/68/33/03/360_F_68330331_dKqChy33w0TcNHJEkqT5iw97QOX8la7F.jpg")
# Contenu de la troisième colonne : 

        with col3:
            st.header("Mon chat en mode regarde vers l'horizon")
            st.image("https://www.shutterstock.com/image-photo/tabby-lying-on-bed-felis-260nw-2676474089.jpg")

# ----------------------------------------------------

elif st.session_state["authentication_status"] is False:
    st.error("Le username ou le password est/sont incorrect(s)")

elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
