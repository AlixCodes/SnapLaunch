import sounddevice as sd
import numpy as np
import time
import webbrowser

URLS = [
    "YOUR LINKS HERE",
    "YOUR LINKS HERE" #add more with a comma
]

#adjust when needed
THRESHOLD = 0.08   
COOLDOWN = 5       

last_clap = 0

def callback(indata, frames, time_info, status):
    global last_clap

    volume = np.sqrt(np.mean(indata.astype(np.float32) ** 2))
    now = time.time()

    if volume > THRESHOLD and (now - last_clap) > COOLDOWN:
        print("SNAP DETECTED | volume =", round(volume, 3))
        for url in URLS:
            webbrowser.open(url)
        last_clap = now

with sd.InputStream(
    channels=1,
    samplerate=44100,
    blocksize=1024,
    callback=callback
):
    print("Welcome Sir, Listening for Snap...")
    while True:
        time.sleep(0.1)
