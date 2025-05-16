<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Telegram Onion Extractor - README</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 2rem;
      line-height: 1.6;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code {
      background-color: #eef;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: monospace;
    }
    pre {
      background: #272822;
      color: #f8f8f2;
      padding: 1rem;
      border-radius: 5px;
      overflow-x: auto;
    }
    .section {
      background: white;
      padding: 1.5rem;
      margin-bottom: 2rem;
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
  </style>
</head>
<body>

  <div class="section">
    <h1>Telegram Onion Link Extractor</h1>
    <p><strong>Goal:</strong> Extract hidden services (.onion links) from public Telegram messages using Telegram APIs and Python tools.</p>
  </div>

  <div class="section">
    <h2>🛠️ Prerequisites</h2>
    <ul>
      <li>Python 3.8+</li>
      <li>Telegram API credentials (from <a href="https://my.telegram.org">my.telegram.org</a>)</li>
      <li>Libraries: <code>telethon</code>, <code>re</code>, <code>pandas</code></li>
    </ul>
  </div>

  <div class="section">
    <h2>📦 Installation</h2>
    <pre><code>pip install telethon pandas</code></pre>
  </div>

  <div class="section">
    <h2>🚀 Step-by-Step Guide</h2>

    <h3>1. Setup Telegram API</h3>
    <pre><code>from telethon.sync import TelegramClient

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
client = TelegramClient('anon', api_id, api_hash)
client.start()</code></pre>

    <h3>2. Fetch Messages from a Channel</h3>
    <pre><code>from telethon.tl.functions.messages import GetHistoryRequest

channel = 'telegram_channel_username'
history = client(GetHistoryRequest(
    peer=channel,
    limit=100,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0
))</code></pre>

    <h3>3. Extract .onion Links using Regex</h3>
    <pre><code>import re

onion_links = []
pattern = r'https?://(?:[a-zA-Z0-9-]+\.)*onion(?:/[\w\-/]*)?'

for message in history.messages:
    matches = re.findall(pattern, message.message or "")
    onion_links.extend(matches)</code></pre>

    <h3>4. Export to CSV</h3>
    <pre><code>import pandas as pd

df = pd.DataFrame(onion_links, columns=['Onion Links'])
df.to_csv('extracted_onion_links.csv', index=False)</code></pre>
  </div>

  <div class="section">
    <h2>✅ Output</h2>
    <p>A CSV file named <code>extracted_onion_links.csv</code> containing all .onion URLs found in the messages.</p>
  </div>

  <div class="section">
    <h2>📌 Notes</h2>
    <ul>
      <li>This method only works on public or accessible channels you’re a member of.</li>
      <li>Ensure compliance with Telegram’s terms of use.</li>
    </ul>
  </div>

  <div class="section">
    <h2>📜 License</h2>
    <p>This project is for educational purposes only.</p>
  </div>

</body>
</html>
