import streamlit as st
import pandas as pd
#import plotly.figuare_factory as ff
import plotly.express as px

st.set_page_config(layout='wide', page_title='My_app')

html ='''
<html>
    <head>
        <title>This HTML App</title>
    </head>
    <body>
        <h1>This Long Text!!!</h1>
        <br>
        <hr>
        <h3>This Small Text!!!</h3>
    </body>
</html>
'''

with open('./com_html.html', 'r', encoding='utf-8') as f:
    filehtml =f.read()
    f.close()

# import matplotlib.pyplot as plt
# global variable
url = "https://www.youtube.com/watch?v=XyEOEBsa8I4"


# data app
df = pd.read_csv('./data/data.csv')
st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('content1...'):
        st.subheader('content1...')
        st.video(url)
    with st.expander('content2...'):
        st.subheader('content2...')
        st.table(df)
    #   dff = df.groupby(by='name').sum()
        dff = df.groupby(by='name')[['kor', 'math', 'eng', 'info']].sum()

        st.table(dff)
    #   st.plotly_chart(df)
        melted = df.melt(id_vars='name', value_vars=['kor', 'math', 'eng', 'info'],
                         var_name='subject', value_name='score')
        fig = px.bar(melted, x='name', y='score', color='subject', barmode='group',
                     title="학생별 과목 점수")
        st.plotly_chart(fig)
    with st.expander('content3_images'):
         st.subheader('content3_images')
         st.image('./images/catdog.jpg')
         st.write('<h1>This is new title</h1>', unsafe_allow_html=True)
         st.markdown(html,unsafe_allow_html=True)
    with st.expander('content3_htmlContent..'):
         st.subheader('content3_htmlContent..')
         import streamlit.components.v1 as htmlviewer
         htmlviewer.html(filehtml,height=800)
with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')