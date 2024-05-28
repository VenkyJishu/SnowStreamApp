import streamlit as st

def app():
    st.title("Welcome to :red[Netflix]  ")
    choice =st.selectbox('Login/Signup',['Login','Sign Up'])
    if choice == 'Login':
        mail = st.text_input("Username")
        password = st.text_input("Password",type='password')
        if st.button('Login'):
            
            st.write("Login is Successful")
        if st.button("Forgot Password"):
            st.text_input("Please enter your mail to send temporary password")
    else:
        mail =st.text_input("Email Address")
        username = st.text_input("Enter Username")
        password = st.text_input('Password',type='password')

        if st.button("Create Account"):
            st.write("Account Created Successfully")


app()
