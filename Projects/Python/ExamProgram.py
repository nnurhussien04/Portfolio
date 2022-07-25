monday = ['Biology','Computing','History']
tuesday = ['Chemistry','Maths']
wednesday = ['Geography','French','Physics']
thursday = ['English','Maths']
friday = ['Computing','History']
saturday = ['Biology','Chemistry','Physics','Maths']
sunday = ['Geography','French']
revisionDay = ''
startTime = ''
numberofSubjects = 0
revisionTime = 0
numberofBreaks = 0
breakTime = 0
totalTime = 0

print('Date of Revision')
revisionDay = input()
print('Start Time')
startTime = int(input())
if revisionDay == 'monday':
    for all_items in monday:
        numberofSubjects = numberofSubjects + 1
elif revisionDay == 'tuesday':
    for all_items in tuesday:
        numberofSubjects = numberofSubjects + 1 
elif revisionDay == 'wednesday':
    for all_items in wednesday:
        numberofSubjects = numberofSubjects + 1
elif revisionDay == 'thursday':
    for all_items in thursday:
        numberofSubjects = numberofSubjects + 1
elif revisionDay == 'friday':
    for all_items in friday:
        numberofSubjects = numberofSubjects + 1
elif revisionDay == 'saturday':
    for all_items in saturday:
        numberofSubjects = numberofSubjects + 1
elif revisionDay == 'sunday':
    for all_items in sunday:
        numberofSubjects = numberofSubjects + 1

revisionTime = numberofSubjects * 60
print(revisionTime)

numberofBreaks = revisionTime/45
breakTime = numberofBreaks * 20

totalTime = revisionTime + breakTime





print('The number of subjects that need revising is',numberofSubjects)
print('You will start revision at',startTime)
print('You will stop revising at',(startTime + totalTime))
print('You will have',numberofBreaks,'breaks')
