# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import numpy as np
import joblib

def Predict(b):
   print(b)
   


def run():
  st.write("IPL Power Play Score Prediction")
  with st.form("my_form"):
    bat_team = st.selectbox('Pick a Batting Team', ['Select Batting Team','Mumbai Indian','Gujarat Titans','Rajasthan Royals','Royal Challengers Bangalore','Delhi Capitals','Chennai Super Kings','Punjab Kings','Sunrisers Hyderabad'])
    bowl_team=st.selectbox('Pick a Bowling Team', ['Select Bowling Team','Mumbai Indian','Gujarat Titans','Rajasthan Royals','Royal Challengers Bangalore','Delhi Capitals','Chennai Super Kings','Punjab Kings','Sunrisers Hyderabad'])
    stadium=st.selectbox('Pick a Stadium', ['Select Stadium','MA Chidambaram Stadium, Chepauk, Chennai','Arun Jaitley Stadium, Delhi','M Chinnaswamy Stadium','Narendra Modi Stadium, Ahmedabad','Wankhede Stadium, Mumbai','Dr DY Patil Sports Academy, Mumbai','Punjab Cricket Association IS Bindra Stadium','Sawai Mansingh Stadium','Rajiv Gandhi International Stadium, Uppal'])
    Bowl_num = int(st.number_input('Enter no. of Bowler'))
    Bat_num = int(st.number_input('Enter no. of Batter'))
    inning=st.selectbox('Select Innings',['Select Innings',1,2])
    arr=[stadium,inning,bat_team,bowl_team,Bat_num,Bowl_num]
    st.form_submit_button('Predict',on_click=Predict(arr))



if __name__ == "__main__":
    run()
