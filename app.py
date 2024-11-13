# app.py
import streamlit as st
from datetime import datetime
import pandas as pd

# Tạo cấu trúc trang chính và tiêu đề
st.set_page_config(page_title="Ứng dụng Cá nhân hóa lịch khám sức khỏe", layout="centered")
st.title("Ứng dụng Cá nhân hóa lịch khám sức khỏe")

# Lưu trữ dữ liệu (giả lập cho bản test ban đầu, sau có thể thay bằng database thực)
if 'user_data' not in st.session_state:
    st.session_state.user_data = []

# Hàm đăng nhập/đăng ký cơ bản (dùng session_state để lưu người dùng tạm thời)
def login():
    st.sidebar.title("Đăng nhập/Đăng ký")
    with st.sidebar.form("login_form"):
        email = st.text_input("Email")
        phone = st.text_input("Số điện thoại")
        password = st.text_input("Mật khẩu", type="password")
        submit = st.form_submit_button("Đăng nhập")
        
        if submit:
            st.session_state['logged_in'] = True
            st.session_state['email'] = email
            st.sidebar.success("Đăng nhập thành công!")

# Hàm cập nhật thông tin cá nhân
def update_profile():
    st.header("Cập nhật thông tin cá nhân")
    with st.form("update_form"):
        name = st.text_input("Họ và tên")
        phone = st.text_input("Số điện thoại")
        age = st.number_input("Tuổi", min_value=1, max_value=120, step=1)
        gender = st.selectbox("Giới tính", ["Nam", "Nữ", "Khác"])
        height = st.number_input("Chiều cao (cm)")
        weight = st.number_input("Cân nặng (kg)")
        blood_pressure = st.text_input("Huyết áp")
        blood_sugar = st.number_input("Đường huyết")
        blood_type = st.selectbox("Nhóm máu", ["A", "B", "AB", "O"])
        submit = st.form_submit_button("Lưu thông tin")
        
        if submit:
            profile = {
                "name": name,
                "phone": phone,
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight,
                "blood_pressure": blood_pressure,
                "blood_sugar": blood_sugar,
                "blood_type": blood_type,
            }
            st.session_state.user_data.append(profile)
            st.success("Thông tin cá nhân đã được cập nhật!")

# Hàm đặt lịch khám
def book_appointment():
    st.header("Đặt lịch khám")
    with st.form("appointment_form"):
        city = st.text_input("Tỉnh/Thành phố")
        district = st.text_input("Quận/Huyện/Thị xã")
        ward = st.text_input("Xã/Phường")
        address = st.text_input("Địa chỉ chi tiết")
        date = st.date_input("Chọn ngày khám")
        time = st.time_input("Chọn giờ khám", value=datetime.strptime("07:00", "%H:%M").time())
        
        services = ["Khám tổng quát", "Xét nghiệm máu", "Siêu âm", "X-quang"]
        selected_services = st.multiselect("Dịch vụ khám", services)
        
        submit = st.form_submit_button("Xác nhận lịch khám")
        
        if submit:
            appointment = {
                "city": city,
                "district": district,
                "ward": ward,
                "address": address,
                "date": date,
                "time": time,
                "services": selected_services
            }
            st.session_state.user_data.append(appointment)
            st.success("Lịch khám đã được xác nhận!")

# Hàm xem lịch khám đã đặt
def view_appointments():
    st.header("Lịch khám đã đặt")
    if len(st.session_state.user_data) > 0:
        for appt in st.session_state.user_data:
            st.write(f"Ngày: {appt.get('date')}, Giờ: {appt.get('time')}, Địa điểm: {appt.get('address')}")

# Hàm chính
def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
    else:
        # Điều hướng giữa các chức năng
        menu = ["Cập nhật thông tin cá nhân", "Đặt lịch khám", "Xem lịch khám đã đặt"]
        choice = st.sidebar.selectbox("Chọn chức năng", menu)
        
        if choice == "Cập nhật thông tin cá nhân":
            update_profile()
        elif choice == "Đặt lịch khám":
            book_appointment()
        elif choice == "Xem lịch khám đã đặt":
            view_appointments()

if __name__ == "__main__":
    main()
