# flask-api

Este repositório cria uma api resful de flask com uwsgi e nginx. A aplicação vai em container de docker. 

Ela possui um virtual environment de python já instalado para testes. 

# Setup 

Para iniciar, execute em terminal e dentro deste repositório clonado :

```
docker build -t api:latest . 
```

E então, para iniciar a api, execute (ainda dentro deste repositório): 

```
bash start-api.sh
```

A api estará na porta 5000, no endereço http://localhost:5000 do navegador. Os endpoints são:

* [GET]/r ; 
* [GET]/d ; e 
*[GET]/dly 

