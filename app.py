import streamlit as st
from assistant import get_response

st.set_page_config(page_title="AI Lab Assistant", page_icon="🤖")

st.title("🤖 AI Lab Assistant")
st.write("Ask anything related to your Computer Science subjects!")

# Initialize chat history (memory)
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("Enter your question:")

# Button click
if st.button("Ask"):
    if user_input:
        # ✅ FIXED: pass chat history
        response = get_response(user_input, st.session_state.history)

        # Store conversation
        st.session_state.history.append(("Student", user_input))
        st.session_state.history.append(("Assistant", response))

# Display chat history
for role, msg in st.session_state.history:
    if role == "Student":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Assistant:** {msg}")