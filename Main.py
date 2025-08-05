import streamlit as st
from PIL import Image
Main_Image = Image.open("PRR_Main_image.png")
#---------------------------------------#
st.set_page_config(page_icon=Main_Image, page_title="PowerHouse River Resort")
st.image(Main_Image, width=250)
st.header("PowerHouse River Resort", divider="green")
st.markdown("**Tented resort facing the river with gentle rocking spacious swings..Relax & Enjoy the river bath in Crystal Clear Water and enjoy the lullaby like soothing rippling sounds from the river... Resort located bordering two streams (island) with Cascading Waterfalls where you can select whether to tryout the mesmerising Waterfall or the calm pool like water bed where you can enjoy unpolluted nature with Kingfishers or big . Experience walking through our Tea Plantation & Tea plucking and choose the tips you want to have a nice cup of green tea. The Restaurant is located inside the Mini Hydro where our customers can enjoy nice meals whether it will be plain rice and curry where the veggies comes from our organic vegetable garden, or a musical koththu or a scrumptious BBQ! Come and experience the Srilnkan Gray Hornbills and Endemic flying around. The natural fish therapy whenever you feels like. Enjoy all of these and work while you relax!**")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
google_map_iframe = """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3162.8851888000005!2d80.3105!3d6.8741!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ae36574f4419451%3A0x1234567890abcdef!2sPowerhouse%20River%20Resort!5e0!3m2!1sen!2slk!4v1689176350000!5m2!1sen!2slk" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" class="map-frame"  <!-- Add a class for CSS styling -->></iframe> """
custom_css = """<style>.map-frame {border-radius: 20px; /* Adjust this value for more or less rounding */overflow: hidden;  /* Ensures the content within the rounded border is also rounded */border: 5px solid #007BFF; /* Optional: Add a border color */}</style>"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(google_map_iframe, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.write("")
st.write("")
st.write("")
st.write("")
youtube_video = """<iframe width="800" height="440" src="https://www.youtube.com/embed/gnJDmQ674DU" title="Visit Powerhouse River Resort..." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" class="yt" allowfullscreen></iframe>"""
custom_css_yt = """<style>.yt {border-radius: 20px; /* Adjust this value for more or less rounding */overflow: hidden;  /* Ensures the content within the rounded border is also rounded */border: 5px solid #007BFF; /* Optional: Add a border color */}</style>"""
st.markdown(custom_css_yt, unsafe_allow_html=True)
st.markdown(youtube_video, unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
with st.container(border=50):
   I1, I2, I3, I4, I5 = st.columns(5)
   with I1:
       Image_1 = Image.open("Image_1.jpg")
       st.image(Image_1, width=700)
   with I2:
       Image_2 = Image.open("Image_2.jpg")
       st.image(Image_2)
   with I3:
       Image_3 = Image.open("Image_3.jpg")
       st.image(Image_3)
   with I4:
       Image_4 = Image.open("Image_4.jpg")
       st.image(Image_4)
   with I5:
       Image_5 = Image.open("Image_5.jpg")
       st.image(Image_5)

   I12, I22, I32, I42, I52 = st.columns(5)
   with I12:
       Image_12 = Image.open("Image_1.jpg")
       st.image(Image_12, width=700)
   with I22:
       Image_22 = Image.open("Image_2.jpg")
       st.image(Image_22)
   with I32:
       Image_32 = Image.open("Image_3.jpg")
       st.image(Image_32)
   with I42:
       Image_42 = Image.open("Image_4.jpg")
       st.image(Image_42)
   with I52:
       Image_52 = Image.open("Image_5.jpg")
       st.image(Image_52)
st.write("© 2025 The Alunes Group. All rights reserved")
st.write("© 2025 Powerhouse River Resort. All rights reserved")
