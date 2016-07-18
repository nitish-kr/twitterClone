    
    
      _                _   _     _                    ____   _                        
     | |_  __      __ (_) | |_  | |_    ___   _ __   / ___| | |   ___    _ __     ___ 
     | __| \ \ /\ / / | | | __| | __|  / _ \ | '__| | |     | |  / _ \  | '_ \   / _ \
     | |_   \ V  V /  | | | |_  | |_  |  __/ | |    | |___  | | | (_) | | | | | |  __/
      \__|   \_/\_/   |_|  \__|  \__|  \___| |_|     \____| |_|  \___/  |_| |_|  \___|
                                                                                      


--

### Setup

#### Pre-requisites:

Install python dev tools & virtualenv

```
sudo apt-get install python-pip python-dev build-essential
```

```
sudo pip install virtualenv
```


Install mysql-server and mysql-client

```
sudo apt-get install mysql-server mysql-client
```


#### Setup twitterClone

Pull the code and edit config

```
git clone https://github.com/nitish-kr/twitterClone
```

```
cp config.py.sample config.py
```


Make virtual env and install dependencies

```
cd twitterClone
```

```
virtualenv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.lock
```

Run flask app

```
python main.py
```

Visit __http://127.0.0.1:5000__

--
