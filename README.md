## python-mouse-capture
Simple example showing mouse events record and play

### Initiate and set up the python virtual environment
- python -m venv .venv
- source .venv/Scripts/activate
- python -m pip install --upgrade pip

### Install mouse package
- pip install -r requirements.txt

### Run capture 
- python capture_mm.py
- - click around and finally right click to end capture
- - This creates the mouse event file  

### Run
- python run_mm.py
- - This loads the mouse event file and plays the mouse movement and click events recorded from `capture_mm.py`

### See
- https://pypi.org/project/mouse/
- https://github.com/boppreh/mouse#api
- https://github.com/boppreh/mouse#mouse.record
