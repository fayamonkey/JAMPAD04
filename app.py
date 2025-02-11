import streamlit as st

st.set_page_config(page_title="Sound Jam Pad", layout="centered")

st.title("Sound Jam Pad")
st.write(
    """
    Click a button below to play a fun sound effect!
    \n_**Note**: Your web browser may require you to allow audio/autoplay for 
    this to work seamlessly._
    """
)

# A small helper function to embed an audio player with autoplay:
def play_sound(sound_url):
    # We use `unsafe_allow_html=True` to embed raw HTML.
    audio_html = f"""
        <audio autoplay>
        <source src="{sound_url}" type="audio/mpeg">
        Your browser does not support the audio element.
        </audio>
        """
    st.markdown(audio_html, unsafe_allow_html=True)

# Dictionary of sound labels to their URLs
sound_dict = {
    "Applause": "https://www.soundjay.com/human/applause-01.mp3",
    "Boo": "https://www.soundjay.com/human/boo-01.mp3",
    "Aww": "https://soundbible.com/mp3/Aww-SoundBible.com-1461570320.mp3",
    "Laugh": "https://soundbible.com/mp3/Kids Laughing-SoundBible.com-156518781.mp3",
    "Ta Da": "https://soundbible.com/mp3/Ta Da-SoundBible.com-1884170640.mp3",
    "Air Horn": "https://soundbible.com/mp3/Air Horn-SoundBible.com-962919848.mp3",
    "Drum Roll": "https://soundbible.com/mp3/Drum Roll-SoundBible.com-1145408114.mp3",
    "Crowd Gasp": "https://soundbible.com/mp3/Audience_ gasp-SoundBible.com-952543671.mp3",
    "Woop Woop": "https://soundbible.com/mp3/Railroad Crossing Bell-SoundBible.com-633573797.mp3" 
}

# Create three columns of buttons (3x3 = 9):
cols = st.columns(3)

buttons = list(sound_dict.keys())

# We will place the 9 buttons in a grid using the columns:
for i, label in enumerate(buttons):
    col_index = i % 3
    with cols[col_index]:
        if st.button(label):
            # Call our helper function to embed the audio markup
            play_sound(sound_dict[label])
