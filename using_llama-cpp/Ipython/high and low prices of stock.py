import autogen
ipy_user = IPythonUserProxyAgent(
    "ipython_user_proxy",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get(
    "content", "").rstrip().endswith(
    "TERMINATE") or x.get("content", "").rstrip().endswith('"TERMINATE".'),
)
# the assistant receives a message from the user, which contains the task description
ipy_user.initiate_chat(
    assistant,
    message="""plot a stacked area chart
     visualizing the yearly high and low 
     prices of Apple (AAPL), Google 
     (GOOGL), Amazon (AMZN), and Microsoft (MSFT)
    use yfinance,matplotlib,pandas packages
    """,
)