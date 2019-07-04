# Home_Project
Prototype of Server for Smart Home

 Version Alpha
## 1)Available Devices
### a)Out  
 -RGB  
  -On/Off  
  -Program (short unsigned int)  
  -Percent (0-100 int)  
###  b)In  
  -Sensors( "double" with max value 999999.9999)  

## 2) Getters/Setters/Changers for Apps
### a) by primary key (id)
 e.g http://127.0.0.1:8000/data/API/error=1
### b) by params
 e.g http://127.0.0.1:8000/data/API/deviceOnOff/?room=0  
 http://127.0.0.1:8000/data/API/deviceOnOff/?manualControl=true&room=0

## 3)Available Search Params for Apps
### a)RGB , Program, Percent
        name
        group
        room
        manualControl
        errorState  
### b)On/Off
        name
        group
        room
        manualControl
        errorState
        turnedON
### c)Sensors
        name
        group
        room
        errorState
### d)Errors
        code
        name
        group
        room
