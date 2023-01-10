import streamlit as vAR_st
#from streamlit_option_menu import option_menu


def areaq():
    vAR_st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Applied AI for Intermediate level</h1>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>Simple application built on Streamlit</p>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the area of triangle </p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2.5px;background-color:gray>",unsafe_allow_html=True)
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((5,2,2,5))
    with col1:
        vAR_st.write("#")
        vAR_st.subheader("Enter x1 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter y1 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter x2 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter y2 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter x3 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter y3 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter x4 ")
        vAR_st.write("###")
        vAR_st.subheader("Enter y4")
    # ------------to create the function to clear the input-----------#
    with bc2:
        vAR_st.markdown("")
        vAR_st.markdown("")
        def clear_text():
            vAR_st.session_state["Clear_x1"] = 0
            vAR_st.session_state["Clear_y1"] = 0
            vAR_st.session_state["Clear_x2"] = 0
            vAR_st.session_state["Clear_y2"] = 0
            vAR_st.session_state["Clear_x3"] = 0
            vAR_st.session_state["Clear_y3"] = 0
            vAR_st.session_state["Clear_x4"] = 0
            vAR_st.session_state["Clear_y4"] = 0
        vAR_st.button("Clear", on_click=clear_text)   
    with col2:
        vAR_input_x1=vAR_st.number_input("",key="Clear_x1") 
        vAR_input_y1=vAR_st.number_input("",key="Clear_y1")
        vAR_input_x2=vAR_st.number_input("",key="Clear_x2")
        vAR_input_y2=vAR_st.number_input("",key="Clear_y2")
        vAR_input_x3=vAR_st.number_input("",key="Clear_x3")
        vAR_input_y3=vAR_st.number_input("",key="Clear_y3")
        vAR_input_x4=vAR_st.number_input("",key="Clear_x4")
        vAR_input_y4=vAR_st.number_input("",key="Clear_y4")
        
    #--------------------------#
    with bc1:
        vAR_st.markdown("")
        vAR_st.markdown("")
        if vAR_st.button("Submit"):
            with col2:
                    vAR_res=0.5*(((vAR_input_x1*vAR_input_y2)+(vAR_input_x2*vAR_input_y3)+(vAR_input_x3*vAR_input_y4)+(vAR_input_x4*vAR_input_y1))-((vAR_input_x2*vAR_input_y1)+(vAR_input_x3*vAR_input_y2)+(vAR_input_x4*vAR_input_y3)+(vAR_input_x1*vAR_input_y4)))
                    vAR_st.success(vAR_res+" Sq units") 
                    
            
            with col1:
                vAR_st.write("# Result ")

