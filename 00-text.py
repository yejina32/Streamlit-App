import streamlit as st

st.title("이것은 타이틀 입니다.") # h1 사이즈
st.title("이것은 :blue[타이틀] 입니다. _스마일_ :sunglasses:")
st.header("이것은 :red[헤더] 입니다.:sparkles:") # h2 사이즈
st.header("One", divider=True)
st.subheader("이것은 :green[서브헤더] 입니다.") # h3 사이즈즈
st.divider()  # 👈 Draws a horizontal rule
st.caption("이것은 :orange[캡션] 입니다.") # 18 pixel 사이즈
st.text("이것은 텍스트입니다.") # 20 pixel 사이즈
st.divider()  # 👈 Draws a horizontal rule
st.markdown("*이것은* **마크다운** 입니다.") # 20 pixel 사이즈
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)