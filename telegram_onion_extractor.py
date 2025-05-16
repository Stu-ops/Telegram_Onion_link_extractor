import os
import re
import json
import asyncio
from datetime import datetime
from telethon import TelegramClient, events

# Telegram API credentials - you need to get these from my.telegram.org
API_ID = API_ID  
API_HASH = "API_HASH"  
CHANNEL_USERNAME = "toronionlinks"  
OUTPUT_FILE = "onion_links.json"
LAST_MESSAGE_ID_FILE = "last_message_id.txt"

# Regular expression to find .onion links
ONION_PATTERN = re.compile(r'https?://(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+onion(?:/[^\s]*)?')

async def extract_onion_links():
    # Initialize the Telegram client
    client = TelegramClient('onion_link_session', API_ID, API_HASH)
    try:
        await client.start()
        print("Connected to Telegram!")
        channel = await client.get_entity(CHANNEL_USERNAME)
        print(f"Found channel: {channel.title}")
        last_message_id = 0
        if os.path.exists(LAST_MESSAGE_ID_FILE):
            with open(LAST_MESSAGE_ID_FILE, 'r') as f:
                try:
                    last_message_id = int(f.read().strip())
                    print(f"Starting from message ID: {last_message_id}")
                except ValueError:
                    print("Invalid last message ID, starting from the beginning")
        messages = await client.get_messages(channel, limit=20)
        
        # Keep track of the highest message ID
        highest_message_id = last_message_id
        extracted_links = []
        for message in messages:
            if message.id <= last_message_id:
                continue
            if message.id > highest_message_id:
                highest_message_id = message.id
            if not message.text:
                continue

            onion_links = ONION_PATTERN.findall(message.text)
            
            for link in onion_links:
                link_entry = {
                    "source": "telegram",
                    "url": link,
                    "discovered_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "context": f"Found in Telegram channel @{CHANNEL_USERNAME}",
                    "status": "pending"
                }
                extracted_links.append(link_entry)
                print(f"Found .onion link: {link}")
        
        with open(OUTPUT_FILE, 'a') as f:
            for link_entry in extracted_links:
                f.write(json.dumps(link_entry) + '\n')
 
        if highest_message_id > last_message_id:
            with open(LAST_MESSAGE_ID_FILE, 'w') as f:
                f.write(str(highest_message_id))
                  
        print(f"Extracted {len(extracted_links)} .onion links from {CHANNEL_USERNAME}")
        print(f"Results saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.disconnect()
        print("Disconnected from Telegram")

if __name__ == "__main__":
    asyncio.run(extract_onion_links())

# pip uninstall telethon
