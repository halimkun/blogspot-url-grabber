from colorama import init, Fore, Back, Style
import feedparser as feed
from parso import parse
import validators
import streamlit as st

# App Function
def validate_url(p) :
    if not validators.url(p):
        return False
    else :
        return True

def parse_url(u):
    if u.endswith("/"):
        pd = u + "feeds/posts/default"
    else :
        pd = u + "/feeds/posts/default"
    return pd

def generate_post_urls(pu):
    code = ""
    with st.spinner("Wait for it...") :
        fd = feed.parse(pu)
        for entry in fd.entries:
            code += entry.link + "\n"
        st.success("Success")
        st.code(code, language='Plain Text')
        st.write("Total : " + str(len(fd.entries)))
        if len(fd.entries) == 0 :
            st.info("Pastikan anda memasukan url valid sesuai contoh, jika masih tidak mendapatkan hasil, kemungkinan website yang anda masukan **tidak memiliki postingan** atau **bukan berbasis pada blogspot**")

# --------------------------------------------------

st.sidebar.markdown('# Blogger Post Url Grabber')
st.sidebar.info("Tools to retrieve all **blogger** / **blogspot** posts. made with **python**")
st.sidebar.write("**for now** : only work with blog base on blogspot")
st.sidebar.write("\n")
url             = st.sidebar.text_input("Website Url :")
btn_get_urls    = st.sidebar.button("Grab Posts")

if btn_get_urls :
    vd = validate_url(url)
    if vd :
        generate_post_urls(parse_url(url))
    else :
        st.warning("Url yang anda masukan tidak valid !")

for _ in range(3):
    st.write("")

st.code('''
Example URL
✓ https://www.haliminfo.com/
✓ http://haliminfo.com
✘ https://www.haliminfo.com/some/path
✘ haliminfo.com
''', language="Plain Text")