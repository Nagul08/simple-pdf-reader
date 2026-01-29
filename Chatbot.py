from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras

load_dotenv()
llm = ChatCerebras(model="gpt-oss-120b")
print ("Yo Howdy")
while(q := input("You: ")) not in ["exit","quit","thats it brotha"]:
    print(f"Clanker: {llm.invoke(q).content}\n")
        