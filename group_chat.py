import autogen

config_list = [
    {
        "model": "gpt-4",
        "api_key": "sk-YOUR-API-KEY"
    }
]

llm_config = {"config_list": config_list, "cache_seed": 52}

user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2, # The number of messages to look back for code execution. Default to 1.
        "work_dir": "groupchat",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config
)

pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(
    manager, message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software."
)