# 🎯 YouTube → Blog Article Converter (Multi-Agent AI System)

[![GitHub Release](https://img.shields.io/github/v/release/raqibulratul-jpg/yt-blog-multiagent?color=brightgreen)](https://github.com/raqibulratul-jpg/yt-blog-multiagent/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/raqibulratul-jpg/yt-blog-multiagent?style=social)](https://github.com/raqibulratul-jpg/yt-blog-multiagent/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/raqibulratul-jpg/yt-blog-multiagent?style=social)](https://github.com/raqibulratul-jpg/yt-blog-multiagent/network/members)


<p align="center">

  <img src="https://img.shields.io/badge/Python-3.10-blue" />
  <img src="https://img.shields.io/github/last-commit/raqibulratul-jpg/yt-blog-multiagent" />
  <img src="https://img.shields.io/github/stars/raqibulratul-jpg/yt-blog-multiagent?style=social" />
  <img src="https://img.shields.io/github/forks/raqibulratul-jpg/yt-blog-multiagent?style=social" />
  <img src="https://img.shields.io/github/license/raqibulratul-jpg/yt-blog-multiagent" />

</p>

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
    A(User Input) --> B(Planner Agent)
    B --> C(Worker Agent)
    C --> D(Evaluator Agent)
    D --> E(Output Blog Article)
