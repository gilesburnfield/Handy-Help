#SDS.py

import os
import sys

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "sys._MEIPASS",
            os.path.abspath(".")
        ),
        relative
    )

def create_db(filename):
    filename = resource_path(filename)
    template = '{}'
    master = open(filename, 'wb')
    master.write (template)
    master.close()

def read():
    filename = resource_path('giles11.txt')
    master = open(filename, 'r')
    master_dict = eval(master.read())
    return master_dict

def write(stro):
    filename = resource_path('giles11.txt')
    master = open(filename, 'wb')
    master.write (stro)
    master.close()
    
def new_job():
    job = raw_input('Job: ')
    if not job in list_jobs():
        master_dict = read()
        master_dict[job] = {}
        master_str = str(master_dict)
        write(master_str)

def list_jobs():
    list_jobs = []
    master_dict = read()
    for jobs in master_dict:
        list_jobs.append(jobs)
    return list_jobs

def list_materials():
    list_materials = []
    master_dict = read()
    for material in master_dict:
        list_materials.append(material)
    return


def job_update(job):    
    if job in list_jobs():
        master_dict =read()
        date = raw_input("Date please: ")
        hours= float(raw_input("Hours please: "))
        rate= float(raw_input("Rate please: "))
        notes = raw_input("What did you do: ")
    
        master_dict[job][date] = {}
        master_dict[job][date]['hours'] = hours
        master_dict[job][date]['rate'] = rate
        master_dict[job][date]['notes'] = notes
        
        master_str = str(master_dict)
        write(master_str)
        return master_dict
    print 'No Job'


def matrials_update(job):
    master_dict = read()
    print master_dict
    matrials = raw_input('What did you buy? ')
    cost = float(raw_input('Cost of '+ matrials +': '))
    description = raw_input('description: ')
    
    master_dict[job][matrials] = {}
    master_dict[job][matrials]['Cost'] = cost
    master_dict[job][matrials]['description'] = description
    
    master_str = str(master_dict)
    write(master_str)
    return master_dict
    
def stats(client):
    a = read()

    job_list =[]
    material_list =[]
    hours = []
    rate = []
    wage =[]
    material = []
    
    hours_total = 0 
    rate_total = 0 
    wage_total = 0
    material_total = 0


    if client == 'total':
        job_list = list_jobs()
    job_list.append(client) 
    for j in job_list:
        print j
        for i in a[j]:
            print i 
            r = a[j][i]['rate']
            h = a[j][i]['hours']
            w = r*h
            hours.append(h)
            rate.append(r)
            wage.append(w)
            hours_total = h + hours_total
            rate_total = r + rate_total
            wage_total = w + wage_total 


    #if client == 'total':
    #    materials_list = list_materials()
    #material_list.append(client)
    #for l in material_list:
    #    for m in a[l]:
    #        em = a[l][m]['Cost']
    #        material.append(m)
    #        material_total = em + material_total



    
    print 'Client - ' , client
    print 'Total hours - ',hours_total
    print 'Material - ',  material_total

    print 'Total Bill -', wage_total


def dowhat():
    ask = 'y'
    
    while ask == 'y':
        print 'Add New Job (N) or Update Exsting Job (U) or Update extras (M) or Look at Stats(S) or look at Job List (L)'
        
        Choice = raw_input("Sooo: ")

        if Choice == 'N':
            new_job()
        elif Choice == 'U':
            job = raw_input("Which job to update? ")
            job_update(job)
        elif Choice == 'S':
            job = raw_input("Which Job? ")
            stats(job)
        elif Choice == 'M':
            job = raw_input("Which Job did you buy matrials for? ")
            matrials_update(job)
        elif Choice == 'L':
            print 'test'
            print list_jobs()
        

        print 'Anymore?(y/n)'
        ask = raw_input("Anymore: ")


print resource_path('giles11.txt')

dowhat()












    


























    


    









