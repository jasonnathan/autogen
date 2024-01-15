import autogen
config_list = [
  {
      
      # "api_key": "NULL",
      # "base_url": "http://localhost:1234/v1",
      "model": "gpt-4",
  }
]

llm_config = {
  "timeout": 600,
  "config_list": config_list, 
  "cache_seed": 42,
  "temperature": 0.4,
  }
user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
   human_input_mode="ALWAYS",
)
coder = autogen.AssistantAgent(
    name="Coder",
    system_message="A master coder specializing in Python programming language.",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Project_manager",
    system_message="Leverages open sourced libraries to implement new product ideas",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
user_proxy.initiate_chat(manager, message="create a custom tool for use in langchain to read and write to spreadsheet and save it to sheet.py")
