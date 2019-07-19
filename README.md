# Procedure
```
git clone https://github.com/kamal2354/MAC-API.git

cd MAC-API

docker build -t getMacInfo:public .
```
## Run container with image id from above
```
docker run -it <image_id>
```
## Run python script with mac address as a parameter, as below
```
python3 getMacInfo.py <MAC>
```
