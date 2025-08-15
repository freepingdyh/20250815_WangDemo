import numpy as np
import pandas as pd
import streamlit as st

st.title("DEMO PAGE")
st.write("This is a demo page for the Streamlit application.")
st.write("## You can use this page to test various features of Streamlit.")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
st.write("### Here are two NumPy arrays:")
st.write("Array 1:", arr1)
st.write("Array 2:", arr2)

df1= pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
st.write(df1)
st.write("### And here is a Pandas DataFrame:")
st.dataframe(df1)
st.write("### And here is a Streamlit table:")
st.table(df1)

st.write("## 核取方塊")
r1 = st.checkbox("外帶")
if r1:
    st.info("外帶選項已選擇")
else:
    st.warning("內用選項已選擇")

checks = st.columns(2)
txt=""
with checks[0]:
    st.write("### 單選按鈕")
    r2 = st.radio("請選擇一個選項", ["排骨飯", "豬肉飯", "牛肉飯"])
    txt+= f"您選擇了: {r2}\n"
    st.info(txt)

txt1 = ""
with checks[1]:
    st.write("### 多按鍵選單")
    r3 = st.multiselect("請選擇以下選項", ["陽春麵", "麻醬麵", "豬肉麵", "牛肉麵"])
    txt1+= f"您選擇了: {r3}\n"
    st.info(txt1)

check1 = st.columns(2)
with check1[0]:
    st.write("### 單選按鈕")
    r4 = st.radio("請選擇一種飲料", ["紅茶", "清茶", "冬瓜茶", "檸檬茶"])
    st.info(f"您選擇的飲料是: {r4}")

with check1[1]:         
    st.write("### 選項按鈕")
    r5 = st.radio("請選擇一種甜點", ["提拉米蘇", "巧克力慕斯", "布丁", "冰淇淋"],key="r5")
    st.info(f"您選擇的甜點是: {r5}")

check2 = st.columns(3)
with check2[0]:
    st.write("### 滑桿")
    r6 = st.slider("請選擇數量", 0.0, 10.0, 5.0, 0.5)
    st.info(f"您選擇的數量是: {r6}")

with check2[1]:
    st.write("### 數字輸入框")
    r7 = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50)
    st.info(f"您輸入的數字是: {r7}")

with check2[2]:
    st.write("### 下拉式選單")
    r8 = st.selectbox("請選擇一個水果", ["蘋果", "香蕉", "橘子", "葡萄"])
    st.info(f"您選擇的水果是: {r8}")

st.write("## 文字輸入框")
r9 = st.text_input("請輸入您的名字", "John Doe")
st.info(f"您輸入的名字是: {r9}")
st.write("## 多行文字輸入框")
r10 = st.text_area("請輸入您的評論", "這是一個很棒的應用程式！")
st.info(f"您輸入的評論是: {r10}")

check3 = st.columns(2)
with check3[0]:
    st.write("## 日期選擇器")
    r11 = st.date_input("請選擇一個日期", pd.to_datetime("2023-10-01"))
    st.info(f"您選擇的日期是: {r11}")
with check3[1]:
    st.write("## 時間選擇器")
    r12 = st.time_input("請選擇一個時間", pd.to_datetime("12:00").time())
    st.info(f"您選擇的時間是: {r12}")   
st.write("## 文件上傳")
uploaded_file = st.file_uploader("請上傳一個文件", type=["txt", "csv", "xlsx"])
if uploaded_file is not None:
    st.success("文件上傳成功！")
    st.write("文件名稱：", uploaded_file.name)
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text_area("文件內容", content, height=300) 
    elif uploaded_file.type == "text/csv":
        df_uploaded = pd.read_csv(uploaded_file)
        st.dataframe(df_uploaded)   
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df_uploaded = pd.read_excel(uploaded_file)
        st.dataframe(df_uploaded)   
else:
    st.warning("請上傳一個文件！")

st.write("## 按鈕") 
if st.button("點擊我"):
    st.success("按鈕被點擊了！")

st.write("## 進度條")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

st.write("## 動畫")
st.balloons()

st.write("## 地圖")
map_data = pd.DataFrame({
    'lat': [22.9843],
    'lon': [120.2078]
})
st.map(map_data)



