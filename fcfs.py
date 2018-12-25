import sys
import json
def tryConvertToInt(string, errorMessage):
    try:
        ret = int(string)
        if abs(ret) is not ret:
            raise ValueError()
        return abs(ret)
    except ValueError:
        print(errorMessage)
        print('exiting...')
        sys.exit(1)
pn = tryConvertToInt(input('number of processes: '), 'invalid number of processes')
if pn is 0:
    print('no processes')
    print('exiting...')
processes = list()
for i in range(pn):
    print('\nProcess', str(i + 1) + ':')
    arrivalTime = tryConvertToInt(input('  * Arrival time: '), 'invalid arrival time')
    executionTime = tryConvertToInt(input('  * Execution time: '), 'invalid execution time')
    processes.append({ 'arrTime': arrivalTime, 'execTime': executionTime })
processes = sorted(processes, key=lambda p: p['arrTime'])
processes[0].update(
    {
        'startTime': processes[0]['arrTime'],
        'endTime': processes[0]['arrTime'] + processes[0]['execTime'],
        'waitTime': 0
    }
)
for i, p in enumerate(processes[1:], 1):
    processes[i].update({
        'startTime': processes[i - 1]['endTime'],
        'endTime': processes[i - 1]['endTime'] + processes[i]['execTime'],
        'waitTime': processes[i - 1]['endTime'] - processes[i]['arrTime']
    })
print('\nAverage service time', sum([x['startTime'] for x in processes]) / pn)
print('Average waiting time', sum([x['waitTime'] for x in processes]) / pn, '\n')
