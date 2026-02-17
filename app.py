import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase


#Load enviroment variables

load_dotenv()

#Step 1 : Connect to Databricks

server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
http_path = os.getenv("DATABRICKS_HTTP_PATH")
access_token = os.getenv("DATABRICKS_ACCESS_TOKEN")


engine = create_engine(
    f"databricks+connector://token:{access_token}@{server_hostname}/default",
    connect_args={
        "http_path": http_path
    }
)

#create sql database obeject

db = SQLDatabase(engine)

# Step 2: Setup OpenAI llm

llm = ChatOpenAI(
    model="gpt-4o-mini", # cost effective & powerful
    temperature=0
    )

#Step 3: Create SQL Agent


agent_executor = create_sql_agent(
    llm =llm,
    db=db,
    agent_type="openai-tools",
    verbose=False
)


#step 4 : Ask question

while True:

    try:
        
        question = input("Please ask your question(or type 'exit' to quit): ")

        if question.lower() == 'exit':
            print("Bye..!")
            break

        response = agent_executor.invoke({"input": question})

        print("\n✅ Final Answer")
        print(response["output"])
    except:
        print("❌ Something went wrong, try again.")