import sys
import time

with open("./request.txt", "w") as request:
    request.write(sys.argv[1])
    
result = sys.argv[1]

while (result == sys.argv[1]):
    with open("./request.txt", "r") as request:
        result = request.read()
        if (result != sys.argv[1]):
            print(result)
    time.sleep(1)
    
with open("./request.txt", "w") as request:
    request.write("")
    