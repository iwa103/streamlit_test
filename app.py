import streamlit as st
import requests

# 日本気象協会のAPIエンドポイント
URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/380000.json"

# Streamlitアプリのタイトル
st.title('気象データ表示')

# データを取得して表示する関数
def fetch_weather_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"データの取得に失敗しました。ステータスコード: {response.status_code}"

# データ取得
weather_data = fetch_weather_data(URL)

# データ表示
if isinstance(weather_data, str):
    st.error(weather_data)
else:
    st.json(weather_data)

# ボタンを追加して、リロード時にデータを更新
if st.button('データ更新'):
    st.experimental_rerun()
