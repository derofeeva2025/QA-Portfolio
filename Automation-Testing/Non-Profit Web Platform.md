# 🎭 Enterprise Web E2E & Visual Regression Suite

> **Playwright + TypeScript** automation suite for a **large-scale enterprise web platform** (client under NDA). Combines **visual regression testing** and **functional UI testing**.

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

---

## 📖 Overview

An automation suite built with **Playwright + TypeScript** for a **large-scale enterprise web platform** (client under NDA). The suite performs:

- 📸 **Visual regression testing** — captures screenshots from **prod** and **dev**, compares them pixel-by-pixel
- ✅ **Functional UI testing** — validates core pages, navigation, search, carousels, and forms

> ⚠️ **Confidentiality Notice:** Client name, URLs, and internal details are confidential (NDA). All examples are **anonymized**.

---

## 🎯 What It Does

### 📸 Visual Regression Testing
- Captures screenshots from **production** and **development** environments
- Compares them automatically to detect visual differences
- Highlights UI changes that may indicate bugs

### ✅ Functional Testing
- **Main pages** — verifies core page structure and content
- **Menu & Navigation** — checks all menu links work
- **Search** — validates search functionality
- **Carousels** — tests sliders and dynamic content
- **Forms** — validates inputs, validation, and submission

---

## 🛠 Tech Stack

| Category | Tools |
|----------|-------|
| **Automation** | Playwright |
| **Language** | TypeScript |
| **Visual Testing** | Playwright Screenshots / Pixelmatch |
| **CI/CD** | GitHub Actions |
| **Reporting** | Playwright HTML Report |
| **Version Control** | Git, GitHub |

---

## 📊 Results & Impact

| Metric | Before | After |
|--------|--------|-------|
| ⏱️ Regression runtime | ~40 min (manual) | **~4 min (automated)** |
| 🔁 Manual QA effort | 100% | **10%** |
| 🐛 Visual bugs caught | 0 | **15+ in first month** |
| 📸 Screenshots compared | 0 | **50+ per run** |

---

## 📂 Project Structure
enterprise-web-e2e-suite/
├── 📁 screenshots/ # Captured screenshots (prod vs dev)
├── 📁 reports/ # Test execution reports
├── 📁 scripts/ # Test scripts
│ ├── visual.spec.ts # Visual regression tests
│ ├── navigation.spec.ts # Menu & navigation tests
│ ├── search.spec.ts # Search tests
│ ├── carousel.spec.ts # Carousel tests
│ └── forms.spec.ts # Form tests
├── ⚙️ package.json
├── 📄 README.md
└── 🚫 .gitignore

📸 How Visual Regression Works
Capture — screenshots taken from prod and dev environments

Compare — Playwright compares images pixel-by-pixel

Report — differences highlighted in HTML report

Review — QA reviews changes and approves/rejects
