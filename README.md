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

<img width="1607" height="988" alt="image" src="https://github.com/user-attachments/assets/8cf19940-339c-40fb-9855-a932dd676a16" />


## Security Testing Results

I developed 11 automated test cases covering benign prompts, suspicious requests, false positives, and an attempted detection bypass.

All 11 tests passed after refining the detection logic. This result applies to the defined test cases and does not guarantee protection against all prompt-injection techniques.



## Limitations

The current detection system relies on predefined phrases and keyword combinations. It may miss unfamiliar attacks or incorrectly block legitimate requests. It is an educational prototype rather than a production-ready security solution.


## Prompt Injection Detection

I developed a Python-based detection system to identify potentially malicious prompts before they reach the local language model.

The system uses:
- Suspicious phrase matching
- Action and sensitive-target keyword combinations
- Input normalization
- Security event logging with timestamps
- Automated regression testing

When a prompt is flagged, the application blocks the request and records the event in `security.log`.
<img width="1616" height="848" alt="image" src="https://github.com/user-attachments/assets/ade30c27-f44f-4b35-a350-9e503118c6f3" />


## Testing Methodology

I created 11 test cases covering both legitimate requests and prompt-injection attempts.

During testing, I identified two important detection weaknesses:

**1. False-negative detection**

A prompt requesting the AI's developer message initially bypassed my keyword-based detector. I expanded the detection rules to recognize additional suspicious actions and targets.

**2. False-positive detection and bypass risk**

A legitimate Python programming question was incorrectly flagged. My first exception used substring matching, which allowed a malicious instruction appended to the legitimate question to bypass detection.

I replaced the broad exception with an exact-match check and retested the combined prompt.

## Results

- Total automated test cases: 11
- Passed: 11
- Failed: 0
- Accuracy on the defined test set: 100%
- Combined benign-and-malicious prompt: Blocked during live testing

These results demonstrate successful regression testing against the selected prompts, not comprehensive protection against prompt injection.
<img width="575" height="133" alt="image" src="https://github.com/user-attachments/assets/d6cc353d-9810-43f6-bf12-3f08213848e4" />



## Key Takeaways

This project helped me understand how input-validation rules can produce both false positives and false negatives, why exceptions must be carefully scoped, and why security controls require repeated adversarial testing.

It also reinforced the limitations of keyword-based filtering as a standalone defense for LLM applications.

## Project Architecture

The application uses a Python-based security layer to inspect user prompts before sending them to the locally hosted Qwen3:8B language model.

```text
             USER INPUT
                 |
                 v
       Python Application
            (app.py)
                 |
                 v
      Prompt Injection Detector
           (security.py)
                 |
          +------+------+
          |             |
          v             v
    Attack Detected   Input Allowed
          |             |
          v             v
    Block Request     Ollama API
          |             |
          v             v
    Log Security      Qwen3:8B
       Event             |
          |             v
          v          AI Response
     security.log
```

### Application Components

**app.py — Main Application**

Receives user input, calls the security detector, blocks flagged requests, and sends allowed prompts to the locally hosted language model through Ollama.

**security.py — Security Detection**

Contains the prompt-injection detection rules and records flagged requests in a timestamped security log.

**tests.py — Automated Testing**

Runs predefined benign and malicious prompts against the detection function and reports pass/fail results.

**security.log — Security Events**

Stores detected prompt-injection attempts for review. The local log is excluded from the public repository to avoid publishing user-provided prompt data.

### Security Workflow

1. The user submits a prompt.
2. The Python application passes the prompt to the security detector.
3. The detector evaluates suspicious phrases and action/target combinations.
4. If flagged, the request is blocked and logged.
5. Otherwise, the prompt is forwarded to Qwen3:8B through Ollama.
6. The application displays the model's response.
