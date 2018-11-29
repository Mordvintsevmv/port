from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth

import json
import time

file = open("port_data.json", "r", encoding="utf8")
text = file.read()
file.close()
data = json.loads(text)
seaport_data = []
seaport_data.extend(data)
port_name = ""
test = seaport_data[0]["transport"]
warning = "Вы что-то не ввели! Проверьте ещё раз!"
success = "Вы удачно добавили транспортирвку!"
start = "Добавьте новую транспортировку!"
def index(request):
    return render(request, 'index.html', {
    })

def all_transport(request):
    return render(request, 'all_transport.html', {
        "seaport_data" : seaport_data,
    })

def port_search(request):
    if request.method == "POST":
        port_name = request.POST.get("port")
        return render(request, 'port_search.html', {
        "port_name" : port_name,
        "seaport_data": seaport_data,
    })
    else: return render(request, 'port_search.html', {
        "seaport_data": seaport_data,})



def in_port(request):
    if request.method == "POST":
        port_name = request.POST.get("port")
        return render(request, 'in_port.html', {
        "port_name" : port_name,
        "seaport_data": seaport_data,
    })
    else: return render(request, 'in_port.html', {
        "seaport_data": seaport_data,})

def out_port(request):
    if request.method == "POST":
        port_name = request.POST.get("port")
        return render(request, 'out_port.html', {
        "port_name" : port_name,
        "seaport_data": seaport_data,
    })
    else: return render(request, 'out_port.html', {
        "seaport_data": seaport_data,})

def transport_search(request):
    if request.method == "POST":
        trasnport = request.POST.get("transport")
        return render(request, 'transport_search.html', {
        "transport" : trasnport,
        "seaport_data": seaport_data,
    })
    else: return render(request, 'transport_search.html', {
        "seaport_data": seaport_data,})

def edit(request):
    if request.method == "POST":
        port_name = request.POST.get("port_name")
        ID = request.POST.get("ID")
        sudno = request.POST.get("sudno")
        model = request.POST.get("model")
        type = request.POST.get("type")
        charac = request.POST.get("charac")
        port_out = request.POST.get("port_out")
        time_out = request.POST.get("time_out")
        port_in = request.POST.get("port_in")
        time_in = request.POST.get("time_in")

        if (port_name == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (ID == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (sudno == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (model == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (type == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (charac == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (port_out == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (time_out == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (port_in == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })
        elif (port_out == ""):
            return render(request, 'edit.html', {
                "warning": warning,
            })

        else:

            zagr = [{
          "name_port" : port_name ,
          "transport" :
          [
            {
              "id" : ID,
              "sudno" :[
                {
                  "name_sudno" : sudno,
                  "model" : model,
                  "type" : type,
                  "char" : charac
                }
              ],
              "out_punkt" : [
                {
                  "name_port": port_out,
                  "out_time" : time_out
                }
                      ],
              "in_punkt" : [
                {
                  "name_port" : port_in,
                  "in_time" : time_in
                }
              ]

            }
          ]
        }]

            zagr_same_port = [{
              "id" : ID,
              "sudno" :[
                {
                  "name_sudno" : sudno,
                  "model" : model,
                  "type" : type,
                  "char" : charac
                }
              ],
              "out_punkt" : [
                {
                  "name_port": port_out,
                  "out_time" : time_out
                }
                      ],
              "in_punkt" : [
                {
                  "name_port" : port_in,
                  "in_time" : time_in
                }
              ]
            }]

            flag = 0
            for i in range (0,len(seaport_data)):
                if (port_name == seaport_data[i]["name_port"]):
                    seaport_data[i]["transport"].extend(zagr_same_port)
                    file = open("port_data.json", "w", encoding="utf8")
                    data = json.dumps(seaport_data)
                    file.write(data)
                    file.close()
                    flag = 1
                    break

            if (flag == 0):
                seaport_data.extend(zagr)
                file = open("port_data.json", "w", encoding="utf8")
                data = json.dumps(seaport_data)
                file.write(data)
                file.close()

            return render(request, 'edit.html', {
            "success" : success
        })
    else:
        return render(request, 'edit.html', {
            "start" : start
        })