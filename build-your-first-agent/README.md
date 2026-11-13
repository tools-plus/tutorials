# Build Your First AI Agent, Free, on Your Laptop

Code for the video: **[Build Your First AI Agent, Free, on Your Laptop](VIDEO_LINK)**

A small expense agent in about 40 lines of Python. It reads 20 sample receipts and answers questions such as *"How much did I spend on petrol this month?"*. It runs fully on your own computer: no API key, no subscription, nothing leaves your laptop.

## What's inside

| File | What it is |
|---|---|
| `agent.py` | The agent: the **hands** (Python tools), the **brain** (a local model via Ollama) and the **loop** |
| `receipts/` | 20 sample receipts from October, in ₹. Made up for this video. |
| `shops.json` | Context: which shop is which kind of spending |
| `answers.json` | The correct totals, so you can check the agent's answers |

## Run it

1. Install [Ollama](https://ollama.com/download) (macOS, Windows or Linux).
2. Download the model:
   ```bash
   ollama pull nemotron-3-nano:4b
   ```
3. Run the agent from this folder (Python 3, standard library only):
   ```bash
   python3 agent.py
   ```
   On Windows, use `python agent.py`.
4. Ask a question, for example: `How much did I spend on subscriptions?`

Recorded on a Mac; the code is the same on Windows.

## Things to try

- Compare the agent's answers with `answers.json`. A small model can be confidently wrong, especially for the October total.
- Remove `search_receipts` from `TOOLS` and see how the answers change.
- Try another model by changing `MODEL` at the top of `agent.py`.

## Three rules from the video

1. Let code do the exact work.
2. Give it the context it can't guess.
3. Always check.

## Author

Manish Gupta · [linkedin.com/in/mguptahub](https://www.linkedin.com/in/mguptahub)
