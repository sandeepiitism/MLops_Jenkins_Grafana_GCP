# MLops_Jenkins_Grafana_GCP
ML pipelines with Kubernetes, GitLab CI, Jenkins, Prometheus, Grafana, Kubeflow &amp; Minikube on GCP

## GCP Bucket
<img width="1902" height="798" alt="Image" src="https://github.com/user-attachments/assets/9b08ff73-6474-4d64-aca5-5199131e7eaa" />

## GCP Ingestion
<img width="1696" height="740" alt="Image" src="https://github.com/user-attachments/assets/89275dbf-4a17-462f-9d12-568eb893ec21" />

#### using Service account settings
<img width="1895" height="772" alt="Image" src="https://github.com/user-attachments/assets/810ea343-82bb-4185-814a-e4609f0a9335" />

## MLFLOW
<img width="1911" height="862" alt="Image" src="https://github.com/user-attachments/assets/0b7e2aae-7241-4ad4-b7f9-990a3ceb13cb" />


#### code structure
<img width="1720" height="957" alt="Image" src="https://github.com/user-attachments/assets/3237c48f-a991-445b-a727-c4b7b870316a" />


## Docker creation
#### This is a docker in docker for Jenkins

``` bash
docker build -t jenkins-dind . 
docker images

docker run -d --name jenkins-dind ^
--privileged ^
-p 8080:8080 -p 50000:50000 ^
-v //var/run/docker.sock:/var/run/docker.sock ^
-v jenkins_home:/var/jenkins_home ^
jenkins-dind
```
<img width="1911" height="1005" alt="Image" src="https://github.com/user-attachments/assets/a502cfd3-3076-4e67-b4ec-cdf2714eb480" />


#### Installing some dependencies once Jemkins container is up and running:

```bash
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
apt install -y python3-venv
exit
```

## Github with Jenkins

https://github.com/user-attachments/assets/dd2d46f1-7624-436b-af1d-4a910834fa8f