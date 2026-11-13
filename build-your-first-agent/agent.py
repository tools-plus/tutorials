import json, os, urllib.request

MODEL = "nemotron-3-nano:4b"
SHOPS = json.load(open("shops.json"))   # which shop is which kind of spending

# The hands: normal Python functions
def list_receipts():
    return "\n".join(sorted(os.listdir("receipts")))

def read_receipt(file):
    return open(os.path.join("receipts", file)).read()

def add_numbers(numbers):
    return str(round(sum(numbers), 2))

def search_receipts(word):
    found = []
    for file in sorted(os.listdir("receipts")):
        text = read_receipt(file)
        if word.lower().rstrip("s") in (text + SHOPS.get(text.splitlines()[0], "")).lower():
            found.append(file + ": " + text.splitlines()[0] + ", total " + text.split("TOTAL")[1].split()[0])
    return "\n".join(found) or "no receipts match"
HANDS = {"list_receipts": list_receipts, "read_receipt": read_receipt, "add_numbers": add_numbers, "search_receipts": search_receipts}

# Tell the model which tools it may ask for
def tool(name, description, **params):
    return {"type": "function", "function": {"name": name, "description": description,
            "parameters": {"type": "object", "properties": params, "required": list(params)}}}

TOOLS = [tool("list_receipts", "List all receipt files"),
         tool("search_receipts", "Find receipts that contain a word, with totals", word={"type": "string"}),
         tool("read_receipt", "Read one receipt file", file={"type": "string"}),
         tool("add_numbers", "Add a list of amounts exactly", numbers={"type": "array", "items": {"type": "number"}})]

# The brain: one call to the model running on this laptop
def think(messages):
    body = json.dumps({"model": MODEL, "messages": messages, "tools": TOOLS, "stream": False, "think": False})
    reply = urllib.request.urlopen("http://localhost:11434/api/chat", body.encode())
    return json.load(reply)["message"]

# The loop: think, act, observe
messages = [{"role": "system", "content": "You track spending from receipt files. Use your tools. Never guess. Use search_receipts, then add_numbers for every total."},
            {"role": "user", "content": input("You: ")}]
while True:
    msg = think(messages)
    messages.append(msg)
    if not msg.get("tool_calls"):
        print("Agent:", msg["content"])
        break
    for call in msg["tool_calls"]:
        name, args = call["function"]["name"], call["function"]["arguments"]
        print("  tool:", name, args)
        messages.append({"role": "tool", "content": HANDS[name](**args)})