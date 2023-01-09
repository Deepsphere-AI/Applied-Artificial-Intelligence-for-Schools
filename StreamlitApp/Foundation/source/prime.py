import streamlit as vAR_st


def prime(b):
    c='prime number'
    for i in range(2,b):
        if b%i==0:
            c='not a prime number'
    return c

def primeornot():
    
    
    w1,col1,col2,w2=vAR_st.columns((1,2,2,1))
    us1,bc1,bc2,us2=vAR_st.columns((4,1.4,1.4,4))

    def cleartext():
        vAR_st.session_state['prime_in']=""
    with col1:
        #vAR_st.write("")
        vAR_st.markdown("##")
        vAR_st.markdown("### Enter the number")
    with col2:
        a=vAR_st.text_input("",key="prime_in")

    
    with bc1:
        vAR_st.markdown("### ")
        if vAR_st.button("submit"):
            if a.isnumeric():
                vAR_ans=prime(int(a))
                if vAR_ans=='prime number':
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Answer is ")
                    with col2:
                        vAR_st.write("")
                        vAR_st.success(vAR_ans)
                    
                else:
                    with col1:
                        vAR_st.markdown("## ")
                        vAR_st.markdown("### Answer is ")
                    with col2:
                        vAR_st.write("")
                        vAR_st.warning(vAR_ans)                  
                # else:
                #     with col1:
                #         vAR_st.markdown("## ")
                #         vAR_st.markdown("### Answer is ")
                #     with col2:
                #         vAR_st.write("")
                #         vAR_st.success("composite")
            else:
                with col2:
                        vAR_st.write("")
                        vAR_st.info("Enter whole number only")
        with bc2:
            vAR_st.markdown("### ")
            vAR_st.button("Clear", on_click=cleartext)
