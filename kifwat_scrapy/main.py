from operator import index
import os
from re import T
import traceback
from django.conf import settings
from django.apps import apps
from demo import settings as base_settings
from unidecode import unidecode
import os     
from dotenv import load_dotenv
import json
import subprocess
from django.db import connection

# Get the cursor object
load_dotenv()
settings_dict = {}
for st in dir(base_settings):
    if st.startswith('_') or not st.isupper():
        continue
    settings_dict[st] = getattr(base_settings, st)
settings.configure(**settings_dict)
apps.populate(settings.INSTALLED_APPS)
process = subprocess.Popen("python manage.py migrate app", shell=True, stdout=subprocess.PIPE)
process.wait()

# from demo.app.models import root,subroot
# newdata = root(name='ramehs')
# newdata.save()
# sdata = subroot(root=newdata)
# sdata.save()
# data = root.objects.all()
# print(data)
from app.models import scrapData,scrapDepartment,scrapCity,scrapQuarters,scrapStreets
def fixField(field):
    field = unidecode(field)
    startwith = [
        ('- ',''),
        ('+ ','plus_'),
        # ("Répartition selon l'âge'",'Repartition_selon_lage'),
        # ("Répartition selon l'activité (Hommes)",'Repartition_selon_lactivite_Hommes'),
        # ("Répartition selon l'activité (Femmes)",'Repartition_selon_lactivite_Femmes'),
        ]
    for data in startwith:
        if field.startswith(data):
            field = field.replace(data[0],data[1],1)
        else:
            if " - " in field:
                field = field.replace(" - ",'_')
                field = f'key_{field}' 
        if field[:1].isnumeric():
            field = field.replace(field[:1],"key_"+field[:1])
    replace = [
        ("'",''),
        (" ",'_'),
        ("(",''),
        (")",''),
        ("dept",'department'),
    ]
    for d in replace:
        field = field.replace(d[0],d[1])
    return field

def uploaddata(oridata,typeofdata,parenturl):
    # with open("out.json",'a') as file:
    #     file.write(json.dumps(oridata)+"\n")
    try:
        data = oridata
        # print(data)
        res={}
        if typeofdata == "region":
            instance = scrapData
            fields = [f.name for f in instance._meta.fields]
            res['regionid'] = uploadInModel(instance,data,fields)
            # return res
        if typeofdata == 'department':
            instance = scrapDepartment
            fields = [f.name for f in instance._meta.fields]
            data["idregion"] = scrapData.objects.get(source=parenturl)
            res['departmentid'] = uploadInModel(instance,data,fields)
            # return res
            # input('press any key')
        if typeofdata == 'city':
            instance = scrapCity
            fields = [f.name for f in instance._meta.fields]
            data["idDepartment"] = scrapDepartment.objects.get(source=parenturl)
            res['cityid'] = uploadInModel(instance,data,fields)
            # return res
            # input('press any key')
        if typeofdata == 'quater':
            instance = scrapQuarters
            fields = [f.name for f in instance._meta.fields]
            data["idCity"] = scrapCity.objects.get(source=parenturl)
            res['quaterid'] = uploadInModel(instance,data,fields)
            # return res
            # input('press any key')
        if typeofdata == 'streets':
            instance = scrapStreets
            fields = [f.name for f in instance._meta.fields]
            data["idQuarter"] = scrapQuarters.objects.get(source=parenturl)
            res['streetid'] = uploadInModel(instance,data,fields)
            # return res
    except Exception as e:
        traceback.print_exc()
        print("got error")
        # input()

def uploadInModel(instance,data,fields):
    fdata = {}
    for key,value in data.items():
        nkey = fixField(key)
        lowerfield = [field.lower() for field in fields]
        if nkey.lower() in lowerfield:
            index = lowerfield.index(nkey.lower())
            fdata[fields[index]] = value
    # newda,created = scrapData.objects.get_or_create(**fdata)
    # print(created)
    def update_and_clean(queryset,fdata):
        for obj in queryset:
            for k,v in fdata.items():
                setattr(obj,k,v)
            obj.clean()
            obj.save()
    try:
        newda = instance.objects.filter(source=fdata['source'])
        if newda.exists():
            update_and_clean(newda,fdata)
            # newda.update(**fdata)
        else:
            newda = instance(**fdata) 
            newda.clean()
            newda.save()
    except Exception as e:
        traceback.print_exc()
        # input("in exep")
        newda = instance(**fdata) 
        newda.clean()
        newda.save()
    # return newda.id
def clear_migrations():
    cursor = connection.cursor()
    # Execute a query to fetch all rows from the migration history table
    cursor.execute("DELETE FROM django_migrations")
    cursor.close()