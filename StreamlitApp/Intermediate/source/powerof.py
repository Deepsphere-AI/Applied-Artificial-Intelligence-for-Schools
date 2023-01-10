import streamlit as vAR_st
from streamlit_option_menu import option_menu

from datetime import date

def power_value():
    vAR_st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Applied AI for Intermediate level</h1>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>Simple application built on Streamlit</p>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Power Value </p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,3,3,6))
    with col1:
        vAR_st.markdown("")
        vAR_st.write("# Enter the Number ")
    # ------------to create the function to clear the input-----------#
    with bc2:
        vAR_st.markdown("")
        vAR_st.markdown("")
        def clear_text():
            vAR_st.session_state["Clear_Value"] = ""
        vAR_st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=vAR_st.text_input("",placeholder="Eg: 2^2",key="Clear_Value")  
    #-----squreroot-------#
    with bc1:
        vAR_st.markdown("")
        vAR_st.markdown("")
        if vAR_st.button("Submit"):
            with col2:
                try:
                    if vAR_input_num !='':
                        vAR_split=vAR_input_num.split('^')
                        vAR_num=float(vAR_split[0])
                        vAR_power=float(vAR_split[1])
                        vAR_ans=pow(vAR_num, vAR_power)
                        vAR_st.markdown("")
                        vAR_st.markdown("")
                        with col1:
                            vAR_st.write("")
                            vAR_st.write("")
                            vAR_st.markdown("")
                            vAR_st.markdown("### Result")
                        with col2:
                            vAR_st.success(vAR_ans)
                
                    else:
                        vAR_st.markdown("")
                        vAR_st.error("Enter the input")
                    
                except BaseException as error:
                    vAR_st.error("Follw this pattern 2^2")
