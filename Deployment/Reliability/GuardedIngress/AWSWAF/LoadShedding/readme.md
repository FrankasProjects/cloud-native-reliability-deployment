# Create a AWS WAF for rate limiting

This script provisions an AWS WAF to an existing AWS EKS cluster, exposing its endpoints via an AWS ALB. 
The AWS WAF applies a load shedding of 100 requests for the path: /login (per IP and across different IPs).

## Prerequisites

1. Terraform installed, AWS CLI configured (with authorization keys)
2. EKS Cluster up and running (link zum script)
3. TeaStore deployed and exposed via an ALB (link to script)

### Initializes the repo

Initialize the repo: ``Terraform init``. This initializes the working directory by installing plugins and the modules created in the project structure. 

### Deploy the AWS WAF Config

Run ``Terraform apply`` confirm with ``yes``.
Note: Sometimes there is an error in binding the correct association when running terraform apply. Simply rerun the script or destroy in advance.

### Test the applied firewall

1. Adjust the URL to the TeaStore URL (DNS of ALB - refer to x for more information on how to receive the URL)
2. Execute the python test script via ``python test.py`` (ensure to be in the correct directory)
3. The error status code 403 should be received (Alternatively: 403 Forbidden is displayed when entering the URL into the browser)

During testing we encountered a delay: Setting a limit to 100 and executing the test script, the 403 status code will be sent after around 200 requests. 

