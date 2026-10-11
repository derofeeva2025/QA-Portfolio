# Job Vacancy Alert Bot

> Automated Telegram bot that monitors **7+ job boards** for remote roles and sends new vacancies within minutes of publication.

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Telegram](https://img.shields.io/badge/Telegram_Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![Claude AI](https://img.shields.io/badge/Claude_AI-D97757?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai/)

---

## Overview

A Python bot that monitors **multiple job boards** for **remote roles** and delivers new vacancies to a **Telegram channel** within minutes of publication.

Built with **Claude AI** as a coding assistant — I defined the requirements, tested the results, and iterated on filters and message format.

---

## Key Features

- **Multi-source monitoring** — 7+ job boards (RSS + JSON APIs)
- **Fast delivery** — new vacancies sent to Telegram within minutes
- **Smart filtering** — removes duplicates, filters out junior-level roles
- **Structured messages** — company, location, salary, tech stack, requirements, responsibilities, apply link, careers page link
- **Fault-tolerant** — per-source error handling; one broken feed never stops the others
- **Scheduled** — runs automatically via GitHub Actions (cron)

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python |
| Scheduling | GitHub Actions (cron) |
| Delivery | Telegram Bot API |
| Data Sources | RSS feeds, open JSON APIs |
| Version Control | Git, GitHub |
| AI Assistant | Claude AI |

---

## How It Works

1. **Trigger** — GitHub Actions runs the bot on a cron schedule
2. **Fetch** — the bot reads RSS feeds and JSON APIs from `feeds.json` and `careers.json`
3. **Deduplicate** — already-sent vacancies are filtered out using `seen.json`
4. **Filter** — junior-level roles are excluded
5. **Format** — each vacancy becomes a structured Telegram message
6. **Send** — the message is delivered to a Telegram channel via Bot API

<img width="233" height="248" alt="Screenshot 2026-10-11 at 7 46 19 PM" src="https://github.com/user-attachments/assets/fe0262e0-79e5-44fd-bfed-2b55ea916ef8" />
Author - Daria Y. — QA, PM, AI Services - LinkedIn: [daria-y-5a319332](https://www.linkedin.com/in/daria-y-5a319332/)
