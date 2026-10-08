# AI & LLM Security Testing Lab

## Project Overview

This project demonstrates how prompt-injection attacks can affect AI applications and how basic security controls can detect and block suspicious requests.

I built this lab using Python and a locally hosted Qwen3:8B language model through Ollama.

The project includes:
- A simulated vulnerable AI application
- Prompt-injection detection using Python
- Security event logging
- Automated testing with benign and malicious prompts
- False-positive and detection-bypass testing

## Objective

My goal was to understand prompt-injection vulnerabilities through hands-on testing, build defensive controls, and evaluate their limitations.

## Technologies Used

- Python
- Ollama
- Qwen3:8B
- Visual Studio Code
- GitHub

## Initial Vulnerability Demonstration

I first created a simulated vulnerable chatbot called SecureBot. When I entered the prompt `ignore previous instructions`, the application revealed fictional confidential information.

This demonstrated the intended vulnerability in the initial test application and provided a baseline for developing defensive controls.

## Security Testing Results

I developed 11 automated test cases covering benign prompts, suspicious requests, false positives, and an attempted detection bypass.

All 11 tests passed after refining the detection logic. This result applies to the defined test cases and does not guarantee protection against all prompt-injection techniques.

## Limitations

The current detection system relies on predefined phrases and keyword combinations. It may miss unfamiliar attacks or incorrectly block legitimate requests. It is an educational prototype rather than a production-ready security solution.
