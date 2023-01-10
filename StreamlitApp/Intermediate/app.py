import streamlit as vAR_st
from streamlit_option_menu import option_menu
from PIL import Image as img
import source.area_perimeter as ap
import source.fact as fact
import source.tyme as tm
import source.unitconv as uc
import source.ratio as rio
import source.areatri as at
import source.areaquad as aq
import source.squareroot as sr
import source.powerof as pv
from source.statistics import stat

def button_rad():
    vAR_st.session_state["main"]="Area & Perimeter"

vAR_st.set_page_config(layout='wide')
with open("/app/applied-artificial-intelligence-for-schools/StreamlitApp/Intermediate/style/style.css") as vAR_f:
    vAR_st.markdown (f"<style>{vAR_f.read()}</style>",unsafe_allow_html=True)

if 'placeholder' not in vAR_st.session_state:
    vAR_st.session_state.placeholder = "select"

col1, col2, col3 = vAR_st.columns((2,5,3))
with col1:
    vAR_st.write("")
with col2:
    vAR_st.image('/app/applied-artificial-intelligence-for-schools/StreamlitApp/Intermediate/image/Logo_final.png')
with col3:
    vAR_st.write("")

with vAR_st.sidebar:
    selected=vAR_st.selectbox("Menu",('Area & Perimeter','Factorial','Statistics','Ratio','Unit conversion', "Time","Area of triange","Area of quadrilateral","SquareRoot","Power of value"),key="main")
    vAR_lib=vAR_st.selectbox("",("Libraries","Streamlit","Pillow","numpy","scipy"))
    vAR_st.button("Clear/Reset", on_click=button_rad)
        

if __name__=="__main__":
    try:
        if selected=="Area & Perimeter":
            ap.areaperimeter()
        if selected=="Factorial":
            fact.factorial()
        if selected=="Unit conversion":
            uc.unitconversion()   
        if selected=="Time":
            tm.tyme()
        if selected=="Statistics":
            stat()
        if selected=="Ratio":
            rio.ratio()
        if selected=="Area of triange":
            at.atri()
        if selected=="Area of quadrilateral":
            aq.areaq()
        if selected=="SquareRoot":
            sr.square_root()
        if selected=="Power of value":
            pv.power_value()
    except BaseException as error:
        vAR_st.error(error)
