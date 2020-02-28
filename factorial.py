import datetime

def factorial(request):
    result = 1
    if request == 1:
        return 1
    else:
        result = request * factorial(request - 1)
        return result


f = open('input.txt', 'r')
request = f.readline().strip()
requestId = 1
time = datetime.datetime.now().time()

log = open('factorial_log.csv', 'w')
log.write('RequestId,Time,N,Result\n')

while request:
    start_time = datetime.datetime.now()
    answer = factorial(int(request))
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(answer)
    log.write(str(requestId) + ',' + str(elapsed_time.microseconds) + ',' + str(request) + ',' + str(answer) + '\n')
    request = f.readline().strip()
    requestId += 1