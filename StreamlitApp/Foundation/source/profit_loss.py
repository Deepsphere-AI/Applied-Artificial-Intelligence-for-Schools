import streamlit as st
import math
import datetime
from datetime import date
import calendar
from PIL import Image

def profit_or_loss():
    
    w1,col1,col2,w2=st.columns((1,2,2,1))
    us1,bc1,bc2,us2=st.columns((5,2,2,5))
    with col1:
        st.write("##")
        st.subheader("Enter the Cost Price ")
        st.write("###")
        st.subheader("Enter the Sell Price ")
        
    # ------------to create the function to clear the input-----------#
    with bc2:
        st.markdown("")
        st.markdown("")
        def clear_text():
            st.session_state["Clear_Cost"] = 0.00
            st.session_state["Clear_Selling"] = 0.00
        st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=st.number_input("",min_value=+0.00,step=1.0,key="Clear_Cost") 
        vAR_input_num_1=st.number_input("",min_value=+0.00,step=1.0,key="Clear_Selling")  
       
    #----- Average -------#
    with bc1:
        st.markdown("")
        st.markdown("")
        if st.button("Submit"):
            with col2:
                if vAR_input_num and vAR_input_num_1 == int or float:
                    vAR_cost_price=vAR_input_num
                    vAR_selling_price=vAR_input_num_1
                    if (vAR_selling_price > vAR_cost_price):
                            vAR_profit = vAR_selling_price - vAR_cost_price
                            with col1:
                                st.subheader("Profit ")
                            st.success(vAR_profit)
                    elif ( vAR_cost_price > vAR_selling_price):
                            vAR_loss = vAR_cost_price - vAR_selling_price
                            with col1:
                                st.subheader("Loss ")
                            st.warning(vAR_loss)
                    else:
                        st.info("No Profit No Loss")
                else:
                    st.error("Error")
