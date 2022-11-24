import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
image3 = Image.open('image/javadexe.png')
st.set_page_config(page_title='arab irani', page_icon=image3, layout='wide')

def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation = load_animation('https://assets9.lottiefiles.com/packages/lf20_e4uqdbmg.json')
image = Image.open('image/img.jpg')
image2 = Image.open('image/football.jpg')


with st.container():
    left, senter, right= st.columns((1,2,3))
    with right:
        st.image(image3)
    with senter:
        st_lottie(animation, height=300, key='coding')
    with left:
        st.subheader('made by javad!')

with st.container():
    st.write('---')
    st.header('عرب زادایمانی')
    st.write('##')
    img, text = st.columns((1, 1))

    with img:
        st.image(image)
    with text:
        st.subheader('زاد ایمانی معروف به عرب در ایران زندگی میکند')
        st.write("""
    ادرس مدرسه: تبریز - جلالیه - مدرسه امام حسین    
 کلاس: دهم ریاضی                                    
 سن: نمد                                           
 محل زندگی: نمد                                    
 مثل سگ سوال پرسیدن: 100                           
        """)
with st.container():
    st.write('---')
    text, img = st.columns((1, 1))

    with img:
        st.image(image2)
    with text:
        st.subheader('فوتبالیست عرب')
        st.write('لامصب فوتبال بازی کردن هم بلده حیون مثل عرب ها بازی میکنه')