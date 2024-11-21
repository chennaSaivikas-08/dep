import streamlit as st

def calculation_thevenins(vth,rth,rl):
    il=vth/(rth+rl)
    pl=il**2*rl
    return il,pl
  

st.title("Thevenin's Theorem")
tab1,tab2=st.tabs(["compute","Explain"])


with tab1:
    col1,col2=st.columns(2)
    with col1:
        with  st.container(border=True):
            vth=st.number_input("Vth(V)",value=1)
            rth=st.number_input("Rth(ohms)",value=10)
            rl=st.number_input("RL(ohms)",value=1000)

            compute=st.button("Compute")
            

    with col2:
        with st.container(border=True):
            if compute:
                il,pl= calculation_thevenins(vth,rth,rl)
                st.write(f"load current={il:.2f}A")
                st.write(f"load power={pl:.2f}W")


with tab2:
    st.write("Thevenin's Theorem is a fundamental principle in electrical engineering")
    st.write("that simplifies the analysis of complex linear circuits. It states that any two-terminal linear circuit, ")
    st.write("consisting of voltage sources, current sources, and resistances, can be replaced by an equivalent circuit")
    st.write("consisting of a single voltage source in series with a single resistance.")
    st.latex(r"V_{th}=V_{oc}")