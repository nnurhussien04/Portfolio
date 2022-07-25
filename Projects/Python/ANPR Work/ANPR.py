import re
import linecache
print('The ANPR System')
Name = input('Enter Name')
PlateNumber = input('Enter Plate Number')
PlateNumber_Format = re.findall("[A-Z][A-Z][0-9][0-9] [A-Z][A-Z][A-Z]",PlateNumber)
StartTime = int(input('Enter the start time in 24hr format'))
EndTime = int(input('Enter the end time in 24hr format'))
if StartTime == EndTime:
    StartSeconds = int(input('Enter the start seconds'))
    EndSeconds = int(input('Enter the end seconds'))
    SpeedSeconds = EndSeconds - StartSeconds
    SpeedSecondsV2 = SpeedSeconds/60
    Speed = (1/SpeedSecondsV2)*60
    if Speed/2 != range(0,300):
        SpeedV2 = round(Speed,1)
        print(SpeedV2,'mph')
    else:
        print(Speed,'mph')
else:   
    SpeedTime = EndTime - StartTime
    SpeedTimeV2 = SpeedTime
    Speed = (1/SpeedTime)*60
    if Speed/2 != range(0,300):
        SpeedV2 = round(Speed,1)
        print(SpeedV2,'mph')
    else:
        print(Speed,'mph')
if Speed > 20:
    print('You are above the speed limit')
    if PlateNumber_Format == []:
        print('Invalid Plate Number')
        PlateNumberFile = open("PlateNumber.txt","a")
        PlateNumberFile.write("\n")
        PlateNumberFile.write(str(Name))
        PlateNumberFile.write(' ')
        PlateNumberFile.write(str(PlateNumber))
        PlateNumberFile.close()
    else:
        print('Plate Number is Valid')
##    try:
##        FinesFiles = open("Fines.txt","a")
##        FinesFiles.write("\n")
##        FinesFiles.write(str(Name))
##        FinesFiles.write("   ")
##        FinesFiles.write(str(PlateNumber))
##        FinesFiles.write("   ")
##        FinesFiles.write(str(SpeedV2))
##        FinesFiles.close()
##        print('Successful')
##    except:
##        print('Failed')
print('Name:',Name)
print('Plate Number:',PlateNumber)
print('Speed:',SpeedV2,"mph")


FinesFilesCheck = open("DriverDetails.txt","r")
FFCheck = FinesFilesCheck.read()
     
if Name in FFCheck:
    def FileNameSearch(string_to_search):
        line_number = 0
        list_of_results = []
        with open("DriverDetails.txt", 'r') as read_obj:
            for line in read_obj:
                line_number += 1
                if string_to_search in line:
                    list_of_results.append(line.rstrip())
        return list_of_results
    
    NameSearch = FileNameSearch(Name)
    for elem in NameSearch:
        print(NameSearch[0])
    print('A fine should be sent in a couple of working days')

    DriverFinesFiles = open("DriverFines.txt","a")
    DriverFinesFiles.write("\n")
    DriverFinesFiles.write(''.join(map(str,NameSearch)))
    DriverFinesFiles.write("      ")
    DriverFinesFiles.write(str(round(Speed,0)))
    DriverFinesFiles.close()

   
else:
    AddressDetails = input('Enter your Address and postcode')
    FinesFilesAddition = open("DriverDetails.txt","a")
    FinesFilesAddition.write("\n")
    FinesFilesAddition.write(str(Name))
    FinesFilesAddition.write("   ")
    FinesFilesAddition.write(str(PlateNumber))
    FinesFilesAddition.write("   ")
    FinesFilesAddition.write(str(AddressDetails))
    FinesFilesAddition.close()
    DriverFinesFiles = open("DriverFines.txt","a")
    DriverFinesFiles.write("\n")
    DriverFinesFiles.write(str(Name))
    DriverFinesFiles.write("    ")
    DriverFinesFiles.write(str(PlateNumber))
    DriverFinesFiles.write("    ")
    DriverFinesFiles.write(str(AddressDetails))
    DriverFinesFiles.write("     ")
    DriverFinesFiles.write(str(round(Speed,0)))
    DriverFinesFiles.close()
    print(" A fine will be sent to you in a couple of working days")
    
        
FinesFilesCheck.close()

