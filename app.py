import streamlit as st
from transformers import pipeline

st.title("📝 Free AI Story Generator")
st.write("Generate a short story from any idea — no API key needed!")

# Load the text generation pipeline
@st.cache(allow_output_mutation=True)
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

prompt = st.text_input("Enter a story idea:", placeholder="A lonely robot on Mars...")

if st.button("Generate Story") and prompt:
    with st.spinner("Writing your story..."):
        results = generator(prompt, max_length=200, num_return_sequences=1)
        story = results[0]['generated_text']
        st.markdown("### ✨ Generated Story:")
        st.write(story)
