import os
import dotenv
import streamlit as st

# Streamlit app
st.subheader('Settings')

# Get API keys from local .env file
dotenv.load_dotenv(".env")
openai_api_key = os.getenv('OPENAI_API_KEY')
serper_api_key = os.getenv('SERPER_API_KEY')

st.session_state.openai_api_key = openai_api_key
st.session_state.serper_api_key = serper_api_key
print(f"st.session_state.openai_api_key:{st.session_state.openai_api_key}")
print(f"st.session_state.serper_api_key:{st.session_state.serper_api_key}")


# openai_api_key = st.text_input("OpenAI API Key", value=st.session_state.openai_api_key, type="password")
# st.caption("*Required for all apps; get it [here](https://platform.openai.com/account/api-keys).*")

# serper_api_key = st.text_input("Serper API Key", value=st.session_state.serper_api_key, type="password")
# st.caption("*Required for news and search; get it [here](https://serper.dev/api-key).*")

# If the 'Save' button is clicked
if st.button("Save"):
    if not openai_api_key.strip() or not serper_api_key.strip():
        st.error("Please provide the missing API keys.")
    else:
        print(f"st.session_state.openai_api_key:{st.session_state.openai_api_key}")
        print(f"st.session_state.serper_api_key:{st.session_state.serper_api_key}")
