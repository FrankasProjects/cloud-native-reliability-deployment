# AWS RDS for Maria DB
This part of the repository replaces the MariaDB container of the TeaStore with an Amazon RDS Maria DB Instance in order to achieve physical data distribution. 
For the creation of the database instance, AWS Controllers for Kubernetes (ACK) is used, which allows to create AWS resources within the Kubernetes environment. 

**NOTE:** The repository also sets a username and password for the created database, since these specific values are later used by the teastore application to access the database and therefore can not be changed. (TODO testing purpose oder ganz rausnehmen?)

## Prerequisites

1. Provisioned EKS Cluster (link)
2. Connection to the cluster (kubectl command)
2. AWS CLI - A command line tool for interacting with AWS services.
3. kubectl - A command line tool for working with Kubernetes clusters.
4. eksctl - A command line tool for working with EKS clusters.
5. Helm 3.7+ - A tool for installing and managing Kubernetes applications.


## Setup 

1. Install ACK controller: ``bash controler.sh``
2. Create Service account for ACK controller: ``bash IAM.sh``
3. Check if the RDS controller is up an running: ``kubectl get deployments -n ack-system``
4. Create the database (including security groups, anmespace, secrets, and subnet groups) via ``bash db.sh``  
**NOTE:** The database takes up to 10 minutes to create

### Physical Data Distribution

The database is created as a Multi-AZ database. For MariaDB instnaces this means, that an additional DB instance is provided in another vailability zone (selected fromt he created subnet group) that serves only as a fallback (linktowebsite).   
In order to achieve further distribution, that also serves requets readreplicas can be created with the following commands:

```
aws rds create-db-instance-read-replica \
    --db-instance-identifier first-read-replica \
    --source-db-instance-identifier maria-db \
    --allocated-storage 20 \
    --max-allocated-storage 20 \
    --availability-zone us-east-2a
```

```
aws rds modify-db-instance \
    --db-instance-identifier first-read-replica  \
    --backup-retention-period 3 \
    --apply-immediately
```

```
aws rds create-db-instance-read-replica \
    --db-instance-identifier second-read-replica \
    --source-db-instance-identifier first-read-replica \
    --allocated-storage 20 \
    --max-allocated-storage 20 \
    --availability-zone us-east-2b
```

Following this approach, cascading read replicas are created. AWS RDS allows up to 4 db instances. Thereby, each replica is added to a chain of replicas, with the advantage taht the main db instance (that also serves the write requests) experiences no downtime when creating additional replicas.  
(Ensure the db replica is available before creating the next one via: ``aws rds describe-db-instances --db-instance-identifier first-read-replica``)

### Deploy TeaStore

Execute `` kubectl create -f C:\Users\frank\Dokumente\Master\Thesis\mastersthesis\Code\teastore\teastore-rds.yaml `` (TODO adjust link)


## Clean Up

The repository created:
1. Shutdown Teastore: ``kubectl delete -f C:\Users\frank\Dokumente\Master\Thesis\mastersthesis\Code\teastore\teastore-rds.yaml``
2. RDS Controller within the cluster: Deletes with the cluster
3. Namespace within the cluster: Deletes with the cluster
4. Database Instance: ``kubectl delete -f rds-mariadb.yaml``
5. ReadReplicas: ``aws rds delete-db-instance --db-instance-identifier second-read-replica --skip-final-snapshot`` (Replace name also with second-read-replicas)
6. Secret within the cluster ``kubectl delete secret maria-db-password``
7. IAM Role for the RDS Controller: ``aws iam delete-role --role-name ack-rds-controller``
8. Subnet Group ``kubectl delete -f db-subnet-groups.yaml``