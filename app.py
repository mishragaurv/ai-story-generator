import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("📝 AI Story Generator")
st.write("Generate a 3-paragraph story from any idea.")

# Get input from user
prompt = st.text_input("Enter a story idea:", placeholder="A lonely robot on Mars...")

if st.button("Generate Story") and prompt:
    with st.spinner("Writing your story..."):
        try:
            # Use GPT-3.5 (compatible with all accounts)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a creative short story writer."},
                    {"role": "user", "content": f"Write a 3-paragraph story about: {prompt}"}
                ]
            )
            story = response.choices[0].message.content
            st.markdown("### ✨ Generated Story:")
            st.write(story)
        except Exception as e:
            st.error(f"Error: {e}")
