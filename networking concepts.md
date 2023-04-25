# networking concepts

        1/19/23

## chapter 1: introduction to networking
### objectives:
- identify types of applications and protocols
- distinguish between client-server and P2P
- describe various hardware and physical topologies
- describe 7 layers of the OSI model
- explore best practices for safety when working with networks and computers
- describe the 7 step troubleshooting model for solving a networking problem


### how networks are used
- network resources - the resources a network makes avaliable to it's users
    - includes applications and the data provided by these applications

### client-server applications
- web service
- email service
- FTP service
- telnet service
- remote desktop
- remote applications

SMTP is also sendmail
POP3 - post office protocol v3, also recivemail
IMAP - internet messaging application protocol, also recievemail

### file and print services
- file services: a server's ability to share data files
- file server: a computer that provides file services
- print servoces: aiblity to share printers across a network
    - with one printer less time is spent on maintinence


### communication services
- convergence: using the same network to delover multiple communication services
- unified communications - refers to the centralized management of multiple communications
- 3 types of communication services
    - VOIP
        - delay sensitive
        - loss tolerant
        - QoS (quality of service) is important for VOIP
    - streaming live audio and video
    - streaming stored audio and video

### controlling network access
- pysical topology - mostly applies to hardware 
- logical topology - has to do with software and describes how access to the network is controlled

### peer to peer model
- p2p is where each computer is in charge of its own access to resources
    - no centralized control
- computers are called nodes or hosts, they form a logical group of users
    - may share resources
    - may prevent access to resources
- each computer user has a windows local account
    - works only on that computer
- advantages
    - simple configuration
    - less expensive, no server to buy
- disadvantages
    - not scalable
    - not nessecarily secure
    - not practical for large installations
- microsoft says 10 or less individuals on the system

### client server model
- a user can sign in to the network from any computer on the network
    - AD DS (active directory domain services)
- NOS is responsible for
    - managing clients data
    - ensures authorized user access
    - controls user file access

### LANs
office or building means LAN
internet, multiple countries, multiple states means WAN
- a LAN can have several switches
- metropolitain area networking (MAN)
    - 

### the seven layer OSI model
TCP is connection oriented, makes sure it gets there
UDP is connectionless, doesnt care if it gets there
ethernet and wifi are layer 2 connections
MAC address means physical
- OSI (open systems interconnection) reference model: a seven layer model developed to categorize the layers of communication
    1. physical
        - hub
        - simplest layer
        - transmitted as RF, copper, or light
        - data unit is a bit

    2. data link
        - switches are ALWAYS layer 2 on a test
        - nic and switch, ARP, and cabling
        - responsible for interfacing with physical hardware
        - protocols at this layer are programmed into the NIC's firmware
        - ethernet and wifi are examples
        - puts control information in a link layer header and at the end of the packet in a trailer
        - MAC address (media access control) - hardware address of the source and destination NICs
        - data unit is a frame

    3. network
        - router
        - moves messages from one node to another
        - identifies each host
        - finds the best route to take
        - IP
        - data unit is a packet

    4. transport
        - transporting application layer payloads from one application to another
        - encapsulation: adding a header to data from the above layer
        - if message too large TCP devides it, called a segment
        - data unit is a segment in TCP or a datagram in UDP

    5. session
        - data unit is a payload

    6. presentation
        - responsible for reformatting, compressing, encrypting, and decrypting data
        - graphics are also in the presentation layer
        - data unit is a payload

    7. application
        - describes the interface between applications on seperate computers
            - SMTP
            - FTP
            - SNMP
            - payload: the data that is passed between applications and the OS
        - data unit is a payload


# 
        1/24/23

PDU: protocol data unit - the technical name for a group of bits as it moves from one layer to the next and from one LAN to the next
- technicians loosely call this group of bits a message or a transmission

### chapter 2
How computers find each other on networks

MAC addresses
- first 24 bits are known as the OUI (organizationally unique identifier)
    - assigned by the IEEE
    - each manufacturer has an OUI
- last 24 bits make up the extension identifier or device ID
    - manufactarers assign each NIC a unique device ID


classes of ip address

class A: 1.x.y.z to 126.x.y.z           126 networks         16,777,214 addresses per network
class B: 128.0.x.y                      16,000 networks      65,000 addresses per network
class C: 192.0.0.x to 223.255.255.x     2,097,152 networks   254 addresses per network

