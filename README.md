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
