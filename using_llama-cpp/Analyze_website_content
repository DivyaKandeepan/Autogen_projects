import autogen

# Define agent configurations
config_list = [
    {
        "model": "Llama-2-7B-GGUF",
        "api_base": "http://127.0.0.1:8000/v1",
        "api_type": "open_ai",
        "api_key": "NULL",  # Placeholder
    }
]

agent_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0.5,
    "request_timeout": 2000,
}

# Create agents for website analysis
reader_agent = autogen.AssistantAgent(
    name="ReaderAgent",
    llm_config=agent_config,
    system_message="ReaderAgent. Extract and summarize website content.",
)

analyzer_agent = autogen.AssistantAgent(
    name="AnalyzerAgent",
    llm_config=agent_config,
    system_message="AnalyzerAgent. Analyze and provide insights based on the extracted content.",
)

user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir":"coding"},
)

# Create a chat group for the website analysis
website_analysis_group = autogen.GroupChat(
    agents=[reader_agent, analyzer_agent, user_proxy],
    messages=[],
    max_round=50,
)

# Create a group chat manager
chat_manager = autogen.GroupChatManager(groupchat=website_analysis_group, llm_config=agent_config)

# Initiate the website analysis session
user_proxy.initiate_chat(
    chat_manager,
    message="""Please analyze the content of this website: https://llama-cpp-python.readthedocs.io/en/latest/ """,
)




#
