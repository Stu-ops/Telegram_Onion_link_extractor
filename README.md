<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Telegram Onion Extractor – Step-by-Step Guide</title>
  <style>
    /* Basic reset & layout */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f5f5f5;
      color: #333;
      line-height: 1.6;
      padding: 2rem;
    }
    .container {
      max-width: 800px;
      margin: auto;
      background: #fff;
      padding: 2rem 2.5rem;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    /* Title */
  h1 {
      text-align: center;
      margin-bottom: 0.5rem;
      font-size: 2rem;
      color: #2c3e50;
    }
    h2.subtitle {
      text-align: center;
      margin-bottom: 2rem;
      font-size: 1.2rem;
      color: #666;
    }

    /* Steps numbering */
  ol.steps {
      counter-reset: step-counter;
      list-style: none;
    }
    ol.steps > li {
      counter-increment: step-counter;
      margin-bottom: 1.5rem;
      padding-left: 2.5rem;
      position: relative;
    }
    ol.steps > li::before {
      content: counter(step-counter);
      position: absolute;
      left: 0;
      top: 0;
      width: 2rem;
      height: 2rem;
      background: #2c3e50;
      color: #fff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
    }
    ol.steps h3 {
      margin-bottom: 0.5rem;
      color: #2c3e50;
      font-size: 1.1rem;
    }

    /* Lists inside steps */
  ul {
      margin: 0.5rem 0 1rem 1.5rem;
    }
    ul li {
      margin-bottom: 0.3rem;
    }

    /* Code blocks */
  pre {
      background: #272822;
      color: #f8f8f2;
      padding: 1rem;
      border-radius: 5px;
      overflow-x: auto;
      margin: 0.5rem 0 1rem;
    }
    code {
      font-family: monospace;
      background: #eef;
      padding: 2px 4px;
      border-radius: 3px;
    }

    /* Footer notes */
  .notes {
      font-size: 0.9rem;
      color: #555;
      margin-top: 2rem;
    }
    .notes ul {
      margin-left: 1.5rem;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Telegram Onion Extractor</h1>
    <h2 class="subtitle">Step-by-Step Implementation Guide</h2>

  <ol class="steps">
      <li>
        <h3>Prerequisites</h3>
        <ul>
          <li>Python 3.8 or higher</li>
          <li>Telegram API credentials from <a href="https://my.telegram.org" target="_blank">my.telegram.org</a></li>
          <li>Libraries: <code>telethon</code>, <code>re</code>, <code>pandas</code></li>
        </ul>
      </li>

  <li>
        <h3>Installation</h3>
        <pre><code>pip install telethon pandas</code></pre>
      </li>

  <li>
        <h3>1. Setup Telegram API</h3>
        <pre><code>from telethon.sync import TelegramClient

api_id   = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

client = TelegramClient('anon', api_id, api_hash)
client.start()</code></pre>
      </li>

  <li>
        <h3>2. Fetch Messages from a Channel</h3>
        <pre><code>from telethon.tl.functions.messages import GetHistoryRequest

channel = 'telegram_channel_username'
history = client(GetHistoryRequest(
    peer       = channel,
    limit      = 100,
    offset_date= None,
    offset_id  = 0,
    max_id     = 0,
    min_id     = 0,
    add_offset = 0,
    hash       = 0
))</code></pre>
      </li>

  <li>
        <h3>3. Extract .onion Links with Regex</h3>
        <pre><code>import re

onion_links = []
pattern     = r'https?://(?:[a-zA-Z0-9-]+\.)*onion(?:/[\w\-/]*)?'

for msg in history.messages:
    text = msg.message or ""
    matches = re.findall(pattern, text)
    onion_links.extend(matches)</code></pre>
      </li>

<li>
        <h3>4. Export to CSV</h3>
        <pre><code>import pandas as pd

df = pd.DataFrame(onion_links, columns=['Onion Links'])
df.to_csv('extracted_onion_links.csv', index=False)</code></pre>
      </li>
    </ol>

  <div class="notes">
      <p><strong>Output:</strong> A file named <code>extracted_onion_links.csv</code> with all discovered .onion URLs.</p>
      <p><strong>Notes:</strong></p>
      <ul>
        <li>Only works on public or joined channels.</li>
        <li>Follow Telegram’s Terms of Service.</li>
      </ul>
      <p><strong>License:</strong> For educational purposes only.</p>
    </div>
  </div>

</body>
</html>
