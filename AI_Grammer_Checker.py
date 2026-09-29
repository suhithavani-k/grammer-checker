import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="AI Grammar Checker",
    page_icon="✍️",
    layout="wide"
)

# Get API key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]

# Create Groq client
client = Groq(api_key=api_key)

# App title
st.title("✍️ AI Grammar Checker")
st.write(
    "Correct grammar, improve writing, rewrite professionally, "
    "and explain grammar mistakes."
)

# Text input
text = st.text_area(
    "Enter your text",
    height=200,
    placeholder="Type your sentence here..."
)

# Check Grammar button
if st.button("Check Grammar"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        prompt = f"""
You are an expert English grammar teacher.

Analyze the following text carefully.

Return your answer in the following format:

## Grammar Corrected
(correct sentence)

## Improved Writing
(improved sentence)

## Professional Rewrite
(professional version)

## Grammar Mistakes
- List every mistake.

## Explanation
Explain each grammar mistake clearly.

## Grammar Rules
Mention the grammar rule used.

Text:
{text}
"""

        with st.spinner("Checking grammar..."):

            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.4
                )

                answer = response.choices[0].message.content

                st.success("Completed!")
                st.markdown(answer)
            except Exception as e:
                st.error("Groq API Error")
                st.exception(e)