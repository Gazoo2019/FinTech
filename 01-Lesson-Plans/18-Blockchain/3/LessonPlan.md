## 18.3 Lesson Plan: Build a Decentralized Network

### Overview

In today’s class, students will implement the proof of work consensum mechanism as well as incorporate a block validation process. Both proof of work and block validation allow blockchains to function as a synchronized decentralized network.

The first part of the class focuses on the structure of the blockchain network and the importance of keeping the nodes in a decentralized blockchain in sync.

Next, you’ll explore the proof of work consensus mechanism.You will build a hash guessing algorithm that incorporates a measure of difficulty. Then, you’ll integrate that proof of work algorithm into the PyChain application that was coded in the previous lesson.

Finally, the class will examine the importance of validation in blockchain systems. Students will write the code to validate a blockchain by comparing hash values.

---

### Class Objectives

By the end of this class, students will be able to:

* Describe the components of a blockchain system and how they combine to form a network.

* Articulate the role that the proof of work consensus mechanism plays in keeping the blockchain network synchronized.

* Explain how a difficulty factor influences the proof of work algorithm challenge.

* Integrate a proof of work consensus mechanism into the PyChain blockchain.

* Explain why the validation process is important to the integrity of a blockchain.

* Validate an entire blockchain by comparing the hash values between blocks.

---

### Instructor Notes

* Today's class will build on the PyChain application that was started during Day 2 of this unit.

* Students will be introduced to the concepts and processes associated with the proof of work consensus mechanism and blockchain validation.

* The Streamlit application will be used to test code.

* Make sure TAs are available to students who are struggling with the Python code, the concept of Python classes, or Streamlit.

---

### Slide Show and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [18.3 Lesson Slides](https://docs.google.com/presentation/d/1Y5MktQx50Lwp36UBZYwjw7RYblycn6GV0EJwqqqwiaE/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Decentralized Systems (10 min)

Welcome the students back to class and recap what they’ve done so far in this unit:

* A lot has been accomplished in this unit so far, specifically related to the innovations and impact of blockchain technology.

* Python was used to build a basic blockchain that can securely store financial or other data records.

* Now it’s time to open the blockchain record-keeping system to other users. When doing so, we need to consider the following:

  * How should the system be shared?

  * Who should become the central authority over the system and its processes?

  * Should there be a central authority to monitor the system in order to ensure the legitimacy of all the transactions being processed? Or should responsibilities for the ledger be distributed among its participants?

* As discussed in previous lessons, distributing a ledger and delegating responsibility for the system away from a single, central authority is called **decentralization**. Decentralization is a fundamental part of blockchain design.

Review the difference between a centralized and decentralized system.

* In a centralized system, a central authority monitors and audits transactions in order to protect the system from fraud and other problems.

* In a decentralized blockchain system, no single entity bears the responsibility of monitoring the system. Instead, rules that govern and protect the system are built into the blockchain functionality.

Tell students that, in this lesson, we’ll learn about some of the algorithms that blockchain uses in order to operate as a distributed, decentralized system.

* We’ll enhance the PyChain blockchain created in the previous lesson by adding an algorithm that allows  decentralized participants to  agree on the recorded transactions across the entire system.

---

### 2. Instructor Do: Components of a Blockchain System (20 min)

**Corresponding Activity:** None

This section focuses on the components of a blockchain system that form the backbone of the decentralized networks—specifically, the blockchain nodes and how they work together to form a network.

#### Blockchain Nodes

Introduce the concept of **nodes**.

* Software, like a Python program, can be used to digitally record data and store it in chained blocks.

* In blockchain systems, a device that runs this software—that is, the device that a participant uses to access and add data to the blockchain—is called a **node**.

* Each node is likely a laptop or desktop computer, but it can also be a server in the cloud.

Explain that each blockchain node has two primary responsibilities:

1. Storing a complete copy of the blockchain

2. Running the software that establishes the communication and operation of the system

Explain that a node can store a copy of the ledger, but the software also determines how the blockchain works as a wider system.

* In a single-node system, the blockchain software might allow users to store and access the records only through the command line or a web application. The logic and design of the code and the application can achieve this.

* For example, Python and Streamlit can be used to run a blockchain system that allows users to store and access records through a web browser application.

* However, we haven't yet accounted for a more complex system with multiple nodes.

#### Blockchain Networks

Explain how individual blockchain nodes are combined to create a blockchain network.

* A **network** is simply a collection of computers that connect to each other in some way. This connection can occur through the internet, over a local WiFi connection, or even via a physical cable that connects two computers.

* A **blockchain network** is composed of all the distributed computers, or nodes, that run a copy of the blockchain.

* Distributing copies of the ledger across the blockchain network increases the robustness of the system. If one node in the network goes down, the other nodes will maintain the integrity of the system with their copies.

* In a multiple-node system, such as a decentralized blockchain, the software logic must evolve with the complexity of the network. The number of nodes and how they’re connected and organized influences three main factors:

  1.  How copies of the ledger are distributed.

  2.  Who gets to add new records to the ledger.

  3. How copies of the ledger, maintained on different nodes, are synchronized with each other.

* People often refer to the logic that’s required to maintain the operation, communication, and rules for a blockchain network as **governance**.

* A popular quote from Sonya Mann of the Zcash Foundation breaks down governance with three basic questions:

  1. What should we do?

  2. Who gets to decide?

  3. How are the deciders chosen and held accountable?

