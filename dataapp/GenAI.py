from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI
key = "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"


def create_agent(file):
    agent = create_csv_agent(
        ChatOpenAI(temperature=0, model_name = "gpt-3.5-turbo", api_key=key),
        file,
        verbose = True,
        agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )
    return agent