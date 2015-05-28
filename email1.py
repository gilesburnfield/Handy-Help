#E-mail

import sys
import imaplib
import getpass
import email
import datetime

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login('hazeldown123@gmail.com', getpass.getpass())
M.select()

def e_mail_process(M):
    email_string = []
    typ, data = M.search(None, 'ALL')
    for num in data[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        #print 'test1' + 'Message %s\n%s\n' % (num, data[0][1])

        msg = email.message_from_string(data[0][1])
        #print msg

        print msg.get_payload(), 'yyyy'
        #print 'Message %s: %s' % (num, msg['Subject'])
        
        # print msg['Subject'], 'test'
        # if msg['Subject'] == 'Gardening':
        #     string = str(msg)
        #     print string, "test"
        #     email_string.append(string)
        #     print 'hello', email_string
        
        # print str(msg['Date']), 

    M.close()
    M.logout()

    return email_string

data = e_mail_process(M)




    


# master_dict= {}

# # master_dict[job] = {}
# # master_dict[job]['labour'] = {}
# # master_dict[job]['materials'] = {}

# for i in data:
    
#     date = i.split(' ')[2] + " " + i.split(' ')[3] + i.split(' ')[4]
#     client = i.split('Client ')[1].split('\r\n')[0]
#     hours = i.split('Hours ')[1].split('\r\n')[0]
#     fee_rate = i.split('Fee rate ')[1].split('\r\n')[0]
#     notes = i.split('Notes ')[1].split('\r\n')[0]

#     try:
#         master_dict
#     except NameError:
#         print False
#         master_dict = {}

#     else:
#         
#       print master dict exstist 
#     # if 
#     # master_dict[client] = {}
#     # master_dict[client]['labour'] = {}
#     # master_dict[job]['materials'] = {}


















#print date, client, fee_rate, notes







