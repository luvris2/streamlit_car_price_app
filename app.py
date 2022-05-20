import streamlit as st
import pandas as pd
import seaborn as sb
import app_home
import app_eda
import app_ml

def main() :
    st.title('자동차 가격 예측')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0] :
        app_home.run_home()
    elif choice == menu[1] :
        app_eda.run_eda()  
    elif choice == menu[2] :
        app_ml.run_ml()

    st.sidebar.image('data/pa22.png')
    st.sidebar.balloons()
    st.text('abc')
if __name__ == '__main__' :
    main()