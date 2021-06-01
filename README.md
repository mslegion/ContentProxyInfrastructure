# ContentProxyInfrastructure

`terrraform` directory contains the terraform code to spin up aws infrastrcutre for the proxy server. 
Backend is assumed to be hashicorp cloud, developers can change it accordingly.
Proxy server port is configured in variables.tf, modify values as needed.

`deployment` directory contains python scripts to automate the deployment, initialisation and running of proxy server to the aws infrastructure.
