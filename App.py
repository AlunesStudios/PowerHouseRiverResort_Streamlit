import streamlit as st
from PIL import Image
from datetime import date, timedelta
Main_Image = Image.open("PRR_Main_image.png")
st.set_page_config(page_title="PowerHouse River Resort")
st.image(Main_Image, width=350)
st.logo(Main_Image)
st.header("PowerHouse River Resort", divider="green",)
st.write("")
tomorrow = date.today() + timedelta(days=1)
#---------------------------------------#
with st.container(border=30):
    st.subheader("• Initial Set-Up", divider="blue")
    Name_Text_Input = st.text_input("**Enter Your Name**", placeholder="Enter your Name")
    col1, col2 = st.columns(2)
    with col1:
        Check_in_Date = st.date_input("**Check-in Date**", value="today", min_value="today")
    with col2:
        Check_out_Date = st.date_input("**Check-out Date**", value=tomorrow, min_value=tomorrow)
    Col1, Col2 = st.columns(2)
    with col1:
        Meal_Plan_Select_Box = st.selectbox("**Select a Meal Plan**", options=["BB", "HB", "FB"])
    with col2:
        Amount_of_Rooms_Number_Input = st.number_input("**Amount of Rooms**", min_value=1, max_value=4)
    # ----------------------------------------------------------------------------------------------#
    if "hello" not in st.session_state:
        st.session_state.hello = False
    if st.button("Next(Refresh)", use_container_width=True):
        st.session_state.hello = True
    if st.session_state.hello:
        if Amount_of_Rooms_Number_Input is None or Amount_of_Rooms_Number_Input == 1:
            Type_of_Room = st.selectbox("**Type of Room**", ["Deluxe", "Standard"])
            st.subheader("• Amount of Pax", divider="blue")
            if Type_of_Room == "Deluxe":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="x1")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="x2")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=1,key="x3")

            elif Type_of_Room == "Standard":
                col1, col2, col3 = st.columns(3)
                with col1:
                    Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,key="x4")
                with col2:
                    Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,key="x5")
                with col3:
                    Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,key="x6")
        elif Amount_of_Rooms_Number_Input == 2:
            with st.container(border=20):
                st.header("Room.1")
                Type_of_Room_1 = st.selectbox("**Type of Room**", ["Deluxe", "Standard"], key="Rom1")
                if Type_of_Room_1 == "Deluxe":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="xg1")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="xg2")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=1, key="xg3")
                elif Type_of_Room_1 == "Standard":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,key="xg4")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,key="xg5")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=2,key="xg6")
            with st.container(border=20):
                st.header("Room.2")
                Type_of_Room_2 = st.selectbox("**Type of Room**", ["Deluxe", "Standard"])
                if Type_of_Room_2 == "Deluxe":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="xc10")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="xc11")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=1,key="xc12")
                elif Type_of_Room_2 == "Standard":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,key="xc13")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,key="xc14")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=2,key="xc15")
        elif Amount_of_Rooms_Number_Input == 3:
            with st.container(border=20):
                st.header("Room.1")
                Type_of_Room_1 = st.selectbox("**Type of Room**", ["Deluxe"], key="Rom11")
                if Type_of_Room_1 == "Deluxe":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="xg12")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="xg23")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=1, key="xg34")
            with st.container(border=20):
                st.header("Room.2")
                Type_of_Room_2 = st.selectbox("**Type of Room**", ["Deluxe"])
                if Type_of_Room_2 == "Deluxe":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="xc108")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="xc119")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=1,key="xc1210")
            with st.container(border=20):
                st.header("Room.3")
                Type_of_Room_3 = st.selectbox("**Type of Room**", ["Standard"])
                if Type_of_Room_3 == "Standard":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,key="xc1317")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,key="xc1418")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,key="xc1519")
        elif Amount_of_Rooms_Number_Input == 4:
            with st.container(border=20):
                st.header("Room.1")
                Type_of_Room_1 = st.selectbox("**Type of Room**", ["Deluxe"], key="Rom11")
                if Type_of_Room_1 == "Deluxe":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="xg121")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="xg232")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=1, key="xg343")
            with st.container(border=20):
                st.header("Room.2")
                Type_of_Room_2 = st.selectbox("**Type of Room**", ["Deluxe"])
                if Type_of_Room_2 == "Deluxe":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=3,key="xc1084")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=1,key="xc1195")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0,max_value=1,key="xc12106")
            with st.container(border=20):
                st.header("Room.3")
                Type_of_Room_3 = st.selectbox("**Type of Room**", ["Standard"])
                if Type_of_Room_3 == "Standard":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,key="xc13177")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,key="xc14188")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,key="xc15199")
            with st.container(border=20):
                st.header("Room.4")
                Type_of_Room_4 = st.selectbox("**Type of Room**", ["Standard"], key=345)
                if Type_of_Room_4 == "Standard":
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        Number_of_Adults = st.number_input("**Adults(Aged 12 & Above)**", min_value=2, max_value=4,key="xc131710")
                    with col2:
                        Number_of_Children_0_5 = st.number_input("**Children(Aged 0-5)**", min_value=0, max_value=2,key="xc141811")
                    with col3:
                        Number_of_Children_6_11 = st.number_input("**Children(Aged 6-11)**", min_value=0, max_value=2,key="xc151912")
        BN = st.selectbox("**Extra Meal Options**", ["BBQ", "Normal"])
        # ---------------------------------------------------------------------------------------------------#
        if "Submit(Refresh)" not in st.session_state:
            st.session_state.Submit_Refresh = False
        if st.button("Submit(Refresh)", use_container_width=True):
            st.session_state.Submit_Refresh = True
        if st.session_state.Submit_Refresh:
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
                    Full_Price_Meal_Plan = Meal_Plan_Select_Box
                    if Full_Price_Meal_Plan == "BB":
                        Full_Price_Room_Number = (1 if Amount_of_Rooms_Number_Input == 1 else 2 if Amount_of_Rooms_Number_Input == 2 else 3 if Amount_of_Rooms_Number_Input == 3 else 4)
                        if Amount_of_Rooms_Number_Input == 1:
                            Full_Price = ((22000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Type_of_Room == "Deluxe" else 28000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Type_of_Room == "Deluxe" else 18000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Type_of_Room == "Standard" else 23000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Type_of_Room == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                        if Amount_of_Rooms_Number_Input == 2:
                            Full_Price_1 = ((22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((22000 if Number_of_Adults == 2 and Type_of_Room_2 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_2 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_2 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_2 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2)
                        if Amount_of_Rooms_Number_Input == 3:
                            Full_Price_1 = ((22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((22000 if Number_of_Adults == 2 and Type_of_Room_2 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_2 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_2 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_2 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_3 = ((22000 if Number_of_Adults == 2 and Type_of_Room_2 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_2 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_2 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_2 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2 + Full_Price_3)
                        if Amount_of_Rooms_Number_Input == 4:
                            Full_Price_1 = ((22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((22000 if Number_of_Adults == 2 and Type_of_Room_2 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_2 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_2 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_2 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_3 = ((22000 if Number_of_Adults == 2 and Type_of_Room_2 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_2 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_2 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_2 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_4 = ((22000 if Number_of_Adults == 2 and Type_of_Room_2 == "Deluxe" else 28000 if Number_of_Adults == 3 and Type_of_Room_2 == "Deluxe" else 18000 if Number_of_Adults == 2 and Type_of_Room_2 == "Standard" else 23000 if Number_of_Adults == 3 and Type_of_Room_2 == "Standard" else 27000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2 + Full_Price_3 + Full_Price_4)
                    elif Full_Price_Meal_Plan == "HB":
                        Full_Price_Room_Number = (1 if Amount_of_Rooms_Number_Input == 1 else 2 if Amount_of_Rooms_Number_Input == 2 else 3 if Amount_of_Rooms_Number_Input == 3 else 4)
                        if Amount_of_Rooms_Number_Input == 1:
                            Full_Price = ((26000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Type_of_Room == "Deluxe" else 34000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Type_of_Room == "Deluxe" else 22000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Type_of_Room == "Standard" else 29000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Type_of_Room == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                        if Amount_of_Rooms_Number_Input == 2:
                            Full_Price_1 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2)
                        if Amount_of_Rooms_Number_Input == 3:
                            Full_Price_1 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_3 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2 + Full_Price_3)
                        if Amount_of_Rooms_Number_Input == 4:
                            Full_Price_1 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_3 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_4 = ((26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 34000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 22000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 29000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 35000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2 + Full_Price_3 + Full_Price_4)
                    elif Full_Price_Meal_Plan == "FB":
                        Full_Price_Room_Number = (1 if Amount_of_Rooms_Number_Input == 1 else 2 if Amount_of_Rooms_Number_Input == 2 else 3 if Amount_of_Rooms_Number_Input == 3 else 4)
                        if Amount_of_Rooms_Number_Input == 1:
                            Full_Price = ((30000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Type_of_Room == "Deluxe" else 40000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Type_of_Room == "Deluxe" else 26000 if Number_of_Adults == 2 and Full_Price_Room_Number == 1 and Type_of_Room == "Standard" else 35000 if Number_of_Adults == 3 and Full_Price_Room_Number == 1 and Type_of_Room == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                        if Amount_of_Rooms_Number_Input == 2:
                            Full_Price_1 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2)
                        if Amount_of_Rooms_Number_Input == 3:
                            Full_Price_1 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_3 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2 + Full_Price_3)
                        if Amount_of_Rooms_Number_Input == 4:
                            Full_Price_1 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_2 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_3 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price_4 = ((30000 if Number_of_Adults == 2 and Type_of_Room_1 == "Deluxe" else 40000 if Number_of_Adults == 3 and Type_of_Room_1 == "Deluxe" else 26000 if Number_of_Adults == 2 and Type_of_Room_1 == "Standard" else 35000 if Number_of_Adults == 3 and Type_of_Room_1 == "Standard" else 43000) + ((Number_of_Adults * 4000) + (Number_of_Children_6_11 * 2000) if BN == "BBQ" else (Number_of_Children_6_11 * 1000)))
                            Full_Price = (Full_Price_1 + Full_Price_2 + Full_Price_3 + Full_Price_4)
                    with st.container(border=40):
                        st.header("**Booking Summary**", divider="grey")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Full Name: {Name_Text_Input}**")
                            st.write(f"**Check-in Date: {Check_in_Date}**")
                            st.write(f"**Check-out Date: {Check_out_Date}**")
                            st.write(f"**Meal Plan: {Meal_Plan_Select_Box}**")
                        with col2:
                            st.write(f"**Amount of Room: {Amount_of_Rooms_Number_Input}**")
                            if Amount_of_Rooms_Number_Input == 1:
                                st.write(f"**Type of Room:{Type_of_Room}**")
                            if Amount_of_Rooms_Number_Input == 2:
                                st.write(f"**Type of Room**")
                                st.write(f"Room.1:{Type_of_Room_1}")
                                st.write(f"Room.2:{Type_of_Room_2}")
                            if Amount_of_Rooms_Number_Input == 3:
                                st.write(f"**Type of Room: Deluxe+Deluxe+Standard**")
                            if Amount_of_Rooms_Number_Input == 4:
                                st.write(f"**Type of Room: Deluxe+Deluxe+Standard+Standard**")
                            st.write(f"**Amount of Pax: {Number_of_Adults + Number_of_Children_0_5 + Number_of_Children_6_11}**")
                            st.write(f"**Full Price: Rs.{Full_Price}**")

st.write("© 2025 The Alunes Group. All rights reserved")
st.write("© 2025 Powerhouse River Resort. All rights reserved")
