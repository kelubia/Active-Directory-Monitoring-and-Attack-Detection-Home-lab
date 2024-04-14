# Active-Directory-Monitoring-and-Attack-Detection-Home-lab

Introduction:
It is crucial to have a thorough comprehension of Active Directory (AD) security measures to safeguard organizational assets, ensure compliance with regulations, and mitigate cyber threats. AD is the foundation of Windows-based network environments, as it oversees resource access, manages user identities, and enforces security policies. By understanding the intricacies of AD security, organizations can strengthen their security posture and protect themselves against various cyber threats.

Active Directory (AD) is crucial to many organizations' IT infrastructure. As such, ensuring its security and protection against cyber threats is essential. One way to achieve this is by setting up an AD Monitoring and Attack Detection Home lab. This simulated environment can help you assess the effectiveness of different monitoring tools, detection mechanisms, and incident response procedures that you can use to defend against malicious activities within AD.

By creating this lab, I can test and fine-tune my existing security controls, such as intrusion detection systems, SIEM solutions, and EDR tools. Additionally, I can practice my incident response procedures in a safe environment and enhance my ability to detect and respond to security threats effectively. 

The home lab also allows me to deploy and test different monitoring solutions, such as network traffic analyzers, log management systems, and threat intelligence platforms. By continuously monitoring and analyzing AD activity logs, I can identify possible security weaknesses, abnormal patterns, and indicators of compromise (IOCs) that may indicate malicious activity. 

Conducting regular AD monitoring and attack detection exercises can help me validate my security posture and readiness to defend against cyber threats. By proactively identifying vulnerabilities and gaps in security controls, I can implement necessary remediation measures to strengthen my security posture and resilience against cyber attacks. In summary, an AD Monitoring and Attack Detection Home lab can help me improve my security posture and prepare me for any potential cyber threats.

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

