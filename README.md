# SnapLaunch

Opens selected websites when a sudden sound (snap/clap) is detected through the microphone.

## Setup

```bash
git clone https://github.com/AlixCodes/SnapLaunch.git
cd SnapLaunch
pip install -r requirements.txt
```

## Usage

1. Add your links:

```python
URLS = [
    "https://youtube.com",
    "https://google.com"
]
```

2. Run:

```bash
python main.py
```

## Config

* `THRESHOLD` → sensitivity to sudden sound spikes
* `COOLDOWN` → delay between triggers (seconds)

## Note

* Works on sudden sound spikes (snap/clap), not continuous noise
