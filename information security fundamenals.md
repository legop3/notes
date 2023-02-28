# information security fundamenals

        1/17/23


## COMMUNICATION

- communication is easily disrupted
- computers are just a bunch of zeros and ones
- noise:
    - a common way for information to be intercepted


# SOCIAL ENGINEERING FUNDAMENTALS - CHAPTER 1

### Social enginerring is the act of manipulating users into revealing confidental information:
- social engineers rely on public informetion
    - OSINT - open source intelligence
- social engineering works because if the lack of user awareness, laziness, and - public networks

### Phishing:
- spear phishing - targets specific groups or individuals
- smishing involves sms phishing
- vishing is initiated by a phone call
- waling attacks the people at the top of a company

### Spam:
- spim is spam over the internet
- common from social media sites
- spam can also come from phone calls or SMS messages commonly

### Pharming:
- redirects a victim from a valid website to a malicious website that collects the users information
    
### Piggybacking:
- refers to when an unauthorized person is allowed by an authorized person to enter a secure location
- tailgating, a similar concept is the same thing without the permission of the authorized person


### Other social engineering techniques:

- Dumpster diving
- Shoulder surfing
- Eliciting information - people that are good at getting other people to willingly say things
- Prepending
- Identity fraud
- credential harvesting
- reconnaissance
- hoax - something that is just not true
- pretexting (or impersonation) - acting to be a different person
- eavesdropping - close enough to listen
- baiting - put something out there as a reward for someone to do something that will compromise themselves
- typo squatting - targeting common typos in web domains, like goggle.com and goole.com

### Principles of social engineering:
- motivation techniques used by social engineers:
    - authority - show confidence/authority, legal, organizational, or social authority
    - indimidation
    - consensus - social proof, research other employees, research about the business
    - scarcity - get yours before its gone -> urgency
    - familiarity - a person that youre familiar with could be used against you
    - trust... heightened trust leading to wrongdoing


### USER SECURITY AWARENESS EDUCATION:
- rules to convey when training employees:
    - never give out authentication details
    - always shield keypads when entering passwords
    - hide documents and devices when not at your desk
    - screen emails and phone calls, keep log of events
    - use encryption when possible (up to date encryption)
    - always shred sensitive information to be discarded
    - always comply with company policy regarding data handling and disposal
    - be careful when using a web browser

- social media - hybrid warfare:
    - threat actors use automated bots in social media sites like twitter and facebook to influence the sentiment of a given user:
        - bots used to manipulate public sentiment on modern issues like politics or abortion
    - hybrid warfare:
        - techniques to manipulate people to believe things that arent true
        - social engineering at a national level
        

# ANALYZING POTENTIAL INDICATORS TO DETERMINE THE TYPE OF ATTACK - CHAPTER 2
## malicious software/malware:
- malware is software that is designed to infiltrate a computer system
- types of malware:
    - ransomware - attacker restricts access, demanding payment - often in bitcoin.
        - cybersecurity insurance that covers paying off ransomware (crazy stuff) these insurance companies sometimes pay off attackers so that they dont attack a target.
    - phishing/spear phishing is a common vector for ransomware

    - trojan horses - appear to preform a desireable function but are actually performing malicious functions behind the scenes
    - remote access trojan (RAT) - most common trojan
        - attackers can eleevate their permissions on the target system

    - rootkit - software designed to gain administrator level control over a computer system without being detected
        - root user (linux) and administrator control (windows)
        - delayed/continued operations from the lower levels of the OS
    
    - worms - self-replicating, leveraging OS and application security holes and use similar os's and applications on the internet and replicate to them
    - fileless virus - stores no files on the computer, run through SSH or a RAT
        - attack may include files, targets weak endpoint security and ineffective access control
    - botnet - one computer controlling a bunch of infected computers or devices
        - bots are unaware of the malware installed on them, can be activated to create a DDOS attack (distributed denial of service)
    - logic bomb - programming malware to do a certian thing at a certain date, time, or condition
    
        
- password attacks:
    - password cracking
        - rainbow tables - a precomputed table used to reverse engineer a hash function and crack passords
        - plaintext - sniffing and keystroke logging, collecting unencrypted credentials
    - passwords are not usually stored as passwords, they are stored as hashes of passwords.
- physical attacks:
    - door access, access logs, video surveillance
    - types of physical attacks
        - malicious flash drives - killer usb
        - malicious usb cables - keystroke injection
        - card cloning attacks - RFID cards can be cloned
        - skimming - credit cards/RFID/NFC

