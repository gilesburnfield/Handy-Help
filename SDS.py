#SDS.py

def read():
    master = open("master.txt", "r")
    master_dict = eval(master.read())
    return master_dict

def write(stro):
    master = open("master.txt", "wb")
    master.write (stro)
    master.close()
print read 


def new_job():
    master_dict = read()
    job = raw_input('Job:')
    master_dict[job] = {}
    master_str = str(master_dict)
    write(master_str)


def job_update(job):
    master_dict =read()
    date = raw_input("Date please: ")
    hours= float(raw_input("Hours please: "))
    rate= float(raw_input("Rate please: "))
    notes = str(raw_input("What did you do: "))
    
    master_dict[job][date] = {}
    master_dict[job][date]['hours'] = hours
    master_dict[job][date]['rate'] = rate
    master_dict[job][date]['Notes'] = notes
        
    master_str = str(master_dict)
    write(master_str)
    return master_dict


def list_jobs():
    list_jobs = []
    master_dict = read()
    for jobs in master_dict:
        list_jobs.append(jobs)
    return list_jobs
        
def stats(client):
    a = read()
    
    hours = []
    rate = []
    wage =[]
    hours_total = 0 
    rate_total = 0 
    wage_total = 0



    if client == 'total':
        job_list = list_jobs()
        

    print job_list

    for j in job_list:

        print j

        for i in a[j]:
            r = a[j][i]['rate']
            h = a[j][i]['hours']
            w = r*h
            hours.append(h)
            rate.append(r)
            wage.append(w)
            hours_total = h + hours_total
            rate_total = r + rate_total
            wage_total = w + wage_total    



    print 'Client - ' , client
    print 'Total hours -',hours_total
    print 'Total Bill -', wage_total


def dowhat():
    ask = 'y'
    
    while ask == 'y':
        print 'Add New Job (N) or Update Exsting Job (U) or Look at Stats(S) or look at Job List (L)'
        
        Choice = raw_input("Sooo: ")

        if Choice == 'N':
            new_job()
        elif Choice == 'U':
            job = raw_input("Which job to update: ")
            job_update(job)
        elif Choice == 'S':
            job = raw_input("Which Job: ")
            stats(job)
        
        elif Choice == 'L':
            print 'test'
            print list_jobs()
        

        print 'Anymore?(y/n)'
        ask = raw_input("Anymore: ")

dowhat()














    


























    


    









