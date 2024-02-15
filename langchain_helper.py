from dotenv import load_dotenv,find_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_community.llms import HuggingFaceHub

load_dotenv()

def generate_petname(animal_name,animal_color):
    repo_id = "google/flan-t5-xxl"
    llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.7, "max_length": 64}
        ) 
    prompt = PromptTemplate(
        input_variables=['animal_name','animal_color'],
        template="I have a {animal_name} pet and its color is {animal_color}, i want  a cool name for it. suggest me five cool names for my pet"
        )
    name = LLMChain(llm=llm,prompt=prompt,output_key='answer')
    response = name({'animal_name':animal_name,'animal_color':animal_color})
    return response


def langchain_Agent():
    repo_id = "google/flan-t5-xxl"
    llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.7, "max_length": 64}
        ) 
    tools = load_tools(["wikipedia","llm-math"],llm=llm)
    agent =initialize_agent(tools,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
    result = agent.run(
        "what is the avg age of dog? Multiply the age by 3"
    )    
    return result

if __name__ == '__main__':
    print(generate_petname("dog","black"))