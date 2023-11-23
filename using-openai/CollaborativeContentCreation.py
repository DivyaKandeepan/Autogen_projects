# Import the openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# Create agents with LLM configurations
llm_config = {"config_list": config_list, "seed": 42}
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A content creator.",
    code_execution_config={"last_n_messages": 2, "work_dir": "content_creation"},
    human_input_mode="TERMINATE"
)
writer = autogen.AssistantAgent(
    name="Writer",
    llm_config=llm_config,
)

editor = autogen.AssistantAgent(
    name="Editor",
    system_message="An editor for written content.",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, writer, editor], messages=[], max_round=10)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Initiate the chat with the user as the content creator
user_proxy.initiate_chat(
  manager, 
  message="Write a 
short article about artificial
intelligence in healthcare."
)

# Type 'exit' to terminate the chat