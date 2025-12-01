import os
import time
import subprocess

LOG_DIR = os.path.dirname(os.path.abspath(__file__))
REQUEST_FILE = os.path.join(LOG_DIR, "request.txt")
RESULT_FILE = os.path.join(LOG_DIR, "result.txt")

def write_result(status, message):
    with open(RESULT_FILE, "w") as f:
        f.write(f"{status}: {message}\n")

def run_program_n_times(n, command):
    successes = 0
    failures = 0

    for i in range(n):
        try:
            print(f"Running attempt {i+1}/{n}...")
            subprocess.run(command, shell=True, check=True)
            successes += 1
        except Exception as e:
            failures += 1

    return successes, failures

def parse_request(line):
    if not line.startswith("run:"):
        raise ValueError("Invalid command format.")

    parts = line.replace("run:", "").strip().split(",", 1)

    n = int(parts[0].strip())
    command = parts[1].strip()

    return n, command

def main():
    print("Microservice running.")

    while True:
        if os.path.exists(REQUEST_FILE):
            try:
                with open(REQUEST_FILE, "r") as f:
                    request = f.read().strip()

                n, command = parse_request(request)
                print(f"Received request: run '{command}' {n} times")

                successes, failures = run_program_n_times(n, command)

                write_result("SUCCESS", 
                    f"Completed {n} runs. Success: {successes}, Failed: {failures}")

            except Exception as e:
                write_result("ERROR", str(e))

            open(REQUEST_FILE, "w").close()

        time.sleep(1)

if __name__ == "__main__":
    main()