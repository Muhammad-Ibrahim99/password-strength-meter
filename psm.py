import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker by Muhammad Ibrahim", page_icon="🔑", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover {background-color: #45a049}
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("🔒Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

#function to check password strength

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9) **.")

    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*) **.")

    #display password strength results
    if score == 4:
        st.success("✅ **Strong Password** your password is secure.")
    elif score == 4:
        st.info(" ⚠ **Moderate Password** - Consider improving security by adding more features")
    else:
        st.error("❌ **Weak Password** - Follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("🔍**Improve Your Password ** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")

#button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠ Please enter a password first!") #show warning if password is empty
