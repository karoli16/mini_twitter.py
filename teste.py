import streamlit as st

# Título do site
st.title("🐦 Mini Twitter")

# Lista para armazenar os tweets (funciona enquanto a sessão está aberta)
if 'tweets' not in st.session_state:
    st.session_state.tweets = []

# Campo para digitar tweet
novo_tweet = st.text_area("O que você está pensando?", max_chars=280)

# Botão para postar
if st.button("Postar"):
    if novo_tweet.strip() != "":
        st.session_state.tweets.insert(0, novo_tweet)  # adiciona no início
        st.success("Tweet publicado!")
    else:
        st.error("Escreva algo antes de postar!")

# Exibe os tweets
st.subheader("Tweets")
for tweet in st.session_state.tweets:
    st.write(f"🗨️ {tweet}")
    st.markdown("---")
