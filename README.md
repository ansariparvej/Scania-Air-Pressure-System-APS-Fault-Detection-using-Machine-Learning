# neurolab-mongo-python

![image](https://www.google.com/search?q=scania+truck+&tbm=isch&ved=2ahUKEwi-3oqE6NH-AhXMzqACHWxnC0QQ2-cCegQIABAA&oq=scania+truck+&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQgAQyBwgAEIoFEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBwgAEIoFEEMyBQgAEIAEMgUIABCABDIFCAAQgAQ6BggAEAUQHlDoDFjoDGD3DmgAcAB4AIAB4QGIAcEDkgEDMi0ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=v3pOZP6CN8ydg8UP7M6toAQ&bih=572&biw=1252#imgrc=FbXRCvxOC0gyuM)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```


To download your dataset

```
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

This is changes made in neuro lab


Git commands

If you are starting a project and you want to use git in your project
```
git init
```
Note: This is going to initalize git in your source code.


OR

You can clone exiting github repo
```
git clone <github_url>
```
Note: Clone/ Downlaod github  repo in your system


Add your changes made in file to git stagging are
```
git add file_name
```
Note: You can given file_name to add specific file or use "." to add everything to staging are


Create commits
```
git commit -m "message"
```

```
git push origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name 

To push your changes forcefully.
```
git push origin main -f
```


To pull  changes from github repo
```
git pull origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name


.env file has
```
MONGO_DB_URL="mongodb://localhost:27017"
AWS_ACCESS_KEY_ID="Your ID"
AWS_SECRET_ACCESS_KEY="Your Key"
```

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```


```

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=
BUCKET_NAME=
MONGO_DB_URL=
```
