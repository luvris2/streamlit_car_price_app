from ast import Num
from unicodedata import numeric
import streamlit as st
import pandas as pd
import joblib

def run_ml() :
    st.subheader('자동차 구매 가격 예측')

    # 예측하기 위해서 필요한 파일 불러오기
    # 인공지능 파일, 스케일러 X/y 파일

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    
    # 성별, 나이, 연봉, 카드빛, 자산 입력 받기

    gender = st.radio('성별', ['남자','여자'])
    if gender == '여자' :
        gender = 0
    else :
        gender = 1

    st.number_input('나이', 1, 150, 30)
    st.text_input('연봉')
    st.text_input('카드빛')
    st.text_input('자산')
    