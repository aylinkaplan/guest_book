# Guest Book

## Installation 
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

# APIs

List of GuestBook: 
```
curl -X GET http://127.0.0.1:8000/api/list/ -H "Authorization: Token af471785429f6c62b7aadeb3dbaf08aea7d3c892" 
```
Detail of a GuestBook : 
```
curl -X GET http://127.0.0.1:8000/api/list/3/ -H "Authorization: Token af471785429f6c62b7aadeb3dbaf08aea7d3c892" 
```
Create of GuestBook : 
```
curl -X POST -d '{"name":"TestUser", "subject": "Example Subject", "message": "Example Message"}' http://127.0.0.1:8000/api/create/ -H "Authorization: Token af471785429f6c62b7aadeb3dbaf08aea7d3c892" -H "Content-Type: application/json"
```
Update of GuestBook : 
```
curl -X PUT -d '{"name":"TestUser2", "subject": "Example Subject2", "message": "Example Message2"}' http://127.0.0.1:8000/api/update/3/ -H "Authorization: Token af471785429f6c62b7aadeb3dbaf08aea7d3c892" -H "Content-Type: application/json"
```
Delete of GuestBook : 
```
curl -X DELETE http://127.0.0.1:8000/api/delete/3/ -H "Authorization: Token af471785429f6c62b7aadeb3dbaf08aea7d3c892" -H "Content-Type: application/json"
```

