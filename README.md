<h1 align="center">Sanic + AIOHttp + MongoDB CRUD API</h3>


<p align="center"> This is the Repository for a CRUD API using Sanic web Framework. The repository also uses AIOhttp to make requests to another Server. The API uses MongoDB as its Database</p>

## 📝 Table of Contents

- [Requirements](#requirements)
- [Note](#note)
- [Running](#running)
<br>
<br>

## 🧐 Requirements <a name = "requirements"></a>

1. Sanic -  ```pip install sanic```
2. AIOHttp - ```pip install aiohttp```
3. Pymongo - ```pip install pymongo[srv]```
<br>
<br>

## 🏁 Note <a name = "note"></a>

Replace MOTOR_URI with your own MongoDB URI

<br>
<br>
## 🔧 Running <a name = "running"></a>

1. Export The Databse Password as Environment Variable
   1. For Windows - ```set MONGO_PASSWORD=<Your Password>```
   2. For Linux - ```export MONGO_PASSWORD=<Your Password>```
2. Run the Server - ```python sanic_crud_api.py```
