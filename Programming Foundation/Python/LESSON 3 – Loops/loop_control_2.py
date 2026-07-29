#continue Skips the current iteration.
for port in range(20, 25):
    if port == 22:
        continue
    print(f"Checking port: {port}")