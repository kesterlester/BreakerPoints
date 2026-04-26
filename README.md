# BreakerPoints

Utility for extracting normalized mechanical coordinates from side-view
photographs of DIN rail circuit breakers.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
python breaker_points.py image.png [output.csv]

```

## Click order:

* upper DIN rail corner
* lower DIN rail corner
* upper panel opening
* lower panel opening
* max upper point
* max forward point
* max lower point

## Example usage:
For this input
```bash
python breaker_points.py examples/sample_breaker.png
```

expect approximately this output:

```bash
point,x_mm,y_mm
a_upper_din,-0.0,35.0
b_lower_din,-0.0,-0.0
c_upper_opening,41.221,38.45
d_lower_opening,40.285,-3.339
e_max_upper,21.292,55.995
f_max_forward,66.106,8.498
g_max_lower,20.212,-19.819
```


## Install

```bash
git clone https://github.com/kesterlester/BreakerPoints.git
cd BreakerPoints
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python breaker_points.py examples/sample_breaker.png
```

