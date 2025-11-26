# 🎯 YouTube → Blog Article Converter (Multi-Agent AI System)

[![GitHub Release](https://img.shields.io/github/v/release/raqibulratul-jpg/yt-blog-multiagent?color=brightgreen)](https://github.com/raqibulratul-jpg/yt-blog-multiagent/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/raqibulratul-jpg/yt-blog-multiagent?style=social)](https://github.com/raqibulratul-jpg/yt-blog-multiagent/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/raqibulratul-jpg/yt-blog-multiagent?style=social)](https://github.com/raqibulratul-jpg/yt-blog-multiagent/network/members)




A powerful AI multi-agent application that **converts YouTube videos into SEO-friendly blog articles**, using a structured workflow:

> Planner → Worker → Evaluator

🚀 Built for real-world automation  
📌 Perfect for creators, students & digital marketers  
🧠 Runs fully autonomously end-to-end  
📍 Deployable on Kaggle Notebook, Google Colab & HuggingFace Spaces  

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧠 Planner Agent | Extracts transcript & creates content generation plan |
| 📝 Worker Agent | Generates summary, SEO title, blog sections |
| 🔍 Evaluator Agent | Improves formatting & validates content quality |
| 🔑 SEO Optimization | Auto keyword extraction for better ranking |
| 🔗 YouTube Input | Just paste any YouTube URL |
| ⏰ Time Saver | Converts 10 min video → Blog in seconds |

---
## 🚀 Run in Google Colab

Open the Colab notebook and run the multi-agent YouTube → Blog converter with a single click 👇

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raqibulratul-jpg/yt-blog-multiagent/blob/main/YT_Blog_MultiAgent.ipynb)

## 🧠 Multi-Agent Architecture

```mermaid
flowchart LR
    A([User Input]) --> B[Planner Agent]
    B --> C[Worker Agent]
    C --> D[Evaluator Agent]
    D --> E((Output Blog Article))




## 🚀 How to Run

You can run the system in three ways:

### 1️⃣ Google Colab — No setup needed (Recommended)
Click the button and start using instantly 👇

➡️ **Open in Colab**  
> Upload a YouTube link → Get SEO-optimized blog article output ✨

### 2️⃣ Kaggle Notebook
Run in a GPU-enabled Kaggle environment.

### 3️⃣ Local Installation

```bash
git clone https://github.com/raqibulratul-jpg/yt-blog-multiagent.git
cd yt-blog-multiagent
pip install -r requirements.txt
python project/run_demo.py
