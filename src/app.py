import streamlit as st

def main():
    st.title("Simple Streamlit Application")
    st.write("Welcome to our application!")
    
    # Add a simple counter
    if 'count' not in st.session_state:
        st.session_state.count = 0

    if st.button('Increment Counter'):
        st.session_state.count += 1

    st.write(f"Counter value: {st.session_state.count}")

if __name__ == "__main__":
    main()