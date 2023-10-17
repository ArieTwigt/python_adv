# RDW Data Exporter


## Initial setup

Steps:

* Create a virtual environment `virtualenv venv --python=python3.12`
* Activate the virtual environment: 
    * Windows: `venv\Scripts\activate`
    * Unix: `. venv/bin/activate`

* Install the required modules:
    * `pip install -r requirements.txt`

* Run the application
    * From the Debugger
    * or: `python main.py`


## Testing

`pytest -v --junitxml=report.xml`