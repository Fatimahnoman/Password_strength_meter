# Project # 2               "Password Strength Meter"


import re 
import streamlit as st

# Page Styling
st.set_page_config(page_title = "Password Strength Meter" , page_icon = "🌙" , layout = "centered") 

#custom css
st.markdown('''  
<style>
    .main {text-align : center;}
    .stTextInput {width : 50%; background-color #4CAF50 ; color : white; font-size : 18px; }
    .stButton button : hover {background-color : #45a049;}
</style>
''' , unsafe_allow_html = True)

# Page Title and Description
st.title (" 🔐 Password Strength Generator ")
st.write ("Enter Your Password below to check its security level. 🔍")

# Function to check Password Strength
def check_password_strength (password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1 # increased score by 1       
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**. ")
    if re.search(r"[A-Z]", password) and re.search (r"[a-z]" ,  password):
        score += 1
    else:
        feedback.append ("❌ Password must have **both uppercase (A-Z) and lower case (a-z) letters**. ")
    
    
    if re.search (r"\d" , password):
        score += 1
    else:
        feedback.append("❌ Password must have **atleast one number (0-9)**. ")
        
# Special Characters
    if re.search (r"[!@#$%^&*]" , password):
        score +=1
    else:
        feedback.append("❌ Password must have **atleast one Special Character (!@#$%^&*)**. ")
        
        
    # Display Password Strength Results
    if score == 4:
        st.success("✅ **Strong Password** - Your Password is secure. ")
    elif score == 3:
        st.info("⚠️**Moderate Password** - Consider improving security by adding more passwords")
    else:
        st.error(" **Weak Password** - Follow the suggestion below to strength it. ")


# Feedback
    if feedback :
        with st.expander("🔍 **Improve your Password**. "):
            for item in feedback:
                st.write(item) 
password = st.text_input("Enter Your Password: " , type = "password" , help = "Ensure your password is strong 🔐") 


# Button Working
if st.button ("Check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first! ") # show warning if password empty
