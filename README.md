## Flask & Rest & json & pony databas


### API endpoints


### /members

#### GET

get list of  all members

#### PUT 








### För att testa använd curl


### GET

`curl http://127.0.0.1:5000/members`

resultatet blir i json


    {
        "1": {
            "name": "bosse",
            "phone": null
        }
    }
    
### PUT, DELETE

exempel med put

   `curl http://127.0.0.1:5000/sections -d '{"code":"B","name":"boxning","leader":1}'  -X PUT -H "Content-type: apllication/json"`

result

    {
        "new": "section:B"
    }







