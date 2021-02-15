# vcenter-esxi-connector
Connector for automation vmware vcenter and esxi  

Scripts on this repository are using vsphere-automation-sdk-python  
Please find the SDK from vmware/vsphere-automation-sdk-python repository on this link  
[vsphere-automation-sdk-python](https://github.com/vmware/vsphere-automation-sdk-python)  

For full reference about vSphere Automation SDK for Python documentation  
Please refer to vSphere Automation SDK for Python.’s documentation on this link  
[vSphere Automation SDK for Python documentation](https://vmware.github.io/vsphere-automation-sdk-python/vsphere/7.0.1.0/index.html)


## How to Use  

1. Clone this repository to your local  

2. Install requirements.  
    For requirements regarding vsphere automation sdk python please refer to [vsphere-automation-sdk-python](https://github.com/vmware/vsphere-automation-sdk-python). Find this command:  

        pip install --upgrade git+https://github.com/vmware/vsphere-automation-sdk-python.git  

    Other requirements can be found at requirements.txt  

3. Run the script. 

    On Linux  

        python3 vcenter_version.py  
        
    On Windows  

        python vcenter_version.py  

4. Output will be printed to .txt file
