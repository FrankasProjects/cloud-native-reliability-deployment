## Install ModSecurity

Modsecurity WAF added to the Ingress Controller but requires the Enterprise Subscription (link). 
To configure rate limiting, the following modsecurity.conf can be used. 


## Tear Down

1. Remove application




# 



helm install haproxy-kubernetes-ingress haproxytech/kubernetes-ingress --create-namespace --namespace ingress-controller --set controller.service.type=LoadBalancer --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-type"="external" --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-nlb-target-type"="ip" --set controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-scheme"="internet-facing"

# change hsot to the load balancer
TODO: get statement to get that hostname without looking in the console

: kubectl -n haproxy-controller get services and replace host with the external ip: looking like k8s-haproxyc-haproxyk-df0198f214-ae90e55b6706ec82.elb.us-east-2.amazonaws.com


https://www.haproxy.com/documentation/kubernetes-ingress/community/installation/aws/


# Modsecurity

: extra readme, da die yaml bisschen anders aussieht

- aus dem rule folder: kubectl create secret generic modsecuritycrs --namespace haproxy-controller --from-file .

- bei updates: kubectl delete secret modsecuritycrs --namespace haproxy-controller

TODO: readme schreiben für annotations (rate liiting through HAproxy ingress controller)
TODO: extend that with the modSecurity WAF


https://d1wqtxts1xzle7.cloudfront.net/64640641/IRJET-V7I6649-libre.pdf?1602306751=&response-content-disposition=inline%3B+filename%3DIRJET_Security_Audit_of_Kubernetes_based.pdf&Expires=1698671654&Signature=YvTgLS2VOx6UOfsoDSqJFgA40UAK~L1aJPuAG4p-q2K-mW-539kORkmkjKVexnXeC-Z5CGB4rjacC1pFiLf-cFLru71bF~UtOua4Br3Udj0s70scR4CgxLVjF9SamCnSmcLKWvz~Wtrmu-BfVtiSQTdMGhwKtYP1mJIuxpT2UTPT2oNN7cwmqjY-M3l5YLIPrumuFI8jPqj1AZ02lpntsSXonnfzhozS7GheLHNy8hvLJEw0pLIvZxGq-RcWJxW3ltLiaH6QQY1VWw2X15Lt5cP8JMmMeqWDDalOr3Xn2ZBXgvfvdBFisypr-ud~AQWI7FeFKVOYWuiHrQ5D9txQPw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

https://opus.campus02.at/frontdoor/deliver/index/docId/68/file/AC16628109.pdf