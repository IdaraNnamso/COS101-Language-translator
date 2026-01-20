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

 hausa_dictionary = { #Emmanuel Igoh BHU/25/04/09/0126
   "hello": "Sannu",
    "bye": "Sai anjima",
    "good morning": "Ina kwana",
    "good evening": "Barka da yamma",
    "welcome": "Maraba",
    "thank you": "Nagode",
    "food": "Abinci",
    "how are you": "Yaya kake?",
    "come": "Zo",
    "go": "Tafi",
    "father": "Uba",
    "mother": "Uwa",
    "boy": "Yaro",
    "girl": "Yarinya",
    "money": "Kudi",
    "what is your name": "Menene sunanka?",
    "brother": "Dan'uwa",
    "sister": "Yar'uwa",
    "school": "Makaranta",
}

igbo_dictionary = { #ADELEKE OLUWATOBILOBA SAMUEL BHU/25/04/05/0042
    "hello": "kedu",  
    "Thank you": "Imena",
    "sorry": "Ndo",
    "water": "Mniri",
    "Goodbye": "Ka omesia",
    "food": "Nri",
    "House": "Ulo",
    "Please": "Biko",
    "Family": "Ezinuio",
    "Mother": "Nne",
    "Father": "Nna",
    "Child": "Nwa",
    "Friend": "Enyi",
    "Day": "Ubochi",
    "Night": "Abali",
    "One": "Otu",
    "Two": "Abuo",
    "Good": "Oma",
    "Yes": "Ee",
    "Love": "Ihunaya"
   
}

zulu_dictionary = { #Adeleke Oluwatobiloba BHU/25/04/09/0075
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
