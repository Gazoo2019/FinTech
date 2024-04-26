## 18.1 Lesson Plan: Introduction to Blockchain

### Overview

Today's class will introduce students to blockchain technologies. Students will learn the fundamentals of blockchain technology and the types of problems that blockchain solves. They’ll also learn the difference between centralized and decentralized blockchain systems.

Students will also be introduced to the Streamlit web application. This application will be used to build the front end of many blockchain applications throughout this unit and beyond.

Many people believe that blockchain is only about cryptocurrencies. The goal of this lesson is to introduce students to the many applications of blockchain—beyond cryptocurrency—and how blockchain technology will affect their lives as a fintech professional.

---

### Class Objectives

By the end of the class, students will be able to:

* Explain how a blockchain works and its implementations.

* Describe the key features of all blockchains.

* Describe the differences between centralized and decentralized systems.

* Launch a shareable web application using the Streamlit Python library.

---

### Instructor Notes

* This unit marks the beginning of the last section of the course: blockchain. This is an exciting, evolving technology that has implications beyond finance. As you teach the lessons in this unit, emphasize the big picture to engage students and get them excited about the content. For example, blockchain technology can be used to build secure, globally distributed software.

* Be sure to review the "Peoplechain" activity before teaching it in class. This activity, which emulates a blockchain using groups of students and Slack, takes place in several consecutive steps and requires pre-class preparation. The activiy requires the creation of four slack channels (see activity instructions) - make sure to invite all students to the channels prior to class.

