Postmortem
Report for 503 Service Unavailable
Issue Summary
We have been working on developing some services and adding some services to the new website and updating the security system, but some users encountered some problems while visiting the website. This was unexpected for us and for the user as well, but it happened and it was that this service was not available despite its work. Correctly, we have received a log report about this problem in may15th, 2024 at 1 AM the server access went down resulting in 503 error for anyone trying to access  website
Timeline
•	01:00 GMT+3 - 503 error when  trying to access to website.
•	01:05 GMT+3 - Check server maintenance.
•	01:10 GMT+3 - Fix faulty firewall conf.
•	01:12 GMT+3 - Sift through logs server side.
•	01:18 GMT+3 - Reboot server.
Root Cause
The firewall has been reviewed and verified to be working properly. 
We reviewed the pages where the malfunction occurred and ensured that they were working properly. 
The project's code was reviewed, errors were confirmed, and they were comprehensively corrected.
A simulation was performed for the user and it was ensured that the fault was removed correctly.
There have been some updates on the server and they have been completed. Some errors occurred in the log and the server was unable to restart automatically. This was done manually and it worked.
Resolution and recovery
•	We have created a force to restart automatically after any update if the server does not respond for 30 seconds 
•	We avoided updates during peak times and official business hours 
•	Ensure that all services are working efficiently, and if one of them does not work, return to the stable restore point until it is presented to the specialist.