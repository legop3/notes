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


# physical access

# chapter 20: installing and configuring wireless security settings
## crypeographic protocols
- WPA2 (wifi protected access 2), or WPA3
  - 128 bit key, 48 bit initialization vector
  - includes support for counter-mode/CBC-MAC protocol (CCMP)
    - MAC is a hash that authenticates the whole process
  - includes AES-based symmetric encryption
  - can be used in PSK (pre shared key) mode, but you shouldn't
  - can also be used in enterprise mode with an authentication server like RADIUS
  - introduced in 2004
- CBC-MAC
  - CCMP, 128 bit keys
- WPA3
  - introduced in 2018
  - 192 bit minumum protocol strength
  - 256 bit galois
  - 384 bit hashed message authentication code
  - elliptic curve digital signature algorithm is supported
- simultaneous authentication of equals
  - 4 way handshake
  - perfect forward secrecy, each communication creates a new key

# chapter 23: implimenting identity and account management controls
- federation
  - principal - the end user themselves, the person who is asking to be authenticated
  - service provider (SP) - the service that the user is logging into, like spotify, google
  - identity provider (idP) - 
    - SAML
    - OAuth2
    - OpenID connect
  - assertion - information produced by the authentication authority to allow the user to do things
  - type 1 error: False Rejection Rate: FRR
  - type 2 error: False Acceptance Rate: FAR
  - crossover rate: equal FRR or FAR indicates quality
  - privilage creep: you may begin to do things that you really aren't supposed to do

# chapter 24: implementing authentication management protocols

# chapter 25: implementing public key infrastructure
- PKI is the systems of people, hardware, software, and policies.
  - creates asymmettic key pairs
- a certificate authority
  - the entity that issues certificates to users
  - most PKI systems use a CA
  - browser shows various indicators when the website is secure
    - a padlock in the locked position is shown when secure
    - the lock shows certificate information when clicked
- types of certificates
- certificate formats
- PKI is meant to develop a trust model
  - decentralized
  - peer to peer
- certificate pinning
  - checks the hashed public key in the server's certificate against a public key used for the server's name
- stapling
  - allows the presenter of the certificate to bear the cost involved when providing OCSP responses
- key escrow: a copy of the user's private key is stored
  - prevents unacceptable data loss
  - allows the government to access your encrypted data
- key recovery agent
  - lost or corrupted keys can be restored
- if a root CA is compromised, all of it's certs are compromised
  - add a layer of security by setting up a root CA that is offline unless needed

# chapter 26; "reading the dictionary"
- no.
# chapter 27: summarizing the importance of policies processes and procedures for incident response.
- incident response plan: a set of instructions to recover from a cybersecurity incident
- the plan ensures that the right people are in place to deal with a threat
- failure to implement a plan can have legal repercussions
- the computer security incident response team (CSIRT) must have skills to deal with the situation
- develop playbooks: provide guidance to the SOC when triaging an incident
- playbooks and procedures should be tested with the teams that will use them
- tabletop exercise
  - the group thinking through what would happen, who would do what
  - missing the realism and stress of actually doing it
- runbooks: an automated response that are based on what's happening
- IRP based on PIR

# chapter 28
- run vulnerability scans often
  - it only takes one exploitable vulnerability
  - programmers are people and people make mistakes
- SIEM dashboard
  - sends alerts
- SIP: voip signaling protocol
# chapter 32
- what is purposeful focus?
- regulations, standards, legislation
  - what is the target?
  - laws affect and protect the privacy of individuals
  - how data is classified
  - how employees are expected to behave
  - how to dispose of IT equipment
  - GDPR - general data protection regulation
    - EU's law about PII
- key frameworks - how do we make it happen?
  - benchmarks and secure configuration guides
    - instruction manuals for hardware or software
    - tells what secure configuration looks like
    - security content automation protocol (SCAP)
      - standardized solution for security automation
  - framework standards
    - employees must abide by them
    - a single cohesive agenda
      - cohesive
  - center for internet security
  - international organization for standardization
    - ISO
  - standards of attestations engagement (SSAE)
  - cloud security alliance (CSA)
  - national institute of standards and technology (NIST)
- policy
  - how do we get granularity?
  - HIPAA!
# chapter 33
- training techniques
  - gamification
  - capture the flag
  - phishing campaigns
  - phishing simulations
  - computer based training
  - role-based training
    - different schemes for finance or HR department
  - all employees should be trained on PII
- data concepts
  - sensitive data is sensitive
  - classified
  - non-classified
  - public information
    - everyone can get it anyway
  - internal information
  - confidential information
  - secret information
  - top secret information
    - nation-level information
# chapter 34 - risk management
- risk types
  - malicious attacks
  - natural threats
  - manmade threats
  - vulnerabilities can be exploited
  - external risk
    - biggest concern to most organizations
  - internal risk
    - stems from those internal to the organization
  - theft of intillectual property
    - primary goal of internal and external threat actors
  - multiparty
    - external actors working with internal actors
- manaagement strategies
  - mitigate the risk 
    - down to an acceptable level according to the organization
  - transfer the risk to someone else
  - avoid the risk by not installing it
    - lost oppurtunity
  - accept all or some consequences of a risk
  - cybersecurity insurance
  - risk management
    - information assurance
- risk analysis
  - steps
    - 1: identify organizations assets
    - 2: identify the vulnerabilities
    - 3: identify threats and threat likelihood / probability
    - 4: identify monetary impact
  - risk matrix / heat map
  - risk appetite
    - how much risk are you willing to have?
  - control risk
    - the control that you put in place may not work to protect the environment
  - risk awareness
    - ability to identify risks before they become threats
  - qualatative risk assessment
    - scale of 1-10 or 1-100
    - likelihood
    - impact
    - likelihood * impact = qualatative risk
  - quantatative risk
    - single loss expectancy (SLE)
      - monetary amount
      - for one loss of a server
    - annualized loss expectancy (ALE)
      - how many servers will we lose a year?
    - annualized rate of occurance (ARO)
      - ALE * SLE = ARO
  - disaster analysis
    - fire
      - supressants - clean agent fire extinguisher safe for people and equipment
    - flood
      - location dependent
  - MTBF
    - mean time before failure
    - average number of failures per million hours of operation
  - MTTR
    - mean time to repair
  - MTTF
    - mean time to failure
  - single point of failure
    - if it fails, the whole thing fails
    - this is what you should mitigate
  - 