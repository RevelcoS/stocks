# Stocks
This is a school flask project for stocks implementation.

![Index](https://raw.githubusercontent.com/RevelcoS/stocks/master/overview/index.png)
![Stocks](https://raw.githubusercontent.com/RevelcoS/stocks/master/overview/stocks.png)


## Installing
To install the server for Windows do the next steps. (Note: python3 is required)
1) Clone the repository by running the following command in shell (or download directly from github.com): 
```
git clone https://github.com/RevelcoS/stocks.git
```
2) Cd into the stocks directory and setup the environment:
```sh
py -3 -m venv env
```

**Step 3 must be done each time the new shell is opened**

3) Activate the environment. Notice, that (env) should appear at the start of command prompt.
```sh
env\Scripts\activate
```
4) Install the packages:
```sh
pip3 install -r requirements.txt
```
5) Setup environment variables
```sh
set FLASK_APP=stocks.py
```

When everything is done, run the server.
## Running
Before running the server, make sure that environment is activated (see the previous step).
To run the server, type the next command in shell:
```sh
python stocks.py
```
The next message should appear on the screen:
```sh
[18:15:18 INFO]: Starting Stocks App
```
The server runs on localhost http://127.0.0.1:5000/