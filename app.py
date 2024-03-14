import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,tool):

    ### LLama2 model
    # Ollama.set_api_key("1234567890")
    # Ollama.set_api_secret("<KEY>")
    # Ollama.set_api_version("v1")
    # Ollama.set_api_server("http://127.0.0.1:11434")
    # llm = Ollama(model="llama2")
    llm = Ollama(model="llama2", base_url="http://127.0.0.1:11434")
    response=llm.invoke("Tell me a joke")
    
    ## Prompt Template

    template="""
        Write a code for {tool} job profile for a requirement of {input_text}
        just give code sample to extract informatio.
            """
    
    prompt=PromptTemplate(input_variables=["code","tool","input_text"],
                          template=template)
    

    print(response)
    return response






st.set_page_config(page_title="Generate Code",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("ENBUILD 🤖")

tool=st.selectbox('Write',
                        ('Terraform','python','Java','Go','Shell','Powershell','C#','C++','Ruby','NodeJS','Perl','PHP','HTML','CSS','Javascript','Typescript','SQL','NoSQL','Docker','Kubernetes'),index=0)
input_text=st.text_input("code for")


submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,tool))
