# 📧 Gmail Workflow Automation with Playwright + pytest-bdd

This project automates basic Gmail workflows using **Playwright**, **pytest**, and **pytest-bdd**. It includes three progressively complex test scenarios — from logging in and out, to sending emails, and adding attachments.

## Set up the project
1. Create and activate virtual environment(Recommended) 
2. Run: 'pip install -r requirements.txt'
3. Create.env file containing your google credentials and name these properties like this(replace asterisks with your values): 
    USERNAME=********
    PASSWORD=********
4. install playwright browsers by running: 'python -m playwright install'
5. Run the tests: 'pytest'

## Features

- ✅ Login and logout automation
- ✉️ Sending emails to contacts
- 📎 Sending emails with attachments
- 🔐 Secure credential handling via `.env`
- 🧪 Behavior-driven development using Gherkin syntax

---

## 📘 Scenarios

- root/features/emailAutomation.feature

## 📘 Steps definitions

- root/tests/test_emailAutomation.py

## TODO

Remove the static 1000 ms waits included in step creating email