# Text Classification


## Dataset

- Language Detection [Dataset](https://www.kaggle.com/datasets/basilb2s/language-detection)
- Text Classification [Dataset]()


## Run Application

- The webserver is available at: `http://localhost:80`
- Documentation is available at: `http://localhost/docs`


Build container from Dockerfile:  

```sh
>> docker build -t app-name .    # build image
>> docker run -p 80:80 app-name  # run container
```

Use docker-compose:  

```sh
>> docker-compose up -d    # start container
>> docker-compose down     # stop container
```

Run application manually:  
The webserver is available at: `http://localhost:8000`  

```sh
>> uvicorn main:app --reload
```

Click `Try it out` and try your text value in /predict Parameters tab:  

<p align="left">
    <img src="./assets/fastapi1.png" height="400" />
    <img src="./assets/fastapi2.png" height="400" />
</p>

## Resource

- [Language Detection](https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku)