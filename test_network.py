import json
import datetime
import time
import os

import pytz
import speedtest

x_servers = json.load(open("servers.json"))

threads = None
# If you want to use a single threaded test
# threads = 1

if not os.path.exists("data"):
    os.makedirs("data")

for _ in range(48):
    now_text = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).isoformat()
    
    print(f"{now_text} RUNNING...")
    
    s = speedtest.Speedtest()
    s.servers = x_servers
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads, pre_allocate=False)
    s.results.share()

    results_dict = s.results.dict()
    
    json.dump(results_dict, open(f"data/{now_text}.json", "w"), indent=2)
    
    print(f"{now_text} DONE...")
    
    # break
    time.sleep(20 * 60) # 20 minutes
    
    