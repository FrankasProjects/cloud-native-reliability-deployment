# Ingress Controller 

This part of the repository implements an Ingress Controller as alternative to the Load Balancer Controller of the baseline architecture. The Ingress Controller, here the HaProxy, serves as a reverse proxy and load balancer that directs traffic to the cluster.   
The HaProxy Ingress Controller is used to deploy functionalities from the section *Guarded Ingress*, as alternative to the AWS-native options. 

## Prerequisites


1. Provisioned EKS Cluster: [Baseline Architecture](https://github.com/frankakn/reliability-deployment/tree/main/Deployment/BaselineArchitecture)
2. Connection to the cluster (via ``aws eks --region us-east-2 update-kubeconfig --name eks-cluster``)
2. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) - A command line tool for interacting with AWS services.
3. [kubectl](https://kubernetes.io/de/docs/tasks/tools/install-kubectl/) - A command line tool for working with Kubernetes clusters.
4. [eksctl](https://eksctl.io/) - A command line tool for working with EKS clusters.
5. [Helm 3.7+](https://helm.sh/) - A tool for installing and managing Kubernetes applications.

## Install HaProxy Ingress Controller

Install via Helm (adjusted from: https://www.haproxy.com/documentation/kubernetes-ingress/community/installation/aws/)
1. ``helm repo add haproxytech https://haproxytech.github.io/helm-charts``
2. ``helm repo update``
3. ``helm install haproxy-kubernetes-ingress haproxytech/kubernetes-ingress --create-namespace --namespace haproxy-controller --set controller.service.type=LoadBalancer --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-type"="external" --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-nlb-target-type"="ip" --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-scheme"="internet-facing" ``
4. Configure App Deployment: The HaProxy creates per default an NLB. The install statement from 3 ensures it is internet-facing, so that the created DNS can be used to access the TeaStore WebUI. Run:: `` kubectl get services --namespace haproxy-controller ``.
5. Insert External IP (similar to kubectl get services --namespace haproxy-controller) into the TeaStore Deployment file as hostname.
5. Deploy Teastore: ``kubectl apply -f (todo) mod.yaml`` 

