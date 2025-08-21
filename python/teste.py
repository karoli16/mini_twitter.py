import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# ----------------------------
# Conectar ao Firebase
# ----------------------------
# Nome do projeto Firebase: minitwtr
cred = credentials.Certificate("firebase_key.json")  # coloque o JSON do seu projeto aqui

# Inicializa apenas se ainda não houver app
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ----------------------------
# Título do app
# ----------------------------
st.title("🐦 Mini Twitter na Nuvem (minitwtr)")

# Campo para digitar tweet
novo_tweet = st.text_area("O que você está pensando?", max_chars=280)

# Botão para postar
if st.button("Postar"):
    if novo_tweet.strip() != "":
        # Adiciona o tweet na coleção 'tweets' do Firestore
        db.collection("tweets").add({"conteudo": novo_tweet})
        st.success("Tweet publicado!")
    else:
        st.error("Escreva algo antes de postar!")

# ----------------------------
# Exibe tweets
# ----------------------------
st.subheader("Tweets")
# Busca tweets em ordem de inserção mais recente (DESC)
tweets_ref = db.collection("tweets").order_by("conteudo", direction=firestore.Query.DESCENDING)

for tweet in tweets_ref.stream():
    st.write(f"🗨️ {tweet.to_dict()['conteudo']}")
    st.markdown("---")
