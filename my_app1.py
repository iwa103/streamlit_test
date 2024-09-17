import streamlit as st
import pandas as pd
import numpy as np

# データフレームを作成
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

st.write("こちらはランダムなデータのデータフレームです：")
st.dataframe(data)  # データフレームの表示

# 折れ線グラフの表示
st.line_chart(data)
