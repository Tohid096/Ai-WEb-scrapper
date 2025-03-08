import streamlit as st
from scrape import (
    scrape_website,
    clean_body_content,
    extract_bodycontent,
    split_dom_content
    )



st.title("AI Scrapper")
url=st.text_input("Enter a Website Url: ")

if st.button("Scrape"):
    st.write("Scraping the website ")
    result = scrape_website(url)
    body_content = extract_bodycontent(result)
    cleaned_content= clean_body_content(body_content)

    st.session_state.dom_content=cleaned_content

    with st.expander("view DOM Content"):
        st.text_area("DOM Content",cleaned_content,height=300)