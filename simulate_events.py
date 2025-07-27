
import time
import random

# Mock AD events to simulate suspicious behavior
events = [
    "User login success",
    "User login failed",
    "Kerberoast attempt",
    "Privilege escalation detected",
    "Suspicious PowerShell command executed"
]

def generate_event():
    """Randomly selects and returns a fake AD event."""
    return random.choice(events)

if __name__ == "__main__":
    print("🚨 Starting AD Event Simulator...")
    while True:
        event = generate_event()
        print(f"[{time.strftime('%H:%M:%S')}] 🚨 Event Detected: {event}")
        # TODO: Replace with real log parsing from Windows Event Logs
        time.sleep(2)
