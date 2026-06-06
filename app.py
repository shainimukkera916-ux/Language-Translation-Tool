import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")
st.subheader("Enter text below to translate")

text = st.text_area("Enter Text")

st.write(f"Characters: {len(text)}")

language_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

source = st.selectbox("Source Language", list(language_map.keys()))
target = st.selectbox("Target Language", list(language_map.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text")
    elif source == target:
        st.warning("Source and target cannot be same")
    else:
        translated = GoogleTranslator(
            source=language_map[source],
            target=language_map[target]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated)