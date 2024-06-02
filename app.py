import streamlit as st
import pandas as pd

# 페이지 제목 설정
st.set_page_config(page_title="Data Viewer", page_icon=":bar_chart:", layout="wide")

# CSV 파일에서 데이터 로드
@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# 제목과 설명 추가
st.title("Data Viewer")
st.markdown("### Browse and filter the dataset below:")

# 데이터 프레임 표시
st.dataframe(data)

# 사이드바에 필터 옵션 추가
st.sidebar.header("Filter Options")

# 나이 필터
age_filter = st.sidebar.slider("Select Age Range", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))
filtered_data = data[(data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1])]

# 도시 필터
cities = st.sidebar.multiselect("Select Cities", options=data['City'].unique(), default=data['City'].unique())
filtered_data = filtered_data[filtered_data['City'].isin(cities)]

# 필터링된 데이터 프레임 표시
st.write("### Filtered Data")
st.dataframe(filtered_data)

# 플롯팅 예제
st.write("### Data Visualization")
st.bar_chart(filtered_data['Age'].value_counts())

