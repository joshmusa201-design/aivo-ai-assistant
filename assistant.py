# i would be creating a siri, a voice assistant that can help you do some specific taxs yh.
import requests
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import subprocess 
from tavily import TavilyClient
import pyautogui
import time

# loading the apikey.
load_dotenv()



# using tavily api to get the lattest news on the internet.
def web_search(query: str):
    tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
    response = tavily_client.search(query)
    return response


def current_weather(baby:str, village):
    # give me the current weather of a city and place
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": baby,
        "country": village,
    }
    api_call = requests.get(url, params=params) 
    searched = api_call.json()
    filter = searched["results"][0]
    latitude = filter["latitude"]
    longitude = filter["longitude"]
    timezone = filter["timezone"]
    urlu = "https://api.open-meteo.com/v1/forecast"
    params = {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
            "current": 
            ["temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "weather_code"
            ],
        }
    results = requests.get(urlu, params=params)
    j_son_result = results.json()
    current = j_son_result["current"] 
    temperature = f"Temperature: {current["temperature_2m"]}℃"
    humidity = f"Humidity: {current["relative_humidity_2m"]}%"
    wind = f"Wind speed: {current["wind_speed_10m"]}km/h"
    return temperature + humidity + wind
        
    
# create a folder in the system
def create_folder(folder_name, folder_location):
    folder = Path.home() / folder_location / folder_name
    folder.mkdir(exist_ok=True)
    
# open a file in the directory
def open_file(directory, name_file, home_path=Path.home()):
    name = home_path / directory / name_file

    with open(name, "r") as f:
        return subprocess [f.read()]

# to create a file a file in any of the directoriies
def create_file(folder, file_name, home_folder=Path.home()):
    file = home_folder / folder / file_name
    file.touch()
    
# to open any app in the system
def open_apps(app_name: str):
    that = pyautogui.press("win")
    time.sleep(2)
    we = pyautogui.write(app_name, interval=0.1)
    fuck = pyautogui.press("enter")

# to write to any file in any of the directories in the system as long as the directory and file exists
def write_file(f_name, content, fold_name, obs=Path.home()):
    file = obs / fold_name / f_name
    file.write_text(content)

    if file.exists() == True:
        return "task completed succesfully"
    else:
        return "the folder does not exist does not exist"

# to help me manage my time
#def calender():
    #open my calender and help me access and schedule my calender
    #pass

# Defining the function schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Get the lattest information on the internet",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string", 
                        "description": "information to search for in the internet"
                    },
                },
                "required": ["query"],
                "additionalProperties": False, # strict mode requirement
            },
            "strict": True # set to strict mode.
        },
    },

    {
        "type": "function",
        "function": {
            "name": "current_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "baby": {
                        "type": "string",
                        "description":"this is the city or village to search for",
                    },
                    "village": {
                        "type": "string",
                        "description": "this is the country or the state the village or city is in"
                    },
                },    
                "required": ["baby", "village"],
                "additionalProperties": False # strict mode requirement
            },
            "strict": True # set to strict mode
        },
    },

    {
        "type": "function",
        "function": {
                "name": "create_folder",
                "description": "Creates a new folder in the specified location on the user's computer. Use this tool when the user explicitly asks to create or make a new folder",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "folder_name": {
                            "type": "string", 
                            "description": "The name the user wants to give the new folder."
                        },
                        "folder_location":{
                            "type": "string",
                            "description": "The location where the new folder should be created, relative to the user's home directory, such as Desktop, Documents, Downloads, or another folder."
                        },
                    },
                    "required": ["folder_name", "folder_location"],
                    "additionalProperties": False, # strict mode requirement},
                },
                "strict": True # set to strict mode.
        },
    },

    {
        "type": "function",
        "function": {
            "name": "open_file",
            "description": "Open and read the contents of a file from a specified directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "The directory/location where the file is stored. e.g Desktop/pile"
                    },
                    "name_file": {
                        "type": "string",
                        "description": "The name of the file to open and read. e.g notes.txt"
                    }
                },
                "required": ["directory", "name_file"],
                "additionalProperties": False
            },
            "strict": True
        },
    },

    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Create a new file with the specified name inside a specified folder.",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder": {
                        "type": "string",
                        "description": "The path to the folder where the new file should be created. e.g Desktop/josh"
                    },
                    "file_name": {
                        "type": "string",
                        "description": "The name of the file to create, including its file extension if needed."
                    },
                },
                "required": ["folder", "file_name"],
                "additionalProperties": False
            },
            "strict": True
        },
    },

    {
         "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write the specified content to a file inside a specified folder",
            "parameters": {
                "type": "object",
                "properties": {
                    "f_name": {
                        "type": "string", 
                        "description": "The name of the file to write to, including its file extension if needed"
                    },
                    "content": {
                        "type": "string",
                        "description": "The text content to write into the file",
                    },
                    "fold_name": {
                        "type": "string",
                        "description": "The path to the folder containing the file."
                    },
                },
                "required": ["f_name", "content", "fold_name"],
                "additionalProperties": False, # strict mode requirement
            },
            "strict": True # set to strict mode.
        },
    },

    
    {
         "type": "function",
        "function": {
            "name": "open_apps",
            "description": "Launch an application on the user's computer when they ask to open or start an app. Use this tool when the user wants to launch a supported application, e.g Spotify, Notepad, Calculator, etc.....",
            "parameters": {
                "type": "object",
                "properties": {
                   "app_name":{
                       "type": "string",
                       "description": "The name of the application the user wants to launch, e.g Spotify, Notepad, Calculator, etc...",
                    }, 
                },
                "required": ["app_name"],
                "additionalProperties": False, # strict mode requirement
            },
            "strict": True # set to strict mode.
        },
    },
]

# Using a model from hugging face.

user_prompt = input("Ask Me Anything: ")

client = InferenceClient(
    provider="auto",
    api_key=os.environ["HF_TOKEN"],
)

messages=[
        {
            "role": "system", 
            "content": "you are a helpful assistant"
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
# giving the model the message and making it aware of the tools i have
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V4.1-Flash",
    messages=messages,
    tools= tools,
    tool_choice="auto"
)


joshua = completion.choices[0].message
message_content = completion.choices[0].message.content

come = joshua.tool_calls

#print("MIXED MESSAGES:", joshua)
#print()
#print("CONTENT:", message_content)
#print()
#print("TOOL COOL:", come)


# Check if model wants to call functions
if come:
    # Add assistant's response to messages
    messages.append(joshua)

    # Process each tool call
    for tool_call in come:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        # Execute the function
        if function_name == "web_search":
            result = web_search(function_args["query"])
        elif function_name == "current_weather":
            result = current_weather(function_args["baby"], function_args["village"])
        elif function_name == "create_folder":
            result = create_folder(function_args["folder_name"], function_args["folder_location"])
        elif function_name == "open_file":
            result = open_file(function_args["directory"], function_args["name_file"])
        elif function_name == "create_file":
            result = create_file(function_args["folder"], function_args["file_name"])
        elif function_name == "write_file":
            result = write_file(function_args["f_name"], function_args["content"], function_args["fold_name"])
        elif function_name == "open_apps":
            result = open_apps(function_args["app_name"])
        
        # Add function result to messages
        messages.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": function_name,
            "content": json.dumps(result),
        })
            
#Get final response with function results
final_response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-0528",
    messages=messages,
)
reason =  final_response.choices[0].message.content
print("FINAL INFORMATION", reason)

for tool_call in come:
    print("TOOL CALLS:", tool_call)
    god_did = json.loads(tool_call.function.arguments)
    print("json load:", god_did) 
print()                         
print("MESSAGES_LIST:", messages)


