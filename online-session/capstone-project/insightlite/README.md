# setup project.

0. make sure to be root folder of project. (`insightlite`)
1. create env named virtual env.
   - `python3 -m venv env`
2. active virtual env.
   - windows `env\Scripts\active`
   - linux/mac `source ./env/bin/active`
3. install dependencies/package
   - `pip install -r requirements.txt`

## HOW TO RUN

1. change directory to app folder
   - `cd app`
2. use uvicorn to run
   - `uvicorn main:app --reload --port 4000`

## if you want to train a ML model

1. update your input dataset.
   - open to file `app/ml_model/train.py`
   - update the input matrix `line:8`.
2. keep your current directory in terminal as
   - `app/ml_model/`
   - `python3 train.py`
   - it will automatically update `model.pkl` file.
