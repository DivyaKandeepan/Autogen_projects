import autogen

# Define agent configurations
config_list = [
    {
        "model": "codellama-7b-instruct.Q5_K_M.gguf",
        "api_base": "http://127.0.0.1:8000/v1",
        "api_type": "open_ai",
        "api_key": "NULL",  # Placeholder
    }
]

agent_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0.5,
    "request_timeout": 4200,
}

# Create agents with different roles and configurations
coding_mentor = autogen.AssistantAgent(
    name="CodingMentor",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.7,
        "request_timeout": 1200,
    },
    system_message="Coding Mentor here! I can guide you through implementing algorithms in Python that student asked to explain.",
)

algorithm_expert = autogen.AssistantAgent(
    name="AlgorithmExpert",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.7,
        "request_timeout": 1200,
    },
    system_message="Algorithm Expert. I specialize in algorithms. i will explain how the algorithm works.",
)

student = autogen.UserProxyAgent(
    name="Student",
    human_input_mode="ALWAYS",
    code_execution_config={"work_dir":"node"},
)
team_groupchat = autogen.GroupChat(
    agents=[coding_mentor,algorithm_expert,student],
    messages=[],
    max_round=10,
)

# Create a GroupChatManager for the "team" groupchat
team_manager = autogen.GroupChatManager(groupchat=team_groupchat, llm_config=agent_config)

# Initiate the chat within the "team" groupchat
student.initiate_chat(
    team_manager,
    message="""I'm learning about sorting algorithms in Python and would like some guidance on implementation. Can you help me?""",
)
