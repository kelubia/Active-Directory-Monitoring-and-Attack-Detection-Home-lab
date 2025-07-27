🏰 Active Directory Monitoring & Attack Detection Lab
Because hackers don’t take vacations, and neither should your AD security skills.

# 🏰 Active Directory Monitoring & Attack Detection Lab  
> _Because hackers don’t take vacations, and neither should your AD security skills._  

This repo is your **hands-on Active Directory (AD) security playground**, where you can:  
✅ Build and simulate an AD environment  
✅ Detect real-world attacks (Kerberoasting, Pass-the-Hash, etc.)  
✅ Practice incident response, SIEM monitoring, and log analysis  
✅ Benchmark detection speed vs. reality  
✅ Add some ✨ AI-powered anomaly detection ✨ (because, why not?)  

---

## 📖 Table of Contents
1. [What is This Lab?](#what-is-this-lab)
2. [Architecture Diagram](#architecture-diagram)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [How to Set Up](#how-to-set-up)
6. [Python Scripts](#python-scripts)
7. [Simulation vs Reality Benchmark](#simulation-vs-reality-benchmark)
8. [Screenshots & Demo](#screenshots--demo)
9. [How to Contribute](#how-to-contribute)
10. [License](#license)

---

## 💡 What is This Lab?
Active Directory is the **brain** of most corporate networks. This lab lets you:  
- **Simulate AD attacks** safely in a home lab  
- **Practice monitoring logs & detecting malicious activity**  
- **Fine-tune SIEM, EDR, and threat-hunting tools**  
- **Build a real-time dashboard to visualize AD activity**  

---

## 🛠 Architecture Diagram 
_(Built using Draw.io – free to copy and edit!)_

**Components:**  
- 🖥 Domain Controller (Windows Server)  
- 💻 Attacker Machine (Kali Linux / Metasploit)  
- 📈 SIEM (Wazuh / Splunk / ELK Stack)  
- 🛡 EDR Agent  
- 🐍 Python-based log monitor & dashboard  

---

## ✨ Features
🔍 **Real-time log monitoring**  
⚔️ **Simulated AD attacks (Kerberoasting, Pass-the-Hash, DCSync)**  
📊 **Grafana / Kibana dashboards**  
🤖 **Optional AI anomaly detection**  
🎓 **Tutorial-friendly setup for students, blue teamers, and homelab nerds**  

---

## ⚙ Tech Stack
- **Windows Server 2019/2022** (Domain Controller)  
- **Kali Linux** (Attack Box)  
- **Python 3.10+** (Log parsing, AI-based detection)  
- **Elastic Stack (ELK) or Grafana** (Dashboards)  
- **Wazuh / Sysmon** (Monitoring & SIEM integration)  

---

## 🚀 How to Set Up
1. Clone the repo:  
   ```bash
   git clone https://github.com/YOURNAME/Active-Directory-Monitoring-and-Attack-Detection-Home-lab.git
   cd Active-Directory-Monitoring-and-Attack-Detection-Home-lab


Prerequisites:
in Draw.io I created the detailed visuals of our network.

![Active Directory Monitoring and Attack Detection Home lab](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/68d91304-34ef-45d9-b359-833730081bdf)


Domain: MyDFIR
Network: 192.168.10.0/24
Splunk Server Sysmon Atomic red Team: 192.16.10.10
Active Directory Splunk universal forwarder Sysmon: 192.16.10.7
Kali Linux Attacker: 192.16.10.250



-Setting Up the Virtual Environment: We created and installed kali linux on our VirtualBox.
I also created VMs for the Active Directory Domain Controller and Member Server. I'll attach the screenshots and processes.
enjoy
I skipped the AD domain and server installations

![1](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/569ba990-7ef7-46dc-9c9e-a9fdbc38ff3c)

![2](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/ce1919f6-ed30-4153-ae7d-f91ce14bada3)

One way to gain a deeper understanding of software performance and behavior is by utilizing Splunk. With this tool, you can capture, generate, and export telemetry data to observability tools, allowing for a more comprehensive analysis. Additionally, it's important to continuously monitor your AD infrastructure using various monitoring tools and techniques. This will enable you to detect potential security threats and anomalies early on, helping to keep your systems safe and secure.
Now install our Splunk server.
![3](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/fc16d0b3-3ce1-401c-8153-1b1b3911a019)
![4](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/244f3ae8-604d-47ad-ab19-0b44837fc0b6)

Network Configuration:
I configured network settings for VMs on VirtualBox, including IP addressing and DNS resolution.
![5](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/f0bbfb8b-d55b-4a7e-9ebf-0782445c6759)


Now, I can go ahead and install our Splunk server.

![6](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/3c45c8cc-4fbf-4b86-8e9a-1c3e7c456a64)
![7](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/c6a2fded-8bb5-4d1b-834a-ea166cbb8725)
![8](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/61850e6a-b339-4386-89b0-9a1af3a1fe2c)
![9](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/6ed7239f-730c-49ae-b3f1-a40a2074b95a)

With Splunk up and running, we will install the Splunk universal forwarder and sysmon on our target machine and our server.
![10](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/b63d1413-40af-4f86-a0fd-f16df6d399fa)
![11](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/592d1eba-3b91-45e8-bdad-4ee2b39c4ea9)


instruct my splunk forwader on what i need to send to my splunk Server using input.conf in the etc/system/local file
![12](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/9ceb9040-cd15-4301-9c13-db5bcbc0321a)

can![13](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/e147f35c-fa90-41c4-a827-7aa421355f19)

[WinEventLog://Application]
index = endpoint
disabled = false
[WinEventLog://Security]
index = endpoint
disabled = false
[WinEventLog://System]
index = endpoint
disabled = false
[WinEventLog://Microsoft-Windows-Sysmon/Operational]
index = endpoint
disabled = false
renderXml = true
source = XmlWinEventLog:Microsoft-Windows-Sysmon/Operational

![14](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/37842ec1-a7fe-4826-9cfb-a6e0ce881a13)
![15](https://github.com/kelubia/Active-Directory-Monitoring-and-Attack-Detection-Home-lab/assets/98921903/509579cb-a7a4-4af5-ae02-bbc4fdc13161)
I ran into an issue of simultaneously running the Splunk server and Windows target machine together on my PC.
sooo on to the cloud we go..... ( not ready to buy a new pc meow)

