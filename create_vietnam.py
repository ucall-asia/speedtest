import json
import os
from re import X

import speedtest

x_servers = json.load(open("servers.json"))

total_servers = 0            
for key in x_servers:
    total_servers += len(x_servers[key])
print(total_servers)

s = speedtest.Speedtest()

speedtest_servers = s.get_servers()
 
append_counting = 0

for key, value in speedtest_servers.items():
    key = str(key)
    if value[0]["cc"] == "VN":
        if key not in x_servers:
            x_servers[key] = []
        else:
            x_servers[key] = x_servers[key]
        for server_obj in value:
            server_obj_host = server_obj["host"]
            exists_server = False
            for x_obj in x_servers[key]:
                if x_obj["host"] == server_obj_host:
                    exists_server = True
                    break 
            if not exists_server:
                x_servers[key].append(server_obj)
                append_counting += 1
    
total_servers = 0            
for key in x_servers:
    total_servers += len(x_servers[key])
                
print(f"Add more {append_counting} servers, and total servers is {total_servers}")
json_text = json.dumps(x_servers, indent=2)

with open("servers.json", "w") as file:
    file.write(json_text)
    file.close()