import streamlit as st
# from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        layout="wide",
        page_title="Hello",
        page_icon=":iphone:",
    )

    # Custom CSS styling
    custom_css = """
        /* Add your custom CSS rules here */
        body {
            background-color: #333;
        }
        .header {
            background-color: #d9d3d2;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        .content {
            margin: 20px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #45a049;
        }
    """

    # Apply the custom CSS
    st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

    # Header
    st.markdown('<div class="header"><h1>Streamlit App</h1></div>', unsafe_allow_html=True)

    # Content
    st.markdown('<div class="content"><p>This is the content of the app.</p></div>', unsafe_allow_html=True)

    # Button
    st.markdown('<button class="button">Click Me</button>', unsafe_allow_html=True)


if __name__ == "__main__":
    run()
