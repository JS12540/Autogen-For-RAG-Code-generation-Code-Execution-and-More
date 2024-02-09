import autogen

config_list = [
    {
        "model": "gpt-4",
        "api_key": "sk-YOUR-API-KEY"
    }
]

llm_config={
    "timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="Frontend Developer",
    llm_config=llm_config,
    system_message="You are an Expert Frontend Developer of tech company"
)

user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=6,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
You have to create an awesome frontend design which should be responsive that takes a pdf and calls the API: http://127.0.0.1:8000/process_pdf/. Response from backend API is in below format:

Backend API response:
[
  {
    "Type of Document": "Electricity Bill",
    "Name of Source Entity": "EDD I AZAMGARH",
    "Date of Document": "18-JAN-2024",
    "Name of Target Entity": "NIRMLA TIWARI",
    "FileName": "8513724591 1.pdf"
  }
]


Store the code in their proper format files. Do not run code , just store them in files
"""

user_proxy.initiate_chat(assistant, message=task)