- adversarial artificial intelligence/AI:
    - examples of adversarial techniques
        - tainted training data
        - overfitting attacks - when the machine memorizes its training data set, it will not generalize to new data.
        - transfer attacks
        - leveraging insecure implementations of machine learning algorithms: CIA, Confidentiality, Integrity, and Avaliability applies.

- supply-chain attacks:
    - in a supply-chain attack, the attackers target security weaknesses in the supply network

- cloud-based vs on-premises attacks:
    - cloud computing is very similar to traditional security
        - who has access? regulatory requirements? right to audit?
    - some types of cloud attacks
        - session hijacking - using an already logged in user to make a legit connection to the service
        - DNS attack - tricks users into visiting a phishing site and giving cridentials
        - XSS - stolen cookies are exploited to gain access
- cryptographic attacks:
    - collision attacks - MD5 hashes, low consumption requirement
    - birthday attack - the chances balance 366: 100%
    - 


        1/24/2023

# chapter 2

## AAA framework
Authentication, Authorization, and Accounting
- intelligently controlling access to computer resources, enforcing policies, auditing usage, and providing information nessescary for the audits

- authentication: find out who the person is
- authorization: find the person's access level
- accounting: log the activity of the user

vulnerable, vulnerable, vulnerable, vulnerable, vulnerable, vulnaerabel, vulnerable, vulnerable, vulnerable,  vulnerable, vulnerable


the what the when the who the whow the wyh the who the how thw whwn 


## types of clouds
- public cloud - apps and storage space
- private cloud - particular organization
- community cloud - hybrid cloud with multiple organizations sharing public cloud

###### wa
##### wa
#### wa
### wa
## wa
# wa


# chapter 10
fog and edge computing: 
edge computing:
- on the consumer side

fog computing:
- decentralized
- focusing on scalability and performance
- mesh stuff?

# chapter 12
- authentication methods
    - CIA: Confidentiality, intrgrity, and avalability
        - confidentiality: only people with authorization can access the data
        - integrity: verification of information (hashes probably)
        - availability: making sure access to the data is possible
    - authentication is NOT authorization
    - authentication *is* verifying the user's identity
    - authoriation verifies that the user has the correct permissions for the action

    - token
        - physical: an actual physical device
        - web tokens: digital process
    - two-step:
        1. user presents cridentials
        2. user recieves an encrypted token for a fixed period of time (one time token)
- biometrics
    - distinctive, measurable body measurments and calculations related to human characteristics
    - fingerprints
    - retinal scan
    - iris recognition
    - facial recognition
    - voice and speech recognition
    - vein authentication
    - gait analysis
    
- efficacy rates
    - bring the CER to the center
    - balance the false rejection vs false acceptance rates
    - FAR: false acceptcance rate
    - FRR: false rejection rate
    
- MFA (multi factor authentication)

- cloud based authentication
    - uses cloud services to authenticate using OAuth2 APIs
    - deployment, cost, control, security, compliance

# chapter 13
reduncany, backups, (non)persistance, on premises vs cloud, recovery
geographic dispersal of data assets

- disk redundancy:
    - raid 0 is only striping, high risk, high speed, lose one lose everything
    - raid 1 is exact copies, lower speed, high resilliancy, lose any disk and rebuild
    - raid 5 is striping and parity, more expensive, recoverable, lose one disk and rebuild
    - raid 6 is striping with dual parity, lose 2 disks and still rebuild
    - raid 10 is mirroring a striped set of disks, like a grid of raid 0 and 1

- network resilliancy
    - redundant switches and routers, IAAS
    - network interface teaming
        - grouping NICs so that each system can use any 
        - software NIC teaming is very inefficient
    - UPS
        - might automatically tell the server to shut down
    - generators
        - 800 to 500,000 watts
        - need sufficient platform, fuel supply, and power transfer equipment
- replication
    - duplicating virtual machines or containers
    - Host Bus Adapters (HBAs)
        - provide two paths to network storage
    - full backups, differential backups, incrimental backups
- non-persistance
    - data that is gone once you turn the system off
    - like stuf in RAM
    - revert to known sate, automatically reset to a known working state
    - last known good configuration, reset to a state where the computer worked correctly
- order to restore
    - connectivity
    - authentication
    - phone systems
    - CRM/SAP/HRM, people management stuff.
- diversity
    - redundancy
    - but with multiple ways to do things
    - failsafes on elevators and machines

#  chapter 14
SOC, RTOS, drones...
