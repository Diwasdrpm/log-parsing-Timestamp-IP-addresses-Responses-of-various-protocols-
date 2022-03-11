import csv
import re

log_file = open('task2.log','r')
log_list_time = []
log_list_ip = []
log_list_request = []


for line in log_file:
    if "HTTP" in line:
        pattern_time = '\d{0,9}\d{0,9}:\d{0,9}\d{0,9}:\d{0,9}\d{0,9}'
        final_time = re.findall(pattern_time, line)
        log_list_time.append(final_time)
        # log_list.append(line.split(' ')[1].split(' ')[0])
        pattern = '\d{1,3}\d{1,3}.\d{1,3}\d{1,3}.\d{1,3}\.\d{1,3}'
        finalIP = re.findall(pattern, line)
        log_list_ip.append(finalIP)
        # for requests
        if "GET" in line:
            log_list_request.append("GET")
        elif "POST" in line:
            log_list_request.append("POST")
        else:
            log_list_request.append("No request(HTTP)")



    elif " FTP" in line:   
        pattern_time = '\d{0,9}\d{0,9}:\d{0,9}\d{0,9}:\d{0,9}\d{0,9}'
        final_time = re.findall(pattern_time, line)
        log_list_time.append(final_time)
        # log_list.append(line.split(' ')[1].split(' ')[0])
        pattern = '\d{1,3}\d{1,3}.\d{1,3}\d{1,3}.\d{1,3}\.\d{1,3}'
        finalIP = re.findall(pattern, line)
        log_list_ip.append(finalIP)
        if "request" in line:
            log_list_request.append(line.split('request')[1].split(',')[0].split('}')[0].split(': ')[1])
        else:
            log_list_request.append("No requests(FTP)")



    elif "Modbus" in line:   
        pattern_time = '\d{0,9}\d{0,9}:\d{0,9}\d{0,9}:\d{0,9}\d{0,9}'
        final_time = re.findall(pattern_time, line)
        log_list_time.append(final_time)
        # log_list.append(line.split(' ')[1].split(' ')[0])
        pattern = '\d{1,3}\d{1,3}.\d{1,3}\d{1,3}.\d{1,3}\.\d{1,3}'
        finalIP = re.findall(pattern, line)
        log_list_ip.append(finalIP)
        if "request" in line:
            log_list_request.append(line.split('request')[1].split(',')[0].split(' ')[1])
        else:
            log_list_request.append("No request(Modbus)")




    elif "BACnet" in line:   
        pattern_time = '\d{0,9}\d{0,9}:\d{0,9}\d{0,9}:\d{0,9}\d{0,9}'
        final_time = re.findall(pattern_time, line)
        log_list_time.append(final_time)
        # log_list.append(line.split(' ')[1].split(' ')[0])
        pattern = '\d{1,3}\d{1,3}.\d{1,3}\d{1,3}.\d{1,3}\.\d{1,3}'
        finalIP = re.findall(pattern, line)
        log_list_ip.append(finalIP)
        if "request" in line:
            log_list_request.append("BACnet request availiable")
        else:
            log_list_request.append("No request(BACnet)")


        
    elif "SNMP" in line: 
        pattern_time = '\d{0,9}\d{0,9}:\d{0,9}\d{0,9}:\d{0,9}\d{0,9}'
        final_time = re.findall(pattern_time, line)
        log_list_time.append(final_time)  
        # log_list.append(line.split(' ')[1].split(' ')[0])
        pattern = '\d{1,3}\d{1,3}.\d{1,3}\d{1,3}.\d{1,3}\.\d{1,3}'
        finalIP = re.findall(pattern, line)
        log_list_ip.append(finalIP)
        if "request" in line:
            # print(line.split('request')[1])
            pattern = '\d{1,3}\d{1,3}.\d{1,3}\.\d{1,3}\d{1,3}.\d{1,3}'
            finalIP = re.findall(pattern, line)
            log_list_request.append(finalIP)
        else:
            log_list_request.append("No request(SNMP)")


    
x=len(log_list_ip)+len(log_list_time)
print(x)
with open('parsed_csv.csv','w') as parsed_csv:
    csv_writer = csv.writer(parsed_csv)
    for item in range(x//2):     
            csv_writer.writerow([log_list_time[item],log_list_ip[item],log_list_request[item]])
    # for item in log_list_time:
    #     csv_writer.writerow(item)
              
        
print("SUCCESSFULLY EXECUTION COMPLETED")
print("OPEN THE CSV FILE TO SEE THE RESULT")
