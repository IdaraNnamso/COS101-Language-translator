import streamlit as st
yoruba_dictionary  = { # Akpan Excellence BHU/25/04/13/0014
    "hello": "Ẹ ǹlẹ́",
    "bye" : "Ó dàbọ̀",
    "good morning" : "e kaaro",
    "good evening" : "ka a ale",
    "welcome" : "kaabo",
    "thank you" : "e dupe",
    "food" : "Ounjẹ", 
    "well done" : "daradara ṣe",
    "how are you" : "Bawo ni",
    "come" : "wá",
    "go" : "lọ",
    "father" : "baba",
    "mother" : "iya",
    "boy" : "ọmọkunrin",
    "girl" : "omobirin",
    "money" : "owo",
    "what is your name" : "Kí ni orúkọ rẹ",
    "brother" : "arakunrin",
    "sister" : "arabinrin",
    "school" : "ile-iwe",

}

zulu_dictionary = { #Emmanuel Igoh BHU/25/04/09/0126
    "good morning" : "sawubona",
    "come" : "woza",
    "enter" : "faka",
    "say" : "ukuthi",
    "go" : "hamba",
    "wash" : "ukuhlamba",
    "big" : "inkulu",
    "dog" : "inja",
    "food" : "ukudla",
    "short" : "okufutshane",
    "brother" : "mfowethu",
    "hear" : "zwa",
    "talk" : "inkulumo",
    "sister" : "dadewethu",
    "sing" : "hlabelelani",
    "run" : "gijima",
    "fan" : "umlandeli",
    "car" : "imoto",
    "chair" : "isihlalo",
    "eat" : "yidla",

}
# Akpan Excellence BHU/25/04/13/0014
st.title("Language Translator")
st.markdown("## Welcome to the Language Translator App")

language = st.sidebar.selectbox(
    "Select language you want to translate among:", dictionaries.keys())

if language:
    selected_dictionary = dictionaries[language]
    word_to_translate = st.selectbox(
        f"Select a word to translate to {language.capitalize()}:", 
        options=[""] + list(selected_dictionary.keys()))
if st.button("Translate"):
    if word_to_translate:
        translation = selected_dictionary.get(word_to_translate, "Translation not found.")
        st.divider()
        st.subheader(f"The translation of '{word_to_translate}' in {language.capitalize()} is: {translation}")
        st.success(f"**{translation}**")
        st.balloons()
        st.write ("Thank you for using the Language Translator App!")
        st.feedback()
