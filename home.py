import streamlit as st

def main():
    _, col1, _ = st.columns(3)
    with col1:
        st.image("images/logo.png")
    
    st.markdown("<h2 style='text-align: center;'>The Third Eye</h2>", unsafe_allow_html=True)
    st.markdown('''
        Welcome to "**Playmath**", a place where you can fiddle with simple yet powerful tools to gain 
        better intuition in various maths domains!

        They are developed mainly out of my desire to explore particular math concepts, but still, 
        I'd like to believe that you'll be benefitted from _playing_ around with them even though you, yourself, didn't do _programming_ part.

        Currently, there're only two playgrounds. Click the sidebar to visit and have fun!
    ''')

    
if __name__=="__main__":
    main()

