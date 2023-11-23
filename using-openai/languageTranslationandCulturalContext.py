import autogen
# Define agent configurations
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)

# Define a function for dynamic conversationd
# Create an assistant agent for translation
    assistant_translator = autogen.AssistantAgent(
        name="assistant_translator",
        llm_config={
            "temperature": 0.7,
            "config_list": config_list,
        },
    )

# Create a user proxy agent representing the user
    user = autogen.UserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",
        code_execution_config={"work_dir": "user"},
    )123456bash

# Initiate a chat session with the 
#assistant for translation
    user.initiate_chat(assistant_translator, message=message)
    user.stop_reply_at_receive(assistant_translator)123bash

#Send a signal to the assistant for
#finalizing the translation
    user.send("Please provide a culturally sensitive translation.", assistant_translator)
    
# Return the last message received from the assistant return user.last_message()["content"]12345bash

# Create agents for the user and assistant
assistant_for_user = autogen.AssistantAgent(
    name="assistant_for_user",
    system_message="You are a language assistant. 
    Reply TERMINATE when the translation is complete.",
    llm_config={
        "timeout": 600,
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.7,
        "functions": [
            {
                "name": "translate_with_cultural_context",
                "description": "Translate and ensure 
                cultural sensitivity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "Text to translate 
                            with cultural sensitivity consideration."
                        }
                    },
                    "required": ["message"],
                }
            }
        ],
    }
)

# Create a user proxy agent representing the user
user = autogen.UserProxyAgent(
    name="user",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "user"},
    function_map={"translate_with_cultural_context": translate_with_cultural_context},
)

# Translate a sentence with cultural sensitivity
user.initiate_chat(
    assistant_for_user,
    message="Translate the phrase 
    'Thank you' into a language that shows respect in the recipient's culture."
)