> **Note** Slack out the following video link so that students can learn more about [Chaos, Cryptography, and Community Control](https://youtu.be/NDIlGMn8LE4) as presented by Sonya Mann and the Zcash foundation.

Explain that these questions of governance are answered by the type of blockchain that it created.

* The four types of blockchain networks are:

  1. **Public:** A public, or permissionless, blockchain has no access restrictions. Anyone with an internet connection can send transactions and validate them. Governance is established through participant consensus.

  2. **Private:** A private, or permissioned, blockchain is the opposite—that is, the blockchain users must be invited. In this case, the controlling party, or creator of the blockchain, establishes the rules of governance.

  3. **Semiprivate:** A semiprivate, or hybrid, blockchain combines the two in some way.

  4. **Consortium:** A consortium blockchain has restricted access, like a semiprivate blockchain, but consists of two or more groups working together for a common purpose.

* Public (permissionless) and private (permissioned) blockchains are the two most common types, by far.

With this understanding of blockchain networks, examine a simple, three-node, decentralized blockchain network.

Navigate to the slide with the image of the three-node blockchain network, and then cover the talking points that follow.

![Three node blockchain network](Images/three-node-blockchain-network.png)

* The nodes in this system can exist anywhere on the planet (and one day, maybe off the planet!).

* To operate as a network, the blockchain nodes must each run software that allows it to communicate with the other nodes.

* To communicate with each other, the computers in a network use a protocol. A **protocol** is a set of rules that the members of a communication system use to share information with each other. One of the most widely used protocols today is **HTTP**, or hypertext transfer protocol. The vast majority of internet communication uses this protocol.

* In a blockchain network, the software running on the nodes uses protocols to synchronize the copies of the ledger, add new records to the ledger, and perform the other tasks that are needed to operate as a blockchain system.

* With a decentralized blockchain, the authority over the system is encoded directly into the system design. The software, with its protocols and its logic, enforces the rules, allowing the system to self-govern to ensure its overall integrity.

* One of the biggest challenges of designing a blockchain system is deciding who can add new records to the ledger and how to synchronize those records across the nodes.

* Many blockchain systems achieve this through a **consensus protocol**, which is also called a **consensus mechanism**.

#### Consensus Protocols

Introduce the concept of consensus protocols by comparing the operations of a centralized versus a decentralized system.

* Adding records to a ledger is easier to control in a centralized system, because a central authority enforces the rules and communication protocols.

  * Consider a group chat, for example, where multiple users send text messages to a group channel. In a centralized system, these messages go to a central server, which processes them in the order received. The server then rebroadcasts the messages in the correct order to the users in the group. So, everyone receives timely updates in their group chat windows.

* A decentralized system like blockchain has no central server or central authority to manage those communications. Instead, the system relies on algorithms, logic, and protocols to ensure that every user’s copy of the ledger reflects the current state of the record. That is, it ensures that each node can add data to the ledger and that all the nodes maintain the same copy of the continually updating ledger over time.

* Ensuring a consensus across the network about the state of the ledger is fundamental to the operation of a blockchain system. Without it, no guarantee would exist that your version of the ledger matched anyone else's version. You therefore wouldn’t be able to trust the system as a whole.

  * For example, would a seller trust the sale of their house to a blockchain system if they couldn't guarantee that the buyer had sufficient funds?

  * To trust the system, all the participants must agree on the state of the ledger across the system.

> Slack out the following links so that students can learn more about the types of blockchain problems that consensus mechanisms seek to solve: [The Byzantine Generals Problem](https://lamport.azurewebsites.net/pubs/the-byz-generals.pdf) and [Irreversible Transactions](https://en.bitcoin.it/wiki/Irreversible_Transactions)

* Consensus mechanisms use protocols and algorithms to achieve a consensus about the state of the system.

* While many approaches exist for reaching a consensus, two of the most common consensus mechanisms are **proof of work** and **proof of stake**.

* The proof of work consensus mechanism forms the basis of trust for most existing blockchains. Though highly effective, proof of work consumes quite a bit of computational power to accomplish, and therefore requires considerable computing resources and a lot of energy to run them.

* While proof of stake requires less computational energy than proof of work, it’s a newer algorithm that has not yet been implemented on the Ethereum network but is in the development stage for Ethereum.

* Proof of stake is currently used on other blockchains, such as Cardono and Tezos.

Slack out the following link so that students can learn more about proof of work and proof of stake: [Consensus Mechanisms page in the Ethereum documentation](https://ethereum.org/en/developers/docs/consensus-mechanisms/).

Explain to students that they will learn to integrate a proof of work consensus mechanism into their blockchain ledger in the next section.

Depending on the time remaining, ask students some or all of the following questions to confirm their understanding of the components of the blockchain system.

**Question:** How do centralized networks and decentralized networks differ in terms of how transactions are authorized?

  * **Answer:** A centralized system has a single, central authority that is responsible for ensuring the authorization and legitimacy of all transactions on the network. In a decentralized system, all of the members, or nodes, that participate in the system are responsible for transaction authorization and legitimacy.

**Question:** What is the name of the device or computer that participants use to access and add data to the decentralized system, or blockchain?

  * **Answer:** The computer used to access the decentralized system is called a node.

**Question:** What are the two primary responsibilities of the blockchain node?

  * **Answer:** The two responsibilities are (1) storing a complete copy of the blockchain and (2) running the software that establishes the operation of the system and the communication between the nodes.

**Question:** What term is used to describe the group of distributed computers that run the software that powers the decentralized system?

  * **Answer:** The group of distributed computers is referred to as the blockchain network.

**Question:** What term is used to define the logic required to maintain the operation, communication, and rules for the blockchain network? What is this logic used to determine?

  * **Answer:** The logic required to maintain the blockchain is referred to as **governance**. Governance determines how copies of the ledger are distributed, who gets to add new records to the ledger, and how copies of the ledger are synchronized across participating nodes.

**Question:** What are the four main types of blockchain networks?

  * **Answer:** The four main types of blockchain networks are:

    1. **Public:** A public, or permissionless, blockchain has no access restrictions. Anyone with an internet connection can send transactions and validate them. Governance is established through participant consensus.

    2. **Private:** A private, or permissioned, blockchain is the opposite—that is, the blockchain users must be invited. In this case, the controlling party, or creator of the blockchain, establishes the rules of governance.

    3. **Semiprivate:** A semiprivate, or hybrid, blockchain combines the two in some way.

    4. **Consortium:** A consortium blockchain has restricted access, like a semiprivate blockchain, but consists of two or more groups working together for a common purpose.

**Question:** What is the primary goal of a consensus protocol? What are two most common consensus protocols used to update records and maintain the current state of the blockchain network?

  * **Answer:** The primary goal of a consensus protocol is to achieve a consensus across participating nodes regarding the state of the blockchain ledger. The two most common consensus protocols are proof of work and proof of stake.

**Question:** What is a common criticism of the proof of work consensus protocol?

  * **Answer:** Performing proof of work requires tremendous computational power. Therefore, it requires a lot of resources and energy.

---

### 3. Instructor Do: Hash Guesser (15 min)

**Corresponding Activity** [Hash Guesser](Activities/01-Ins_Hash_Guesser)

In this section, you will discuss the relationship between the hash code and the proof of work consensus mechanism. This section will end with a demonstration of the code for a hash guesser program.

Use the `app.py` file located in the `Unsolved` folder to live-code the program for students.

**Files:**

[Starter file](Activities/01-Ins_Hash_Guesser/Unsolved/hash_guesser.py)

[Solution file](Activities/01-Ins_Hash_Guesser/Solved/hash_guesser.py)

#### Proof of Work in a Blockchain System

Start by explaining the role that proof of work plays in the blockchain ecosystem.

* A computer can quickly complete the process of recording data to a block and then adding that block to the chain.

* The proof of work consensus mechanism is used to make it more difficult to add a block to the chain. This makes it less worthwhile to try to cheat the system.

* One of the most popular consensus algorithms today, proof of work was originally based on the **hashcash** algorithm, which was created in the 1990s to combat email spam.

  * The idea behind an algorithm like this is to protect a system from spammers and malicious hackers.

  * Consider the original use case for hashcash: email. Hashcash requires a computer to solve a computational problem before sending an email. When you send regular emails for work or for keeping in touch with friends, solving the problem requires such a small amount of computational energy that you’re not likely to notice your computer doing it. Now, imagine that you’re a spammer who wants to send millions of emails every day. What was a negligible amount of energy suddenly becomes very expensive.

  * In this case, the economic incentive is designed to allow authorized users to use the system without a problem but to make it hard for malicious users to ruin the system for everyone else. Blockchain applies this same concept.

Next, illustrate how proof of work functions in a blockchain.

* In a blockchain scenario, the required extra work involves a guessing game for the participants.

* Specifically, the algorithm chooses a random number. Then, each participant guesses a number until someone guesses correctly. The first participant to guess the correct number gets to add a block to the chain.

> **Note:** Remind students that a random number guesser was used to determine which group mined the transactions in the Peoplechain activity from the first blockchain lesson. The group that guessed the instructor-generated number won the privilege of mining transactions to the chain.

* Whoever completes the work first wins the privilege of adding a new data block to the chain.

* Why is adding a new block to the chain considered a privilege? Because the person who adds the block receives compensation for their efforts in the form of a block reward.

* A **block reward** is a transaction that allocates funds to the user who spent the energy to build that block. The source of these funds varies across blockchains. In the Bitcoin blockchain, the funds are allocated by the chain itself. On the Ethereum blockchain, some of the block reward funds are allocated through fees charged to each transaction.

* In blockchain, the process of doing work to add a block to the chain is called **mining**. And, the participants who want to add a new block are called **miners**.

Explain that, at a high level, the proof of work process is as follows:

  1. The system sets the difficulty of the work that’s required to mine a block. The difficulty determines how much effort, or computational power, will be required to complete the necessary work.

  2. The participants compete to be the first to finish the work.

  3. The first to finish gets to add a record to the ledger.

Break this down for the students further.

* In the proof of work algorithms that blockchains like Bitcoin and Ethereum use, the algorithms require miners to generate a cryptographic hash for the previous block on the chain that contains a specific pattern.

* Calculating the hash for a block is a trivial task for most computers. So, the proof of work algorithm adds difficulty in the following way: it requires miners to find a set of inputs to include in their blocks that results in a specific pattern in the block hash.

* The pattern that the blockchain system usually requires is a certain number of zeros at the beginning of the block hash.

Navigate to the slide showing a hash code beginning with four zeros, similar to the following:

  ```text
  00003fa996ced47773f2dea29cce9b11f951e6dafe321a84ac7d32791c3b4660
  ```

* Without an enormous amount of luck, our block hash won't have those four zeros. So, the data attributes in the block will need to be changed until the block hash begins with four zeros. There is a way for miners to do this without compromising the integrity of either the transaction or the other data that the block stores.

* The computer can go through many changes and hashes before reaching a set of inputs that creates a block hash with the correct pattern.

* The first miner to find the input change that results in the correct pattern for the block hash wins the privilege of adding a new block to the chain.

Demonstrate how this hash guessing approach works in code.

Start by creating the required code outside of a block just to discover how it works. Later you'll create a version that works with our `PyChain` blockchain.

#### Generate the Correct Hash Pattern

Start by building the hashing function for a numerical input. To do so, we’ll use the [hashlib library from PyPi](https://pypi.org/project/hashlib/) and incorporate a function called `hash_number`, as the following code shows:

  ```python
  # Imports
  import hashlib

  # A hashing function
  def hash_number(number):
      sha = hashlib.sha256()
      value = str(number).encode()
      sha.update(value)
      return sha.hexdigest()
  ```

* This code uses the `sha256` function from hashlib to convert a number to a hash code.

* The `encode` function converts the number from human-readable to computer-readable syntax.

Next, test the function by using a `count` variable that is set to 0, as the following code shows:

  ```python
  count = 0
  hash = hash_number(count)
  print(f"The first hash is {hash}")
  ```

Navigate to a terminal instance, activate the Conda environment, and run the code, highlighting the resulting hash (which should appear something like the following):

  ```shell
  The first hash is 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9
  ```

Next, write code that checks whether the resulting hash string starts with four zeros:

  ```python
  while not hash.startswith("0000"):
      count += 1
      hash = hash_number(count)

  print(f"Found a hash with four zeros after {count} attempts")
  print(hash)
  ```

* The [`startswith` function](https://docs.python.org/3/library/stdtypes.html#str.startswith) checks for a pattern at the start of any text string. It returns `True` if it finds the pattern at the start of the string. It returns `False` otherwise.

* The code also uses a `while` loop statement to continue looping through the code, for as long as the hash does not start with four zeros.

* Inside the `while` loop, the `count` code increments by 1 each time the `while` loop runs, calculating a new hash for the updated count. This is how the value of the input is changed until a hash with the desired pattern is achieved.

Run this code for the students in the terminal to demonstrate the final result. A statement similar to the following should appear:

  ```shell
  The first hash is 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9
  Found a hash with four zeros after 88484 attempts
  ```

Now a TA should slack the `app.py` file from the `Solved` folder to the students: [Solution file](Activities/01-Ins_Hash_Guesser/Solved/hash_guesser.py)

Instruct students to run the code on their own machines, adjusting the number of zeros associated with the `startswith` function.

TAs should be available to troubleshoot any issues with running the file. (**Note:** The most common issue is that the Conda development environment is not activated.)

After a couple of minutes, ask the students if they noticed anything when the number of zeros was altered.

* The more zeros that are required, the more attempts it takes for the algorithm to find the matching pattern.

* This is the key to proof of work—the challenge and computational power of finding the hash that matches the required pattern.

Explain to students that the first step toward integrating proof of work into our PyChain is to incorporate hashing into the Block data class.

Ask if students have any questions about the hash guesser code before moving on.

---

### 4. Everyone Do: Add Hashing to a Block (20 min)

**Corresponding Activity** [Add Hashing to a Block](Activities/02-Evr_Add_Hashing_to_a_Block)

In this section, you will work with the students to add a `nonce` to the Block data class, which is part of the process of implementing proof of work into the PyChain application.

Slack out the starter file so the students can code along.

**Files:**

[Starter file](Activities/02-Evr_Add_Hashing_to_a_Block/Unsolved/app.py)

[Solution file](Activities/02-Evr_Add_Hashing_to_a_Block/Solved/app.py)

Start by explaining that a proof of work algorithm requires a certain computation to complete before it allows a new block to be added to the chain.

* The proof of work algorithm sets a difficulty level on the network by setting the difficulty of the required computation.

* This is how a blockchain system controls the amount of time it takes to mine new blocks.

* Adjusting the difficulty of the required work affects the time it takes to complete the work.

* Blockchains use this trick to adjust the mining rate of the system. By adjusting the difficulty, they can speed up or slow down, depending on how quickly new blocks get mined.

Explain that, in this part of the lesson, we’ll set and adjust the difficulty of the mining process as it relates to the Block class from the PyChain ledger. This, in turn, will allow us to speed up or slow down the rate at which blocks can be mined.

Open the  [starter file](Activities/02-Evr_Add_Hashing_to_a_Block/Unsolved/app.py) and direct students to do the same. Tell them to code along on their own computers while you demonstrate.

Take a couple of minutes to review the current hashing function for the Block class from the PyChain application.

* This function uses all the data attributes in the block to generate a cryptographic hash of the block.

* This cryptographic hash is a fixed-length output that represents those exact inputs.

Present the code:

  ```python
  def hash_block(self):
      sha = hashlib.sha256()

      data = str(self.data).encode()
      sha.update(data)

      creator_id = str(self.creator_id).encode()
      sha.update(creator_id)

      timestamp = str(self.timestamp).encode()
      sha.update(timestamp)

      prev_hash = str(self.prev_hash).encode()
      sha.update(prev_hash)

      return sha.hexdigest()
  ```

Explain that, to implement proof of work, the `hash_block` function needs to be adjusted.

Add an extra data attribute called a **nonce** to the block class. Define the `nonce` attribute with a data type of `int` and a default value of 0.

  ```python
  nonce: int = 0
  ```

Explain the concept of a nonce:

* The nonce takes the place of the `count` variable from the `hash_guesser` program.

* The nonce is added for the purpose of changing the block’s hash. This is how new hashes will be produced until one is generated that meets the system’s requirements- without changing the stored data in the block.

* Nonce stands for “number used once.” The number in this attribute is only used once to generate a hash for the block. If that hash doesn’t meet the requirement, a different number will be used, and so on, until the hash requirement is met.

Next, adjust the Block's `hash_block` function to include this new data attribute:

  ```python
  nonce = str(self.nonce).encode()
  sha.update(nonce)
  ```

* The nonce value can now be hashed and included in the Block's information.

The complete `Block` data class is now as follows:

  ```python
  from dataclasses import dataclass
  from typing import Any
  import datetime as datetime
  import hashlib

  @dataclass
  class Block:
      data: Any
      creator_id: int
      prev_hash: str = "0"
      timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
      nonce: int = 0

      def hash_block(self):
          sha = hashlib.sha256()

          data = str(self.data).encode()
          sha.update(data)

          creator_id = str(self.creator_id).encode()
          sha.update(data)

          prev_hash = str(self.prev_hash).encode()
          sha.update(prev_hash)

          timestamp = str(self.timestamp).encode()
          sha.update(timestamp)

          nonce = str(self.nonce).encode()
          sha.update(nonce)

          return sha.hexdigest()
  ```

Finally, along with the students, test the altered code by creating a test block.

Start by creating a `block`, and then run the code in the terminal.

  ```python
  # Create a test block and view the nonce and hash
  block = Block("test", 1)
  print(f"The original nonce is: {block.nonce}")
  print(f"The original block hash is: {block.hash_block()}")
  ```

* The original nonce value should be 0 and there should also be a resulting hash for the block.

Now write the code to update the nonce value, leaving the other information the same. The code is as follows:

  ```python
  # Update the test block and view the nonce and hash
  block.nonce += 1
  print(f"The new nonce is now: {block.nonce}")
  print(f"The new block hash is now: {block.hash_block()}")
  ```

* Navigate to a terminal instance and run the file, highlighting how the hash codes for the two different nonce values are completely different.

* Stress that this is the nature of hash codes: even slightly different inputs yield completely different hash outputs.

Ask if there are any questions about this initial phase of incorporating proof of work into the PyChain before moving on.

---

### 5. Everyone Do: Integrate Proof of Work into PyChain (20 min)

**Corresponding Activity** [Proof of Work](Activities/03-Evr_Proof_of_Work)

In this section, you will work with the students to integrate a proof of work consensus mechanism into the PyChain application.

Slack the starter file out to students so that they can code along with the activity.

**Files:**

[Starter file](Activities/03-Evr_Proof_of_Work/Unsolved/proof_of_work.py)

[Solution file](Activities/03-Evr_Proof_of_Work/Solved/proof_of_work.py)

Explain to students that, in the activity, they will be integrating proof of work functionality into the PyChain application that they developed previously.

Open the [starter file](Activities/03-Evr_Proof_of_Work/Unsolved/proof_of_work.py) and direct students to do the same. Tell them to code on their own computers while you demonstrate.

Examine the provided code.

* The `Block` class includes the `nonce` variable and the code to hash it.

* The `PyChain` class includes the code to both add a new block to the chain, and to list the chain. This code was created in the prior lesson.

#### Create a proof_of_work Function

Explain that incorporating proof of work functionality into the Pychain requires adding a `proof_of_work` function inside the `PyChain` class. The code is as follows:

  ```python
  def proof_of_work(self, block):
      # TODO: Implement proof of work
      return block
  ```

* Inside the `PyChain` class, we first need to define a `proof_of_work` method that accepts a block. This block will be the **candidate block**&mdash;that is, the block being created to add to the chain.

* The proof of work algorithm needs to change the block's nonce until it gets a hash that meets the system requirement. (The actual requirement will be coded later).

* Once it gets the correct nonce, the `proof_of_work` function will return the updated block.

Explain that the full code for this `proof_of_work` function will be implemented in a few minutes.

Update the `add_block` method of the `PyChain` class.

  ```python
  def add_block(self, candidate_block):
      block = self.proof_of_work(candidate_block)
      self.chain += [block]
  ```

* Use the `proof_of_work` function to update the block’s nonce until it gets one that satisfies the proof of work algorithm.

* If this function generates a hash that satisfies the pattern that the proof of work algorithm defines before any other nodes do (that is, if it’s the first node to get the correct number of leading zeros), it will add the updated block to the blockchain.

Confirm for students that the adjusted `PyChain` data class should now appear as follows:

  ```python
  @dataclass
  class PyChain:
      chain: List[Block]

      def proof_of_work(self, block):
          # TODO: Implement proof of work
          return block

      def add_block(self, candidate_block):
          block = self.proof_of_work(candidate_block)
          self.chain += [block]
  ```

Explain that in this next step, we will complete the code for the `proof_of_work` function.

#### Code the proof_of_work Function

Update the `proof_of_work` function to check the hash of the candidate block as follows:

  ```python
  def proof_of_work(self, block):
      calculated_hash = block.hash_block()
      return block
  ```

* Hash the candidate block and check whether this hash meets the system requirement.

* Assign the hash of the candidate block to a variable named `calculated_hash`.

Write the code to check the `calculated_hash` variable against the pattern required by the blockchain. The code is as follows:

  ```python
  num_of_zeros = "0000"

  while not calculated_hash.startswith(num_of_zeros):
      block.nonce += 1
      calculated_hash = block.hash_block()

  return block
  ```

* Use the `calculated_hash` variable similar to the way it was used in the `hash_guesser` code.

* Run a `while` loop that increments the nonce until it gets a hash that meets the requirement.

* Set the requirement as a hash starting with four zeros.

* Once a nonce is found that results in a hash that meets the requirement, the block is returned, including the updated nonce value.

The current `proof_of_work` method is now as follows:

  ```python
  def proof_of_work(self, block):
      calculated_hash = block.hash_block()
      num_of_zeros = "0000"

      while not calculated_hash.startswith(num_of_zeros):
          block.nonce += 1
          calculated_hash = block.hash_block()

      return block
  ```

Explain to students that one quick additional code change is needed.

* Instead of hard coding four zeros for our hash requirement, a Python trick is used to make it easier to change the difficulty requirement for the blockchain computation. Here’s the code:

  ```python
  @dataclass
  class PyChain:
      chain: List[Block]
      # Add a difficulty attribute to PyChain
      difficulty: int = 4

  #Inside proof_of_work, add a num_of_zeros variable
  num_of_zeros = "0" * self.difficulty
  ```

* Multiply any Python string by a number: Python will duplicate the string characters that number of times.

* If the string "0" is multiplied by 4, the result is a string of four zeros, or "0000".

* This allows for storage of the system’s difficulty (that is, the number of zeros that a block’s hash must start with) directly in the data class.

* In the `PyChain` data class, a `difficulty` data attribute is created with type `int` with a default value of `4`. This acts as a default value of our difficulty level.

* The difficulty level of the PyChain application can now be dynamically adjusted.

* The complete `PyChain` data class is now as follows:

  ```python
  @dataclass
  class PyChain:
      chain: List[Block]
      difficulty: int = 4

      def proof_of_work(self, block):
          calculated_hash = block.hash_block()

          num_of_zeros = "0" * self.difficulty

          while not calculated_hash.startswith(num_of_zeros):
              block.nonce += 1
              calculated_hash = block.hash_block()

          return block

      def add_block(self, candidate_block):
          block = self.proof_of_work(candidate_block)
          self.chain += [block]
  ```

Let students know that, with those few lines of code, a proof of work consensus mechanism has just been built into the PyChain application.

Ask for a volunteer to review the high-level steps for the PyChain application, including the proof of work integration. (Assume that the application starts with a call to the `add_block` function.) An acceptable answer would be something similar to the following:

  * Starting at the `add_block` function, the candidate_block goes to the `proof_of_work` function.

  * The `proof_of_work` function passes the `block` to the Block class's  `hash_block` function, where all of the block information, including the `nonce`, are hashed via the `sha256` algorithm. A hash code is returned and assigned to the value `calculated_hash`.

  * The `num_of_zeros` value is established based on the `difficulty` level.

  * The starting values of the `calculated_hash` are compared to the `num_of_zeros` requirement.

  * If the starting values of the `calculated_hash` meet the requirement, the block is returned to the `add_block` function and is written to the chain and the program exits.

  * If the starting values of the `calculated_hash` do not meet the requirement, the nonce value is incremented by 1, a new hash is generated, and the comparison is made again until it does meet the requirement.

Ask students if they have any questions about the code that has just been created.

Now that the `proof_of_work` function has been built, it’s time to test it using a Streamlit application.

---

### 6. Student Do: Dynamic Difficulty ( 20 min)

**Corresponding Activity** [Dynamic Difficulty](Activities/04-Stu_Dynamic_Difficulty)

In this activity, students will test the integration of the proof of work consensus mechanism in the PyChain application.

Slack out the following instructions and starter file to students.

**Files:**

[Instructions](Activities/04-Stu_Dynamic_Difficulty/README.md)

[Starter file](Activities/04-Stu_Dynamic_Difficulty/Unsolved/app.py)

---

### 7. Instructor Do: Review Dynamic Difficulty (10 min)

**Corresponding Activity** [Dynamic Difficulty](Activities/04-Stu_Dynamic_Difficulty)

In this review, focus on the role of the proof of work consensus mechanism in adding a block to the chain.

As you are testing the application, Be sure to adjust the difficulty level when testing the application.

If the class is running on time, live code the full solution for the students. If you do not have the full 10 minutes available for the review, use the solution file to highlight the code solutions for the students, and focus on demonstrating the application.

> **Note:** Feel free to use the following video to guide your review:
>
> [Dynamic Difficulty Solution Walkthrough](https://fast.wistia.net/embed/iframe/nf7i0n0i64)

**Files:**

[Instructions](Activities/04-Stu_Dynamic_Difficulty/README.md)

[Solution file](Activities/04-Stu_Dynamic_Difficulty/Solved/app.py)

[Starter file](Activities/04-Stu_Dynamic_Difficulty/Unsolved/app.py)

Start by reviewing the code that is contained within the `app.py` starter file, highlighting the following information:

* The `Block` class contains the `nonce` variable and the code required to hash the value.

* The `PyChain` class has the `proof_of_work` function declared, but it is not complete.

* Explain the role of the [Streamlit `cache_resource` decorator function](https://docs.streamlit.io/library/advanced-features/caching). Streamlit is inherently designed in such a fashion that it re-runs the entire script, everytime the user interacts with functions. This can cause unnecessarily running of functions that don't need to be updated, and might slow the app down if those functions take a long time to run. This is where caching comes into play. Caching allows us to store results of slow function calls, so they only need to run when updates are made. This makes our apps run much faster.

This function will keep the page from refreshing all of the content when updates are made.

  ```python
  @st.cache_resource()
  ```

* Based on the Streamlit code, specifically the `setup` function, a "Genesis" block will be created and added to the PyChain when the application is launched.

  ```python
  def setup():
      print("Initializing Chain")
      return PyChain([Block(data="Genesis", creator_id=0)])


  pychain = setup()
  ```

* There is a Streamlit `button` in place to add a new block to the chain. All of the necessary code is included inside the button function.

Next, complete the code for controlling the level of difficulty associated with the proof of work consensus mechanism.

Start by creating the `difficulty` data attribute inside the `PyChain` class as follows:

  ```python
  # Add a `difficulty` data attribute with a data type of `int` and a default
  # value of 4.
  difficulty: int = 4
  ```

Inside the `proof_of_work` function, create the variable `num_of_zeros`. Here’s the code:

  ```python
  # Add a `num_of_zeros` data attribute that multiplies the string value ("0") by the `difficulty` value.
  num_of_zeros = "0" * self.difficulty
  ```

* The `self` modifier allows the function to access the PyChain class’s `difficulty` attribute.

Pose the following question to students:

**Question:** What functionality is gained by setting this `difficulty` attribute and adding it to the `proof_of_work` function?

  * **Answer:** The `difficulty` attribute allows us to dynamically control how hard it will be for the `proof_of_work` function to compute a hash code that meets the `num_of_zeros` requirement.

Next, ask for a volunteer to provide the code for the Streamlit `slider`. Be sure to add the `slider` to the application `sidebar`. Here’s the code:

  ```python
  # Add a Streamlit slider named "Block Difficulty" that allows the user to update a difficulty value. Set this equal to the variable `difficulty`
  difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 4)
  ```

Pose the following question to students:

**Question:** What do the numbers associated with the slide bar indicate?

  * **Answer:** The range of the slider is from 1 to 5, with the slider starting at a value of 4.

Explain that, with the `difficulty` variable defined by the slider, we now need to connect that variable to the `difficulty` attribute of the PyChain class, so that this slider variable in Streamlit will actually update our blockchain. Here’s the code:

  ```python
  # Update the `difficulty` data attribute of the `PyChain` data class (`pychain.difficulty`) with this new `difficulty` value
  pychain.difficulty = difficulty
  ```

With all of the code now in place, navigate to a terminal instance, launch the Streamlit application, and demo the code:

  ```shell
  streamlit run app.py
  ```

Highlight that the PyChain ledger includes the `Genesis` block as the application is launched. The `prev_hash` value for this block is 0.

Add a new block to the chain (e.g., Test Block 1). Once the block appears, highlight the values associated with the new block's  `prev_hash` and `nonce` values.

Adjust the `difficulty` via the slider to a value of 2 and add a new block to the chain (i.e,. Test Block 2). Point out the new nonce value, which should be much smaller than that associated with Test Block 1.

Before moving on, ask students if they have any questions about how to integrate the proof of work consensus mechanism into the PyChain application.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Proof of Work Validation (20 min)

**Corresponding Activity** [Proof of Work Validator](Activities/05-Ins_Proof_of_Work_Validation)

In this section, you will demonstrate the code to add validation to the PyChain. This is just a demonstration of code that will help students understand how to add validation to PyChain. Not a working application.

**Files:**

[Starter file](Activities/05-Ins_Proof_of_Work_Validation/Unsolved)

[Solution file](Activities/05-Ins_Proof_of_Work_Validation/Solved)

Explain that, although a proof of work consensus mechanism has been added to the PyChain, there is still no way to be 100% sure that the block is actually valid and that the integrity of the chain is intact.

* For example, there’s a chance that the miner could have been a bad actor and altered the state of one of the preceding blocks. Or, the miner could claim to have found the right nonce value to generate a hash that matches the requirement but, in reality, they have not done the work.

Explain that part of the goal of the proof of work consensus mechanism is to prevent the rest of the nodes on the network from synchronizing their copies with an invalid copy of the ledger.

* In a blockchain that has multiple participants, all the participants must be able to trust the validity of each new block that gets added to the chain.

* To accomplish this, all of the nodes, even those that didn't participate in the competition to write the block, work together to validate the new record in the ledger.

* Luckily for everyone, only the hash code is needed to verify the validity of the new block. Specifically, the block information, which includes the updated nonce value, is hashed to check if it has the correct number of leading zeros. The winning miner already used the nonce that should work, so the validators need to hash that block only once to check its validity.

* Unfortunately, without multiple nodes, this type of validation is hard to test! If there is only one node in the system, there are no other nodes to perform the validation. A network with multiple nodes only requires sending the candidate block to each node and having them hash the block to confirm its validity.

> **Note:** Slack out links to the [Bitcoin Wiki proof of work](https://en.bitcoin.it/wiki/Proof_of_work) page and the [Ethereum proof of work](https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/) documentation page so that students can learn more.

Explain that it’s possible to add another useful type of validation to our blockchain, especially in a scenario where the blockchain consists of a single node: validating the full chain, rather than just the new block.

* Besides validating the candidate block, a blockchain system might also want to validate the entire chain—in other words, validate all of the existing records before adding a new block.

* Many ways exist to do this, and each blockchain has its own validation process.

* For the PyChain ledger, the validation that will be added cryptographically links all the blocks in the ledger through their hashes.

#### Validate the Chain

Open the [starter file](Activities/05-Ins_Proof_of_Work_Validation/Unsolved) for this demo.

Remind students that in our `Block` data class, the hash value of the previous block is already stored in the `prev_hash` data attribute:

  ```python
  @dataclass
  class Block:
      data: Any
      creator_id: int
      timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
      prev_hash: str = "0"
      nonce: int = 0
  ```

Explain that we can manually validate the entire chain by calculating the hash of a block and then checking if the `prev_hash` attribute value in the next block matches.

Navigate to the slide deck image that illustrates this process:

![An illustration depicts comparing the prev_hash attribute value of Block 1 to the hash of Block 0.](Images/block-validator.png)

* The Block 0 data can be validated by checking if the `prev_hash` attribute value in Block 1 matches the calculated hash of Block 0.

Explain the high-level steps for the eventual PyChain validator:

1. Hash the first block in the chain.

2. Access the `prev_hash` attribute value from the next block.

3. Compare the two hashes.

4. Repeat Steps 1 through 3 for each block in the chain until every block’s `prev_hash` value has been evaluated.

5. If all comparisons result in matches, the entire blockchain is valid. Otherwise, it’s invalid.

Ask students if they have any questions about this high-level process.

Next, we’ll implement these steps in code.

First, define an `is_valid` method in the `PyChain` data class:

  ```python
  def is_valid(self):
  ```

Next, calculate the hash of the first block.

To do so, access the first block in the chain.

  ```python
  block = self.chain[0]
  ```

* The first block has an index position of 0, the first block can be accessed with `self.chain[0]`

Then, calculate the hash of that first block by calling the `hash_block` method:

  ```python
  block_hash = block.hash_block()
  print(block_hash)
  ```

Explain that this code takes care of Step 1: hash the first block in the chain.

Remind students that the second step in the process is to access the `prev_hash` attribute value in the next block. The third step is to compare the two hashes. Here’s the code:

  ```python
  next_block = self.chain[1]
  print(next_block.prev_hash)
  ```

* To access the second block, use index position 1 in the chain.

* Then access the value that’s stored in that block’s `prev_hash` attribute.

Finally, compare the two hashes, as shown in the following code:

  ```python
  for block in self.chain[1:]:

      if block_hash != block.prev_hash:
          print("Blockchain is invalid!")
          return False

      block_hash = block.hash_block()
  ```

* The two hashes are compared by manually reviewing the two printed values.

* This completes Steps 2 and 3.

Explain that Step 4 is to repeat Steps 1–3 for each block in the chain.

* To avoid a manual comparison, the code is modified to loop through all the remaining blocks. The loop starts at index position 1 in the chain.

* Then, the loop checks the hash of the previous block to see if it matches the `prev_block` value in the current block.

* If they don't match, the loop will immediately return `False` to alert us that the blockchain is invalid.

* At the end of each time through the loop, we calculate the hash of the current block and store it in `block_hash`. We thus get a new block to compare against during the next loop iteration.

* The loop will check each block, comparing the hash of the block to the following block's `prev_hash` value.

Explain that with Step 4 addressed, we just need to work through Step 5: evaluate the validity of the entire chain. If all the comparisons result in matches, the entire blockchain is declared valid. The code is as follows:

  ```python
  def is_valid(self):
      block_hash = self.chain[0].hash_block()

      for block in self.chain[1:]:
          if block_hash != block.prev_hash:
              print("Blockchain is invalid!")
              return False

          block_hash = block.hash_block()

      print("Blockchain is Valid")
      return True
  ```

* If all of the block hashes are calculated and compared without returning `False`, the entire chain is valid, and a value of  `True` is returned.

The complete code that’s now associated with our `PyChain` data class is as follows:

  ```python
  @dataclass
  class PyChain:
      chain: List[Block]
      difficulty: int = 4

      def proof_of_work(self, block):
          calculated_hash = block.hash_block()
          num_of_zeros = "0" * self.difficulty

          while not calculated_hash.startswith(num_of_zeros):
              block.nonce += 1
              calculated_hash = block.hash_block()
          print("Wining Hash", calculated_hash)

          return block

      def add_block(self, candidate_block):
          block = self.proof_of_work(candidate_block)
          self.chain += [block]

      def is_valid(self):
          block_hash = self.chain[0].hash_block()

          for block in self.chain[1:]:
              if block_hash != block.prev_hash:
                  print("Blockchain is invalid!")
                  return False

              block_hash = block.hash_block()

          print("Blockchain is Valid")
          return True
  ```

Ask the students if they have any questions about the code to validate a single-node blockchain.

Tell students that, in the next activity, they’ll have the opportunity to test the validation functionality. The activity also incorporates Streamlit.

---

### 10. Student Do: Validating the Blockchain (20 min)

**Corresponding Activity:** [Validating the Blockchain](Activities/06-Stu_Validating_the_Blockchain)

In this activity, students will use Streamlit to test the validation functionality associated with the PyChain.

**Files:**

[Instructions](Activities/06-Stu_Validating_the_Blockchain/README.md)

[Starter file](Activities/06-Stu_Validating_the_Blockchain/Unsolved/app.py)

---

### 11. Instructor Do: Review Validating the Blockchain (10 min)

**Corresponding Activity:** [Validating the Blockchain](Activities/06-Stu_Validating_the_Blockchain)

The goal of this part of the lesson is to review the entire PyChain application with the students to confirm they understand the functionality of the blockchain.

> **Note:** Feel free to use the following video to guide your review:
>
> [Validating the Blockchain Solution Walkthrough](https://fast.wistia.net/embed/iframe/64lpn3rnqb)

Time permitting, live code the activity for the students. If time is short, review the solution code and then run the application by using Streamlit.

**Files:**

[Instructions](Activities/06-Stu_Validating_the_Blockchain/README.md)

[Starter file](Activities/06-Stu_Validating_the_Blockchain/Unsolved/app.py)

[Solution file](Activities/06-Stu_Validating_the_Blockchain/Solved/app.py)

Open the starter file and review the provided code.

* The `app.py` file includes the full `Block` class. The `PyChain` class includes the `proof_of_work` function that was created in the prior activity.

* The `PyChain` class also includes the `is_valid` function declaration, but almost no contents. Part of the task is to build out that functionality.

* The Streamlit code includes the `difficulty` slider and the "Add Block" button.

* It looks like a button will need to be added to invoke the `is_valid` function from the `PyChain` class.

Begin the coding portion of the review with building out the `is_valid` function contained inside the `PyChain` class.

The first task is to hash the first block in the chain by using the following code:

  ```python
  # Add the code to generate the hash of the first block in the chain.
  # Set the hash equal to a variable called block_hash
  # Hint - The first block in the chain is at index position 0.
  block_hash = self.chain[0].hash_block()
  ```

* To access the chain, we use the `self` keyword.

* The first block in the chain is accessed through index position 0.

* Once the block is accessed, the next step is to call the Block's `hash_block` function.

Next, write the code that creates the for loop, which is as follows:

  ```python
  for block in self.chain[1:]:
  ```

* The loop starts with the second block in the chain, index position 1, and includes all other blocks.

Then, write the code that compares the hash of the first block (index 0) to the `prev_hash` value contained in the second block (index 1):

  ```python
  # Code an if statement that compares the block_hash of the
  # previous block to the prev_hash value of the current block
  # If the two hashes are NOT equal, print a statement that says
  # "Blockchain is invalid", and then return the value False
  if block_hash != block.prev_hash:
      print("Blockchain is invalid!")
      return False
  ```

* If the two hash values are NOT equal, the block will be deemed invalid—thus the print statement and the return value of `False`.

* Once an invalid comparison is found, there is no need to continue through the loop, so the return value forces the loop to exit.

Finally, write the code that hashes the current block and sets that value equal to the variable `block_hash`:

  ```python
  # Set the block_hash value equal to the hashed value of the current
  # block
  block_hash = block.hash_block()
  ```

* This sets the stage for the next comparison between blocks (i.e., index position 1 to 2, and 2 to 3, etc.)

Point out that all of the block hashes match the `prev_hash` value of the next block, which indicates that the blockchain is valid.

With the `is_valid` function complete, turn your attention to creating the Streamlit validation button.

Ask a student to volunteer the code for creating a Streamlit button, which is as follows:

  ```python
  # Add a button with the text “Validate Blockchain” to your Streamlit interface.
  if st.button("Validate Blockchain"):
  ```

Next, code what action the button will take when pressed:

  ```python
  # Call the `is_valid` method of the `PyChain` data class and `write` the
  # result to the Streamlit interface
  st.write(pychain.is_valid())
  ```

* The function of the button is to access PyChain's `is_valid` function.

* Based on the way the `is_valid` function is written, two things are going to happen:

  1. A sentence will appear in the terminal that tells us if the PyChain is valid or invalid.

  2. Either `True` or `False` will be returned.

* We want to know the outcome of the validation, so `st.write` is used to display the returned value to the screen for the application’s user.

With all of the code in place, navigate to your terminal instance and run the application.

Start the demonstration by adding two blocks to the chain (possible suggestions for input text are “Test Block 1” and “Test Block 2”). As you are adding these blocks, be sure to adjust the `difficulty` slider to demonstrate how altering the level of difficulty changes the time associated with mining each of the blocks.

Then press the validation button. Point out where `True` prints to the screen and where the `Blockchain is Valid` statement prints to the terminal.

Now, recap everything students learned today about the blockchain validation process:

* Hashing

* The role of the nonce value and difficulty metric

* Proof of work consensus mechanism

* Blockchain validation

Ask students if they have any questions about the material, particularly proof of work and validation.

Let them know that it’s a huge accomplishment to work through all of these blockchain basics. They’ll put all of this information to use as they begin to work with the Ethereum blockchain in the next unit.

* The PyChain application mirrored a centralized blockchain: a single node creates a transaction that also becomes a block; the block is verified through proof of work; multiple blocks build the chain; and the chain can be verified through each block's hash.

* The next unit will explore a decentralized blockchain, specifically the Ethereum blockchain, that consists of multiple users, or nodes.

* Additionally, blocks will consist of multiple transactions.

* That being said, the overarching functionality is the same: users create transactions; transactions make up blocks; proof of work is used to verify transactions and build blocks; and a validation process ensures the integrity of the blockchain.

---

### 12. Instructor Do: Structured Review (35 min)

> **Note:** If you are teaching this lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

---

## End Class

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
