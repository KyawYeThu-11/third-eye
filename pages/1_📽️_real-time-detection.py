import streamlit as st
from detect import open_webcam

def main():
    st.subheader("Detection in Real Time")
    if st.button("Start video"):
        open_webcam()

if __name__=="__main__":
    main()