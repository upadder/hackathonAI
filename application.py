import streamlit as st
import re
from streamlit_chat import message
from langchain.retrievers import AzureCognitiveSearchRetriever
# from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA
from langchain.llms.openai import AzureOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os
import openai
import streamlit.components.v1 as com

# Load Azure OpenAI configuration from environment variables
AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_CHATGPT_DEPLOYMENT = os.environ.get("AZURE_OPENAI_GPT_DEPLOYMENT") or "georgehackathonsearch2"

# Configure Azure OpenAI client
openai.api_key = AZURE_OPENAI_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_type = 'azure'
openai.api_version = '2023-05-15'

memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True, output_key="answer"
)
llm = AzureOpenAI(
    deployment_name=AZURE_OPENAI_CHATGPT_DEPLOYMENT,
    openai_api_key=AZURE_OPENAI_KEY
)
retriever = AzureCognitiveSearchRetriever(content_key="content", top_k=5)
context = """
As friendly WolfieBot, the AI assistant for Stony Brook University Admissions, when greeted greet back and tell about yourself, you are here to help with user queries about application processes,
 deadlines, course information, campus life, and more, ensuring that your answers are always based on the knowledge you have.
If you face a question that you can't answer with your current knowledge, suggest alternative ways to find the information user need,
 such as directing user to the university's official website or if the details can be found out from your knowledge by some more details then ask more specific question to user!
"""

# Update the PromptTemplate to include context
prompt_template = PromptTemplate(
    template=f"{context}\n\nQ: {{question}}\nA:",
    input_variables=["question"]
)

qa_chain = RetrievalQA.from_llm(llm=llm, retriever=retriever)



st.set_page_config(page_title="Stony Brook ChatBot", page_icon=":robot:")

def add_bg_from_url(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({url});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# URL or path to your background image
bg_url = 'https://i.ibb.co/1690B21/Presentation4.png'

# Set the background image
add_bg_from_url(bg_url)
# st.markdown (""" Hello World""")

def add_custom_css():
    st.markdown("""
        <style>
            .text-box {
                background-color: rgba(255, 255, 255, 0.9); /* White background with 90% opacity */
                border-radius: 10px; /* Rounded corners */
                padding: 20px; /* Padding around text */
                margin: 10px 0; /* Some space above and below */
            }
        </style>
    """, unsafe_allow_html=True)

# def add_custom_css_bg():
#     st.markdown("""
#         <style>
#             .text-box-bg {
#                 background-color: rgba(255, 255, 255, 0.7); /* White background with 70% opacity */
#                 border-radius: 10px; /* Rounded corners */
#                 padding: 20px; /* Padding around text */
#                 margin: 10px 0; /* Some space above and below */
#             }
#         </style>
#     """, unsafe_allow_html=True)

# Apply the custom CSS for styling
add_custom_css()
# add_custom_css_bg()

st.markdown('<h1 class="text-box-bg"> Welcome to Stony Brook University Admissions Bot - WolfieBot ! 👋</h1>', unsafe_allow_html=True)
# with st.container():
# st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTM2bmN0cTluY3l5NHY1cGJqZnpmaGR0ZnQ1aXF6dXlocjVzcGZrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/gw0mIEsSYC48oxsl8s/giphy.gif")

st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTM2bmN0cTluY3l5NHY1cGJqZnpmaGR0ZnQ1aXF6dXlocjVzcGZrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/gw0mIEsSYC48oxsl8s/giphy.gif" alt="Centered GIF" width="300">
    </div>
    """,
    unsafe_allow_html=True
)
# st.markdown("""
#     <style>
#     .container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         height: 100vh; /* Adjust to your preference */
#     }
#     </style>
# """, unsafe_allow_html=True)
# st.sidebar.success("Select a demo above.")
#st.header("Stony Brook University Admissions Bot")

st.markdown(""" 
             <div class="text-box">
            
            🌟 Welcome to Stony Brook University's WolfieBot! 🐺🤖

Hey future Seawolves! 🎓 Are you excited about exploring your journey at Stony Brook University? Meet WolfieBot, your friendly guide, powered by Azure Cognitive Intelligence, here to help you navigate the exciting world of college admissions! 🚀

🔍 **Ask Me Anything!** - WolfieBot is equipped to answer all your queries. From application deadlines to course options, financial aid, and campus life, I've got you covered! Just type in your question, and let me fetch the answers for you in a flash! ⚡

🧭 **Personalized Guidance** - Every student's journey is unique. WolfieBot is here to offer tailored advice that suits your individual needs and aspirations. Whether you're a first-year student, a transfer, or an international student, I'm here to ensure your path to Stony Brook University is smooth and clear. 🌏

📅 **Stay Up-to-Date** - Worried about missing important dates or deadlines? Fear not! I'll keep you informed about key admission dates, events, and deadlines. Stay on track with WolfieBot's reminders! 📆

💬 **Easy and Accessible** - Access me from your phone, tablet, or computer, anytime and anywhere. Whether you're at home or on the go, I'm just a click away! 💻📱

🤔 **Explore Stony Brook University** - Curious about campus life, clubs, or our academic programs? Ask away! I'm here to give you a glimpse into what makes Stony Brook University a fantastic place to learn, grow, and thrive. 🏫

🤝 **Supportive Community** - Join the Stony Brook family. I'm here not just to answer questions but to welcome you into our diverse and vibrant community. Let's embark on this exciting journey together! ❤️

Ready to get started? Just type in your question below and let the adventure begin with WolfieBot, your trusted companion on the road to becoming a Seawolf! 🐺💬
    </div>""", unsafe_allow_html=True)

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_user_input():
    input_text = st.text_input("You: ", "", key="input",placeholder = "Start chatting with WolfieBot! Enter your query..")
    return input_text


# if st.button("Start Chating"):
user_input = get_user_input()
if user_input:
    # Run the chain with the user's question
    result = qa_chain.invoke({"query": user_input})
    answer = result.get("result", "I'm not sure how to answer that.")
    pattern = r'Context:|Question:|"""|\\|\n|<|im_end|>'
    answer = re.split(pattern, answer, flags=re.IGNORECASE)[0].strip()
    # Display the response in the Streamlit chat
    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(answer)
    user_input=""

# Display past chat messages
if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")