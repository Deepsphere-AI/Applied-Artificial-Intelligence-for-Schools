import streamlit as vAR_st
import math
#import source.head as head

def button_rad():
    vAR_st.session_state["rad"]= 0
    vAR_st.session_state["rad2"]= 0
def button_sq():
    vAR_st.session_state["sq"]= 0
    vAR_st.session_state["sq2"]= 0
    vAR_st.session_state["rth_in"]=0
    vAR_st.session_state["rtb_in"]=0
    vAR_st.session_state["rth_inp"]=0
    vAR_st.session_state["rtb_inp"]=0
    vAR_st.session_state["rhm_in1"]=0
    vAR_st.session_state["rhm_in2"]=0
    vAR_st.session_state["rhm_p"]=0
    vAR_st.session_state["tb1"]=0
    vAR_st.session_state["tb2"]=0
    vAR_st.session_state["th"]=0
    vAR_st.session_state["tb1_p"]=0
    vAR_st.session_state["tb1_p"]=0
    vAR_st.session_state["ts1"]=0
    vAR_st.session_state["ts1"]=0
    vAR_st.session_state["ts2"]=0
def button_rect():
    vAR_st.session_state["leng"]= 0
    vAR_st.session_state["brth"]= 0
    vAR_st.session_state["leng2"]= 0
    vAR_st.session_state["brth2"]= 0

