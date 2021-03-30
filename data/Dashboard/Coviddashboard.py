import streamlit as st
import pandas as pd
import numpy as np 
import seaborn as sns
import plotly_express as px
from PIL import Image
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title('Covid 19 India-Cases')
st.header('This is my dashboard to showcases Covid-19 Stats across all States.')
st.markdown("Dashboard by AdityaIngle")

#Inserting Image for Appeal
Image = Image.open(r"C:\Users\Asus\Desktop\MinProject\data//covid-share.jpg")
st.image(Image)

#Insert Sidebar
st.sidebar.title("Select Following Features")

@st.cache
def load_data():
    df = pd.read_csv(r"C:\Users\Asus\Desktop\MinProject\data/india_covid.csv")

    return df

#to display data
df = load_data()

numeric_columns = df.select_dtypes(['int64']).columns
states_columns = df.select_dtypes(['object']).columns

#checkbox
checkbox = st.sidebar.checkbox("Show Data")
if checkbox:
  df = load_data()  
  st.dataframe(df)

 
#Display Header
st.sidebar.header("Parameters")
selectbox_1 = st.sidebar.selectbox('State', df['State'].unique())
visualization = st.sidebar.selectbox('Select Plot', ('Box ', 'Line' , 'Histogram'))
#select_status = st.sidebar.radio('Select Status', ('Confirmed Cases','Active Cases','Recovered Cases','Death Cases'))
selected_state = df[df['State']==selectbox_1]

def get_total_dataframe(df):
    total_dataframe = pd.DataFrame({
     'Status':['Confirmed','Recovered','Deaths','Active'],
     'Number of cases':(df.iloc[0]['Confirmed Cases'],df.iloc[0]['Active Cases'],
      df.iloc[0]['Recovered Cases'],df.iloc[0]['Death Cases']) 
    }

    )
    return total_dataframe
state_total = get_total_dataframe(selected_state)    

#Visualization
st.sidebar.checkbox("Show Analysis by State", True, key=1) 
select = st.sidebar.selectbox('Select a State',df['State'])
#get the state selected in the selectbox 
state_data = df[df['State'] == select]
select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed', 'Active', 'Recovered',
'Deceased'))

if st.sidebar.checkbox("Show Analysis by State", True, key=2):
 st.markdown("## **State level analysis**")
 st.markdown("### Overall Confirmed, Active, Recovered and" + "Deceased cases in %s yet" % (select)) 
if not st.checkbox('Hide Graph', False, key=1):
 state_total_graph = px.bar( state_total, x='Status', y='Number of cases',
 labels={'Number of cases':'Number of cases in %s' % (select)}, color='Status')
 st.plotly_chart(state_total_graph)
