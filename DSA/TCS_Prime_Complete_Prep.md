# TCS Prime — Complete Preparation Document

> Single offline-readable reference. Everything in one place.
> Table of contents at top for quick navigation.

## Table of Contents

1. [OOP (Object-Oriented Programming) — Python focused](#1-oop-python-focused)
2. [Computer Networks](#2-computer-networks)
3. [Operating Systems](#3-operating-systems)
4. [DBMS and SQL](#4-dbms-and-sql)
5. [Python — Resume-Level Questions](#5-python)
6. [NumPy and Pandas](#6-numpy-and-pandas)
7. [Machine Learning Foundations (Supervised Learning)](#7-ml-foundations)
8. [Linear Algebra and Probability Basics](#8-linear-algebra-and-probability)
9. [Hugging Face and Transformers](#9-hugging-face-and-transformers)
10. [Requirement Engineering](#10-requirement-engineering)
11. [DSA — Must-Know Patterns](#11-dsa-patterns)
12. [Project Questions Based on Your Resume](#12-project-questions)
13. [HR and Behavioral](#13-hr-and-behavioral)
14. [Final Interview-Day Checklist](#14-final-checklist)

---

# 1. OOP (Python focused)

## The Four Pillars

**Memorize this order: Encapsulation, Inheritance, Polymorphism, Abstraction.**

### Interview one-liner (have this ready)

> "The four pillars of OOP are Encapsulation, Inheritance, Polymorphism, and Abstraction. Encapsulation is bundling data and methods together while hiding internal state. Inheritance lets one class derive from another. Polymorphism means the same method can behave differently based on context. Abstraction means exposing only what is necessary and hiding implementation details."

---

## 1.1 Class and Object

- **Class** — a blueprint. Defines what an object looks like and what it can do. No memory taken until an object is created.
- **Object** — an instance of a class. Has its own state and occupies memory.

### Python Example

```python
class Car:
    def __init__(self, color, speed):   # __init__ is the constructor
        self.color = color               # self = this object
        self.speed = speed
    
    def start(self):
        print(f"{self.color} car is starting at {self.speed} km/h")

my_car = Car("Red", 60)                  # object creation
my_car.start()
```

### Key concepts

- **`self`** — refers to the current instance. Equivalent to `this` in Java. Must be the first parameter of every instance method.
- **`__init__`** — Python's constructor method. Runs automatically when an object is created.
- **`__str__`** — defines how the object is printed when you use `print(obj)`.

### Likely questions

**"What is the difference between a class and an object?"**
> A class is a blueprint — a definition. An object is an actual instance of that class with its own data, stored in memory.

**"What is `self` in Python?"**
> It is a reference to the current instance of the class. Python passes it automatically when you call a method on an object. It lets a method access the object's own attributes and other methods.

**"What is a constructor?"**
> A special method that runs automatically when an object is created. In Python, it is `__init__`. Used to initialize the object's attributes.

---

## 1.2 Encapsulation

**Definition:** Bundling data and the methods that operate on that data into one unit (a class), while hiding the internal state.

**Python's convention for access control** (Python does not have strict `private`/`public` like Java):

| Naming | Meaning |
|---|---|
| `name` | Public — accessible anywhere |
| `_name` | Protected by convention — "internal use only" |
| `__name` | Private — Python name-mangles it to `_ClassName__name` |

### Example

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0          # private (name-mangled)
    
    def deposit(self, amount):       # public interface
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

### Likely questions

**"What is encapsulation?"**
> Encapsulation is bundling data and methods into one unit and hiding internal state. In Python, I use naming conventions — a single underscore signals protected, double underscore triggers name-mangling for privacy. Access is controlled through public methods like getters and setters.

**"Why encapsulation?"**
> Three reasons. First, it prevents invalid modification of state. Second, it lets me change internal implementation without breaking code that uses the class. Third, it makes debugging easier because all modifications go through controlled methods.

---

## 1.3 Inheritance

**Definition:** A mechanism where one class derives properties and methods from another. Creates an "is-a" relationship.

### Types of Inheritance

1. **Single** — one child inherits from one parent.
2. **Multilevel** — chain: `C inherits B inherits A`.
3. **Hierarchical** — multiple children share one parent.
4. **Multiple** — one child inherits from multiple parents. **Python supports this directly** (unlike Java).
5. **Hybrid** — combination.

### Python Example

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):                       # single inheritance
    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Rex")
d.eat()      # inherited from Animal
d.bark()     # defined in Dog
```

### Method Resolution Order (MRO) and the Diamond Problem

**The Diamond Problem** — happens with multiple inheritance. If class D inherits from B and C, and both B and C inherit from A, which A gets inherited?

```
      A
     / \
    B   C
     \ /
      D
```

Python solves this using the **C3 linearization algorithm**, visible via `ClassName.__mro__`. Python walks the MRO left-to-right, depth-first, while preserving consistency.

### Likely questions

**"What is inheritance?"**
> Inheritance allows a class to derive attributes and methods from another class, establishing an 'is-a' relationship. It enables code reuse — a Dog class inheriting from Animal gets all Animal's behavior for free and only adds Dog-specific things.

**"Does Python support multiple inheritance?"**
> Yes, Python supports multiple inheritance directly — a class can inherit from multiple parent classes. Java does not allow this with classes to avoid the Diamond Problem, and instead uses interfaces. Python solves the Diamond Problem using the C3 linearization algorithm, accessible via the class's `__mro__` attribute.

**"What is the Diamond Problem?"**
> It is an ambiguity in multiple inheritance. If class D inherits from B and C, and both B and C inherit from A, then when D calls a method defined in A, it's ambiguous which path to use. Python resolves this deterministically using MRO.

**"What is MRO?"**
> Method Resolution Order — the sequence Python follows when looking up methods in a class hierarchy. For multiple inheritance, it uses the C3 linearization algorithm — roughly left-to-right, depth-first, while preserving consistency. You can inspect it with `ClassName.__mro__`.

---

## 1.4 Polymorphism

**Definition:** "Many forms" — the same interface behaves differently depending on the context.

### Two types

1. **Compile-time (Static) Polymorphism** — Method Overloading. Same method name, different parameters. **Python does not natively support method overloading** — the last defined method overrides earlier ones. You can simulate it using default parameters or `*args`.

2. **Run-time (Dynamic) Polymorphism** — Method Overriding. A child class provides its own implementation of a method defined in the parent class.

### Python Example (Method Overriding)

```python
class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof")          # overrides parent's sound()

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()                  # calls correct version based on actual object
```

### Duck Typing (Python-specific)

> "If it walks like a duck and quacks like a duck, it's a duck."

Python does not check an object's type — it only checks whether the object has the required methods. This is a form of polymorphism.

### Likely questions

**"What is polymorphism?"**
> Polymorphism means 'many forms' — the ability to use the same interface for different underlying forms. In practice, it lets me write code that works with a general type and behaves correctly regardless of the specific subclass. For example, I can loop over a list of animals and call `sound()` on each — each type knows its own implementation.

**"Difference between overloading and overriding?"**
> Overloading is defining multiple methods with the same name but different parameters — it happens within one class. Overriding is when a child class provides its own version of a method defined in the parent class — it happens across classes. Overloading is compile-time; overriding is run-time. Python does not support traditional overloading — I simulate it with default arguments or variable-length arguments.

**"What is duck typing?"**
> Python's philosophy that type is determined by behavior, not by explicit class. If an object has the methods I need, I can use it — I don't check its class. This is a flexible form of polymorphism.

---

## 1.5 Abstraction

**Definition:** Showing only essential features and hiding implementation details.

### Two ways in Python

1. **Abstract classes** — using the `abc` module. Cannot be instantiated directly; must be subclassed.
2. **Interfaces** — Python does not have a formal `interface` keyword like Java. Abstract classes with only abstract methods serve the same purpose.

### Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):                 # abstract class
    @abstractmethod
    def start(self):
        pass                         # no implementation
    
    def stop(self):                  # concrete method
        print("Vehicle stopped")

class Car(Vehicle):
    def start(self):
        print("Car started")         # must implement abstract method

c = Car()
c.start()
c.stop()

# v = Vehicle()  # ERROR — cannot instantiate abstract class
```

### Likely questions

**"What is abstraction?"**
> Abstraction means exposing only what is necessary and hiding implementation details. Users of a class know what it does but not how it does it. In Python I use the `abc` module's `ABC` class and `@abstractmethod` decorator to create abstract classes that cannot be instantiated directly — they must be subclassed.

**"Difference between abstract class and interface?"**
> An abstract class can have both abstract methods (no implementation) and concrete methods (with implementation). An interface has only method signatures — no implementation. Java differentiates them clearly. Python does not have a formal `interface` keyword, but abstract classes with only abstract methods effectively serve as interfaces.

**"Difference between Abstraction and Encapsulation?"**
> Encapsulation is about bundling data and methods and controlling access to internal state — it's a code-organization concept. Abstraction is about hiding implementation complexity from the user — it's a design concept. Encapsulation is the 'how' of hiding; abstraction is the 'what'.

---

## 1.6 Advanced OOP Concepts

### Static Methods and Class Methods

```python
class MyClass:
    count = 0                        # class variable (shared)
    
    def __init__(self):
        self.instance_var = 10        # instance variable
    
    def instance_method(self):        # receives self (the object)
        pass
    
    @classmethod
    def class_method(cls):            # receives cls (the class)
        return cls.count
    
    @staticmethod
    def static_method():              # receives nothing
        return "no self, no cls"
```

- **Instance method** — takes `self`. Works on individual objects.
- **Class method** — decorator `@classmethod`. Takes `cls`. Works on the class itself.
- **Static method** — decorator `@staticmethod`. Takes nothing. Utility function grouped inside the class for organization.

### `final`, `static`, packages (Java vocabulary — Python equivalents)

- **`final`** in Java → Python uses naming convention `UPPERCASE` for constants. No strict enforcement.
- **`static`** in Java → Python uses `@staticmethod` or class-level variables.
- **Packages** → Python uses modules (files) and packages (folders with `__init__.py`).

### Memory — Stack vs Heap (Java concept, Python equivalent)

- **Stack** — stores function call frames, local variables, control flow.
- **Heap** — stores objects and dynamic data.

In Python, almost everything is an object stored on the heap. Local variable *references* sit on the stack, but the objects they point to are on the heap.

### Garbage Collection

- Python automatically manages memory using **reference counting** plus a **cyclic garbage collector** for circular references.
- When an object's reference count drops to zero, Python frees its memory automatically.
- You can force garbage collection with `import gc; gc.collect()`.

### Likely questions

**"What is garbage collection?"**
> It is the automatic memory management process — the runtime identifies objects that are no longer being used and frees their memory. Python uses reference counting plus a cyclic garbage collector. When an object's reference count drops to zero, it is cleaned up automatically.

**"What is the difference between stack and heap?"**
> Stack stores function calls and local variables — it's fast, small, and managed automatically. Heap stores dynamically allocated objects — it's larger and managed by the garbage collector. In Python, objects live on the heap; variable references sit on the stack.

**"What is `@staticmethod` vs `@classmethod`?"**
> `@staticmethod` creates a method that doesn't receive `self` or `cls` — it's a utility function that's just organized inside the class. `@classmethod` receives `cls` — the class itself — and is typically used for alternative constructors or factory methods that work on the class rather than an instance.

---

# 2. Computer Networks

## 2.1 Basics

- **Network** — two or more devices connected to share data and resources.
- **LAN** — Local Area Network. Limited area like an office or home. High speed.
- **MAN** — Metropolitan Area Network. Covers a city.
- **WAN** — Wide Area Network. Spans countries or globally. The Internet is the largest WAN.

### Topologies (network structures)

- **Bus** — single backbone cable, all devices connect to it. Cheap but one failure affects everyone.
- **Star** — all devices connect to a central hub/switch. Most common in homes and offices. Hub failure breaks the whole network.
- **Ring** — devices connected in a loop. Data travels in one direction. One break affects everyone.
- **Mesh** — every device connects to every other. Very reliable but expensive. Used in the Internet backbone.
- **Tree** — hierarchical, combination of bus and star.
- **Hybrid** — mix of topologies.

---

## 2.2 OSI Model (7 Layers) — Memorize in order

Mnemonic from top to bottom: **"All People Seem To Need Data Processing."**

| Layer | Name | Function | Example Protocols |
|---|---|---|---|
| 7 | Application | User-facing, apps and services | HTTP, HTTPS, FTP, SMTP, DNS |
| 6 | Presentation | Data format, encryption, compression | SSL/TLS, JPEG, GIF |
| 5 | Session | Manages sessions between apps | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery, reliability | TCP, UDP |
| 3 | Network | Routing, logical addressing | IP, ICMP, ARP |
| 2 | Data Link | Physical addressing, error detection | Ethernet, PPP, MAC |
| 1 | Physical | Physical transmission of bits | Cables, hubs, repeaters |

### Devices at each layer

- **Layer 1 (Physical)** — Hub, Repeater, Cables
- **Layer 2 (Data Link)** — Switch, Bridge
- **Layer 3 (Network)** — Router
- **Layer 7 (Application)** — Gateway

### Likely questions

**"What are the layers of the OSI model?"**
> Seven layers, from top to bottom: Application, Presentation, Session, Transport, Network, Data Link, Physical. The mnemonic is 'All People Seem To Need Data Processing.' Each layer has a specific responsibility — for example, the Transport layer handles end-to-end delivery with TCP or UDP, and the Network layer handles routing via IP.

**"Name a protocol at each layer."**
> Application — HTTP, HTTPS, FTP, SMTP. Presentation — SSL/TLS. Session — NetBIOS. Transport — TCP, UDP. Network — IP, ICMP. Data Link — Ethernet. Physical — physical cables, no protocol per se.

---

## 2.3 TCP/IP Model (4 Layers)

Simpler and more practical than OSI. This is what the Internet actually uses.

| TCP/IP Layer | Maps to OSI |
|---|---|
| Application | OSI layers 5, 6, 7 |
| Transport | OSI layer 4 |
| Internet | OSI layer 3 |
| Network Access (Link) | OSI layers 1, 2 |

### Interview one-liner

> "The TCP/IP model is a 4-layer practical model used by the actual Internet. It combines the top three OSI layers into a single Application layer and the bottom two into a Network Access layer. The middle two — Transport and Internet — map directly to OSI's Transport and Network layers."

---

## 2.4 TCP vs UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable (acknowledgments, retransmission) | Unreliable (best-effort) |
| Order | Guaranteed order | No order guarantee |
| Speed | Slower | Faster |
| Use cases | Web (HTTP), email, file transfer | Video streaming, gaming, DNS |
| Overhead | High | Low |

### 3-Way Handshake (TCP connection establishment) — **VERY IMPORTANT**

1. **SYN** — Client sends SYN packet to server saying "I want to connect."
2. **SYN-ACK** — Server responds with SYN-ACK saying "OK, I'm ready."
3. **ACK** — Client sends ACK saying "Great, connection established."

After this, data can flow.

### Likely questions

**"Difference between TCP and UDP?"**
> TCP is connection-oriented and reliable — it guarantees delivery, order, and error correction using acknowledgments. It's used where reliability matters — HTTP, email, file transfer. UDP is connectionless, fast, but unreliable — it sends data without guarantees. UDP is used where speed matters more than reliability, like video streaming, gaming, and DNS lookups.

**"Explain the 3-way handshake."**
> It's how TCP establishes a connection. First, the client sends a SYN packet to the server saying 'I want to connect.' Second, the server replies with SYN-ACK — acknowledging the client and sending its own SYN. Third, the client replies with ACK, completing the handshake. Now both sides know the other is ready and data can flow reliably.

---

## 2.5 HTTP, HTTPS, FTP, SMTP

- **HTTP** — HyperText Transfer Protocol. Web communication. Port 80. **Not encrypted.**
- **HTTPS** — HTTP Secure. Same but encrypted via SSL/TLS. Port 443.
- **FTP** — File Transfer Protocol. Port 21. Used for file uploads/downloads.
- **SMTP** — Simple Mail Transfer Protocol. Sends email. Port 25.
- **POP3/IMAP** — Receive email. POP3 downloads; IMAP keeps on server.

### Difference between HTTP and HTTPS

- HTTPS adds SSL/TLS encryption.
- HTTPS protects against man-in-the-middle attacks and eavesdropping.
- HTTPS uses port 443; HTTP uses port 80.
- HTTPS requires an SSL certificate.

---

## 2.6 Data Transmission Terms

- **Bandwidth** — maximum capacity of the channel (theoretical). Measured in bits per second (bps).
- **Latency** — delay between sending and receiving. Measured in milliseconds.
- **Throughput** — actual speed of data transfer in practice.
- **Analog vs Digital** — analog is continuous waves (old phones); digital is discrete 0s and 1s (computers).

---

## 2.7 IP, MAC, Port

- **IP Address** — logical address. Identifies a device on a network. Two versions:
  - **IPv4** — 32-bit, like `192.168.1.1`. ~4.3 billion addresses.
  - **IPv6** — 128-bit, like `2001:db8::1`. Virtually unlimited addresses.
- **MAC Address** — physical address. Permanent, assigned to the network card. 48-bit, like `AA:BB:CC:11:22:33`.
- **Port Number** — identifies a specific process on a device. 0-65535. HTTP=80, HTTPS=443, SSH=22, FTP=21.

### Likely questions

**"Difference between IP and MAC?"**
> IP is a logical address — it can change based on the network. MAC is a physical hardware address — permanent, assigned to the network interface card. IP is used for routing across networks; MAC is used for delivery within a single network.

**"What is a port?"**
> A port is a number identifying a specific process or service on a device. It lets multiple applications on the same device share one IP address. For example, a web server listens on port 80 or 443, while an SSH server listens on port 22.

---

## 2.8 Network Devices

- **Router** — connects different networks, operates at Layer 3 (Network). Uses IP addresses.
- **Switch** — connects devices within a single network, operates at Layer 2 (Data Link). Uses MAC addresses.
- **Hub** — old dumb device. Broadcasts to all ports. Layer 1. Mostly outdated.
- **Bridge** — connects two network segments. Layer 2.
- **Gateway** — connects networks using different protocols. Layer 7.

### Likely question

**"Difference between router and switch?"**
> A router connects different networks and uses IP addresses to route traffic between them — operating at Layer 3. A switch connects devices within one network and uses MAC addresses for fast local delivery — operating at Layer 2. A home setup typically has both: the router connects your home to the Internet; the switch (often built into the router) connects your devices to each other.

---

## 2.9 DNS and DHCP

- **DNS (Domain Name System)** — translates human-readable domain names (like `google.com`) to IP addresses. Like a phonebook for the Internet.
- **DHCP (Dynamic Host Configuration Protocol)** — automatically assigns IP addresses to devices joining a network. Without DHCP, you'd manually configure every device.

### Likely question

**"Difference between DNS and DHCP?"**
> DNS translates domain names to IP addresses — when you type `google.com`, DNS returns the server's IP. DHCP is the opposite — when your device joins a network, DHCP automatically assigns it an IP address so it can communicate. DNS is name-to-IP; DHCP is IP assignment.

---

## 2.10 Flow Control and Congestion Control

- **Flow Control** — prevents the sender from overwhelming the receiver. Uses techniques like sliding window.
- **Congestion Control** — prevents the network itself from being overwhelmed. Uses techniques like slow start and TCP backoff.

---

# 3. Operating Systems

## 3.1 Basics

- **OS** — software that manages hardware resources and provides a platform for applications to run.
- **Types** — Batch, Multi-programming, Multi-tasking, Real-time, Distributed, Network.
- **System Calls** — interface for user programs to request services from the kernel. Examples: `read()`, `write()`, `fork()`, `exec()`.

---

## 3.2 Process and Thread

### Process vs Program

- **Program** — a static file on disk. Inactive code.
- **Process** — a program in execution. Has its own memory space, registers, and resources.

### Process States (lifecycle)

1. **New** — just created.
2. **Ready** — waiting to be assigned to CPU.
3. **Running** — currently executing on CPU.
4. **Waiting (Blocked)** — waiting for an I/O event.
5. **Terminated** — finished execution.

### PCB (Process Control Block)

A data structure the OS maintains for each process. Stores:
- Process ID
- State
- Program counter (next instruction)
- CPU registers
- Memory management info
- I/O status

### Thread

A **lightweight process**. Multiple threads can exist within a single process and share memory, but each has its own execution path.

### Process vs Thread (common question)

| Feature | Process | Thread |
|---|---|---|
| Memory | Separate memory space | Shared memory with other threads |
| Creation overhead | High | Low |
| Communication | IPC required (expensive) | Shared memory (cheap) |
| Crash isolation | Process crash doesn't affect others | Thread crash can affect whole process |

### Likely questions

**"Difference between process and thread?"**
> A process is an independent program in execution with its own memory space. A thread is a lightweight unit of execution inside a process — multiple threads within one process share memory and resources. Processes are isolated; threads share state. Process creation is expensive; thread creation is cheap.

**"Difference between process and program?"**
> A program is a static file on disk — inactive code. A process is that program actively executing — it has a program counter, memory, and state. You can have multiple processes running the same program simultaneously.

---

## 3.3 CPU Scheduling

The OS decides which process runs next on the CPU.

| Algorithm | Description | Pros | Cons |
|---|---|---|---|
| **FCFS** (First-Come First-Served) | Run in arrival order | Simple | Long wait for short jobs if big job is first (convoy effect) |
| **SJF** (Shortest Job First) | Pick shortest next | Optimal average waiting | Impractical (need to know burst time); can starve long jobs |
| **Round Robin** | Each process gets fixed time slice | Fair; responsive | Context switching overhead |
| **Priority Scheduling** | Higher priority runs first | Flexible | Starvation of low priority (fix: aging) |

### Interview one-liner

> "Common CPU scheduling algorithms are First-Come First-Served, Shortest Job First, Round Robin, and Priority Scheduling. FCFS is simple but can cause long waits for short jobs behind a big one — the convoy effect. SJF gives optimal average waiting time but needs to know job length in advance. Round Robin is the most commonly used in practice — it gives each process a fixed time slice, providing fairness and responsiveness, but introduces context-switching overhead. Priority scheduling runs highest-priority jobs first but can starve low-priority ones unless we use aging."

---

## 3.4 Synchronization

When multiple processes or threads share resources, we need to prevent race conditions.

- **Critical Section** — a section of code where shared resources are accessed. Must be protected.
- **Race Condition** — when the outcome depends on the unpredictable order of execution.
- **Mutex** — mutual exclusion lock. Only one thread holds it at a time.
- **Semaphore** — a signaling mechanism. Can allow N threads at once (counting semaphore) or act like a mutex (binary semaphore).
- **Producer-Consumer Problem** — classic synchronization problem. One thread produces data; another consumes. Must coordinate using buffers and semaphores.

### Likely questions

**"What is a race condition?"**
> A situation where the outcome of a program depends on the timing or ordering of events — typically when multiple threads access shared data simultaneously without proper synchronization. The classic fix is to protect the critical section with a mutex or semaphore.

**"Difference between mutex and semaphore?"**
> A mutex is a lock — only one thread can hold it at a time, ensuring mutual exclusion. A semaphore is a signaling mechanism — a counting semaphore allows up to N threads to proceed, while a binary semaphore is like a mutex. Mutex is strictly for locking; semaphore is more general and can be used for signaling too.

---

## 3.5 Deadlock — **VERY IMPORTANT**

A situation where two or more processes are blocked forever, each waiting for a resource the other holds.

### Four Necessary Conditions (must have all four for deadlock)

1. **Mutual Exclusion** — resource can be held by only one process at a time.
2. **Hold and Wait** — a process holds one resource while waiting for another.
3. **No Preemption** — resource cannot be forcibly taken from a process.
4. **Circular Wait** — there is a circular chain of processes, each waiting for the next.

### Deadlock Handling

- **Prevention** — remove at least one of the four conditions.
- **Avoidance** — use algorithms like Banker's Algorithm to check before granting resources.
- **Detection and Recovery** — let deadlocks happen, detect them (wait-for graph), recover by killing a process.
- **Ignore** — some OSes like Linux do this in certain cases (ostrich algorithm).

### Likely questions

**"What is a deadlock?"**
> A deadlock is a situation where two or more processes are blocked forever, each waiting for a resource that another process holds. Four conditions must all be present: mutual exclusion, hold and wait, no preemption, and circular wait. Prevent a deadlock by breaking any one of these conditions, or use detection-and-recovery.

**"Four conditions of deadlock?"**
> Mutual Exclusion — resources can't be shared. Hold and Wait — a process holds a resource while waiting for another. No Preemption — resources can't be forcibly taken. Circular Wait — processes form a cycle of dependencies. All four must be true simultaneously for deadlock.

---

## 3.6 Memory Management

### Paging

- Divides physical memory into fixed-size **frames** and logical memory into fixed-size **pages**.
- A **page table** maps pages to frames.
- **Advantages:** eliminates external fragmentation, allows physical memory to be non-contiguous.
- **Disadvantages:** internal fragmentation (last page may not be full), overhead of page table.

### Segmentation

- Divides memory into variable-size segments based on logical units (code, data, stack).
- **Advantages:** logical structure, easier sharing.
- **Disadvantages:** external fragmentation.

### Fragmentation

- **Internal** — wasted space inside an allocated block. (Paging has this.)
- **External** — wasted space between blocks. (Segmentation has this.)

### Virtual Memory

- Allows programs to use more memory than physically available by using disk as overflow.
- **Demand Paging** — load pages into memory only when needed, not all upfront.
- **Page Fault** — when a program accesses a page not currently in RAM, OS loads it from disk.

### Likely questions

**"What is virtual memory?"**
> Virtual memory is an abstraction that lets programs use more memory than physically available. The OS uses disk storage as an extension of RAM, swapping pages in and out as needed. Demand paging loads pages only when accessed — when a program accesses a page not in RAM, a page fault occurs and the OS brings it in from disk.

**"Difference between paging and segmentation?"**
> Paging divides memory into fixed-size blocks called pages — it eliminates external fragmentation but causes internal fragmentation. Segmentation divides memory into variable-size logical segments — code segment, data segment, stack segment. Paging is purely about size; segmentation is about logical structure.

---

## 3.7 Disk Scheduling

Algorithms to decide the order of disk read/write requests.

- **FCFS** — serve in order of arrival. Simple but inefficient.
- **SSTF** (Shortest Seek Time First) — serve request closest to current head position. Can starve distant requests.
- **SCAN (Elevator)** — head moves in one direction until the end, then reverses. Fair.
- **C-SCAN** — like SCAN but only serves in one direction, then jumps back.

---

## 3.8 File Systems

- **File Allocation** — how files are stored on disk. Methods: contiguous, linked, indexed.
- **Directory** — organizes files into a hierarchy.

---

# 4. DBMS and SQL

> TCS loves DBMS and SQL questions. **This is your strength** — you write SQL daily at Fern.

## 4.1 Basics

- **DBMS (Database Management System)** — software to create and manage databases. Examples: MySQL, PostgreSQL, SQL Server, Oracle.
- **RDBMS (Relational DBMS)** — DBMS based on the relational model (tables with rows and columns). SQL is its language.
- **Database Models** — Hierarchical, Network, Relational, Object-oriented, Document (NoSQL).

---

## 4.2 ER Model

Used for database design before creating tables.

- **Entity** — a real-world object (e.g., Student, Course).
- **Attribute** — a property of an entity (e.g., Student's name, age).
- **Relationship** — how entities relate (e.g., Student enrolls in Course).
- **ER Diagram** — visual representation.

### Cardinality

- One-to-One (1:1) — one husband ↔ one wife
- One-to-Many (1:N) — one department → many employees
- Many-to-Many (M:N) — many students ↔ many courses

---

## 4.3 Relational Model

- **Schema** — the structure (column names and types).
- **Instance** — the actual data in the table at a given time.
- **Constraints** — rules on the data (NOT NULL, UNIQUE, CHECK, etc.).

---

## 4.4 Keys — **VERY IMPORTANT**

| Key | Definition |
|---|---|
| **Primary Key** | Uniquely identifies each row. NOT NULL and UNIQUE. Only one per table. |
| **Foreign Key** | References the primary key of another table. Used to link tables. |
| **Candidate Key** | Any column (or set) that could be a primary key. The PK is chosen from candidate keys. |
| **Super Key** | Any set of attributes that uniquely identifies a row (includes candidate keys plus extras). |
| **Composite Key** | A primary key made of multiple columns combined. |
| **Unique Key** | Enforces uniqueness but allows one NULL value (unlike PK). |

### Relationship between keys

- Super Key ⊇ Candidate Key ⊇ Primary Key

### Likely questions

**"Difference between primary key and unique key?"**
> Both enforce uniqueness. The primary key is NOT NULL — every row must have a value. A unique key allows exactly one NULL value. A table can have only one primary key but multiple unique keys. The primary key is typically the main identifier; unique keys are used for additional uniqueness constraints like email addresses.

**"Difference between primary key and foreign key?"**
> A primary key uniquely identifies rows within its own table. A foreign key is a column in one table that references the primary key of another table, creating a relationship. The PK enforces entity integrity; the FK enforces referential integrity.

**"What is the difference between candidate key and primary key?"**
> A candidate key is any column or set of columns that could uniquely identify a row. A table may have multiple candidate keys. The primary key is the one candidate key the designer chooses as the main identifier. For example, in an Employee table, both employee_id and email could be candidate keys; the designer picks one as the primary key.

---

## 4.5 Normalization — **VERY IMPORTANT**

Process of organizing data to reduce redundancy and improve integrity.

### The Normal Forms

| Form | Rule | What it solves |
|---|---|---|
| **1NF** | Each column contains atomic (indivisible) values; no repeating groups | Removes multi-valued cells |
| **2NF** | In 1NF + no partial dependency (non-key fully depends on entire primary key) | Removes partial dependency |
| **3NF** | In 2NF + no transitive dependency (non-key depends only on PK, not on another non-key) | Removes transitive dependency |
| **BCNF** | Stricter 3NF — every determinant is a candidate key | Handles edge cases 3NF misses |

### Functional Dependency (FD)

If knowing column A tells you column B's value, we say `A → B` (A determines B).

### Example progression

**Unnormalized:**
| StudentID | Name | Courses |
|---|---|---|
| 1 | Alice | Math, Science |

**1NF (atomic values):**
| StudentID | Name | Course |
|---|---|---|
| 1 | Alice | Math |
| 1 | Alice | Science |

**2NF (remove partial dependency)** — split so that Name (which depends only on StudentID, not on Course) is in a separate table.

**3NF (remove transitive dependency)** — if Course → Department and Department has more info, split Department into its own table.

### Likely questions

**"What is normalization?"**
> Normalization is organizing a database to reduce redundancy and ensure data integrity. We apply normal forms in sequence — 1NF requires atomic values, 2NF removes partial dependencies, 3NF removes transitive dependencies, and BCNF is a stricter 3NF. Most real databases aim for 3NF — it's a good balance between integrity and query performance.

**"Difference between 2NF and 3NF?"**
> 2NF removes partial dependencies — every non-key column must depend on the *entire* primary key, not just part of it. 3NF removes transitive dependencies — a non-key column must depend *only* on the primary key, not on another non-key column. 3NF builds on 2NF.

---

## 4.6 SQL Commands

SQL is divided into categories:

### DDL (Data Definition Language) — define structure

- `CREATE` — create tables, databases, indexes
- `ALTER` — modify structure
- `DROP` — delete tables/databases
- `TRUNCATE` — remove all rows (faster than DELETE, cannot be rolled back in most systems)

### DML (Data Manipulation Language) — modify data

- `INSERT` — add rows
- `UPDATE` — modify rows
- `DELETE` — remove rows

### DQL (Data Query Language) — retrieve data

- `SELECT` — fetch data

### DCL (Data Control Language) — permissions

- `GRANT` — give permissions
- `REVOKE` — remove permissions

### TCL (Transaction Control Language) — manage transactions

- `COMMIT` — save changes
- `ROLLBACK` — undo changes
- `SAVEPOINT` — set a rollback point

### Likely question

**"Difference between DELETE, TRUNCATE, and DROP?"**
> DELETE removes specific rows based on a WHERE clause — can be rolled back, triggers fire, slower. TRUNCATE removes all rows instantly — cannot be rolled back in most systems, triggers don't fire, much faster, resets auto-increment counters. DROP removes the entire table including its structure — the table no longer exists.

---

## 4.7 Joins — **ESSENTIAL**

Joins combine rows from two or more tables based on a related column.

### Types

| Join | Description |
|---|---|
| **INNER JOIN** | Returns only matching rows from both tables |
| **LEFT JOIN** (LEFT OUTER) | All rows from left + matching from right; NULL where no match |
| **RIGHT JOIN** (RIGHT OUTER) | All rows from right + matching from left; NULL where no match |
| **FULL OUTER JOIN** | All rows from both tables; NULL where no match |
| **CROSS JOIN** | Cartesian product — every row of A with every row of B |
| **SELF JOIN** | Joining a table with itself |

### Example

```sql
-- INNER JOIN
SELECT e.name, d.department_name
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.id;

-- LEFT JOIN
SELECT e.name, d.department_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.id;
-- Returns all employees, with NULL for those without a department.
```

### Likely questions

**"Types of joins?"**
> Inner Join returns only matching rows from both tables. Left Join returns all rows from the left table plus matching ones from the right, with NULLs where there's no match. Right Join is the opposite. Full Outer Join returns all rows from both. Cross Join returns the Cartesian product. Self Join is a table joined with itself — useful when the table has a hierarchical relationship like employees reporting to managers.

**"Difference between INNER and LEFT JOIN?"**
> INNER JOIN returns only rows that have a match in both tables. LEFT JOIN returns all rows from the left table even if there's no match on the right — the unmatched right columns will be NULL. INNER shrinks the result; LEFT preserves the left side.

---

## 4.8 Subqueries and Aggregates

### Subquery
A query inside another query.

```sql
SELECT name FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
```

### Aggregate Functions
- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- Operate on groups of rows.

### GROUP BY
Groups rows with the same values. Used with aggregates.

```sql
SELECT department, AVG(salary) 
FROM Employees
GROUP BY department;
```

### HAVING
Filters groups after GROUP BY. WHERE filters rows before grouping; HAVING filters after.

```sql
SELECT department, AVG(salary) 
FROM Employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

### Likely question

**"Difference between WHERE and HAVING?"**
> WHERE filters individual rows before grouping. HAVING filters groups after GROUP BY has been applied. For example, `WHERE salary > 50000` filters employees with salary above 50K; `HAVING AVG(salary) > 50000` filters departments whose average salary is above 50K.

---

## 4.9 Transactions and ACID

A **transaction** is a sequence of operations treated as a single unit — either all succeed or all fail.

### ACID Properties

- **Atomicity** — all or nothing. Partial changes are not allowed.
- **Consistency** — database moves from one valid state to another; all rules must hold.
- **Isolation** — concurrent transactions don't interfere. They appear to run serially.
- **Durability** — once committed, changes persist even through crashes.

### Likely question

**"Explain ACID properties."**
> ACID stands for Atomicity, Consistency, Isolation, Durability. Atomicity means a transaction is all-or-nothing — either fully succeeds or fully rolls back. Consistency means the database moves from one valid state to another, respecting all rules. Isolation means concurrent transactions don't interfere with each other. Durability means committed changes survive crashes. These four properties ensure data reliability in RDBMS.

---

## 4.10 Indexing

An **index** is a data structure that speeds up lookups on a column.

- **Primary Index** — automatically created on primary key.
- **Clustered Index** — physically reorders the table based on the indexed column. Only one per table.
- **Non-clustered Index** — separate structure pointing to rows. Multiple allowed.

### Trade-offs

- **Pro:** Fast SELECT queries.
- **Con:** Slows down INSERT, UPDATE, DELETE (index must be maintained); uses additional storage.

### Likely question

**"What is indexing, and what are the trade-offs?"**
> An index is a data structure — typically a B-tree — that allows fast lookup on a column. It's like the index at the back of a book. It dramatically speeds up SELECT queries with WHERE clauses on the indexed column. The trade-off is that INSERT, UPDATE, and DELETE become slower because the index must be maintained, and the index takes additional storage. I'd index frequently-searched columns but avoid over-indexing.

---

## 4.11 Common SQL Queries You Should Know

```sql
-- Second highest salary
SELECT MAX(salary) FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);

-- Or using LIMIT
SELECT DISTINCT salary FROM Employees
ORDER BY salary DESC LIMIT 1 OFFSET 1;

-- Nth highest salary using subquery
SELECT salary FROM Employees e1
WHERE N-1 = (SELECT COUNT(DISTINCT salary) FROM Employees e2 WHERE e2.salary > e1.salary);

-- Find duplicates
SELECT name, COUNT(*) FROM Employees
GROUP BY name HAVING COUNT(*) > 1;

-- Count employees per department
SELECT department, COUNT(*) FROM Employees
GROUP BY department;

-- Top earners per department
SELECT department, name, salary
FROM Employees e1
WHERE salary = (SELECT MAX(salary) FROM Employees e2 WHERE e2.department = e1.department);
```

---

# 5. Python

> **High-probability questions** because your resume says Python.

## 5.1 Python Basics

- **Interpreted** language — runs line by line. No explicit compilation.
- **Dynamically typed** — variable types are decided at runtime. No declaration of types.
- **High-level** — abstracts away low-level details.
- **Multi-paradigm** — supports OOP, functional, procedural.

### Data Types

- **Numeric:** int, float, complex
- **Sequence:** list, tuple, range
- **Text:** str
- **Mapping:** dict
- **Set:** set, frozenset
- **Boolean:** bool
- **None:** NoneType

---

## 5.2 Mutable vs Immutable

| Mutable (can change) | Immutable (can't change) |
|---|---|
| list | tuple |
| dict | str |
| set | int, float, bool |
| | frozenset |

### Likely question

**"Difference between list and tuple?"**
> A list is mutable — you can add, remove, or change elements after creation. A tuple is immutable — once created, its contents cannot be changed. Lists use square brackets; tuples use parentheses. Tuples are faster and use less memory, so they're good for fixed data. Lists are more flexible for dynamic collections.

---

## 5.3 Key Concepts

### `is` vs `==`

- `==` compares **values** — are they equal?
- `is` compares **identity** — are they the same object in memory?

```python
a = [1, 2]
b = [1, 2]
print(a == b)   # True (same content)
print(a is b)   # False (different objects)
```

### `None`

- Represents absence of value. Similar to `null` in other languages.
- Use `is None` for comparison, not `== None`.

### List Comprehension

Compact way to create lists.

```python
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Lambda Functions

Anonymous one-line functions.

```python
square = lambda x: x**2
print(square(5))   # 25

# Common with map, filter, sorted
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
```

### Decorators

Functions that modify or enhance other functions.

```python
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function
# Hello!
# After function
```

### Generators

Functions that yield values lazily using `yield`.

```python
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)   # 0, 1, 2, 3, 4
```

Generators are memory-efficient — they produce values on demand rather than storing them all.

### *args and **kwargs

- `*args` — variable number of positional arguments, received as a tuple.
- `**kwargs` — variable number of keyword arguments, received as a dict.

```python
def demo(*args, **kwargs):
    print(args)     # tuple
    print(kwargs)   # dict

demo(1, 2, 3, name="Alice", age=30)
# (1, 2, 3)
# {'name': 'Alice', 'age': 30}
```

---

## 5.4 Python-Specific OOP Differences

- **No strict private** — use `_name` (convention) or `__name` (name-mangled).
- **Multiple inheritance supported** — unlike Java.
- **No method overloading** — use default arguments instead.
- **Everything is an object** — even functions and classes are objects.
- **Self required** — unlike Java's implicit `this`.

---

## 5.5 Likely Python Questions

**"What are the key features of Python?"**
> Python is interpreted, dynamically typed, high-level, and multi-paradigm — it supports OOP, functional, and procedural programming. It has simple, readable syntax, extensive standard library, strong community, and huge ecosystem for data science, web, and ML.

**"What's the difference between list and tuple?"**
> List is mutable — you can change it after creation. Tuple is immutable. Lists use square brackets, tuples use parentheses. Tuples are faster and used for fixed data; lists for dynamic collections.

**"What is a dictionary in Python?"**
> A dictionary is a collection of key-value pairs. Keys must be immutable and unique. Average lookup time is O(1) because it's implemented as a hash table. Defined with curly braces — `{"name": "Alice", "age": 30}`.

**"What is list comprehension?"**
> A compact syntax for creating a list by applying an expression to each element of an iterable, optionally with a condition. For example, `[x**2 for x in range(10) if x % 2 == 0]` creates a list of squares of even numbers from 0 to 9. It's more concise and often faster than a for-loop.

**"What are decorators?"**
> Decorators are functions that modify or enhance other functions without changing their source code. They're applied using the `@` syntax above a function definition. Common uses include logging, timing, authentication, and caching.

**"What is the difference between `is` and `==`?"**
> `==` compares values — whether two objects have equal content. `is` compares identity — whether two references point to the same object in memory. For example, two lists with the same contents are equal with `==` but are different objects with `is`.

**"What are *args and **kwargs?"**
> `*args` lets a function accept any number of positional arguments, received as a tuple. `**kwargs` accepts any number of keyword arguments, received as a dictionary. They're used when you don't know in advance how many arguments will be passed.

**"Difference between deep copy and shallow copy?"**
> A shallow copy creates a new object but references the same nested objects. A deep copy creates a completely independent copy, including nested objects. Use `copy.copy()` for shallow and `copy.deepcopy()` for deep.

---

# 6. NumPy and Pandas

> Likely questions because your resume lists these.

## 6.1 NumPy

**NumPy** is the fundamental package for numerical computing in Python.

- **ndarray** — the core data structure. A multi-dimensional array of homogeneous type.
- **Faster than Python lists** because it stores data in contiguous memory and operations are written in C.

### Basic Operations

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.zeros(5)                    # array of zeros
c = np.ones((3, 3))                 # 3x3 matrix of ones
d = np.arange(0, 10, 2)            # 0, 2, 4, 6, 8
e = np.linspace(0, 1, 5)           # 5 evenly spaced points

# Shape and type
print(a.shape)     # (4,)
print(a.dtype)     # int64

# Operations are vectorized (applied element-wise)
a + 1              # [2, 3, 4, 5]
a * 2              # [2, 4, 6, 8]
a.sum()            # 10
a.mean()           # 2.5

# Reshape
m = np.arange(12).reshape(3, 4)    # 3x4 matrix
```

### Broadcasting

NumPy automatically expands arrays of different shapes when doing arithmetic, if shapes are compatible.

```python
a = np.array([1, 2, 3])
b = 10
print(a + b)       # [11, 12, 13]
```

### Likely questions

**"What is NumPy and why use it?"**
> NumPy is the core library for numerical computing in Python. Its main object is the ndarray — an efficient, multi-dimensional array. It's much faster than Python lists because it stores data in contiguous memory and performs operations in compiled C code. It's the foundation for pandas, scikit-learn, and most of the data science stack.

**"Difference between NumPy array and Python list?"**
> A Python list can hold mixed types and is backed by a general-purpose object array. A NumPy array holds homogeneous types, stores data contiguously, and uses vectorized C operations. For numerical work, NumPy is orders of magnitude faster and uses less memory.

**"What is broadcasting?"**
> Broadcasting is NumPy's rule for performing arithmetic between arrays of different shapes. Smaller arrays are automatically stretched to match the larger ones when compatible. For example, adding a scalar to an array adds it to each element; adding a 1D array to a 2D array adds it to each row.

---

## 6.2 Pandas

**Pandas** is built on NumPy. Provides high-level data structures for tabular data.

- **Series** — 1D labeled array.
- **DataFrame** — 2D labeled table. Like a spreadsheet or SQL table.

### Basic Operations

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})

# Load from CSV
df = pd.read_csv("file.csv")

# Inspect
df.head()           # first 5 rows
df.tail()           # last 5 rows
df.shape            # (rows, columns)
df.columns          # column names
df.dtypes           # data types
df.describe()       # statistical summary
df.info()           # info about DataFrame

# Access
df["name"]          # single column (Series)
df[["name", "age"]] # multiple columns
df.iloc[0]          # first row by position
df.loc[0]           # first row by label
df.iloc[0:3, 0:2]   # rows 0-2, columns 0-1

# Filter
df[df["age"] > 25]

# Group by
df.groupby("department")["salary"].mean()

# Missing values
df.dropna()         # drop rows with any NaN
df.fillna(0)        # replace NaN with 0

# Merge / Join
pd.merge(df1, df2, on="id", how="inner")
```

### Likely questions

**"What is the difference between Series and DataFrame?"**
> A Series is a one-dimensional labeled array — like a single column. A DataFrame is a two-dimensional labeled table — like a spreadsheet with multiple columns. A DataFrame can be thought of as a collection of Series sharing the same index.

**"Difference between `iloc` and `loc`?"**
> `iloc` is position-based indexing — you use integer positions. `loc` is label-based — you use row/column labels. `df.iloc[0]` gets the first row by position; `df.loc["Alice"]` gets the row labeled "Alice".

**"How do you handle missing values in pandas?"**
> Common options are `dropna()` to remove rows or columns with missing values, `fillna(value)` to replace them with a specific value (like 0 or the mean), or `interpolate()` for numerical series. The right choice depends on how much data is missing and whether the missingness has meaning.

**"What is groupby?"**
> `groupby` splits the data into groups based on column values, lets you apply an aggregation function (like mean, sum, count) to each group, and combines the results. For example, `df.groupby("department")["salary"].mean()` computes the average salary per department — similar to SQL's GROUP BY.

---

# 7. ML Foundations

> Your resume says "Supervised Learning." Expect basic ML questions.

## 7.1 Types of Machine Learning

1. **Supervised Learning** — learns from labeled data. Input and correct output given. Examples: classification, regression.
2. **Unsupervised Learning** — learns from unlabeled data. Finds structure. Examples: clustering, dimensionality reduction.
3. **Reinforcement Learning** — learns by trial and error, receiving rewards. Examples: game playing, robotics.

### Likely question

**"What are the types of machine learning?"**
> Three main types. Supervised learning uses labeled data — the model learns a mapping from inputs to known outputs. Classification and regression fall here. Unsupervised learning uses unlabeled data — the model finds patterns or groupings, like clustering. Reinforcement learning involves an agent learning by interacting with an environment and receiving rewards, used in games and robotics.

---

## 7.2 Supervised Learning

### Classification vs Regression

| | Classification | Regression |
|---|---|---|
| Output | Discrete category | Continuous number |
| Example | Spam or not spam | Predict house price |
| Metrics | Accuracy, Precision, Recall, F1 | RMSE, MAE, R² |

### Common Algorithms

- **Linear Regression** — fits a line for continuous output.
- **Logistic Regression** — despite the name, it's for classification. Outputs probability.
- **Decision Tree** — tree of if-else questions splitting data.
- **Random Forest** — ensemble of decision trees (your Bitcoin project used this).
- **SVM (Support Vector Machines)** — finds a hyperplane separating classes.
- **K-Nearest Neighbors (KNN)** — classifies based on nearest points.
- **Naive Bayes** — probabilistic classifier based on Bayes' theorem.

---

## 7.3 Random Forest (from your project)

**Definition:** An ensemble of decision trees. Each tree is trained on a random subsample of the data using a random subset of features at each split. At prediction time, all trees vote and the majority class wins.

**Why it works:**
- Randomness makes trees diverse, reducing overfitting.
- Voting across many trees reduces variance.
- Handles tabular data, mixed feature types, and missing values gracefully.
- Gives feature importance.

### Likely questions

**"What is Random Forest?"**
> Random Forest is an ensemble learning method — a collection of decision trees. Each tree is trained on a random bootstrapped subset of the data, and at each split only a random subset of features is considered. At prediction time, all trees vote, and the majority wins. This randomness prevents overfitting that a single deep decision tree would have.

**"Why is it called 'Random' Forest?"**
> Two sources of randomness. First, each tree trains on a random bootstrap sample of the data. Second, at each split within a tree, only a random subset of features is considered. This dual randomness makes the trees diverse, and averaging many diverse trees produces a robust, generalizing model.

---

## 7.4 Model Evaluation

### Classification Metrics

- **Accuracy** — fraction of correct predictions. Can be misleading for imbalanced data.
- **Precision** — of the items predicted positive, how many actually are. TP / (TP + FP).
- **Recall** — of the actual positive items, how many were caught. TP / (TP + FN).
- **F1 Score** — harmonic mean of precision and recall. Balances both.
- **Confusion Matrix** — table showing TP, FP, TN, FN.

### Regression Metrics

- **MSE (Mean Squared Error)** — average of squared differences.
- **RMSE** — square root of MSE, same units as output.
- **MAE (Mean Absolute Error)** — average of absolute differences.
- **R² (R-squared)** — fraction of variance explained. 1 is perfect, 0 is baseline.

### Likely questions

**"Difference between precision and recall?"**
> Precision answers: when the model says positive, how often is it right? TP over TP plus FP. Recall answers: of all the actual positives, how many did the model catch? TP over TP plus FN. High precision with low recall means the model is cautious but misses many. High recall with low precision means the model catches everything but has many false alarms. F1 is the balance.

**"Why is accuracy misleading for imbalanced data?"**
> If 95% of examples are negative, a model that always predicts negative gets 95% accuracy while being useless. In imbalanced problems like fraud detection or ransomware classification, what matters is catching the rare positive cases — precision and recall are more informative. I saw this in my Bitcoin ransomware project — 99% accuracy looked great but the model failed on rare ransomware families because of class imbalance.

---

## 7.5 Overfitting vs Underfitting

- **Overfitting** — model memorizes training data. High training accuracy, low test accuracy. Fails to generalize.
- **Underfitting** — model is too simple. Both training and test accuracy are low.

### How to handle overfitting

1. More training data.
2. Regularization (L1, L2).
3. Cross-validation.
4. Simpler model.
5. Dropout (in neural networks).
6. Early stopping.

### Bias-Variance Trade-off

- **Bias** — error from oversimplifying. High bias → underfitting.
- **Variance** — error from sensitivity to training data. High variance → overfitting.
- Ideal: low bias, low variance. Usually a trade-off.

### Likely question

**"What is overfitting and how to prevent it?"**
> Overfitting is when a model learns the training data too well — including noise — and fails to generalize to new data. Symptoms are high training accuracy and low test accuracy. To prevent it: get more data, use simpler models, apply regularization (L1 or L2), use cross-validation, and apply early stopping. For neural networks, dropout is another technique.

---

## 7.6 Train-Test Split and Cross-Validation

- **Train-test split** — split data into training (usually 70-80%) and test (20-30%). Train on training, evaluate on test.
- **Stratified split** — preserves class distribution — important for imbalanced data.
- **Cross-validation** — divide data into K folds; train on K-1, test on 1; rotate; average results. Gives a more reliable estimate.

---

## 7.7 Feature Engineering Concepts

- **Feature scaling** — normalizing features to similar ranges. Important for distance-based algorithms (KNN, SVM) and gradient descent.
  - **Min-Max Scaling** — scale to [0, 1].
  - **Standardization** — zero mean, unit variance.
- **One-Hot Encoding** — convert categorical variables to binary columns.
- **Label Encoding** — assign integer codes to categories (used for ordinal data).

---

# 8. Linear Algebra and Probability

> Your resume mentions these foundations. Basic questions may come.

## 8.1 Linear Algebra (basics)

- **Scalar** — a single number.
- **Vector** — an ordered list of numbers. 1D.
- **Matrix** — a 2D array of numbers.
- **Tensor** — generalization to N dimensions.

### Key operations

- **Matrix Multiplication** — A (m×n) multiplied by B (n×p) gives C (m×p). Inner dimensions must match.
- **Transpose** — flip rows and columns. A of shape (m,n) becomes A^T of shape (n,m).
- **Determinant** — scalar value that tells if a matrix is invertible.
- **Inverse** — A^(-1) such that A · A^(-1) = I (identity matrix).
- **Eigenvalues / Eigenvectors** — used in PCA, recommender systems, etc.

### Dot Product

For two vectors: sum of element-wise products.
- Used to measure similarity between vectors.
- Cosine similarity in NLP uses it.

---

## 8.2 Probability and Statistics

### Probability basics

- **Probability** — likelihood of an event. Between 0 and 1.
- **Independent events** — outcome of one doesn't affect the other.
- **Conditional Probability** — P(A|B) = P(A and B) / P(B). Probability of A given B.
- **Bayes' Theorem** — P(A|B) = P(B|A) · P(A) / P(B). Foundation of Naive Bayes classifier and Bayesian networks.

### Statistics basics

- **Mean** — average.
- **Median** — middle value.
- **Mode** — most frequent.
- **Variance** — average squared deviation from mean.
- **Standard Deviation** — square root of variance. Same units as data.
- **Normal Distribution** — bell curve. Defined by mean and standard deviation.

### Likely questions

**"What is Bayes' theorem?"**
> Bayes' theorem gives the probability of an event based on prior knowledge of related conditions. Formula: P(A|B) = P(B|A) × P(A) / P(B). It's used in spam filtering, medical diagnosis, and Bayesian networks. If I know the probability of symptoms given a disease, Bayes lets me compute the probability of the disease given symptoms.

**"Difference between mean, median, and mode?"**
> Mean is the average — sum divided by count. Median is the middle value when data is sorted. Mode is the most frequently occurring value. Mean is sensitive to outliers; median is not. For skewed distributions, median is often a better measure of central tendency.

---

# 9. Hugging Face and Transformers

> Resume lists these. Be ready for basics.

## 9.1 What is Hugging Face?

- A company and platform that hosts thousands of pre-trained machine learning models.
- Provides the **transformers** Python library to load and use these models.
- **Hub** hosts models, datasets, and demos (Spaces).

## 9.2 What is Transformers (library)?

- A Python library by Hugging Face that makes it easy to use pre-trained models — BERT, GPT, Phi-3, Llama, and thousands more.
- Handles model loading, tokenization, fine-tuning, and inference.

## 9.3 What is a Transformer (model architecture)?

- A neural network architecture introduced in 2017 by Google in the paper "Attention is All You Need."
- Uses **attention mechanism** to process sequences (like text).
- Replaced RNNs and LSTMs for most NLP tasks.
- Foundation for GPT, BERT, T5, and modern LLMs.

### Key concepts

- **Attention** — mechanism that lets the model focus on relevant parts of the input when producing output.
- **Self-Attention** — each token attends to other tokens in the same sequence.
- **Encoder** — processes input (used in BERT).
- **Decoder** — generates output (used in GPT).
- **Encoder-Decoder** — for translation (T5).

### Likely questions

**"What is Hugging Face?"**
> Hugging Face is a company and platform that hosts thousands of pre-trained ML models, datasets, and demos. Their `transformers` Python library is the most popular way to use modern NLP models like BERT, GPT, and LLaMA. I used Hugging Face in my LLM fine-tuning project for Phi-3-mini and for the Schema-Based Instruction Dataset.

**"What is a Transformer?"**
> A Transformer is a neural network architecture introduced in 2017. It uses an attention mechanism to model relationships between tokens in a sequence. Unlike RNNs, Transformers process sequences in parallel, making them much faster to train. They are the foundation of modern LLMs like GPT and BERT.

**"What is attention?"**
> Attention is a mechanism that lets the model focus on the most relevant parts of the input when producing each output. In self-attention, each token in the sequence computes a weighted combination of all other tokens, capturing long-range dependencies that RNNs struggled with.

---

# 10. Requirement Engineering

> Your resume lists this — from your Fern experience.

## 10.1 What is Requirement Engineering?

The process of defining, documenting, and maintaining the requirements for a software system.

### Phases

1. **Elicitation** — gathering requirements from stakeholders via interviews, surveys, observation.
2. **Analysis** — understanding, prioritizing, resolving conflicts.
3. **Documentation** — writing SRS (Software Requirements Specification).
4. **Validation** — confirming with stakeholders that requirements are correct.
5. **Management** — handling changes throughout the project.

### Types of Requirements

- **Functional** — what the system should do. E.g., "The system should allow customers to transfer money."
- **Non-Functional** — how the system should perform. E.g., "Response time should be under 2 seconds."
- **Business** — high-level goals.
- **User** — what end users need.
- **System** — detailed technical requirements.

### Likely questions

**"What is requirement engineering?"**
> Requirement engineering is the process of defining, documenting, and maintaining a software system's requirements. It involves eliciting requirements from stakeholders, analyzing and prioritizing them, documenting them in an SRS, validating with stakeholders, and managing changes. In my role at Fern, I write specifications for enhancements — that's essentially the documentation phase, translating client needs into detailed specs for the development team.

**"Functional vs Non-functional requirements?"**
> Functional requirements describe what the system should do — specific features and behaviors, like 'allow users to transfer money.' Non-functional requirements describe how well the system should perform — qualities like performance, security, scalability, usability. For example, 'the transfer should complete within 2 seconds' is non-functional.

---

# 11. DSA Patterns

> Focus on conceptual understanding rather than memorizing code. Have clear answers for "how would you approach X?"

## 11.1 Arrays

### Key Patterns

- **Traversal** — single loop, handle off-by-one carefully.
- **Two Pointer** — one from start, one from end; converge. For sorted arrays or pair-sum problems.
- **Sliding Window** — for contiguous subarray problems. Maintain a window and slide.
- **Prefix Sum** — precompute sums up to each index for fast range queries.

### Common Problems

- **Maximum Subarray Sum (Kadane's Algorithm)** — O(n), track running sum and max.
- **Two Sum** — use hashmap to find complement in O(n).
- **Rotated Array Search** — binary search with a twist.
- **Merge Intervals** — sort by start, merge overlapping.

### Key concept: Subarray vs Subsequence

- **Subarray** — contiguous elements.
- **Subsequence** — elements in order but not necessarily contiguous.

## 11.2 Strings

- **Palindrome** — two pointers from both ends.
- **Anagram** — compare character frequency (use dict or counter).
- **Longest Substring Without Repeat** — sliding window with a set.
- **Pattern Matching** — basic idea is enough; knowing that KMP exists for O(n+m) is good.

```python
# Palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Anagram
def is_anagram(a, b):
    return sorted(a) == sorted(b)

# Count frequency
from collections import Counter
Counter("hello")   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Longest unique substring (sliding window)
def longest_unique(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

## 11.3 Linked List

- **Types:** Singly, Doubly, Circular.
- **Reverse a linked list** — iterative: track prev, current, next.
- **Cycle Detection** — Floyd's algorithm (slow and fast pointers).
- **Find middle** — slow and fast pointers.

```python
# Reverse linked list
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Cycle detection (Floyd's)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## 11.4 Stack and Queue

- **Stack** — LIFO. Use for parentheses matching, undo operations, DFS.
- **Queue** — FIFO. Use for BFS, scheduling.
- **Deque** — double-ended. Used in sliding window max problems.
- **Priority Queue (Heap)** — elements ordered by priority.

### Balanced Parentheses Check

```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack
```

## 11.5 Trees

- **Binary Tree** — each node has up to 2 children.
- **BST (Binary Search Tree)** — left < root < right. Allows O(log n) search.

### Traversals (memorize)

- **Inorder** — Left, Root, Right. For BST: gives sorted order.
- **Preorder** — Root, Left, Right.
- **Postorder** — Left, Right, Root.
- **Level-order (BFS)** — use queue.

```python
# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# BFS
from collections import deque
def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## 11.6 Graphs

- **Representation** — Adjacency List (most common) or Adjacency Matrix.
- **BFS** — queue-based. Used for shortest path in unweighted graphs.
- **DFS** — recursion-based. Used for cycle detection, topological sort.

## 11.7 Searching & Sorting

- **Binary Search** — requires sorted array. O(log n). **Master this.**
- **Bubble Sort** — O(n²). Conceptual only.
- **Merge Sort** — O(n log n). Divide-and-conquer.
- **Quick Sort** — O(n log n) average, O(n²) worst. Pivot-based.

```python
# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 11.8 Hashing

- **HashMap** — O(1) average lookup. Python's `dict` is a hashmap.
- **Applications** — frequency counting, fast lookup, duplicate detection.

## 11.9 Complexity

### Big-O notation

Gives the **upper bound** on growth rate.

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Array access, dict lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort, quick sort avg |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2^n) | Exponential | Subsets, brute force |

### Likely questions

**"What is Big-O?"**
> Big-O describes how an algorithm's running time or space grows as the input size grows. It's an upper bound — worst-case. O(1) is constant, O(log n) is logarithmic, O(n) is linear, O(n log n) is typical of efficient sorts, O(n²) is quadratic. It's used to compare algorithms independent of hardware.

**"What's the difference between O(n) and O(log n)?"**
> O(n) means the time grows linearly with input size — doubling input doubles time. O(log n) means it grows logarithmically — even doubling input adds only a small fixed amount of time. Binary search is O(log n); scanning a list is O(n). For large inputs, the difference is dramatic.

---

# 12. Project Questions

## 12.1 Fern Software — Likely Questions

**"Walk me through a typical day."**
> A typical day involves checking new Freshdesk tickets from clients, triaging them by severity and module, and working on the highest-priority ones. I replicate issues in test environments, use SQL Server to investigate — queries, logs, SQL Profiler — and identify root causes. For data issues, I write SQL scripts to fix them; for code issues, I document findings and coordinate with the development team. I also attend client calls, internal case discussions, and occasionally support UAT and Go-Live activities.

**"Describe a challenging issue you resolved."**
> I was part of the investigation on a live payment and settlement issue at one of our clients that was blocking their operations. I helped identify the root cause by analyzing transaction patterns in SQL Server and coordinating the fix. After resolution, I received direct appreciation from our director for the effort.

**"What SQL do you write?"**
> Mostly T-SQL on SQL Server — complex joins across multiple tables, stored procedures for client reports, data-fix scripts for production, and queries using SQL Profiler to debug performance issues. I also write Excel-exported reports for clients from SQL results.

**"Give me an example of a specification you wrote."**
> I've written over ten specifications that have shipped to production — mostly enhancements to existing reports and new features in loans and savings modules. The process is: understand the client's need on calls, translate it into a detailed spec with expected inputs, outputs, validations, and edge cases, and hand it off to the development team. I also coordinate testing once the feature is built.

**"Have you used any testing tools or methodologies?"**
> I do functional, regression, database, and performance testing for new patches and features. I use SQL Profiler for performance bottlenecks and write test cases in spreadsheets or ticket systems. I'm familiar with black-box testing methodology — testing behavior without knowing internal implementation.

---

## 12.2 pgmpy — Likely Questions

**"Why pgmpy?"**
> My role at Fern is primarily client-facing, so I wanted to stay close to development work on my own time. I looked for open-source projects with beginner-friendly issues, and pgmpy fit well — it's a research-grade library used for Bayesian networks and causal inference. I started with small contributions and gradually took on bigger refactors. Over seven months I've landed three PRs and was ranked among the top 13 contributors to their 1.1.0 release.

**"What exactly did you contribute?"**
> My main contribution was a refactoring of the dataset and example-model discovery system. The library used to have a manual registry — a hardcoded dictionary mapping names to classes — which didn't scale. I refactored the base class to inherit from skbase, which provides automatic class discovery and tag-based metadata. Now, adding a new dataset or model is just a matter of declaring a new class with tags, and everything else — discovery, loading, filtering — happens automatically.

**"What is skbase?"**
> skbase is a lightweight base-class library for scientific Python projects. It provides tag management, automatic class discovery via `all_objects`, and tag-based filtering. It's used by sktime and other libraries. By inheriting from `skbase.base.BaseObject`, my dataset classes got all this functionality without my writing it from scratch.

**"What's a Bayesian network?"**
> A Bayesian network is a directed acyclic graph where nodes represent random variables and edges represent conditional dependencies. It's used to model probabilistic relationships and do inference — computing the probability of variables given evidence. Applications include medical diagnosis, spam filtering, and causal reasoning.

**"Did you write everything yourself?"**
> I want to be clear about scope. I wrote the base class framework — `_BaseDataset`, the tag schema, the public API, and the tests. There are also mixin classes in the file for specific data formats — covariance matrices, Tubingen benchmarks, BIF files, and DAGitty — that were contributed by other maintainers. My framework was designed so these could be added as mixins without touching the base class, which is exactly how those contributions landed.

---

## 12.3 LLM Fine-Tuning Project — Likely Questions

**"Tell me about this project."**
> It was a self-driven learning project from July 2025. I fine-tuned Microsoft's Phi-3-mini, a 3.8 billion parameter instruction-tuned LLM, to generate structured outputs for math word problems. Given a problem, the model outputs a Schema label and a Sub-Category label. I used LoRA for parameter-efficient fine-tuning, 4-bit quantization to fit into a free Colab GPU, and Unsloth for speedup. My goal was to learn the modern fine-tuning stack hands-on.

**"What is LoRA?"**
> LoRA stands for Low-Rank Adaptation. Instead of updating all the weights of a pretrained model, you freeze them and inject small trainable matrices alongside each target layer. If a linear layer computes y = Wx, LoRA replaces it with y = Wx + B·A·x, where W is frozen and A and B are small rank-r matrices. I used rank 16. This trains a few million parameters instead of billions — a ~200x reduction with minimal quality loss.

**"What is 4-bit quantization?"**
> It compresses model weights from 16-bit or 32-bit floats to 4 bits per weight, cutting memory roughly 4x with minor precision loss. It's what made Phi-3-mini fit on a free Colab T4 GPU, which has about 15 GB of VRAM.

**"Honest scope: I did this in July, so specific hyperparameter values might take me a moment to recall."** Use this upfront if unsure.

---

## 12.4 Bitcoin Ransomware Project — Critical Framing

**Deliver this upfront:**

> "That was my UG final-year project in 2024 — a team project. My contribution was primarily at the team discussion and coordination level; my teammates handled most of the modeling. The project built a Random Forest classifier on the UCI BitcoinHeist dataset to detect ransomware addresses. It was my first exposure to ML concepts like supervised classification and class imbalance. Since graduating and starting the pgmpy contribution, my technical focus has shifted to production work and open-source — which is why I've built up hands-on work there that is more directly mine."

**If pushed:** "My specific coding contribution was limited. That's actually one of the reasons I've invested heavily in pgmpy — I wanted hands-on technical work that is genuinely mine rather than shared team credit."

**Do not volunteer technical depth on this project. Keep responses short. Redirect to pgmpy or Fern.**

---

# 13. HR and Behavioral

## 13.1 Common HR Questions

### "Tell me about yourself"

> Good morning/afternoon. My name is Avinash. I am a Software Analyst Trainee at Fern Software, where I have been for over a year and a half, working on a fintech core banking product. My day-to-day involves client ticket triage, SQL-based root cause analysis, UAT and Go-Live support, and writing specifications for enhancements. 
>
> Alongside my role, I contribute to an open-source Python library called pgmpy, used in causal inference and probabilistic ML research. I've landed three PRs in the last seven months and was ranked among the top 13 contributors to their latest release. I also did a self-driven project on LLM fine-tuning with LoRA earlier this year.
>
> I completed my B.Tech in IT from Anna University in 2024 with a CGPA of 8.19. I'm looking for a role with broader technical exposure and stronger development focus, which is why I'm very interested in this TCS opportunity.

### "Why TCS?"

> My time at Fern has been valuable — fintech domain, SQL, client experience. But it's primarily support, not development. I've been using my personal time on pgmpy to stay close to coding, and I'd like that to be my day-to-day role. TCS Prime offers broader scale, technical depth across domains, and more experienced engineers to learn from. That combination is why I'm interested.

### "Strengths"

> Three things. First, I'm honest about what I know and don't know, which makes me reliable. Second, I'm self-driven — my pgmpy work happened entirely on personal time because I wanted to grow technically. Third, I'm good with clients — I've received director-level appreciation for handling a live production issue while maintaining professional communication.

### "Weaknesses"

> My role is primarily support, so my exposure to large-scale system design and formal enterprise software engineering practices is limited. I address this through open-source contribution in pgmpy, where I go through proper PR review. A Prime role would accelerate my growth in these areas.

### "Where do you see yourself in 5 years?"

> I see myself as a strong backend or full-stack developer with solid domain expertise — ideally continuing in fintech given my background, but open to other domains. I'd like to combine production engineering with continuous learning, and continue contributing to open source.

### "Why should we hire you?"

> I bring three things. Real production experience — 1.5 years in a client-facing fintech role means I understand how systems behave in production. Self-driven learning — my open-source work shows I invest in my growth. And honest communication — I know what I know and what I don't, and I ask the right questions rather than bluffing.

### "Tell me about a conflict you handled"

> During a Go-Live, there was a disagreement about the severity of an issue — the development team considered it minor, but the client was blocked. I documented the client impact clearly, coordinated a quick call between both sides, and we agreed on an expedited fix. It reinforced for me that most conflicts are really communication gaps — once both sides see the same facts, resolution usually follows.

### "Tell me about a failure"

> In the Bitcoin Ransomware project, I took on a role I wasn't prepared to contribute to technically. I should have stepped up to code or clearly volunteered a different part — documentation, presentation. Instead, I stayed in the middle. That's one of the reasons I've committed to hands-on work at Fern and pgmpy since — I learned that genuine skill comes from doing, not just observing.

### "Any questions for us?"

Always have 2-3 questions ready:
1. "What does onboarding look like for someone joining Prime at my level?"
2. "What kinds of projects is the team I'd be joining currently working on?"
3. "What qualities do you see in the top performers on this team?"

**Avoid** in round 1: salary, leave, work-from-home.

### Closing

> "Thank you for the conversation. I'm genuinely excited about this opportunity, and I appreciate the chance to discuss my work."

---

# 14. Final Checklist

## Night Before
- [ ] Phone charged + portable charger packed.
- [ ] Bag ready — laptop NOT needed, resume printed (2 copies).
- [ ] Documents downloaded offline on phone.
- [ ] Water bottle + snack for bus.
- [ ] Alarm set for Chennai arrival.

## On Bus
- [ ] Sleep first — do NOT stress-study.
- [ ] If awake in the morning, read this doc at your own pace.

## Morning Before Interview
- [ ] Breakfast + water.
- [ ] 10 minutes glancing through cheat sheet (not full script).
- [ ] Deep breath. Trust the prep.

## During Interview
- **Pause before answering** — 1 second = confidence.
- **Speak slowly** — slower than your natural pace.
- **Eye contact** with the interviewer (or camera if virtual).
- **"I want to be honest..."** is your power phrase.
- **When unsure:** "I'm not fully sure, but my best understanding is..."
- **Never bluff.** Interviewers can always tell.
- **Sip water** if you need a pause.

## Closing Line
> "Thank you for the conversation. I'm genuinely excited about this opportunity, and I appreciate the chance to discuss my work."

---

## FINAL WORD

You have:
- **1.5 years of real production experience** at Fern.
- **7 months of genuine open-source contribution** to pgmpy.
- **Self-driven learning** on LLMs and the modern ML stack.
- **A clean academic record** — 8.19 CGPA.
- **Honest self-awareness** about what you've done and what you haven't.

That's a substantive profile. More substantive than most candidates walking into TCS Prime. Walk in, be honest, pause before answering, and trust the preparation.

Good luck tomorrow.
