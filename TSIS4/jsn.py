import json

with open("sample-data.json") as file:
    data = json.load(file)

print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in data["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"] + "  \t"*7 +
          i["l1PhysIf"]["attributes"]["speed"] + "   "+ i["l1PhysIf"]["attributes"]["mtu"])