---

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [18.1 Lesson Slides](https://docs.google.com/presentation/d/1A2Qks3TdudxOM0hOkUucLIj63kaOG107OVsEDpFCTBE/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (10 min)

Welcome students to the class, and congratulate them for starting the final lap in their boot camp marathon: blockchain. Some might say this is the most exciting lap!

Open the lesson slides and highlight the following points:

* Blockchain is exciting and critical for any career in fintech. Blockchain technology powers not just cryptocurrencies, but also decentralized applications and, in some cases, even business networks. It may be a buzzword in the industry, but it’s actually much more than that—it’s a new way of thinking about money and software applications.

* Traditional financial institutions were intially skeptical about blockchain technology. As time moves forward, blockchain has become more mainstream and these institutions are staying on top of the trends. 

* According to [Forbes](https://www.forbes.com/sites/forbesbusinesscouncil/2021/06/23/trends-in-blockchain-why-big-banks-are-adopting-this-technology/?sh=74ecabb51e27), in 2018, Deloitte conducted a Global Blockchain Survey with 1,000 banks that revealed how curious the industry was about Blockchain technology. More than 95% of respondents affirmed they would make some level of investment in blockchain or distributed ledger technology. 

* Two years later in 2020 there was an unprecedented pandemic and which as a result seemed to rapidly expand the digitization of the economy, and it looks as though the curiosity revealed in the Deloitte study has turned into action.

* According to [Business Insider](https://markets.businessinsider.com/news/currencies/blockchain-technology-financial-institutions-jpmorgan-bitcoin-citi-cryptocurrency-transactions-btc-2021-2) Bank of America's research found that JPMorgan and Citi are using blockchain technology, and other banks are considering allowing clients to hold crypto in bank accounts as of Febuary 2021.

* In addition [CNBC](https://www.cnbc.com/2021/08/23/visa-buys-cryptopunk-nft-for-150000.html) reported in August 2021 that VISA purchased their very own [cryptopunk](https://www.larvalabs.com/cryptopunks) NFT.

* In this lesson, students will explore the fundamentals of a blockchain.

This topic may be intimidating to some students, so offer some words of encouragement. Tell them you’re proud of how far you’ve come together as a group. After 17 weeks, they can now use Python, Pandas, and machine learning. By the end of this unit, they’ll be able to speak “blockchain.” It’ll be challenging, but you know they can do it!

Answer any questions before moving on.

---

### 2. Instructor Do: Blockchain Skill Check (10 min)

Before diving in, get a sense of the students’ blockchain knowledge.

Open the slides and go to the “Have you heard?” slide. Tell students to answer the following questions with a thumbs-up for “yes” or a thumbs-down for “no.”

* How many of you have heard of blockchain before?

* How many of you have heard of cryptocurrency before?

* How many of you have conducted a transaction on a blockchain using a digital wallet?

* How many of you have ever traded cryptocurrency?

Next, ask the students to hold out a [fist-to-five](https://k12teacherstaffdevelopment.com/tlb/what-is-fist-to-five-strategy/) (fist for 0, 5 fingers up for 5) to answer the following questions:

* How familiar are you with blockchain?

* How comfortable are you having a conversation about blockchain technology?

Remark on the results, depending on how students answered. For example:

* “It looks like we have some blockchain experts—awesome!”

Take a mental note of the students who have strong familiarity with blockchain. This way, you can pair them with students who have less knowledge about the topic for the group activities.

Next, ask the students to again hold out a fist-to-five (fist for 0, 5 fingers up for 5) to answer the following questions.

* Before starting this course, how familiar were you with Python?

* Before starting this course, how comfortable were you having a conversation about machine learning?

Use this moment to remind students that, just as they gained Python and ML skills, they’ll soon become well versed in blockchain technology. Learning blockchain may seem like learning a new language, but they’ve already shown that they can learn a new language (Python), and you and the TAs will be there to guide them along the way.

---

### 3. Instructor Do: Introduction to Blockchain (15 min)

In this section, you'll formally introduce the concept of blockchain, including the definition and the key features of blockchains.

#### What Is Blockchain?

Start this introduction by asking for volunteers to share their definition of a blockchain. Incorporate their responses into the lecture, which should cover the following points:

* A **blockchain** is a technology that records and shares data over a network, such as the internet.

* Blockchains can be thought of as a bunch of computers that allow users to securely record and access data from anywhere on the network. The computers work together to make sure that they all agree on what was recorded. Therefore, we can trust that the system will always have a complete and accurate record of the data.

* Blockchains can be used for all sorts of financial applications or services for which recording transactions or other data has importance. Over the course of this module, you’ll learn all about the technology that powers a blockchain - specifically, how it works and why we can trust it to maintain complete and accurate data records.

Explain that the most well-known blockchain application is cryptocurrency—a digital currency for which users can record the storage and transfer of value between participants on the blockchain.

* Most often, people associate blockchain with cryptocurrencies. This association is accurate (cryptocurrency is one application of blockchain). But it’s not the full story.

* Blockchains can be used to record any type of transaction or data. Examples include recording an agreement to buy a house, recording a vote, and even recording a marriage contract.

* All kinds of industries- from finance to healthcare, logistics, real estate, and energy- are finding ways to apply blockchain technologies. Many applications of blockchain prove useful, convenient, and even fun. Here are a few examples:

  * [Mythical Games](https://mythicalgames.com/), a large games studio, allows users to buy and sell digital in-game items over a blockchain, even across different games.

  * [Doc.ai](https://doc.ai/) links medical records across a distributed ledger to lower healthcare costs and advance scientific research.

  * [Bloq](https://www.bloq.com/), an infrastructure platform, allows any company to add blockchain applications to its existing business.

  * [TraDove](https://www.tradove.com/login), a platform that connects suppliers with customers, resembles Alibaba.com, but it relies on blockchain to enable trust and lower transaction costs.

#### Features of Blockchain

Explain that most blockchains, regardless of their use case, share the following key features:

* **Decentralization**: A blockchain is decentralized, because all the users can simultaneously edit the blockchain. Every user always has direct access to the blockchain, and no central authority monitors the user transactions. This is the defining feature of a blockchain.

* **A distributed architecture**: A blockchain is distributed for two reasons. First, many computers in various locations store identical copies of the same ledger. Second, these computers communicate with each other to arrive at particular decisions, like the validity of a new block in the chain.

* **Trust**: The technology is designed so that users can trust that the blockchain accurately records all its data and prevents tampering with that data. Without this trust, no one would use a blockchain for a transaction.

* **Record keeping**: In a blockchain, each **block** represents a transaction (or group of transactions), and the **chain** links these transactions over time.

* **Transparency**: Anyone can review the history of the transactions in a blockchain. This doesn’t mean that anyone can review all the data that the transactions contain. The data itself might be private or sensitive. But users can verify the existence of the transactions - specifically, who added data to the chain and when. Not all blockchains have full transparency, but it’s a common feature.

Explain that, although people commonly associate blockchain technology with cryptocurrencies, these key features belong to any blockchain application.

* It’s important for you as a fintech professional to distinguish the difference between blockchains and cryptocurrencies.

* A blockchain isn’t a cryptocurrency. Rather, it’s a common component of how cryptocurrencies are structured.

* Furthermore, blockchain technology has applications beyond the creation of cryptocurrencies.

The following activity encourages students to think about blockchain beyond just cryptocurrency by asking them to examine a number of blockchain use cases.

---

### 4. Student Do: Use Case Study (15 min)

**Corresponding Activity:** [01-Stu_Use_Case_Study](Activities/01-Stu_Use_Case_Study)

In this activity, students will work in groups to examine a use case for different cryptocurrency and blockchain projects. The goal is for the students to list the blockchain features that are applicable to each of the use cases.

* Break students into groups of three. Each group will examine one of the use cases from the provided list.

* You can either assign each group a use case or allow groups to select one themselves.

Monitor group discussions as students work. Identify students who are actively engaged in the research process and with their peers. Keep these students in mind for later group activities, when it might be helpful to pair them with students who are less comfortable with the material.

Have a TA slack out the following instructions to the class.

**Files:**

[Instructions](Activities/01-Stu_Use_Case_Study/README.md)

---

### 5. Instructor Do: Use Case Study Review (10 min)

**Corresponding Activity:** [01-Stu_Use_Case_Study](Activities/01-Stu_Use_Case_Study)

**Files:**

[Instructions](Activities/01-Stu_Use_Case_Study/README.md)

Begin the activity review by asking students to list the five key features of blockchains:

* Decentralization

* Distributed architecture

* Record keeping

* Trust

* Transparency

Using these features as a guide, ask groups to share a few of the features they curated from the use cases in the activity. Talking points for each of the use cases have been provided to assist in facilitating the discussion.

#### Bitcoin in Venezuela

Source: [BBC News](https://www.bbc.co.uk/news/business-47553048)

* Decentralization: There is no fear of the government devaluing the currency.

* Distributed architecture: Users only need a computer in order to participate in the Bitcoin blockchain. It’s publicly accessible to almost anyone in the world, and it doesn’t require bank accounts that are located abroad.

* Trust: Users trust that their currency will not be devalued and that their funds are secure.

#### Monero

Source: [Brave New Coin](https://bravenewcoin.com/insights/monero-no-plans-to-go-'legit')

* Decentralization: There is no authority overseeing the distribution or use of the Monero cryptocurrency. Therefore, its use in potentially illegal transactions is unmonitored.

* Trust: Users trust that the transactions conducted on the blockchain will remain anonymous and private.

#### Stellar

Source: [Investopedia](https://www.investopedia.com/news/what-stellar/)

* Transparency: Stellar is open source.

* Distributed architecture: Stellar’s business focuses primarily on developing markets where a centralized system can be more challenging to implement. The cross-border nature of the systems design is integral to making the application accessible.

* Record keeping: Stellar seeks to provide money remittance and bank loan distribution to the unbanked population—two areas where accurate and immutable records are paramount.

#### Ethereum

Source: [TechRadar](https://www.techradar.com/uk/news/charting-the-rise-and-rise-of-ethereum)

* All five key features are demonstrated by the Ethereum blockchain and underlie its success, especially as it relates to the creation of smart contracts.

* **Smart contracts** are key in Ethereum’s success. They allow for the creation of decentralized financial (DeFi) applications. The creation and distribution of smart contracts embody all five features of blockchain technology.

#### Machine-to-Machine Transactions

Source: [DXC Technology](https://blogs.dxc.technology/2019/01/29/machines-that-pay-each-other-using-digital-wallets/)

* Record keeping: The record-keeping functionality makes it easy to track usage and payments from one machine to another.

* Distributed architecture: The software can be scaled to many machines.

#### CryptoCribs

Source: [Bitcoin News](https://news.bitcoin.com/meet-cryptocribs-a-rental-service-that-aims-to-decentralize-airbnb/)

* Trust: Trust is integral to the short-term, peer-to-peer rental business.

* Decentralization: CryptoCribs is a service provider. Its application is built on a decentralized network, which makes it more resistant to outages.

* Distributed architecture: Because all renters and rentees can access the software, CryptoCribs works toward eliminating intermediaries in the rental process.

#### Proof of Impact

Source: [Proof of Impact](https://proofofimpact.com)

* Distributed architecture: Proof of Impact provides data that is readily available to all users.

* Trust: The immutable nature of information contained on a blockchain ensures data integrity.

Once each of the groups has had a chance to participate in the discussion, ask if there are any additional questions or insights before proceeding to the next activity.

---

### 6. Instructor Do: Centralized vs. Decentralized Systems (15 min)

In this section, you’ll cover decentralization and its importance in the blockchain ecosystem.

* Decentralization is a defining feature of blockchain—it’s what distinguishes blockchains from traditional banking systems, which are centralized and highly regulated.

Tell students that now they'll learn how a centralized banking system operates, and then contrast that system with a decentralized blockchain.

#### Centralization and Traditional Banking

Define centralization and cover some of its advantages and disadvantages.

* Historically, most systems that maintain financial records—for example, banks and governments—have been **centralized**. This means that one location or one authoritative source runs the financial tasks that are involved in maintaining the system.

  * For example, banks keep internal logs of their money flows. A bank exchanges assets (like cash and stocks) with a wide variety of customers. But the bank doesn't rely on those customers to agree on the amount of money that the bank currently has. The bank keeps its own, authoritative record.

  * People usually consider banks as trustworthy institutions. So, when $50 is transferred from one bank account into a friend's account at a different bank, both parties can trust that the money will arrive at the correct destination, and that the bank will record a decrease of $50 in the sender's balance and an increase of $50 in the receiver's balance.

* The bank's internal log of its money flow is an example of a centralized accounting system, which is also called a **ledger**.

* At a basic level, a ledger keeps track of financial transactions. Any financial ledger includes both **settlement and reconciliation**.  A ledger must facilitate the transfer of assets between one entity and another, which is known as a **settlement**. A ledger must also verify that all its transactions have been correctly done, which is known as **reconciliation**.

* Centralization has advantages.

  * It makes transactions easy and fast. Transactions just need to be logged to the appropriate server, and it's done!

  * Transactions are not cross-checked against other copies on the network, which saves time and energy. If the settlement and reconciliation of a single transaction in a centralized system was reviewed, it could likely be determined, in a simple manner, whether that transaction was correctly done.

* However, centralization also has hidden costs.

  * For instance, say that a centralized system processes millions or even billions of transactions every day. There are now complex and expensive problems.

    * First, investment in extra servers is needed, in case a server goes down or reaches capacity.

    * Any downtime can lead to a chain reaction of failed transactions and other issues, which is a costly problem to solve.

    * Finally, specialists are required, and need to be paid, to monitor these millions of transactions and audit any that appear erroneous.

Blockchain technology mitigates these types of problems by using distributed ledgers and decentralization.

#### Decentralization and Blockchains

Review the concept of decentralization.

* At this point, we know that the concept of decentralization is a system where control is spread across all users of the blockchain.

* What does this look like in practice? A decentralized blockchain is copied and maintained by local computers—of Bitcoin users, for example.

* Unlike a centralized financial system that has one authoritative ledger to record all transactions, the ledger of a blockchain is **distributed** across all the computers that have a copy of the blockchain.

* All of these computers update the ledger with the current transactions, and no single authority monitors the ledger for problematic transactions. Instead, the blockchain technology itself has fraud prevention built in.

Go to the following image in the slide deck. This image illustrates all the computers in a distributed ledger system jointly maintaining a ledger, without a central authority to supervise the system:

![An illustration of a decentralized computer network.](Images/decentralized-network-diagram.png)

* When correctly designed, this kind of distributed ledger—spread across thousands or millions of computers, or **nodes**—is more immune to server outages, malicious hackers, and other factors that can cause transactions to go wrong.

* If one computer goes offline, millions remain to both maintain the transaction history and continue processing new transactions. Even if a malicious hacker compromises the blockchain on thousands of computers, the system is designed so that the remaining blockchains- replicated on potentially thousands or millions more computers - will automatically identify the compromised blockchains as invalid.

* Distributed blockchain technology has a built-in auditing system.

* By contrast, the legacy technology of banks has to rely on more costly techniques to monitor problematic transactions. This is just one reason why large banks, credit card companies, and other traditional financial institutions are embracing blockchain technology.

* A decentralized blockchain network uses a set of rules, called a **blockchain standard**, to govern what the blockchain code can do. The blockchain standard sets a system for copying and distributing transaction records. The blockchain standard assures that all of the computers in the network are validating transactions using the same rules. This way, the collection of records represents a source of truth.

* Enough blockchain copies in agreement about what transactions took place and when determines the **source of truth**, or historical record.

* That a number of copies of the blockchain record in agreement creates the source of truth is what prevents hackers from compromising the system.

  * An example is creating enough fake users with changed records that the entire decentralized network thinks that this changed record must be the source of truth. This is theoretically possible for a distributed ledger like Bitcoin.

  * If 51% of Bitcoin users agree on the exact properties of the ledger at an exact point in time, that becomes the ledger. However, think about the difficulty of realizing such an attack. The attacker would have to set up an operation that generates more false transactions than those in the entire existing operation of all other Bitcoin users (hence, becoming 51% of the blockchain).

  * This would require prohibitively large amounts of resources, like server space, energy, and time. This is why no one has ever successfully attacked a massively distributed cryptocurrency, like the Bitcoin ledger.

#### Centralized Blockchains

While most blockchains are decentralized, it’s possible to operate a blockchain as a centralized system.

  * In a centralized blockchain, only certain participants with special permission can perform transactions on the blockchain. These are called **permissioned** blockchains.

  * Consider a hypothetical blockchain that allows various departments of a city government to record transactions about each property that’s located within its jurisdiction. These might include property tax payments, emergency services, ownership status, and street maintenance history. Placing all this in a single ledger would be terrific for efficiency.

  * Maybe the city would also want to make some of this information publicly reviewable. But they wouldn’t want anybody to be able to edit who owns a property!

  * By contrast, **permissionless** blockchains allow anyone to transact, or make changes, on the blockchain as it continues forward. (However, users can’t go back and edit the history of the transactions in the blockchain.)

Go to the following image in the slides, and then summarize the concept of decentralization in the following way:

![An illustration compares a centralized financial system to a decentralized blockchain system.](Images/decentralized-vs-centralized-diagram.png)

Explain that, in summary, blockchains apply new technology to an old problem: record keeping.

  * Using blockchain's decentralized system, copies of records are stored on every computer, or node, that exists on the blockchain network.

  * This stands in contrast to a centralized system where records are only stored on, and only accessible from, a single server or a single location.

  * Decentralizing the recording of data, such as financial transactions, has many benefits, including reliability and security.

Ask students if they have any questions about the concept of decentralization and how it relates to blockchain before moving on to the next activity.

---

### 7. Student Do: Peoplechain (20 min)

**Corresponding Activity:** [02-Stu_Peoplechain](Activities/02-Stu_Peoplechain)

Explain to students that, working in groups, they will emulate the basic functioning of a blockchain by creating a distributed-ledger-like system.

Each group will act as the following:

* A blockchain user, sending and receiving cryptocurrency.

* A blockchain node with responsibilities for validating transactions.

* A blockchain miner with responsibilities for writing blocks to the chain.

Before class, create four new channels in the class’s group Slack with the following names:

* Balance
* Broadcasted Transactions
* MemPool
* Blockchain

All students need to subscribe to all four channels in order to successfully participate in the activity.

Ask a TA to slack out the instructions for the activity to the students.

**Files:**

* [Instructions](Activities/02-Stu_Peoplechain/README.md)

#### Activity Overview

In this activity, students will emulate the activities of a fictitious blockchain that are involved in confirming a transaction.

You’ll first break students into groups of three or four people. Each group should choose a name that corresponds to the first name of one of the students in the group (for example, Group Tom or Group Adriana).

The activity is divided into four steps.

1. Post cryptocurrency balances on the blockchain.

2. Create blockchain transactions.

3. Validate blockchain transactions.

4. Mine blockchain transactions.

Groups must complete each step before they can proceed to the next step. Work with your TAs to make sure every group stays on task throughout the activity.

#### Instructions

##### 1. Post Cryptocurrency Balances on the Blockchain

Each group will post a (fictitious) balance of their cryptocurrency account in the Balance channel in Slack. The message should be sent by the individual that the group is named after. For example, Adriana should post the balance for Group Adriana. It should be posted in the following format:

  ```text
  Group Tom: 10 BTC
  ```

The starting balance for each group can be verified by looking for the message posted by the group’s namesake.

##### 2. Create a Blockchain Transaction

Now, each group will act as a Bitcoin user. Each group member (the group namesake) who posted in the Balance channel in Step 1 will now post one transaction in the following format to the Broadcasted Transactions channel:

  ```text
  To: Group Adriana, from: Group Tom, amount: 3 BTC, fee: .01 BTC
  ```

Every transaction, no matter the size, should include a fee of .01 BTC.

> **Note:** Groups are not required to post valid transactions. For example, they can send more BTC than they have (according to the balance they posted in Step 1), or send BTC to themselves from someone else. Transactions will be validated in the next step.

##### 3. Validate Blockchain Transactions

In this step, each group will act as a node in the blockchain network by validating the transactions.

In this activity, a transaction is **valid** if it meets the following conditions:

* The group name in the “from” section (see the transaction format in Step 2) matches the name of the sender in the Slack message. Think of this as a digital signature.

* The amount sent is not larger than the group’s balance

To validate a transaction:

* One student from each group should give it a “thumbs up” in the Broadcasted Transactions channel.

* Once a transaction has received a “thumbs up” from at least half of the groups in the class, a TA should copy the transaction from the “Broadcasted Transactions” channel and paste it in the “MemPool” channel in Slack.

> **Note:** Explain to students that, in a blockchain network, a mempool contains validated transactions that are waiting to be confirmed.

##### 4. Mine Blockchain Transactions

In this final step, students will act as miners on the blockchain.

You, the instructor, will choose a random number between 1 and 10. Ask each group to post their guess in the Class Activities channel.

The group that guesses correctly first gets to add five transactions to the next block in the Blockchain channel. To do so, one of the group members will create a “block” message in the channel. In this case, a “block” should look like the following code snippet:

  ```text
  Previous block hash - 0
  to: Group Adriana, from: Group Tom, amount: 3 BTC, fee: .01 BTC
  to: Group Tom, from: Group Adriana, amount: 1.33333 BTC, fee: .01 BTC
  to: Group Arturo, from: Group Aubrey, amount: 7 BTC, fee: .01 BTC
  to: Group Jose, from: Group Nikhel, amount: 1.25 BTC, fee: .01 BTC
  to: Group Samson, from: Group Tanisha, amount:  2.7594 BTC, fee: .01 BTC
  Current block hash - 1
  ```

For this task, be aware of the following:

* The transactions can be copied and pasted from the MemPool channel. Once a transaction is “mined,” it should be marked in MemPool with a checkmark so that it’s not duplicated on the blockchain by other miners.

* For the first block that’s mined, the previous block hash is 0, and the current block hash is 1. For the second block that’s mined, the previous block hash is 1, and the current block hash is 2. The hash count progresses until all transactions have been mined in blocks.

> **Note** Explain to students that the hash code acts as an identifier that links the current block to the previous block. The concept of linking blocks is extremely important to ensuring the integrity of the chain. In the next lesson, we’ll explore how blocks are linked using hash values in greater detail.

* The mining group will receive a reward of 1 BTC as well as the sum of all transaction fees for the transactions added to the pool, for a total of 1.05 BTC to add to their cryptocurrency balance.

Repeat Step 4 until all transactions from the MemPool channel are added to the chain.

---

### 8. Instructor Do: Peoplechain Review (10 min)

**Files:**

* [Instructions](Activities/02-Stu_Peoplechain/README.md)

Ask the students the following questions as a way to connect what they did in the activity with blockchain fundamentals:

**Question:** What were the four main steps associated with creating our People chain? How do these steps relate to real blockchain functionality?

Allow students to answer, and then expand on their responses with the following talking points:

* The four main steps are:

  1. Post cryptocurrency balances on the blockchain.

  2. Create blockchain transactions.

  3. Validate blockchain transactions.

  4. Mine blockchain transactions.

* **Post cryptocurrency balances on the blockchain:** In a real blockchain, cryptocurrency balances are usually accessed through a cryptocurrency wallet.

* **Create blockchain transactions:** All transactions on a blockchain contain at least the information detailed in the activity transactions: sender, receiver, amount of the transaction, and a transaction fee.

* **Validate blockchain transactions:** Every transaction posted to the blockchain must be validated before it’s written to a block. The validation process keeps users from spending more cryptocurrency than they have. Transactions usually wait in the mempool to be validated and written to the blockchain.

* **Mine blockchain transactions:** Once transactions are validated, they’re pulled from the mempool and mined into blocks. Each block consists of a group of validated transactions. Each block has an identifier that ties it to the previous block, which helps to ensure the continuity of the chain.

**Question:** In the activity, was it easy to determine if a group posted an invalid transaction?

  * **Answer:**  Yes. You could check the transaction against the record, which was posted in the Slack channel. In a real blockchain, there are also cryptographic features that prevent invalid transactions.

**Question:** In our fictitious blockchain, how would a user commit fraud?

  * **Answer:** In order for a false transaction to be added to the mempool and, therefore, the blockchain, it would need to appear as though the majority of groups validated the false transaction. Also, the group trying to commit fraud would have needed to win the competition (guessing the random number correctly) in order to mine the false transaction to the blockchain.

**Question:** How does this system of validating and mining transactions, as well as making transactions public, make it more difficult to commit fraud?

  * **Answer:** The ledger, or record, is public, so transactions are visible to all users of the blockchain. Due to this system of checks and balances, users will likely notice if a fraudulent transaction is posted to the chain.

Answer any questions before moving on.

---

### 9. BREAK (15 min)

---

### 10. Instructor Do: Blockchain Rules and Trust (15 min)

In the first part of this section, you’ll introduce the concept of permissioned and permissionless blockchains. The second part of the section deals with the concept of trust in a blockchain.

#### Permissioned vs. Permissionless Blockchains

Start by reviewing the concept of blockchain standards.

* **Blockchain standards** are a set of rules that define the blockchain code and how it operates. Who creates the rules that define the blockchain standard? It depends on whether the blockchain is permissioned or permissionless.

* A **permissioned** blockchain has a trusted, third-party arbiter - for example, a government, corporate CEO or Board of Directors, or another well -respected institution acting as the central decision-making authority.

* A **permissionless** blockchain doesn’t have a central authority to provide trust. Instead, people place their trust in the prespecified rules of the blockchain, which are the incentives that keep the users acting appropriately.

  * For permissionless, or **open**, blockchains, the code of the blockchain includes its “rules of the game.” This code runs for all the users of the chain and is distributed across all the users.

  * Bitcoin and Ethereum are examples of permissionless blockchains.

* What if the rules need to change? In this case, permissionless blockchains are rather democratic.

  * The users of the chain can vote on the proposed changes. If a threshold of votes (usually a majority) accepts the changes, the code is rewritten going forward.

  * However, a strong disagreement concerning the proposed changes to a standard might result in a blockchain fork. Those in favor of the new standard, **fork** the code into a new blockchain that contains the new rule. Those opposed to the new standard continue using the original blockchain.

Go to the slide that shows the following image of a blockchain fork:

![An illustration depicts a blockchain fork.](Images/blockchain-fork.png)

* One well-known example of a blockchain fork was the classic fork of Bitcoin to Bitcoin Cash.

Have a TA slack out the following link so that students can learn more about this fork: [Some Bitcoin Backers Are Defecting to Create a Rival Currency](https://www.nytimes.com/2017/07/25/business/dealbook/bitcoin-cash-split.html).

Summarize the points about permissed and permissionless blockchains:

* The key difference between permissioned and permissionless blockchains is who writes the rules for how the ledger works.

* Ultimately, blockchains (permissioned or permissionless) are about trust. Does the user trust the authority of the entity that’s running a permissioned chain? Or, do they instead trust more in the algorithmic design of a permissionless chain?

* Trust is a subjective concept, but its presence (or lack thereof) can determine the fate of a blockchain.

#### Trust and Value

In this section, you'll examine the concepts of trust and value in a financial context. In doing so, you'll explain why blockchains came into existence and what drives much of their continued success.

* Any financial transaction involves a trusted third party: a person, an institution, or a concept. Without that, the transaction simply doesn’t occur.

  * For example, imagine that someone wants to buy a laptop with a bag of seashells. Unless the seller is a passionate seashell collector, they won’t sell their laptop for that bag. If the same person instead offered a five-inch stack of a particular type of paper (say, $100 bills), they might readily accept. This is because the seller trusts the concept of dollars. If a buyer gives those pieces of paper to someone, that person will in turn do something.

  * Or, perhaps the seller doesn’t trust the person who’s offering them the five-inch stack of bills. That does seem suspicious, right? But if the buyer used Venmo to pay, the seller would feel sure that the money was legitimate and not fake.

  * Why? Because there is trust in the institution that is Venmo. In this case, trust is everything. The money is just a digital row in a database of figures that Venmo tracks, but it has value because of the trust factor.

* In sum, value is built entirely around trust. And because trust is a concept, value is also a concept. Even though a $100 bill hardly differs physically from a paper towel, everyone agrees that it’s worth something—and so it is.

* This level of trust might seem a little scary. What if Venmo overwrites that data entry? Or, what if the US government behaves wildly when printing paper money? In this case, everyone might end up with so much paper money that it’s no longer worth anything.

* These scenarios might seem far-fetched. But after 2008–2009, when the US government’s central bank created nearly a trillion dollars to purchase bonds, they seemed less far-fetched than many people had previously believed. At the same time, this monetary policy shocked many people’s concept of value, insofar as value is defined by the paper that governments print.

* The effort of central banks in many countries and regions during this time to create lots of new money was an attempt to jolt economies out of their near collapse. But this shock of monetary policy was one reason why people began to turn to Bitcoin and other cryptocurrencies as perhaps a more trustworthy source of value.

* One way that Bitcoin builds trust from its users is by strictly controlling supply. By design, only 21 million coins can ever be created.

  * This proved an appealing way to solve the problem of preserving the value of this currency. But, some currencies that came shortly after—Ethereum, for example—had no restriction on supply. Yet, people seemed to trust this currency, too.

  * Why? One answer might be that Ethereum adopted many of the security aspects of Bitcoin but improved the usability of doing transactions. And as more users adopted Ethereum for its usability, they began to trust it both as a way to send money and as a store of value.

* In sum, cryptocurrencies began by presenting an alternative currency in which to place trust, at a time when people questioned their trust in traditional currencies.

* One possible reason that some cryptocurrencies have maintained that trust is that they continue to evolve toward greater usability.

* As long as cryptocurrencies and, more importantly, blockchain, continue to strike that balance between trust and usability, they’re likely here to stay.

#### Blockchain Recap

Recap what students have learned so far: some basic blockchain operations like transaction verification and mining,  the key features of blockchain, blockchain standards, and the importance of trust.

Using the following questions, summarize the lesson through a quick Q&A.

**Question:** What are the key features of blockchain technology?

  * **Answer:** Decentralization, distributed architecture, record keeping, trust, transparency.

**Question:** Why would a fintech entrepreneur want to build a software application that uses blockchain?

  * **Answer:** There are many possible answers to this question, including the following:

    * Permissionless blockchain enables fast, global transactions that are not managed by a single authority.

    * Blockchain supports borderless, neutral, and censor-resistant finance.

    * The decentralized nature of blockchain offers a more secure infrastructure for the next generation of application and web development.

    * A blockchain removes intermediaries such as PayPal, Venmo, and Cash App, and allows for peer-to-peer payments—and thus lower fees.

Explain that the next lessons move beyond blockchain basics and theory and into coding an actual blockchain using Python. For the rest of this lesson, they’ll learn how to use a Python library called Streamlit, which they’ll use to test the functionality of basic blockchain code.

---

### 11. Instructor Do: Introducing Streamlit (15 min)

**Corresponding Activity:** [Streamlit](Activities/03-Ins_Streamlit)

In this section, you will introduce students to the Streamlit library for use with web applications.

**Files:**

Use the starter file to demo the code for the students.

[Starter file](Activities/03-Ins_Streamlit/Unsolved/app.py)

[Solution file](Activities/03-Ins_Streamlit/Solved/app.py)

Begin by explaining that Streamlit is a Python library that allows developers to quickly turn Python scripts into shareable web applications.

* Streamlit can be used with almost any Python script.

* Streamlit is a Python library that is used to create user-friendly webpage interfaces. In this course, Streamlit will be used to build a front-end interface for blockchain functionality.

* Streamlit is a Python library that works only with Python files (`.py` files). Therefore, it won’t work with Jupyter notebooks (`.ipynb` files). Although Python files can be coded in JupyterLab, it’s recommended that you write the applications in Visual Studio Code. Regardless of the integrated development environment (IDE) you use, the Streamlit applications need to be run from a new terminal instance.

Ask a TA to slack out the [Streamlit Gallery page](https://streamlit.io/gallery) to the students.

Allow the students a few minutes to explore the types of web applications that can be created using the Streamlit library. Then, discuss a couple of the applications with the students and ask for volunteers to share one or two favorites.

Next, have a TA slack out the links to the [Streamlit website](https://www.streamlit.io/) and the [Streamlit GitHub page](https://github.com/streamlit/streamlit).

Explain to students that, by using the documentation provided on the [Streamlit website](https://www.streamlit.io/), it’s relatively simple to create web applications like the ones just discussed by incorporating the Streamlit functions into a Python file. This will be demonstrated in the next section.

#### The Streamlit Library

In this section, demonstrate how to use Python and Streamlit to build a basic interactive web application.

First, confirm that students have installed the Streamlit library to their Conda development (`dev`) environments. Then, demonstrate these steps:

* Launch the Conda `dev` virtual environment in the terminal, and then run the following command:

  ```shell
  pip install streamlit
  ```

* Once you’ve installed Streamlit, navigate to the `app.py` file associated with this activity and  import Streamlit into a new Python file as the following code shows:

  ```python
  import streamlit as st
  ```

##### Run the Streamlit Application

In this section, you’ll demo how to run the Streamlit application. Show students these steps:

* Back in the terminal, navigate to the root folder in which your `app.py` file is located and then run the following command:

  ```shell
  streamlit run app.py
  ```

Explain to students that they should always navigate to the folder in which the Python file for their Streamlit application resides.

The following image should match the result that you are seeing, which displays the web address of our running application:

![A screenshot depicts the resulting screen in the terminal window.](Images/streamlit-server-terminal-text.png)

Point out to students that the Streamlit application server is currently serving the web application at `http://localhost:8501`.

* Navigate to this URL, there will be a blank page with a menu (or hamburger) button which looks like three horizontal lines in the upper-right corner of the page.

![A screenshot depicts the page.](Images/streamlit-empty-page.png)

* The Streamlit interface currently renders a blank website because nothing has been written to the page.

With the Streamlit server up and running, it’s time to code some Streamlit functions to display webpage content.

##### Display Content on Your Webpage

Demonstrate the Streamlit functionality for the students. Be sure to cover the following points:

* One of the terrific things about Streamlit is that almost any text can be written from Python directly to the webpage by using the `st.write` function.

* This includes strings, variables, Pandas DataFrames, Markdown syntax, and even emojis.

Pass the string “Hi, this is our first web app in Python! :sunglasses:” to the `st.write` function:

```python
st.write("Hi, this is our first web app in Python! :sunglasses:")
```

While writing the code, have a TA slack out the link to the [Streamlit documentation on the `write` function](https://docs.streamlit.io/en/stable/api.html?highlight=st.write#streamlit.write).

Highlight that the Streamlit documentation is thorough and quite easy to navigate. It generally includes an example of how the code can be used.

Save the file and refresh the webpage. The following image shows the resulting webpage:

![A screenshot depicts our string with the sunglasses emoji at the end.](Images/first-streamlit-st-write.png)

Next, use `st.write` to display a Markdown heading.

  ```python
  st.write("# Python Web App")
  ```

Next, import the Pandas library and create a DataFrame.

  ```python
  import pandas as pd

  df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
  st.write(df)
  ```

Again, save `app.py`, navigate to the terminal, and show where the Streamlit application is still running. Then, navigate to the webpage and click the refresh button.

The following image shows the result you should see on your screen:

![A screenshot depicts the resulting webpage.](Images/app-streamlit-write.png)

Explain that Streamlit offers a streamlined process for displaying Python data on a webpage.

* While this is helpful and fun, web applications become truly useful when users can directly interact with the data or add new data to the webpage. Streamlit helps with this, too.

##### Enable Interaction with Your Web Application

Explain that, to enable interaction with the web application, we add a box to our webpage where users can input data.

In this case, we add a text box, where users can enter text (that is, data in the form of a string).

* Define a new variable named `input_value` to store the string that a user enters.

* Set the `input_value` variable equal to an instance of the `st.text_input` function. This function accepts a unique string that displays on the webpage to describe the text box.

Describe the purpose of the text box by entering the string “Enter a Message”:

  ```python
  input_value = st.text_input("Enter a Message")
  ```

Next, add a "Display Message" button to the webpage for more interactivity.

  ```python
  if st.button("Display Message"):
      st.write(input_value)
  ```

* To create a button, use the Streamlit `st.button` function.

* The button uses  a Python `if` statement so that the function is not triggered until the button on the screen is clicked.

* When a user clicks the “Display Message” button, Streamlit will run the `st.write` function contained inside the button's function.

* The `input_value` contains the string that the user entered in the text box.

Go through the process of saving the file and refreshing the page for the web application.

Demonstrate that you can now type text in the text box (which is the gray box that displays after “Enter a Message”).

Type “Hello there my friends” in the box. We then click the “Display Message” button, and the text that we typed displays on the page!

![A screenshot depicts the updated webpage.](Images/streamlit-ui-elements.png)

Explain that we will be using Streamlit throughout the blockchain units to add front-end functionality to our blockchain work.

Reassure students that the Streamlit documentation is excellent and will prove helpful as they work with Streamlit in this unit and beyond.

Ask students if they have any questions about importing Streamlit to their conda development environment or creating and launching the application, then move to the next activity.

### 12. Student Do: A Streamlit App (20 min)

**Corresponding Activity:** [Streamlit App](Activities/04-Stu_A_Streamlit_App)

In this activity, students will create and launch their own basic Streamlit application.

If they are having trouble launching the application, confirm that they have installed the Streamlit library in the development environment, and that it is active. Otherwise, encourage students to use the Streamlit documentation to resolve any issues.

Slack out the following instructions and starter file to the students.

**Files:**

[Instructions](Activities/04-Stu_A_Streamlit_App/README.md)

[Starter file](Activities/04-Stu_A_Streamlit_App/Unsolved/app.py)

### 13. Instructor Do: Review Streamlit App (10 min)

**Corresponding Activity:** [Streamlit App](Activities/04-Stu_A_Streamlit_App)

If time permits, use the starter file to live code the activity. If time is running short, use the solution file to review the code with the students.

The most significant aspect of the review is demonstrating the process of running the application via the terminal.

**Files:**

[Instructions](Activities/04-Stu_A_Streamlit_App/README.md)

[Solution file](Activities/04-Stu_A_Streamlit_App/Solved/app.py)

[Starter file](Activities/04-Stu_A_Streamlit_App/Unsolved/app.py)

As you work through the following solution, call on students or ask for volunteers to help write the code.

  ```python
  # Import the libraries for Pandas and Streamlit
  import streamlit as st
  import pandas as pd

  # Create a title for your application using markdown syntax and the Streamlit
  # `write` function.
  st.write("# Streamlit Web Application")

  # Create an opening sentence for your application using regular text and the
  # Streamlit `write` function.
  st.write("Streamlit allows you to make shareable web applications.")

  # Create a Pandas dataframe
  df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

  # Write the Pandas dataframe to the page
  st.write(df)

  # Create a text input box using the Streamlit `text_input` function.
  # Save the input as a variable.
  text = st.text_input("Enter a message here")

  # Utilize the Streamlit `button` function to display the text input variable
  # created in the prior step to the page.
  if st.button("Display the Text Message"):
      st.write(text)
  ```

At this point, ask the following question:

**Question:** Did anyone have time to determine the difference between the Streamlit `text_input` function and the `text_area` function?

  * **Answer:** The `text_input` function is best for one-line input, while the `text_area` function is designed to accommodate multi-line text.

After writing the necessary code, navigate to the terminal, activate your Conda `dev` environment, and run the Streamlit application:

  ```shell
  streamlit run app.py
  ```

If time permits, use the [Streamlit documentation on `sidebar`](https://docs.streamlit.io/en/stable/api.html?highlight=sidebar#add-widgets-to-sidebar) to code the bonus section.

Ask for a volunteer to share how to code a sidebar select box that allows the user to choose their favorite Python library. Here’s the code:

  ```python
  library = st.sidebar.select box(
      "What is your favorite Python library?",
      ("Pandas", "NumPy", "Streamlit")
  )
  ```

Ask for another volunteer for the code to display the choice in the sidebar. Here’s the code:

  ```python
  if st.sidebar.button("Display selection"):
      st.sidebar.write(library)
  ```

Ask the students if they have any questions about the Streamlit web application, its code, or how it’s run.

Let students know that Streamlit will be used in the Unit 18 homework, as well as lessons and homework throughout the blockchain section of the course.

Ask for any remaining questions regarding Streamlit or blockchain before ending the class.

### 14. Structured Review

---

### End Class

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
