# Text Classification


## Dataset

- Language Detection [Dataset](https://www.kaggle.com/datasets/basilb2s/language-detection)
- Text Classification [Dataset]()


## Run Application

- The webserver is available at: `http://localhost:80`
- Documentation is available at: `http://localhost/docs`


<!-- ```sh
>> docker build -t app-name .
>> docker run -p 80:80 app-name
``` -->

```sh
>> docker-compose up -d    # start container
>> docker-compose down   # stop container
```

Click `Try it out` and try your text value in /predict Parameters tab:  

<p align="left">
    <img src="./assets/fastapi1.png" height="400" />
    <img src="./assets/fastapi2.png" height="400" />
</p>

## Resource

- [Language Detection](https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku)