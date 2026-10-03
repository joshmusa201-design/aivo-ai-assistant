# Jarvis 🎙️

A local voice AI assistant inspired by Jarvis.

Jarvis listens for **"Hey Jarvis"**, converts your voice into text, sends it to an AI model, uses tools when necessary, and speaks the response back to you.

## ✨ Features

* 🎙️ Wake-word detection with **OpenWakeWord**
* 🗣️ Speech-to-text with **PyWhisperCpp**
* 🤖 AI tool/function calling
* 🌐 Internet search
* 🌤️ Current weather
* 📁 Create folders and files
* 💻 Open applications
* 🔊 Text-to-speech with **pyttsx3**

## 🧠 How It Works

```text
"Hey Jarvis"
      ↓
OpenWakeWord
      ↓
SoundDevice
      ↓
PyWhisperCpp
      ↓
AI Model
      ↓
Tool Calling (if needed)
      ↓
Python Function
      ↓
AI Response
      ↓
pyttsx3
      ↓
🔊 Jarvis speaks
```

The AI model decides whether a tool is needed. If it is, it provides the parameters required by the function. The Python program then executes the function and returns the result to the model.

## 🛠️ Technologies

* Python
* OpenWakeWord
* SoundDevice
* PyWhisperCpp
* Hugging Face Inference API
* Tavily
* Open-Meteo
* pyttsx3
* PyAutoGUI
* Requests

## 🚀 Run It

Install the dependencies:

```bash
pip install -r requirements.txt
```

Add your required API keys to `.env`, then run:

```bash
python your_file.py
```

Say:

> **"Hey Jarvis"**

## 📚 What I Learned

This project taught me how to connect **audio, speech recognition, AI models, tool/function calling, APIs, and text-to-speech** into one working system.

I also learned more about **CPU vs GPU inference**. My attempted GPU setup wasn't suitable for my hardware, while CPU inference for speech recognition was significantly slower.

Most importantly, I learned how AI tool/function calling works: the model doesn't directly execute my Python functions. It provides the tool name and the parameters needed, and my program executes the actual function.

## 🔮 Future Improvements

* Continuous conversations
* Better voice interaction
* More tools 
* Faster inference
* Better error handling
* Memory
  
## Demo_Jarvis🎥 

https://github.com/user-attachments/assets/6b619a41-45e2-4847-a774-5b9460131d87




  