127.0.0.1 is loopback

APIPA: automatic private addressing, used when DHCP server doesn't work.
range 169.254.0.1 to 169.254.255.254

a double colon in an ipv6 address means that block is all zeros
0000 and :: mean the same thing
an address can only have one double colon

TCP OSI data units:
data -> segment -> packet -> frame -> bit

best path = router
routing metrics: the lowest cost provides the best path
NetBIOS is microsoft

# chapter 4
structured cabling and networking elements

- maximum distance for ethernet cable is 100 meters/ about 330 feet without an amplifier
- 802.3 is wired standard, 802.11 is wireless standards

- full duplex: signals can travel both directions over a medium simultaneously
- half duplex: signals can travel in both directions but only in one direction at a time
- simplex: signals can only travel in one direction

- 4 properties of an analog signal
    - amplitude: measure of strength at any given point
    - frequency: number of times amplitude cycles over time
    - wavelength: distance between one peak and the next
    - phase: progress of wave over time compared to a fixed point

- throughput: the amount of data transmitted during a given time period (called payload rate or effective data rate), the current transfer rate
- bandwidth: difference between the highest and lowest frequencies, static

STP and UTP can transmit at the same rate

EMI: electromagnetic interference, also RFI: radio frequency interference
crosstalk: noise generated across twisted pair wiring
- alien crosstalk: occurs between two cables
- near cross talk: occurs near source
- far end crosstalk: occurs at the far end

scatter, refraction, reflection are issues in wifi

mac address is 48 bits

MAC sublayer and link control in 802.11

"a lot of people weren't really smart back in the day"

AAA: authentication, authorization, accounting

MFA factors:
- knowledge: something you know
- possession: something you have
- inherence: something you are
- 

# chapter 10: networking segmentation and virtualization
- supernetting??????
## segmentation
- dividing a network into multiple smaller networks
- traffic on one network is seperated from another network's traffic
- each network is.. 
- all classes can be subnetted
- https://subnetting.net for practice

## supernetting
- combine contiguous networks that use the same CIDR block into one supernet
- also calld classless routing

network bits are the ones at the beginning, host bits are the zeroes at the end.

# windows server :)
- Domain Name System
- Dynamic Host Configuration Protocol
- Cloud omputing
  - a collection of technology
- FAT - file allocation table (32: 32 gigabytes)
- NTFS - new technology file system
- ## Active Directory
  - the doundation of a windows netowkr environment. enables administrators to create and manage users and groups, set network-wide user and computer policies
- resillient file system
  - a file system that is compatible with NTFS but does not have compression, disk quotas
- ## file and sharing print functions
  - share permissions
  - different than NTFS permissions
  - read
    - view files, copy files, view attributes of file
  - change
    - all permissions of read, plus changing files and folders, change contents, and delete files and folders
  - full control
    - all permissions of change, plus being allowed to change the permissions, change owners of files and folders
  - 
- ## NTFS permissions
  - read - can read files and attributes. can't run executables
  - read and execute - same as read, can run executables
  - list folder contents - 
  - write
  - modify - everything but full control
  - full control - everything, including changing permissions and taking ownership
- ## chapter 6: directory service
  - LDAP
    - lightweight directory access protocol
    - DAP with tcp/ip
  - hierarchical organization
    - makes managament of policies easier
    - scalability
    - security
    - flexibility
    - policy based administration
  - logical structure
    - organizaitonal units
      - groups of people
        - students, faculty, administration
        - contains and groups people, computers, and printers
    - domains
      - a campus, an office building
      - contains the organizational units
    - trees
      - a collection of domains
    - forests
      - a collection of trees
  - folder objexts
    - built in
      - administrator and guest accounts built in
      - cant disable the administrator account
    - computers
    - foreign security principles
    - managed service accounts
    - users
      - stores two default users, several default groups
  - domain objects
    - a leaf object is a user, or a printer
- ## chapter 10
  - 



# final exam study:
cengage 2-1j: expanding your network
cengage 2-2j: when not to use server core (minimal server without GUI)

report:
intro: state your problem
main topic: solve your problem
conclusion: mitigate the problem

quiz:
network+ 7,8,10
windows server chapter 1

class a: 1-126
class b: 128-191
class c: 192-223