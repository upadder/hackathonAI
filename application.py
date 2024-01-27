import streamlit as st
from streamlit_chat import message
from langchain.retrievers import AzureCognitiveSearchRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain.llms.openai import AzureOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os
import openai

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

def load_chain():
    prompt_template = """{context}  Question: {question}  Answer here:"""
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    retriever = AzureCognitiveSearchRetriever(content_key="content", top_k=10)

    llm = AzureOpenAI(deployment_name=AZURE_OPENAI_CHATGPT_DEPLOYMENT, temperature=0.7, openai_api_key=AZURE_OPENAI_KEY,verbose=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": PROMPT},
    )

    return chain



chain = load_chain()
print(chain)
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")

st.write("# Welcome to Stony Brook University Admissions Bot - WolfieBot ! 👋")
st.sidebar.success("Select a demo above.")
#st.header("Stony Brook University Admissions Bot")

st.markdown(""" 🌟 Welcome to Stony Brook University's WolfieBot! 🐺🤖

Hey future Seawolves! 🎓 Are you excited about exploring your journey at Stony Brook University? Meet WolfieBot, your friendly guide, powered by Azure Cognitive Intelligence, here to help you navigate the exciting world of college admissions! 🚀

🔍 **Ask Me Anything!** - WolfieBot is equipped to answer all your queries. From application deadlines to course options, financial aid, and campus life, I've got you covered! Just type in your question, and let me fetch the answers for you in a flash! ⚡

🧭 **Personalized Guidance** - Every student's journey is unique. WolfieBot is here to offer tailored advice that suits your individual needs and aspirations. Whether you're a first-year student, a transfer, or an international student, I'm here to ensure your path to Stony Brook University is smooth and clear. 🌏

📅 **Stay Up-to-Date** - Worried about missing important dates or deadlines? Fear not! I'll keep you informed about key admission dates, events, and deadlines. Stay on track with WolfieBot's reminders! 📆

💬 **Easy and Accessible** - Access me from your phone, tablet, or computer, anytime and anywhere. Whether you're at home or on the go, I'm just a click away! 💻📱

🤔 **Explore Stony Brook University** - Curious about campus life, clubs, or our academic programs? Ask away! I'm here to give you a glimpse into what makes Stony Brook University a fantastic place to learn, grow, and thrive. 🏫

🤝 **Supportive Community** - Join the Stony Brook family. I'm here not just to answer questions but to welcome you into our diverse and vibrant community. Let's embark on this exciting journey together! ❤️

Ready to get started? Just type in your question below and let the adventure begin with WolfieBot, your trusted companion on the road to becoming a Seawolf! 🐺💬
 """)

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ", "", key="input",placeholder = "Start chatting with WolfieBot! Enter your query..")
    return input_text


user_input = get_text()

if user_input:
    output = chain.run(question=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
