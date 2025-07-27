
import random
import time

# Simple anomaly detection mock-up
def detect_anomaly(event):
    """Mock AI anomaly detection."""
    anomalies = ["Kerberoast attempt", "Privilege escalation detected"]
    return event in anomalies

events = [
    "User login success",
    "User login failed",
    "Kerberoast attempt",
    "Privilege escalation detected"
]

if __name__ == "__main__":
    print("🤖 AI Anomaly Detector Running...")
    while True:
        event = random.choice(events)
        is_anomaly = detect_anomaly(event)
        print(f"[{time.strftime('%H:%M:%S')}] Event: {event} | Anomaly: {is_anomaly}")
        time.sleep(2)
