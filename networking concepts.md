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
        - data unit is a bit
        - simplest layer
        - transmitted as RF, copper, or light
    2. data link
        - nic and switch
        - responsible for interfacing with physical hardware
        - protocols at this layer are programmed into the NIC's firmware
        - ethernet and wifi are examples
        - puts control information in a link layer header and at the end of the packet in a trailer
        - data unit is a frame
        - MAC address (media access control) - hardware address of the source and destination NICs
    3. network
        - router
        - moves messages from one node to another
        - identifies each host
        - finds the best route to take
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