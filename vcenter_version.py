# Sample script for generating vcenter version

import requests
import urllib3
from com.vmware.appliance.system_client import Version
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification
session.verify = False

# Disable the secure connection warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
f = open("output.txt", "w")
vsphere_client = create_vsphere_client(server="your_ip", username="your_username", password="your_password", session=session)

# Get vCenter version
vcenter_version = vsphere_client.appliance.system.Version.get()
print(vcenter_version)
f.write(str(vcenter_version))
f.close
