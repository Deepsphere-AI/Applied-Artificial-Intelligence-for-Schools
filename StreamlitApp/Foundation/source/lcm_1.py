import streamlit as vAR_st
from PIL import Image


def clear_input():
    vAR_st.session_state["clear"]= 0
    vAR_st.session_state["clear2"]= 0

def lcm():
    
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
    with col1:
        vAR_st.markdown("##")
        vAR_st.subheader("Enter number 1")
        #vAR_st.write("")
        vAR_st.markdown("###")
        vAR_st.subheader("Enter number 2")
    with col2:
        num1 = vAR_st.number_input("",key="clear")
        num2 = vAR_st.number_input("",key="clear2")
    with bc1:
        if vAR_st.button("LCM"):
            if num2!=0 and num1!=0:
                def getHCF(num1, num2):
                    while num1!=num2:
                        if num1>num2:
                            num1=num1-num2
                        else:
                            num2=num2-num1
                    return num1
                hcf = getHCF(num1,num2)
                lcm = (num1*num2)//hcf
                with col1:
                    
                    vAR_st.subheader('LCM is')
                with col2:
                    vAR_st.success(lcm)
            else:
                with col2:
                    vAR_st.info("Please enter the value")
        
        with bc2:
            vAR_st.button("clear",on_click=clear_input)



