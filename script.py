import time
import sys

def main():
    print("Starting test script...")
    for i in range(5):
        print(f"Processing step {i + 1}")
        sys.stdout.flush()
        time.sleep(1)
    print("Script completed successfully!")

if __name__ == "__main__":
    main() 