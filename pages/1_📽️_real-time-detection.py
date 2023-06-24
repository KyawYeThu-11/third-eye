import streamlit as st
import av
from streamlit_webrtc import webrtc_streamer, VideoHTMLAttributes
from detect import predict

def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    predicted_image = predict(img)

    # img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
    return av.VideoFrame.from_ndarray(predicted_image, format="bgr24")

def main():
    st.subheader("Detection in Real Time")
    webrtc_streamer(key="example", 
                    video_frame_callback=callback,
                    rtc_configuration={
                        "iceServers":[{"urls": ["stun:stun.l.google.com:19302"]}]
                    },
                    video_html_attrs=VideoHTMLAttributes(
                        autoPlay=True, controls=True, style={"width": "100%"}, muted=True
                    ))

if __name__=="__main__":
    main()
### Implementation with pure openCV (only works in local) ###

# from detect import open_webcam

# def main():
#     st.subheader("Detection in Real Time")
#     if st.button("Start video"):
#         open_webcam()

# if __name__=="__main__":
#     main()