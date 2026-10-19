with open("event_log.txt", "w") as f:
    f.write("Event processing started...\n")
    f.write("Loading attendee data...\n")
    f.write("Generating ticket summary...\n")


with open("event_log.txt", "a") as f:
    f.write("Finalizing event schedule...\n")
    f.write("Event processing completed.\n")


with open("event_log.txt", "r") as f:
    content = f.read()
    print("Complete File Content:\n", content)


with open("event_log.txt", "r") as f:
    for line in f:
        print(line.strip())
