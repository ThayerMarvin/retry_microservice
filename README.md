# Retry Microservice
How to send a request

Write a run command in the request.txt file. The command must follow this format: "run: n,command", where n is the number of times to run the command and command is the program you want to execute.

    with open('request.txt', 'w') as f:
        f.write("run: 5,python test_program.py")

How to receive the results

Results can be read directly from the result.txt file.

    with open('result.txt', 'r') as f:
        results = f.read()




