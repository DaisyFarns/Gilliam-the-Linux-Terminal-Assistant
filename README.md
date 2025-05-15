# UNDER DEVELOPMENT NOT RELEASED YET USE AT OWN RISK
# It's like co-pilot for Linux, but doesn't suck, and instead of a pilot sitting beside you, they will instead be right inside your ass.
# Gilliam-the-Linux-Terminal-Assistant
# Gilliam is your trusted friend, not a root kit, even though it does kind of look like one. Don't however be fooled, it's like giving your machine over to ChatGPT, which will seamlessly intergrate with your terminal.
# System-Agent v0.1


## Overview

The **System-Agent** is a smart, AI-powered terminal agent designed to monitor and maintain your Linux system. It can run diagnostics, interact with system commands, troubleshoot errors, and even execute root-level fixes—after confirming your permission. Powered by **OpenAI's GPT-4**, the agent helps you solve complex system issues with ease.

---

## Features:
- **Real-time system health monitoring** (CPU, memory, disk usage).
- **Interactive error detection and troubleshooting** with GPT.
- **Root-level execution** with explicit user permission.
- **Flashy terminal output** with colorful animations and messages.
- **Smart command execution**, capable of suggesting and implementing fixes for errors.

---

## Prerequisites

Before running the System-Agent, ensure you have the following installed:
- **Python 3.x** (python3)
- **pip** (Python package manager)
- **psutil** (for system statistics)
- **openai** (for GPT-4 powered responses)

---

# 🤖 Gilliam: The Linux Terminal Assistant (v1.1 Python Fork)

> ⚠️ **WARNING:** This version is under active development. Use at your own risk, and preferably in a virtual environment or isolated shell environment.



Gilliam is your AI-powered, shell-integrated assistant built for hackers, coders, sysadmins, and digital outlaws. This Python-based fork introduces a modular core, CLI enhancements, and is designed for direct terminal usage—no web UI, no bullshit.

---

## 🚀 Features

- Natural language interaction in the terminal
- Shell command explanation and generation
- GPT-style responses using web or API access (configurable)
- Modular, extensible Python architecture
- Runs in Linux/macOS (WSL support included)

---

### 🐍 Requirements

- Python 3.8+
- `pip` package manager
- Git
- Unix-based shell (bash, zsh, etc.)

---

### 📥 Step-by-Step Install

1. **Clone the Repo**
```bash
git clone https://github.com/Hakkadex/Gilliam-the-Linux-Terminal-Assistant.git
cd Gilliam-the-Linux-Terminal-Assistant
```

2. **Set Up Python Environment**
(Recommended to avoid polluting your system)

```bash
python3 -m venv gillenv
source gillenv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, manually install core packages:
```bash
pip install openai rich requests
```

4. **Run the Assistant**
```bash
python3 terminal-agent.py
```

---

## ⚙️ Configuration (Optional)

- Edit `terminal-agent.py` or add `.env` for:
  - API keys (if using OpenAI)
  - Custom model
  - Proxy settings
  - Logging

---

## 🧪 Testing

Want to check if it's working?
Run:
```bash
python3 terminal-agent.py
```

Say something like:
```
Gilliam, show me how to make a bash function that kills Chrome.
```

---

## 📦 Dependencies & Setup

### Required Python Packages

The `terminal-agent.py` script depends on the following Python packages:

```
openai>=1.0.0
rich>=13.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

---

### Installing Dependencies

Place a file named `requirements.txt` in the root of the repo with the above packages listed. Then run:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries to run Gilliam smoothly.

---

### Optional: Environment Variables

For API keys and sensitive configs, create a `.env` file in the repo root with:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure your `.gitignore` excludes `.env` to keep secrets safe.

The script uses `python-dotenv` to load these variables automatically.

---

### Summary

1. Create `requirements.txt` with the dependency list.  
2. Run `pip install -r requirements.txt`.  
3. (Optional) Add `.env` with your API keys.  
4. Run `python3 terminal-agent.py` and watch the magic.

---

## 🛠️ Roadmap / To-Do

- TUI interface (curses or Rich)
- Offline model integration
- Plugin system
- Prompt customization per user shell
- Web socket CLI relay

---

## 🤝 Contributing

Pull requests welcome. Fork the repo, do your chaos, and send it up.

---

## 🧠 Credits

- Original Author: [Hakkadex](https://github.com/Hakkadex)
- Python Fork & Contributor: [DaisyFarns](https://github.com/DaisyFarns)
- Terminal Integration & Madness: Metal Knight

---

## ☠️ License

MIT. Use it, modify it, turn it into a war machine. Just don't blame us when it achieves sentience.