def areaperimeter():
    vAR_st.markdown(" <h1 style='text-align: center; color: Black;font-size: 25px;'>Applied AI for Intermediate level</h1>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: blue; font-size:29px;'>Simple application built on Streamlit</p>", unsafe_allow_html=True)
    vAR_st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Area and Perimeter for circle, rectangle, square, right angle triange, rhombus and trapezium</p>", unsafe_allow_html=True)
    vAR_st.markdown("<hr style=height:2px;background-color:gray>",unsafe_allow_html=True)
    w1,c1,c2,w2=vAR_st.columns((1,2,2,1))
    with c1:
        vAR_st.markdown("## ")
        vAR_st.markdown("### Select the shape")
    with c2:
        vAR_shapes=vAR_st.selectbox('',['select','Circle','Rectangle','Square','Right angled Triangle','Rhombus','Trapezium'],key='placeholder')
    if vAR_shapes=="Circle":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("## ")
            vAR_st.markdown("### Select")
        with col2:
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Radius of Circle")
            with col2:
                vAR_a=vAR_st.number_input("",key='rad',min_value=0.00)
            vAR_ar=3.14*vAR_a**2
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Area is")
                    with col2:
                        vAR_st.markdown("### ")
                        vAR_st.success(vAR_ar)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_rad)
                    
        
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Radius of Circle")
            with col2:
                vAR_b=vAR_st.number_input("",key='rad2',min_value=0.00)
            vAR_rp=2*3.14*vAR_b
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Perimeter is")
                    with col2:
                        vAR_st.markdown("### ")
                        vAR_st.success(vAR_rp)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_rad)
                    
        else:
            pass
    elif vAR_shapes=="Rectangle":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            
            vAR_st.markdown("## ")
            vAR_st.markdown("### Select")
        with col2:
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Lenght of rectangle")
                vAR_st.markdown("## ")
                vAR_st.markdown("### Breadth of rectangle")
            with col2:
                vAR_l=vAR_st.number_input("",key="leng",min_value=0.00)
                vAR_b=vAR_st.number_input("",key="brth",min_value=0.00)
            vAR_arect=vAR_l*vAR_b
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Area is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_arect)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_rect)
                    
            
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Lenght of rectangle")
                vAR_st.markdown("## ")
                vAR_st.markdown("### Breadth of rectangle")
            with col2:
                vAR_l=vAR_st.number_input("",key="leng2",min_value=0.00)
                vAR_b=vAR_st.number_input("",key="brth2",min_value=0.00)
            vAR_prect=2*(vAR_l+vAR_b)
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.write("")
                        vAR_st.markdown("### ")
                        vAR_st.markdown("### Perimeter is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_prect)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_rect)
                    
        else:
            pass
    elif vAR_shapes=="Square":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("## ")
            vAR_st.markdown("### Select")
        with col2: 
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Value of side")
            with col2:
                vAR_s=vAR_st.number_input("",key='sq',min_value=0.00)
            vAR_arect=vAR_s**2
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Area is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_arect)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    
                
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Value of side")
            with col2:
                vAR_s=vAR_st.number_input("",key='sq2',min_value=0.00)
            vAR_prect=4*vAR_s
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Perimeter is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_prect)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    
            
        else:
            pass
    elif vAR_shapes=="Right angled Triangle":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("##")
            vAR_st.markdown("### Select")
        with col2: 
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Height")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Base")
            with col2:
                vAR_h=vAR_st.number_input("",key="rth_in",min_value=0.00)
                vAR_b=vAR_st.number_input("",key="rtb_in",min_value=0.00)
            vAR_ta=vAR_h*vAR_b*0.5
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Area is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_ta)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Height")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Base")
            with col2:
                vAR_h=vAR_st.number_input("",key="rth_inp",min_value=0.00)
                vAR_b=vAR_st.number_input("",key="rtb_inp",min_value=0.00)
            p2=(vAR_h**2)+(vAR_b**2)
            pa2=math.sqrt(p2)
            pa1=vAR_b+vAR_h
            vAR_prt=pa1+pa2
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Perimeter is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_prt)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    


    elif vAR_shapes=="Rhombus":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            #vAR_st.write("")
            vAR_st.markdown("## ")
            vAR_st.markdown("### Select")
        with col2: 
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Diagonal 1")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Diagonal 2")
            with col2:
                vAR_d1=vAR_st.number_input("",key="rhm_in1",min_value=0.00)
                vAR_d2=vAR_st.number_input("",key="rhm_in2",min_value=0.00)
            vAR_da=vAR_d1*vAR_d2*0.5
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Area is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_da)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Value of side")
            with col2:
                vAR_s=vAR_st.number_input("",key='rhm_p',min_value=0.00)
            vAR_rhmp=4*vAR_s
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Perimeter is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_rhmp)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    


    elif vAR_shapes=="Trapezium":
        w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
        us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))
        with col1:
            vAR_st.markdown("##")
            vAR_st.markdown("### Select")
        with col2: 
            vAR_r=vAR_st.selectbox("",["Area","Perimeter"])
        if vAR_r=="Area":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Base 1")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Base 2")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Height")
            with col2:
                vAR_b1=vAR_st.number_input("",key='tb1',min_value=0.00)
                vAR_b2=vAR_st.number_input("",key='tb2',min_value=0.00)
                vAR_h=vAR_st.number_input("",key='th',min_value=0.00)
            vAR_ta=(vAR_b1+vAR_b2)*(vAR_h*0.5)
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Area is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_ta)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    
        elif vAR_r=="Perimeter":
            with col1:
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Base 1")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the Base 2")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the side 1")
                vAR_st.write("")
                vAR_st.markdown("### ")
                vAR_st.markdown("### Enter the side 2")
            with col2:
                vAR_pb1=vAR_st.number_input("",key='tb1_p',min_value=0.00)
                vAR_pb2=vAR_st.number_input("",key='tb2_p',min_value=0.00)
                vAR_ps1=vAR_st.number_input("",key='ts1',min_value=0.00)
                vAR_ps2=vAR_st.number_input("",key='ts2',min_value=0.00)
            vAR_tp=vAR_pb1+vAR_pb2+vAR_ps1+vAR_ps2
            with bc1:
                vAR_st.write("")
                if vAR_st.button("Submit"):
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Perimeter is")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_tp)
                with bc2:
                    vAR_st.write("")
                    vAR_st.button("Clear", on_click=button_sq)
                    


