import streamlit as vAR_st
from streamlit_option_menu import option_menu

def square_root():
    vAR_st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Applied AI for Intermediate level</h1>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>Simple application built on Streamlit</p>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Square Root</p>", unsafe_allow_html=True)
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
            vAR_st.session_state["Clear_Square"] = 0
        vAR_st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_num=vAR_st.number_input("",step=1.0,key="Clear_Square")  
    #-----squre-------#
    with bc1:
        vAR_st.markdown("")
        vAR_st.markdown("")
        if vAR_st.button("Submit"):
            with col2:
                if vAR_input_num >0:
                    vAR_square = vAR_input_num ** 0.5
                    #vAR_square=round(vAR_square,2)
                    with col1:
                        vAR_st.markdown("### Result")
                    with col2:
                        vAR_st.success(vAR_square)
                else:
                    vAR_st.error("Enter positive number")
                
