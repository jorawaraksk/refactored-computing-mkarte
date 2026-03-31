#!/bin/bash

# Start lightweight Flask web server (needed for Render)
python3 web_alive.py &

# Start the Save Restricted Bot in the background
python3 bot.py &

# Start the Video Compressor Bot in the foreground
python3 -m bot
