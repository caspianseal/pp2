import json

# Load JSON data from file
with open('sample-data.json') as f:
    data = json.load(f)

# Extract interface status data
interface_status = data['imdata']

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface status data
for status in interface_status:
    dn = status['l1PhysIf']['attributes']['dn']
    description = status['l1PhysIf']['attributes'].get('descr', '')
    speed = status['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = status['l1PhysIf']['attributes'].get('mtu', 'inherit')
    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))
