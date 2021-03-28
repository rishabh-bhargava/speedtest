# speedtest
Running Internet speed tests on a machine. There are a couple of use cases:
* Checking Internet speeds on machines in the cloud
* Checking Internet speeds at home so you can provide real data to your shitty Internet Service Provider

# Requirements
Install using `pip`:
```bash
pip install -r requirements.txt
```

# How to run
Run the following command:
```bash
python main.py
```

This will run in the foreground (as of now) and store data in the format `<timestamp>|<download_speed>|<upload_speed>` in log files of the format `speedtest_results.<timestamp>.log`. The logs are going to rotate every hour. Other notes:
* `timestamp` is in UTC
* `download_speed` and `upload_speed` are in bits/second