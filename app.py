import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📝 AI Story Generator")
st.write("Generate a 3-paragraph story from any idea.")

prompt = st.text_input("Enter a story idea:", placeholder="A lonely robot on Mars...")

if st.button("Generate Story") and prompt:
    with st.spinner("Writing your story..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a creative short story writer."},
                    {"role": "user", "content": f"Write a 3-paragraph story about: {prompt}"}
                ]
            )
            story = response['choices'][0]['message']['content']
            st.markdown("### ✨ Generated Story:")
            st.write(story)
        except Exception as e:
            st.error(f"Error: {e}")
