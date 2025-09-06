import streamlit as st
from agent_utils import get_search_results

st.set_page_config(
    page_title='Search AI Agent',
    page_icon='🔎',
    layout='centered'
)

st.title('🔎 Search AI Agent')
query = st.text_input(label='Ask anything', placeholder='eg. Give top AI news')

if st.button('Search'):
    if query.strip():
        with st.spinner('Searching...'):
            response = get_search_results(query)
        st.success("✅ Here's what I found:")
        st.write(response)
    else:
        st.warning('⚠️ Please enter a query before searching')