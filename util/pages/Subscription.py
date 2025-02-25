import streamlit as st
import PIL as Image
#from st_paywall import add_auth
import os

st.title("Subscribe to :rainbow[Personal AI Services]")

def subscription():
    st.markdown("### It is developing, to be launched in the end of April")
    st.markdown("### Feel free to contact us by email:  <admin@aibyml.com>")
    
def subscribe():
    # Everything is accessible via the st.secrets dict:
    st.write("AIA username:", st.secrets["aia_username"])
    st.write("AIA password:", st.secrets["aia_password"])
    st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

    # And the root-level secrets are also accessible as environment variables:
    st.write(
        "Has environment variables been set:",
        os.environ["db_username"] == st.secrets["db_username"],
    )
    st.title("🎈 Tyler's Subscription app POC 🎈")
    #st.balloons()

    #add_auth(equired=True, login_button_text="Login with Google", login_button_color="#FD504D",login_sidebar=True)

    st.write("Congrats, you are subscribed!")
    st.write("the email of the user is " + str(st.session_state.email))

if __name__ == "__main__":
  subscription()
