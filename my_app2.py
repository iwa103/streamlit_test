import streamlit as st
import requests
import pandas as pd

# 日本気象協会のAPIエンドポイント
URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/110000.json"

# Streamlitアプリのタイトル
st.title('3-Day Rain Probability Forecast for Ehime Prefecture')

# データを取得して表示する関数
def get_rain_forecast():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        # JMA JSONデータの解析
        try:
            # 2番目のtimeSeriesブロックで降水確率情報を取得
            pops_series = data[0]['timeSeries'][1]
            time_defines = pops_series['timeDefines']  # 降水確率対象の時間リスト
            areas_forecast = pops_series['areas']  # 地域ごとの降水確率リスト

            # データフレームの準備
            rain_data = {}
            rain_data['Date and Time'] = time_defines

            for area_forecast in areas_forecast:
                area_name = area_forecast['area']['name']
                rain_data[area_name] = area_forecast['pops']

            # データをデータフレームに変換
            rain_df = pd.DataFrame(rain_data)
            rain_df.set_index('Date and Time', inplace=True)

            # データフレームを表示
            st.subheader('Rain Probability Table')
            st.dataframe(rain_df)

        except Exception as e:
            st.error(f"Could not parse rain forecast data: {str(e)}")
    else:
        st.error(f"Failed to retrieve data. Status code: {response.status_code}")

# ボタンが押されたら降水確率データを取得
if st.button('Get Rain Forecast'):
    get_rain_forecast()
