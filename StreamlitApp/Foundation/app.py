import streamlit as vAR_st
from PIL import Image
from streamlit_option_menu import option_menu
import source.datatype as dt
import source.roundingoff as ro
import source.calculator as calc
import source.ascdesc as ad
import source.tables as tb
import source.prinum as nr
import source.prime as pr
import source.lcm_1 as lcm
import source.profit_loss as pl


#vAR_st.set_page_config(layout='wide')



#for creating the side menu



with vAR_st.sidebar:
    
    vAR_selected=vAR_st.selectbox("Menu",('Data type', 'Rounding Off','Arithmetic Operation','Sorting order',"Multiplication tables","Numbers within a range","Prime or not","LCM","Profit or Loss"),key="Clear8")
    vAR_lib=vAR_st.selectbox("",("Libraries","Streamlit","Pillow"),key="Clear9")
    vAR_st.button("Clear/Reset",on_click=dt.clear_text)
    
        
        
    

        

col1, col2, col3 = vAR_st.columns([3,5,3])
with col1:
    vAR_st.write('')
with col2:
    vAR_st.image('Image/ds.png')
with col3:
    vAR_st.write('')

vAR_st.markdown("<h1 font='IBM Flex Sans'; style='text-align: center; color: black; font-size:29px;'>Applied AI for Schools - 6th Grade</h1>", unsafe_allow_html=True)
vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: blue; font-size:29px;'>Simple applications built on Streamlit</p>", unsafe_allow_html=True)
if vAR_selected=="Data type":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the data type</p>", unsafe_allow_html=True)

if vAR_selected=="Rounding Off":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Rounding Off the numbers</p>", unsafe_allow_html=True)

if vAR_selected=="Arithmetic Operation":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for basic arithmetic operations</p>", unsafe_allow_html=True)

if vAR_selected=="BMI":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to calculate BMI</p>", unsafe_allow_html=True)

if vAR_selected=="Sorting order":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for Sorting numbers</p>", unsafe_allow_html=True)

if vAR_selected=="Tables":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application for printing multiplication tables</p>", unsafe_allow_html=True)

if vAR_selected=="Numbers within a range":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to print numbers within a range</p>", unsafe_allow_html=True)

if vAR_selected=="Prime or not":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the given number is prime number or not a prime number</p>", unsafe_allow_html=True)

if vAR_selected=="LCM":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the LCM</p>", unsafe_allow_html=True)

if vAR_selected=="Profit or Loss":
    vAR_st.markdown("<p font='IBM Flex Sans'; style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: </span>Application to find the Profit and Loss</p>", unsafe_allow_html=True)





#for horizontal line
vAR_st.write("")
vAR_st.write("")
vAR_st.markdown("""
<hr style="width:100%;height:3px;background-color:gray;border-width:10">
""", unsafe_allow_html=True)

#for opening the css file
with open('style/style.css') as f:
    vAR_st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
    try:
        if vAR_selected=='Data type':
            dt.datatype()

        if vAR_selected=='Rounding Off':
            ro.roundup()

        if vAR_selected=='Arithmetic Operation':
            calc.calculator()

        

        if vAR_selected=="Sorting order":
            ad.ascdesc()

        

        if vAR_selected=="Multiplication tables":
            tb.tables()
        
        if vAR_selected=="Numbers within a range":
            nr.numrange()

        if vAR_selected=="Prime or not":
            pr.primeornot()

        if vAR_selected=="LCM":
            lcm.lcm()

        if vAR_selected=="Profit or Loss":
            pl.profit_or_loss()
            

        


        


        




    except BaseException as error:
        print("Error Message",error)
        vAR_st.write(error)

#-----------------------------------------------------------------------------------------------------------------
