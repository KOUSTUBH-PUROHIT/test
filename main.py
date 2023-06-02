import streamlit as st
import speech_recognition as sr
# import PyAudio
def convert_speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Speak something...")
        audio = r.listen(source)

    try:
        st.info("Recognizing...")
        text = r.recognize_google(audio)
        st.success(f"Speech to text: {text}")
    except sr.UnknownValueError:
        st.warning("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    st.title("Speech to Text Converter")

    image="preview.png"
    image_width = st.sidebar.slider("Image Width", min_value=100, max_value=800, value=200, step=100)
    st.sidebar.write("Image Size:", image_width)
    st.image(image, width=image_width)

    # img_style = f"margin: 0 auto; width: {image_width}px"
    # st.markdown(f'<img src="{image}" style="{img_style}">', unsafe_allow_html=True)
    # Record button
    # col1, col2, col3 = st.columns([1, 2, 1])
    # with col2:
    if st.button("Start Recording"):
       convert_speech_to_text()

if __name__ == "__main__":
    main()

