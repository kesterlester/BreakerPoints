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
python breaker_points.py examples/default.png
```

expect approximately this output:

```bash
a_upper_din_x_mm,a_upper_din_y_mm,b_lower_din_x_mm,b_lower_din_y_mm,c_upper_opening_x_mm,c_upper_opening_y_mm,d_lower_opening_x_mm,d_lower_opening_y_mm,e_max_upper_y_mm,f_max_forward_x_mm,g_max_lower_y_mm
-0.0,35.0,0.0,0.0,43.817,41.412,45.019,-3.874,60.916,64.256,-32.996
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

## See also example data:

https://docs.google.com/spreadsheets/d/14H9yaAH8xREWJ71rreWgcpF8mjq-DGHhI8DOZ1dkf-s/edit?usp=sharing


