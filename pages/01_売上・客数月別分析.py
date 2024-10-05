import streamlit as st
from datetime import datetime

# 現在の年と月を取得
current_year = datetime.now().year
current_month = datetime.now().month

# 年を選択するセレクトボックス（範囲を必要に応じて調整）
year = st.selectbox('年を選択してください', list(range(current_year - 1, current_year + 1)))

# 月を選択するセレクトボックス
month = st.selectbox('月を選択してください', list(range(1, 13)))

# 選択された年と月を表示
st.write(f"選択された日付: {year}年 {month}月")