import streamlit as st
from PIL import Image
from datetime import date, timedelta
Main_Image = Image.open("PRR_Image.jpg")
st.set_page_config(page_title="PowerHouse River Resort")
st.image(Main_Image, width=250)
st.logo(Main_Image)
st.header("PowerHouse River Resort", divider="green",)
st.write("")
tomorrow = date.today() + timedelta(days=1)
#---------------------------------------#
with (st.form("Booking Registration")):
    st.subheader("• Initial Set-Up", divider="blue")
    Name_Text_Input = st.text_input("**Enter Your Name**")
    col1, col2 = st.columns(2)
    with col1:
        Check_in_Date = st.date_input("**Check-in Date**", value="today", min_value="today")
    with col2:
        Check_out_Date = st.date_input("**Check-out Date**", value=tomorrow, min_value=tomorrow)
    Meal_Plan_Select_Box = st.selectbox("**Select a Meal Plan**", options=["BB", "HB", "FB"])
    Amount_of_Rooms_Number_Input = st.number_input("**Amount of Rooms**", min_value=1, max_value=4)
    #----------------------------------------------------------------------------------------------#
    if Amount_of_Rooms_Number_Input == 1:
        Type_of_Room_1 = st.selectbox("**Type of Room**", ["Deluxe", "Standard"])
        st.subheader("• Amount of Pax", divider="blue")
        if Type_of_Room_1 == "Deluxe":
            col1, col2, col3 = st.columns(3)
            with col1:
               Number_of_Adults_1 = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3)
            with col2:
               Number_of_Children_0_5_1 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1)
            with col3:
               Number_of_Children_6_11_1 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=1)
        elif Type_of_Room_1 == "Standard":
            col1, col2, col3 = st.columns(3)
            with col1:
                Number_of_Adults_1 = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4)
            with col2:
                Number_of_Children_0_5_1 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2)
            with col3:
                Number_of_Children_6_11_1 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2)
        BN = st.selectbox("**Extra Meal Options**", ["BBQ", "Normal"])
        #---------------------------------------------------------------------------------------------------#
    if st.form_submit_button("Submit-(Refresh)"):
        check = 0
        if Check_out_Date == Check_in_Date:
            check = 0
            st.info("Please Change the Check-out date")
        elif Check_in_Date > Check_out_Date:
            check = 0
            st.info("Please have the Check-out date be later after Check-in date")
        if Name_Text_Input == "":
            check = 0
            st.info("Please Enter Your Full Name")
        else:
            check = 1
            if check == 1:
               if Type_of_Room_1 == "Deluxe" and BN == "BBQ":
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*4000)+(Number_of_Children_6_11_1*2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*4000)+(Number_of_Children_6_11_1*2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*4000)+(Number_of_Children_6_11_1*2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*4000)+(Number_of_Children_6_11_1*2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 4000) + (Number_of_Children_6_11_1 * 2000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons(border=50)
               if Type_of_Room_1 == "Deluxe" and BN == "Normal":
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*2000)+(Number_of_Children_6_11_1*1000))
                          with st.container():
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*2000)+(Number_of_Children_6_11_1*1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*2000)+(Number_of_Children_6_11_1*1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 2000) + (Number_of_Children_6_11_1 * 1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1+Number_of_Children_0_5_1+Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*2000)+(Number_of_Children_6_11_1*1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 1 and Number_of_Children_6_11_1 == 0:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 2000) + (Number_of_Children_6_11_1 * 1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 2 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1 * 12000) + (Number_of_Children_6_11_1 * 6000) + (Number_of_Adults_1 * 2000) + (Number_of_Children_6_11_1 * 1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
                      if Number_of_Adults_1 == 3 and Number_of_Children_0_5_1 == 0 and Number_of_Children_6_11_1 == 1:
                          Total_Price = ((Number_of_Adults_1*12000)+(Number_of_Children_6_11_1*6000)+(Number_of_Adults_1*2000)+(Number_of_Children_6_11_1*1000))
                          with st.container(border=50):
                              st.header("Summary", divider="green")
                              st.write(f"**Full Name: {Name_Text_Input}**")
                              st.write(f"**Check-in Date: {Check_in_Date}**")
                              st.write(f"**Check-out Date: {Check_out_Date}**")
                              st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                              st.write(f"**Amount of Rooms: {Amount_of_Rooms_Number_Input}**")
                              st.write(f"**Amount of People: {Number_of_Adults_1 + Number_of_Children_0_5_1 + Number_of_Children_6_11_1}**")
                              st.write(f"**Total Price: {Total_Price}**")
                              st.balloons()
st.write("© 2025 The Alunes Group. All rights reserved")
st.write("© 2025 Powerhouse River Resort. All rights reserved")
