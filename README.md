# Infrastrcture-Setup

`terrraform` directory contains the terraform code to spin up aws infrastrcutre for the proxy server. 

Backend is assumed to be hashicorp cloud, developers can change it accordingly.

`versions.tf` file can be modified to change the backend source as required.

`variables.tf` file can be modified to change
- aws region
- proxy port
- key pair name
- etc...

---------------

`deployment` directory contains python scripts to automate the deployment, initialisation and running of proxy server to the aws infrastructure.
