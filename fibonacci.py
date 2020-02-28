import datetime

def fibonacci(request):
    answer = []
    count = 0
    s1 = 0
    s2 = 1
    while count < request:
        answer.append(s1)
        s3 = s1 + s2
        s1 = s2
        s2 = s3
        count += 1
    return answer


f = open('input.txt', 'r')
request = f.readline().strip()
requestId = 1
time = datetime.datetime.now().time()

log = open('fibonacci_log.csv', 'w')
log.write('RequestId,Time,N,Result\n')

while request:
    start_time = datetime.datetime.now()
    answer = fibonacci(int(request))
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(','.join(str(x) for x in answer))
    log.write(str(requestId) + ',' + str(elapsed_time.microseconds) + ',' + str(request) + ',' + '*'.join(str(x) for x in answer) + '\n')
    request = f.readline().strip()
    requestId += 1
