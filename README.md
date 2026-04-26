# BreakerPoints

Utility for extracting normalized mechanical coordinates from side-view
photographs of DIN rail circuit breakers.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
python breaker_points.py image.jpg output.csv
```

Click order:

* upper DIN rail corner
* lower DIN rail corner
* upper panel opening
* lower panel opening
* max upper point
* max forward point
* max lower point

## Install

```bash
git clone https://github.com/kesterlester/BreakerPoints.git
cd BreakerPoints
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python breaker_points.py examples/sample_breaker.png
```

