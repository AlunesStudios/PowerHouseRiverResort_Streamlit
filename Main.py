import streamlit as st
from PIL import Image
Main_Image = Image.open("PRR_Main_image.png")
#---------------------------------------#
st.set_page_config(page_icon=Main_Image, page_title="PowerHouse River Resort")
st.image(Main_Image, width=250)
st.header("PowerHouse River Resort", divider="green")
st.markdown("**Unwind at our riverside tented resort set between two streams with waterfalls. Enjoy river baths, birdwatching, tea plucking, and organic meals at our hydro-powered restaurant. Relax with fish therapy or work in nature’s calm**")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.write("")
st.write("")
st.write("")
st.write("")
Loc_para, loc_map = st.columns(2)
with Loc_para:
    st.header("**The Location**", divider="grey")
    with st.container(border=20):
       st.write("**Powerhouse River Resort is nestled in the tranquil village of Godagampola, Parakaduwa, in the lush and scenic Ratnapura District of Sri Lanka. Just 5.7 km from the town of Eheliyagoda and around 60  km from the nearest airport, the resort is easily accessible yet feels completely secluded in nature. Surrounded by dense greenery, flowing streams, and sprawling tea estates, the location offers a perfect blend of serenity and natural beauty. Set between two streams with cascading waterfalls, the resort provides an ideal setting for nature lovers and those seeking a peaceful riverside escape. Its elevated positioning within a tea-growing region adds a cool, refreshing atmosphere, making it a unique getaway not far from Colombo.**")
with loc_map:
    google_map_iframe = """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3162.8851888000005!2d80.3105!3d6.8741!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ae36574f4419451%3A0x1234567890abcdef!2sPowerhouse%20River%20Resort!5e0!3m2!1sen!2slk!4v1689176350000!5m2!1sen!2slk" width="300" height="300" style="border:0;" allowfullscreen="" loading="lazy" class="map-frame"  <!-- Add a class for CSS styling -->></iframe> """
    custom_css = """<style>.map-frame {border-radius: 20px; /* Adjust this value for more or less rounding */overflow: hidden;  /* Ensures the content within the rounded border is also rounded */border: 5px solid #007BFF; /* Optional: Add a border color */}</style>"""
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(google_map_iframe, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

Room_para, Room_pic = st.columns(2)
with Room_para:
    st.header("**The Rooms(Tents)**", divider="grey")
    with st.container(border=20, height=575):
        st.write("**The rooms at Powerhouse River Resort are designed to blend comfort with nature, offering a cozy and peaceful retreat surrounded by lush greenery and the soothing sounds of flowing water. Each room is spacious and thoughtfully furnished, featuring comfortable bedding, private bathrooms, and large windows or open areas that bring in natural light and fresh air. Some rooms offer direct views of the river or waterfalls, creating a calming atmosphere ideal for relaxation. Whether you choose a tented room for a rustic experience or a more standard setup, every stay promises tranquility, privacy, and a close connection to nature.**")
with Room_pic:
    st.write("")
    st.header("")
    with st.container(border=20, height=575):
        Image_Room_1 = Image.open("Image_1.jpg")
        Image_Room_2 = Image.open("Image_2.jpg")
        Image_Room_3 = Image.open("Image_3.jpg")
        Image_Room_4 = Image.open("Image_4.jpg")
        Image_Room_5 = Image.open("Image_5.jpg")
        st.image([Image_Room_1, Image_Room_4, Image_Room_5, Image_Room_3, Image_Room_2])

Food_Info, Food_Pic = st.columns(2)

with Food_Info:
    st.header("**The Food**", divider="grey")
    with st.container(border=20):
        st.write("**The Powerhouse River Resort offers a unique dining experience set within a charming mini hydro structure, surrounded by lush greenery, waterfalls, and natural pools. Guests can savor traditional Sri Lankan cuisine, including flavorful plain rice and curry made with vegetables from the resort’s organic garden, as well as musical koththu and BBQ dishes. The menu caters to various preferences, with chicken, fish, and vegetarian options readily available, and special meats like pork prepared on request for an additional fee. Reviewers consistently praise the food as fresh, tasty, and superbly prepared—often cooked live—making it a highlight of the stay and perfectly complementing the resort’s serene, nature-filled atmosphere.**")
with Food_Pic:
    st.header("")
    st.write("")
    with st.container(border=20, height=430):
        Food_Image_1 = Image.open("310165472.jpg")
        Food_Image_2 = Image.open("310165482.jpg")
        Food_Image_3 = Image.open("310165499.jpg")
        Food_Image_4 = Image.open("310165505.jpg")
        Food_Image_5 = Image.open("310165509.jpg")
        Food_Image_6 = Image.open("310165519.jpg")
        Food_Image_7 = Image.open("310165527.jpg")
        Food_Image_8 = Image.open("310165545.jpg")
        st.image([Food_Image_1,Food_Image_2,Food_Image_7,Food_Image_8,Food_Image_6,Food_Image_3,Food_Image_4,Food_Image_5])

st.header("The Video")
video = """<iframe width="300" height="100" src="https://www.youtube.com/embed/vo8R6brrvZE" title="Powerhouse River Resort | සත්කාරයේ චමත්කාරය | සොදුරු නවාතැන | Sonduru Nawathena" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen class="VIDEO"> </iframe>"""
vid_css = """<style>.VIDEO {border-radius: 20px; /* Adjust this value for more or less rounding */overflow: hidden;  /* Ensures the content within the rounded border is also rounded */border: 5px solid #92E287; /* Optional: Add a border color */}</style>"""
st.markdown(vid_css, unsafe_allow_html=True)
st.markdown(video, unsafe_allow_html=True)
