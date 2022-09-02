# Movies-scraper


## Table of Content
- [Movies scraper](#movies-scraper)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [Author](#author)

## Tools
1. Python
2. BeautifulSoup
3. Streamlit 
4. Pytube



## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherif-abdallah/movies-scraper movies-scraper
```
* Install Python 3.8 venv, pip and compiler

```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd movies-scraper
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies: <br>
Go the `.env` file and Change  `DEBUG = True` `PRODUCTION = False`


* Finally run The Server
```sh
(venv)$ python -m streamlit run app.py
```
* And navigate to `http://127.0.0.1:8000`.

## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)
