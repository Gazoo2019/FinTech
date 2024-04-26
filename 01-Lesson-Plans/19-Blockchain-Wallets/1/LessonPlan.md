## 19.1: Blockchain Transactions and Web3.py

---

### Overview

In today's class, students will be introduced to using Web3.py and adding transactions. They will also learn about the Ethereum blockchain and how blockchains generally work, along with Ethereum transactions and using Web3.py as a provider.

The goals for today's class are for the students to understand how transactions work and how they can connect to Ethereum.

### Class Objectives

By the end of this lesson, students will be able to:

* Articulate how nodes and the mempool play roles in adding transactions to the Ethereum blockchain.

* Explain how gas fees help determine which transactions are selected for addition to the Ethereum blockchain.

* Describe the six steps required to add a transaction to the Ethereum blockchain.

* Compare and contrast low-, medium-, and high-gas strategies.

* Utilize Web3.py as a provider to access account addresses and balances, and convert ether into different denominations.

* Use Web3.py to define the parameters required for an Ethereum transaction, including the sender, receiver, gas, and ether.

* Explain the role of a testnet in the Ethereum ecosystem.

### Instructor Notes

* Today's class will introduce blockchain and Web3.py to students. The activities will help them develop an understanding of the process for adding transactions to the Ethereum blockchain, which they will need for the homework at the end of this unit. Each coding challenge is an opportunity to make connections between how the Ethereum blockchain functions and how students can contribute to it.

* The coding activities are designed to get more difficult as the lesson progresses, but the initial activities will give students the chance to establish comfort and build momentum with Web3.py and blockchain. As they learn the fundamentals, some students may find the code drills to be trivial, but the drills will help them become fluent in both syntax and fundamental problem-solving.

* Code drills range in complexity and pace, so the time allotted to each section of activities may need to be adjusted to allow students to work through the problems at their own pace. You may find it helpful to review specific drills or exercises with the entire class; the majority of your time should be spent rotating between groups of students as needed to help them with any issues. Be sure to ask students how they are feeling about Web3.py in general, and give them some words of encouragement from your own experience.

* Allow students time to ask questions about the Ethereum blockchain and transactions. The concepts they will learn today are very important for the next few units.

* Slack out the [Web3.py documentation](https://web3py.readthedocs.io/en/stable/). Students will need to reference this throughout this unit.

* Ensure that you have a working login for the [Blocknative Mempool Explorer](https://explorer.blocknative.com/).

* Overall, this should be a fun day that helps students build confidence in their programming skills. Be sure to offer plenty of support and encouragement to beginners.

* Remind the class that a student guide for each unit can be found in that unit's supplemental folder. Each guide contains helpful links and FAQs for the unit. The Unit 19 Student Guide can be found [here](../Supplemental/StudentGuide.md). If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

### Class Slides and Time Tracker

The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1WGgUnjd5n87LryZXSf9Hsgch6yZGCqWulU5vnFx_l_E/edit?usp=sharing).

To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

**Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (10 min)

Welcome everyone to Week 19 of their FinTech Boot Camp!

Start with a brief recap of last week’s lessons about the structure of blockchains and how they operate on a network of nodes. Continue by defining a blockchain transaction and explaining its importance. Then, explain transactions on the Ethereum blockchain.

Discuss the activities that students completed in the last unit:

* You built a local blockchain and a decentralized network using a Python library called Streamlit.

* You constructed a complete PyChain blockchain ledger instance.

* In the homework assignment, you designed this ledger to record financial transactions among multiple parties. Each block on the PyChain ledger contained a Record data attribute, which held the data that was stored in the block.

Introduce the differences between the Ethereum blockchain and the blockchain students built in the previous unit; also explain the purpose of Web3.py:

* On the Ethereum blockchain, instead of a Record attribute, each block has an attribute named Transactions, which stores data.

* This week, you will learn about Web3.py and how to use it to help send transactions on the Ethereum blockchain.

Explain that the ability to send transactions on blockchain is an important skill:

* You will need to know how to send transactions if you plan on working in an industry with blockchain.

* Let's say you work for a company that wants to make million- or even billion-dollar transactions. Any bank is going to charge a percentage as a fee to send such a large amount of money. A blockchain developer with the ability to send cryptocurrency to facilitate purchases becomes very valuable, as they can help save thousands of dollars in transaction fees. In addition, the transaction or transactions will also be stored on the blockchain in its ledger.

* Ethereum is the most actively used blockchain, and it has its own cryptocurrency, ether. It is the second-largest cryptocurrency in terms of market capitalization, and it is the second-most valuable.

* Ethereum is special because it can do things other blockchains cannot, like store entire contracts that automate transactions.

* These contracts can be as simple as an IOU between two parties or they could involve transfers of ownership of cryptocurrency, other financial assets, or even copyrights to intellectual property. Contracts can be as complex as a multiparty international real-estate transaction.

---

### 2. Instructor Do: Adding Transactions to the Blockchain (10 min)

In this activity, refer to the previous units and how the students built a ledger. Discuss how Ethereum transactions are added to the blockchain. As you define the process and concepts, make sure there is time for the students to make connections and ask questions.

Review the process that the PyChain ledger used and compare it to the Ethereum blockchain:

* In the previous unit, you constructed a complete PyChain blockchain ledger instance. The ledger took records from the activity of financial transactions among multiple parties. Each block on your PyChain ledger contained a record data attribute, which held the data that was stored in the block.

* Similar to Bitcoin, Ethereum has a blockchain that stores data in blocks. Ethereum blocks store data such as transactions and smart contracts. The part of the block that stores the transactions is an attribute known as the **transactions attribute**. On the Bitcoin blockchain, this attribute is called a **record attribute**.

Reference the slides as needed to explain the steps for processing a transaction on the Ethereum blockchain.

* First, a member of the blockchain network, or a blockchain participant (you in this case), creates a transaction that will store data or transfer assets over the blockchain.

Ask the students what they think will happen next. Discuss their answers and, if possible, direct them to the correct answer.

* **Question:** What happens after the transaction is created?

* **Answer:** The participant sends this transaction to the blockchain network. This is why you are learning Web3.py today.

Continue to reference the slides as needed, explaining the steps for processing a transaction on the Ethereum blockchain:

* Once the blockchain receives the transaction, the network holds the transaction in a waiting area inside the memory of the network's nodes. The waiting area is known as a **mempool**.

* An Ethereum node’s mempool is where all new transactions wait to be confirmed by the blockchain network, added to a block, and included in the chain.

* **Question:** Why would a transaction be in the waiting area, or mempool? What would keep it from being processed?

Try to help the students reach the answer themselves. Provide the following hint:

* **Hint:** Each computer or server that maintains a copy of the blockchain ledger and validates new transactions—in other words, each participant on the blockchain network—is called a node.

* **Answer:** Each node on the network has a local mempool. When a new transaction is sent to the network, nodes add the new transaction to their local mempools.

* The size of a mempool can vary depending upon the network traffic, or the number of transactions that network participants are generating at any given time.

* In summary, a miner selects the transaction and chooses to process it.

Show a simulation of this Blocknative Mempool Explorer; explain how it works, and make connections to last week's lessons.

[Blocknative Mempool Explorer](https://explorer.blocknative.com/)

Remind the class that the PyChain ledger from last week’s lesson had one transaction on each block on the chain. Reiterate that in real-life blockchains, most blocks are capable of holding considerably more data.

* A miner on the Ethereum blockchain will decide which transactions they would like to mine after they enter a mempool.

* Then, a miner will bundle that transaction with many other chosen transactions that are waiting in the mempool. These are typically transactions that were created on the network around the same time.

* The miner then writes all of the bundled transactions into the same new block on the chain.

* An Ethereum block currently averages around five hundred transactions and about two megabytes of data per block. However, the number of transactions included in any Ethereum block depends on the size and complexity of the transactions.

* The following image illustrates this process:

![mempool to transaction](Images/19-1-mempool-to-transaction.png)

Explain the diagram to students, emphasizing the following:

* The diagram depicts the process of bundling transactions from the mempool into blocks on the chain.

* After an Ethereum participant creates a transaction, it is sent to the network mempools where it waits to be picked up by a miner. A miner bundles transactions from their node’s mempool into a block and then mines the new block.

* Once the block has been mined, it is sent across the rest of the network for validation; it is then added to the ledger.

* Recall from the previous unit that mining is the process of adding a new block to a blockchain.

Answer any questions before moving on.

---

### 3. Instructor Do: Blockchain Transaction Fees (15 min)

In this section, students will learn the concept of gas. First, explain the roles of miners and how transaction fees impact mining speed.

In the next few talking points, discuss how miners work on the Ethereum blockchain, and note that other blockchains that do not use gas fees. Use the slides to help students grasp the concept of gas.

* The fee structure makes the strategy for mining on Ethereum different from Bitcoin.

* Recall that with Bitcoin, the previous block’s hash is first added to the new block’s data, thereby linking the new block to the chain.

* The next step is that network participants (nodes) compete to mine the new block by completing proof of work&mdash;i.e., adding a nonce to the block’s data that will cause the block’s hash to meet the system’s requirements.

* Finally, the successful miner distributes the new block across the network so that all nodes can validate the new block’s hash and then update the ledger with the new block.

* Ethereum miners do not view all transactions in the mempool as having equal priority. The reward for mining each transaction is different.

* Ethereum has set up its transaction fee and payment structure. Let's take a closer look at these transaction fees.

Then, begin to discuss a **blockchain transaction fee** and its purpose.

* A transaction fee on any blockchain is an incentive given to people or miners to run the blockchain on their machines; otherwise, miners would have high energy costs and no return.

![Transaction with gas](Images/19-1-transaction-with-gas.png)

* This is also why many blockchain networks charge a transaction fee every time a participant records a new transaction onto the chain.

* Wiring money through a bank also generally has a transaction fee, but blockchain transaction fees are structured differently.

* Each blockchain network has its own rules for calculating these fees, and pricing can vary even within one network. Often, transaction fees increase or decrease based on supply and demand.

Then, continue to explain transaction fees by walking students through the process of adding a transaction as well as the concept of a mempool on the ethereum blockchain:

* On the Ethereum network, transactions wait in the network mempools before a miner picks them up and adds them to the chain.

* Miners don’t necessarily add transactions to blocks on a first-come-first-serve basis.

* Computational power on the Ethereum network and space within each block are both limited, and demand for them fluctuates.

* During periods of high demand, the number of transactions sitting in an Ethereum node’s mempool may exceed the number of transactions that can fit into a single block.

* The node’s miner will decide which transactions to put in a new block and which to leave in the mempool until later.

* During periods of high traffic, when lots of users are sending transactions, miners will prioritize transactions that pay higher fees.

* In Ethereum, the participant who completes proof of work first and mines a new block receives the transaction fees for all the transactions contained within that block.

* In other words, in the Ethereum ecosystem, the transaction fees are included in the block reward.

Please note that Ethereum transitioned from the Proof-of-Work consensus mechanism to Proof-of-Stake in late 2022. Encourage students to review the speficic details of the Proof-of-Stake implementation for  Ethereum [here](https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/).

Take a moment to rewind and discuss general rules for adding blocks to blockchains.

* Ethereum rules align with previously learned concepts; a block reward allocates funds to the participant who spent the energy to mine a block, and it incentivizes a blockchain network’s participants to spend energy completing proof of work and mining new blocks.

* After a block is mined and validated, it is written to all of the nodes’ ledgers, which effectively executes the block’s transactions across the network.

* On Ethereum, this entire process usually takes between 15 seconds and 5 minutes, depending on network traffic.

Show the following image to the class, and discuss each step of the process for adding a transaction to the Ethereum blockchain.

* The following image illustrates the complete process for adding a transaction to the Ethereum blockchain.

  ![A diagram depicts the process of adding a transaction to the blockchain.](Images/19-1-how-transactions-are-added-to-the-chain.png)

* Notice that this process includes the following steps:

  * Blockchain participants create transactions.

  * Miners bundle transactions waiting in the mempools into new blocks.

  * Miners compete to complete proof of work and mine new blocks.

  * A successful miner sends the new block around the network for validation and receives a block reward.

  * The new block is linked to the blockchain.

  * All blockchain nodes update their copies of the ledger with the new block.

  * The transaction has been inalterably written onto the blockchain.

Now, begin explaining the cost and fee structure for each individual transaction:

* We’re about to review the actual cost and fee structure for sending a transaction to Ethereum.

* Compare this to traditional banking systems; Ethereum’s transaction fee does not depend on the value of the transaction being processed.

* The transaction fee depends on a variety of factors, such as the amount of computational power&mdash;or gas&mdash;that is required to validate the transaction and add it to a block. For this reason, Ethereum's transaction fee is known as a gas fee.

* Gas fees are calculated by multiplying the units of gas required to validate the transaction by the price of each gas unit.

* The price of gas fluctuates based on network traffic&mdash;i.e., the number of transactions waiting for miners in the mempool. The gas price increases during periods of high demand, when many transactions are in competition to be mined at the same time.

* When more participants want to add transactions to the chain, the cost of adding a particular transaction to the chain goes up.

Slack out [Ethereum Gas Explained](https://defiprime.com/gas) to students, and inform them that they can find additional information about Ethereum gas in this helpful article.

Discuss the benefits of using Ethereum blockchain for financial transactions.

* Ethereum nodes are globally distributed; when someone across the globe sends you money, you can access it almost instantly.

* This eliminates needing to wait for your bank to open to withdraw your new funds or pay fees for currency exchange.

* Ethereum’s dynamic, supply and demand&ndash;based fee structure offers another unique benefit for financial transactions: the cost of the transaction is not related to the value of the transaction.

* Processing a cryptocurrency transaction that transfers 100 ether between participants can require the same amount of gas (i.e., the same number of gas units) as processing a transaction of 100,000 ether.

  * Contrast this with traditional money transfer systems, which charge increasingly higher fees to send larger amounts of money.

* In 2018, the cryptocurrency exchange Binance demonstrated the real-world usefulness of a blockchain transaction-fee system by transferring $600 million in Bitcoin for a transaction fee of just $7! A comparable transaction through traditional financial institutions like banks, or even through digital payment platforms like PayPal, could have cost millions of dollars in fees.

Ask the class if they have any questions about Ethereum blockchain transaction fees before moving on.

---

### 4. Everyone Do: Introduction to Web3.py (15 min)

**Corresponding activity:** [Connect to Blockchain with Web3](Activities/01-Evr-Connect-to-Blockchain-Using-Web3)

Slack out the [Web3.py documentation](https://web3py.readthedocs.io/en/stable/) to students for future reference.

In this activity, students will establish a connection to the Ethereum blockchain with Web3.py. Discuss key concepts and definitions with the students, then demonstrate live code so students can gain experience before using Web3.py independently.

Open `Connect-to-Blockchain-Using-Web3.ipynb` in the `Unsolved` folder and begin coding in Jupyter Notebook.

**File:** [Connect to Blockchain with Web3](Activities/01-Evr-Connect-to-Blockchain-Using-Web3/Unsolved/Connect-to-Blockchain-Using-Web3.ipynb)

Ensure everyone has Web3.py installed. If someone seems to be struggling, be sure to have the TA or another student help them so they can keep up for the duration of this lecture and coding session.

  ```bash
  pip install web3
  ```

To start, explain the purpose of Web3.py and how students can use it:

* Web3.py is a library that allows us to talk to Ethereum nodes in Python.

* Web3.py is a software development kit (SDK) like any other SDK you've used to talk to other APIs, but this time the API originates from an Ethereum node.

* Web3.py can help you read block data, sign and send transactions, and deploy and interact with contracts.

* Web3.py allows us to communicate with the blockchain and serves as a window for reading the ledger.

Then, define protocols, a remote procedure call (RPC), and how Web3.py plays a role in connecting nodes on the blockchain:

* Computers in the blockchain network share information by using protocols like the consensus protocols that we learned last week, but these are not the only kind of protocol out there.

* A remote procedure call (RPC) communicates information across a network.

* A procedure call is an instruction to a computer to execute a process, or a procedure.

* A RPC is when a computer program’s request causes a procedure to execute on a computer or shared network at a remote location. The computer or network then completes the request made by the initial computer.

Discuss the next few talking points, which explain how RPCs are helpful to the blockchain:

* When a program is executed using the RPC model, it does not matter whether the requesting computer or network is in a different location than the executing computer or network.

* Web3.py makes this possible with an RPC provider, commonly referred to as a provider. This provider facilitates the connection and communication between our computers and the Ethereum blockchain network. Web3.py comes bundled with several default providers.

* The `EthereumTesterProvider` allows us to simulate interactions with an Ethereum blockchain.

* This means that we don’t have to run our own blockchain or blockchain nodes in order to test code that interacts with the Ethereum blockchain.

* Instead, we will interact with a “mock” blockchain that the ethereum-tester library and the `EthereumTesterProvider` make available for testing.

Check in on students; confirm that they have installed Web3.py. Quickly go over installing Web3.py and demonstrate it by entering the following command in your terminal. Ensure that your TA circulates the room to assist students during the demonstration.

Import `Web3`, then the `EthereumTesterProvider` module.

  ```python
  from web3 import Web3
  from web3 import EthereumTesterProvider
  ```

Instantiate a new `Web3` object and create a new `Web3` instance.

* A new `Web3` object is instantiated by defining a new variable named `w3` and setting its value equal to a new instance of our imported `Web3` class (the Web3.py library and its functionality).

* This new variable, `w3`, will make the functions in the Web3.py library easier to access.

  ```python
  # Create an instance of Web3
  w3 = Web3()
  ```

Remind the class that Web3.py provides Python functions for performing various blockchain operations, such as accessing information on the latest block added to the chain or viewing the balance of cryptocurrency in an account.

Set the name `variable` as `provider`, and set it equal to an instance of the `EthereumTestProvider`.

Then, update our `Web3` instance by passing it the imported `EthereumTesterProvider` as a parameter.

* This will make it so we can access the test provider and use Web3.py functions.

  ```python
  # Create an instance of the EthereumTesterProvider
  provider = EthereumTesterProvider()

  # Update the Web3 instance to include the provider
  w3 = Web3(provider)
  ```

* Now that we have passed the provider to `w3`, we should be able to perform some basic blockchain calls!

* Information such as the block number, miner, block size, and gas used can be requested for the most recent block on the mock EthereumTesterProvider blockchain. To access this information, we call `w3.eth.get_block(“latest”)`.

  ```python
  # Access information for the most recent block
  w3.eth.get_block(“latest”)
  ```

Here’s a sample of what the response should look like:

![getBlock Response](Images/19-1-getBlock-Response.png)

Point out that the data shows characteristics of a mock blockchain. This will allow us to test how any code interacts with a blockchain.

Tell the class the above output has some of the same attributes as the PyChain blocks, including nonce, hash, timestamp, and difficulty. Also, note that since this is Block 0 in the chain, it points to a previous hash (called a parent hash, in this data) of 0.

In the next few talking points, demonstrate some of the features the EthereumTesterProvider allows us to use:

* The `EthereumTesterProvider` instance includes several pre-populated mock-blockchain participant accounts, each containing 1,000,000 ether. These mock accounts can be used to test transactions.

* Compare these mock accounts to real participant accounts on a real blockchain; these mock accounts are each identified by an address that is unique to the account. The account addresses that are associated with our mock blockchain can be viewed by calling `w3.eth.accounts`.

  ```python
  # Print a list of accounts on the blockchain
  print(w3.eth.accounts)
  ```

* This will return a list of all of the account addresses that are included on the mock development blockchain. The list should look something like this:

  ```text
  [
    '0xaBbACadABa000000000000000000000000000000',
    '0xaBbACaDaBA000000000000000000000000000001',
    '0xAbbAcaDaBA000000000000000000000000000002',
    '0xabBACadaBA000000000000000000000000000003',
    '0xabbAcADABa000000000000000000000000000004',
    '0xaBBACADABA000000000000000000000000000005',
    '0xaBbaCadaBA000000000000000000000000000006',
    '0xAbbAcAdaBA000000000000000000000000000007',
    '0xaBBAcadabA000000000000000000000000000008',
    '0xABbacaDabA000000000000000000000000000009'
  ]
  ```

In the next few talking points, explain the output of the code above and refer to the slides as needed:

* Each address contains 42 characters. The first two characters (“0x”) indicate to programs or APIs that what follows is a hexadecimal number.

* The next 40 characters in the address are the last 40 characters of a hashed key that is associated with a participant’s account.

* The address is a unique identifier for a participant’s Ethereum blockchain account.

The Web3.py library also provides the method `get_balance`. If we pass this method an account address, it will fetch the corresponding account balance.

Pass one of the addresses that was returned from the previous call as a string parameter to the `get_balance` method. This will allow us to view the balance of ether in that participant’s account.

* This function from Web3.py accepts an address and returns its balance.

  ```text
  # Access the balance of an account using the address
  w3.eth.get_balance("0xaBbACadABa000000000000000000000000000000")
  ```

* This code will return the following account balance:

  ```python
  1000000000000000000000000
  ```

Explain that the number may look long, but it is not a dollar amount.

* The `get_balance` always returns the account balance in wei, which is the smallest denomination of ether. There are 1,000,000,000,000,000,000 wei in one ether. The image here displays all the denominations of ether.

  ![Denominations of ether](Images/19-1-denominations-of-ether.png)

* To get a clear representation of how much ether we have, we need to convert the integer representation of our account balance from wei to ether.

Explain that we will use Web3.py to do this for us!

* It has a built-in method for this conversion. It is coded using `w3.fromWei` and can be passed our wei integer and the denomination to convert to&mdash;in this case, ether.

* Then, let's pass the result of our `w3.eth.get_balance` call as a variable named `balance`. We’ll then pass balance and a value of “ether” for the denomination to the `w3.fromWei` method.

Tell the class that with this step, the balance of the account we have selected can now be called simply by calling the `balance` variable, as shown in the following code.

  ```python
  # Access the balance of an account using the address
  balance = w3.eth.get_balance("0xaBbACadABa000000000000000000000000000000")
   # Convert balance from wei to ether
  w3.fromWei(balance, “ether”)
  ```

* The `fromWei` method should return a much smaller number than the `get_balance` method returned. `fromWei` returns the following balance:

  ```text
  Decimal('1000000')
  ```

Explain the following points about ether denominations:

* The account balance is actually 1,000,000 ether.

* The value of ether constantly fluctuates. In 2020, the value of one ether in US dollars ranged approximately from $116 to $740.

* Let the dramatic difference between the account balance in ether and the originally returned balance in wei be a cautionary tale: when sending transactions over blockchain platforms, always ensure that you list the transaction value in the correct denomination. You don’t want to accidentally send someone 1,000 times more money than you meant to!

In the next few talking points, summarize what the class just learned and prepare students to establish a connection using Web3.py independently:

* You have just used Web3.py to talk to Ethereum nodes with Python.

* Remember, you’re using a remote procedure call, which communicates information across a network.

* A remote procedure call is when a computer program’s request causes a procedure to execute on a computer or shared network at a remote location. The computer or network then completes the request made by the initial computer.

Refer to the slides in the next few talking points, and give a few examples from the code to remind students:

* `w3.eth.get_blockAccess` uses `Web3` to get a block from the chain; we specified in the parenthesis to get the latest block.

  ```python
  w3.eth.get_block(“latest”)
  ```

* We accessed the list of accounts using `w3.eth.accounts`.

* Then, we accessed the balance of a specific account by placing it inside `w3.eth.get_balance("0xaBbACadABa000000000000000000000000000000")`.

* Finally, we converted the balance from wei to ether with `Web3` by using `w3.fromWei` and passing in the parameters `balance` and `'ether’`.

---

### 5. Students Do: Ethereum Through Web3.py (30 min)

In this activity, students will use Web3.py to connect to a local mock development blockchain. They will then check the account balance of one of the accounts that is available on the mock blockchain.

**Corresponding activity:** [Ethereum Through Web3.py](Activities/02-Stu-Ethereum_through_Web3py)

In this activity, students will use Web3.py to connect to a local mock development blockchain. They will then check the account balance of one of the accounts that is available on the mock blockchain.

Have a TA circulate the class and provide assistance to students who are struggling or in need of clarification.

Provide this [resource](https://web3py.readthedocs.io/en/stable/) for students to help them through this activity.

Tell students to open `ethereum_through_web3py.ipynb` in the `Unsolved` folder.

**File:** [Ethereum Through Web3.py](Activities/02-Stu-Ethereum_through_Web3py/Unsolved/ethereum_through_web3py.ipynb)

**Instructions:** [README.md](Activities/02-Stu-Ethereum_through_Web3py/README.md)

---

### 6. Instructor Do: Review Ethereum Through Web3.py (10 min)

**Corresponding activity:** [Ethereum Through Web3.py](Activities/02-Stu-Ethereum_through_Web3py)

This will be a quick review to explain how to complete the previous activity. Be sure to answer questions and ask for feedback along the way to ensure the class has a solid understanding of Web3.

**Files:** [Ethereum Through Web3.py](Activities/02-Stu-Ethereum_through_Web3py/Solved/ethereum_through_web3py.ipynb)

Open `ethereum_through_web3py.ipynb` in the `Unsolved` folder and begin coding in Jupyter Notebook.

* We needed to import Web3.py, just like we did in the last activity.

  ```python
  from web3 import Web3, EthereumTesterProvider
  ```

* Step 2 instructed us to define a new variable named `w3` and set it equal to a new `Web3()` instance. As in the previous activity, we are creating another instance of Web3.

  ```python
  # Create an instance of Web3
  w3 = Web3()
  ```

* Step 3 had us define a variable named `provider`. Set this variable equal to `EthereumTesterProvider()`, and then pass it to the `Web3` instance.

* Since we are still using Python, we already know how to set variables. `provider` equals `EthereumTesterProvider()`.

* In the previous activity, you created an instance of the `EthereumTesterProvider` like this:

  ```python
  # Create an instance of the EthereumTesterProvider
  provider = EthereumTesterProvider()
  ```

* Remember, you have also passed variables into functions using Python and have created the `Web3` instance in the previous step to make it more accessible throughout the program.

  ```python
  # Pass the provider as a parameter to the Web3 instance
  w3 = Web3(provider)
  ```

* Step 4 had us call the `w3.eth.get_block('latest')` and print the result to check that the mock blockchain was working.

* Remember, you did this in the previous activity, too, as it shows the `latest` block’s information.

  ```python
  # Access information for the most recent block created on the mock blockchain
  print(w3.eth.get_block('latest'))
  ```

* In Step 5, you called `w3.eth.accounts` and printed the result to view your available accounts on the blockchain.

* You are using the same `print()` method that you have familiarized yourself with in previous units and then passing in `w3.eth.accounts` to display the account list.

  ```python
  print(w3.eth.accounts)
  ```

* In Step 6, you called `w3.eth.get_balance()` and passed it to one of the available addresses as a string to check the balance of the account on the chain. Save the balance as a variable named `wei_balance`.

* This is the same syntax used to declare other Python variables. First, we take `wei_balance` and set it equal to `w3.eth.get_balance`; then, we pass in an account from the list as a string.

* To check the balance, use the `print()` method and pass in the variable that you just created, `wei_balance`.

  ```python
  wei_balance = w3.eth.get_balance("0xaBbACadABa000000000000000000000000000000")

  # Print the balance of the account in wei
  print(wei_balance)
  ```

* In Step 7, you used the `w3.fromWei` function to convert your balance from wei to ether.

* Set a new variable in order to do this conversion. In this case, `eth_balance` is what will be called because it represents the account balance in ether.

* The next step is setting `eth_balance` equal to the `w3.fromWei` function mentioned in the instructions.

* Finally, the parameters for this function should include the `wei_balance` variable that we created above and the balance in wei from the specified account. Then, enter the word `'ether'` in single quotes to specify what we are converting the balance to.

  ```python
  # Convert the balance from wei to ether
  eth_balance = w3.fromWei(wei_balance, 'ether')

  # Print the balance in ether
  print(eth_balance)
  ```

Do a quick check-in with the class about how they feel; ask if they have any more questions. Then, announce that it’s time for a break.

---

### 7. Break (15 min)

---

### 8. Instructor Do: Transactions with Web3.py (15 min)

**Corresponding activity:** [Demo Transactions with Web3.py](Activities/03-Ins_Transactions_with_Web3py)

In this demonstration, instructors will show students how to use Web3.py to create a transaction.

Open `Demo-Transactions_with_Web3py.ipynb` in the `Unsolved` folder and begin coding in Jupyter Notebook.

**File:** [Demo Transactions with Web3.py](Activities/03-Ins_Transactions_with_Web3py/Solved/Demo-Transactions_with_Web3py.ipynb)

For the next talking points, reference the code or the slides as you review Web3.py syntax and explain what it means on the Ethereum blockchain:

* Once we are connected to a `Web3` mock blockchain instance, we can use several Web3.py methods to create and send ether-based transactions from one account to another.

Start by calling `web3.eth.send_transaction` and passing it a few parameters. Explain the required parameters to the class; the slides can serve as a point of reference before instructors begin coding:

* `from:` the 42-character Ethereum account address from which the transaction is sent.

* `to:` the 42-character Ethereum account address to which the transaction is sent.

* `gas:` an integer representing the maximum units of gas to be used in mining the transaction. A standard ether transfer requires at least 21,000 units of gas. Any unused gas will be returned to the sender.

* `value:` an integer representing the amount of money, in wei, that this transaction will transfer from the sender to the recipient.

Point out that in order to send our transaction, we’ll need the string Ethereum addresses of the sender and receiver, the integer value of the money (in wei) that we are transferring, and the units of gas that we’re willing to spend on the transaction.

* `w3.eth.accounts` allows us to list the pre-populated participant accounts on our mock development blockchain. Call this function; then, we can copy an address to use as the sender and another address to use as the recipient in our transaction.

  ```python
  # Access a list of accounts on the blockchain
  w3.eth.accounts
  ```

* This should return our list of account addresses in a string, as shown below:

  ```text
  [
  '0xaBbACadABa000000000000000000000000000000',
  '0xaBbACaDaBA000000000000000000000000000001',
  '0xAbbAcaDaBA000000000000000000000000000002',
  '0xabBACadaBA000000000000000000000000000003',
  '0xabbAcADABa000000000000000000000000000004',
  '0xaBBACADABA000000000000000000000000000005',
  '0xaBbaCadaBA000000000000000000000000000006',
  '0xAbbAcAdaBA000000000000000000000000000007',
  '0xaBBAcadabA000000000000000000000000000008',
  '0xABbacaDabA000000000000000000000000000009'
  ]
  ```

Explain that we’ll assign one of these accounts to a variable called `sender` and another to a variable called `receiver`. For this demonstration, we’ll set the address ending in “3” as our sender and the address ending in “4” as our receiver.

  ```python
  # Set the sender address
  sender = '0xabBACadaBA000000000000000000000000000003'

  # Set the receiver address
  receiver = ‘0xabbAcADABa000000000000000000000000000004’

  ```

* Next, we allocate gas (the price that the miner will be paid) for the transaction in order for our transaction to be mined and added to the blockchain.

* This is done by naming a variable to represent gas. For this example, define the variable as `gas`, and then set it equal to the units of gas you are willing to pay the miner.

  ```python
  # Set the units of gas
  gas = 21000
  ```

Then, explain that we will specify the value or the amount of cryptocurrency to transfer from the sender to the receiver. For this example, let’s transfer 200 ether.

* Remember that transactions are done in wei. Earlier, we used the `w3.from.Wei` function to convert from wei to ether.

* Now, we want to do the opposite: convert an amount of ether (in this case, 200 ether) into the equivalent amount of wei. Web3.py has a method called `w3.toWei` that allows us to perform this conversion.

  ```python
  # Convert balance from ether to wei
  value = w3.toWei(200, 'ether')
  ```

* If we print our converted value, it should look like this:

  ```text
  200000000000000000000
  ```

Point out that we have now defined all of the parameters that we need to send our transaction.

* The next step is to communicate the transaction to the mock development blockchain; we’ll use the `eth.sendTransaction function`, and we’ll specify the values for the parameters to, from, gas, and value.

  ```python
  # Send the transaction to the blockchain
  w3.eth.send_transaction({'to': receiver , 'from': sender , ‘gas’: gas, 'value': value})
  ```

Take a moment to congratulate the class. With just a few lines of code, we sent our first financial transaction using Web3.py!

In the next activity, students will try to create a transaction independently. Ensure that they have a moment to ask questions.

---

### 9. Students Do: Transactions with Web3.py (30 min)

**Corresponding activity:** [Transactions with Web3](Activities/04-Stu-Transactions_with_Web3py)

In this activity, students will create their transaction between Ethereum accounts. They will use Web3.py to connect to a local mock development blockchain. Then, they will create, send, and review a financial transaction by using several Web3.py methods.

Tell students to open `transactions_with_web3py.ipynb` in the `Unsolved` folder and begin coding in Jupyter Notebook.

**File:** [Transactions with Web3](Activities/04-Stu-Transactions_with_Web3py/Unsolved/transactions_with_web3py.ipynb)

Encourage students to ask questions and work together.

Have the TA circulate the room to encourage collaboration and answer student questions as needed.

Refer students to documentation for Web3.py, the `EthereumTestProvider`, and Ethereum for Developers to help them do research on the new technology that they are learning. Links are provided below:

**References:**

[Web3.py](https://web3py.readthedocs.io/en/stable/)

[EthereumTestProvider](https://web3py.readthedocs.io/en/stable/providers.html#ethereumtesterprovider)

[Ethereum](https://ethereum.org/en/developers/docs/)

**Instructions:** [README.md](Activities/04-Stu-Transactions_with_Web3py/README.md)

---

### 10. Instructor Do: Review Transactions with Web3.py (10 min)

**Corresponding activity:** [Transactions with Web3](Activities/04-Stu-Transactions_with_Web3py)

Ask students how they did, and give them time to ask questions. Then, either live code the `Unsolved` version of the activity or review  the `Solved` version if time is limited.

As students have completed the first, second, and third steps multiple times, they can all be wrapped into one talking point.

**File:** [Transactions with Web3](Activities/04-Stu-Transactions_with_Web3py/Solved/transactions_with_web3py.ipynb)

* The first step is to import Web3.py `EthereumTesterProvider` and then create an instance of `Web3` and an instance of the `EthereumTesterProvider`.

Remind the class that they imported `web3` and the `EthereumTesterProvider` in the previous activity. The first step is to import `web3` and the `EthereumTesterProvider`.

* In order to create an instance of `Web3`, we set `w3` equal to `Web3()` and create an instance of the `EthereumTesterProvider` by setting the `provider` variable equal to `EthereumTesterProvider()`.

  ```python
  # Imports
  from web3 import Web3, EthereumTesterProvider

  # Create an instance of Web3
  w3 = Web3()

  # Create an instance of the EthereumTesterProvider
  provider = EthereumTesterProvider()
  ```

* Next, we pass the provider into the `Web3` instance or the `w3` variable as a parameter.

  ```python
  w3 = Web3(provider)
  ```

* In Step 4, we call `w3.eth.accounts` and print the result. We’ve done this before by passing `w3.eth.accounts` into the `print()` method.

  ```python
  print(w3.eth.accounts)
  ```

* As previously discussed, this prints a list of accounts on the blockchain.

* In the next part of Step 4, we define two new string variables named `sender` and `receiver`. This references the sender and receiver of the transaction.

* In order to do this, we copy two of the account addresses from the list of accounts.

* Then, set one account address as the string for the `sender` variable, and set the other account address as the string for the `receiver` variable.

* This is a simple Python variable, and both the `sender` and `receiver` are strings. The syntax should be as follows: `sender` equals address in quotes as a string, and `receiver` equals address in quotes as a string.

  ```python
  # Set the sender address
  sender = "0xaBbACadABa000000000000000000000000000000"

  # Set the receiver address
  receiver = "0xaBbACaDaBA000000000000000000000000000001"
  ```

* In Step 5, we set the units of `gas` to 21,000 to ensure that the transaction gets mined and added to the blockchain.

* This specifies the variable `gas` to equal `21000`.

  ```python
  # Set the variable gas equal to 21000 units
  gas = 21000
  ```

* In Step 6, we use the `w3.toWei` function to convert 333 ether into the equivalent denomination of wei. Then, we save the amount in wei as a variable named `value`.

* `value` equals the amount of ether in wei, `w3.toWei` is used for the conversion, and then as parameters we use the amount and denomination, `(333,'ether')`.

  ```python
  # Convert balance from ether to wei
  value = w3.toWei(333,'ether')

  # Review the value in wei
  value
  ```

* In Step 7, we call `w3.eth.send_transaction` and pass in `receiver` as the `to` parameter, `sender` as the `from` parameter, `gas` as the `gas` parameter, and the `value` variable as the `value` parameter.

* The object that is being created represents the transaction hash code. Therefore, we set a variable for this example, we will call it `transaction_hash_code`, and we set it equal to `w3.eth.send_transaction`.

* After, we will view the `transaction_hash_code` object that was created.

  ```python
  # Send the transaction to the blockchain
  transaction_hash_code = w3.eth.send_transaction({
      'to': receiver,
      'from': sender,
      'gas': gas,
      'value': value
  })

  # Review the transaction hash code
  transaction_hash_code
  ```

* In Step 8, we call the `eth.getTransactionReceipt` function and pass the hash code that is returned from sending the transaction as the parameter to review the transaction receipt.

* This allows us to review the transaction receipt using the HexBytes hash code returned from sending the transaction.

  ```python
  # Review the transaction receipt using the HexBytes hash code returned from sending the transaction
  w3.eth.getTransactionReceipt(transaction_hash_code)
  ```

* Finally, in Step 9 we call the `eth.get_block` function and pass it the parameter `latest`.

* We will use this to confirm that you can see the HexBytes code from your transaction in the information provided.

  ```python
  # Review the information from the latest block to confirm your transaction's inclusion
  latest = w3.eth.get_block('latest')

  # Review the latest block
  latest
  ```

Allow time for a Q&A session about the activity.

---

### 11. Everyone Do: Review Web3.py/Fundamental Concepts (20 min)

Now, we will discuss Infura and testnets. These tools are useful for testing and hosting. The students do not need these tools for class, but they can use them for projects.

Begin by explaining how these tools help develop transactions for Web3:

* When programming, we usually follow a pattern after coding a finished product. If things go smoothly, we test and deploy. Otherwise, we test, test, test, test, and then deploy.

* Deploying a transaction that is not ready for deployment can cost us a lot in assets or crypto.

* Testnets such as Kovan, Rinkeby, Ropsten, and Goerli today give us the ability to test any transactions we deploy to the blockchain.

* **Question:** How is a transaction tested without using real money or ether? How will testnets such as Kovan, Rinkeby, Ropsten, and Goerli help?

  * **Answer:** Faucets for each testnet give developers "fake" ether to use!

Elaborate on why they are called "testnets." Before launching anything on the Ethereum blockchain or making changes to the blockchain itself, a version of it is deployed to the Ethereum test network.

* We use these "testnets" to work out any issues we may have before sending real assets. All these testnets can provide ether tokens that carry no real-world value and can be requested from the testnet.

* Kovan defines itself as the "Fast and Reliable Ethereum Test Chain. Kovan is a Proof of Authority (PoA) publicly accessible blockchain for Ethereum; created and maintained by a consortium of Ethereum developers, to aid the Ethereum developer community."

* Explain that because most testnets are not for-profit businesses, most are not always reliable or fast. The goal of the testnet is to catch issues before they are deployed on the blockchain.

* The proof of authority aspect of the Ethereum blockchain gives access to a node, allowing us to use test ether.

Now, take a moment to answer any questions if needed. Then, begin to discuss Infura with the class by covering the next few talking points:

* **Infura** defines itself as a means to provide the tools and infrastructure that allow developers to easily take their blockchain application from testing to scaled deployment&mdash;with simple, reliable access to Ethereum and IPFS.

* **IPFS**, the **InterPlanetary File System**, is a protocol and peer-to-peer network for storing and sharing data in a distributed file system. The file storage is on the blockchain!

* Infura is a development suite that provides API access to the Ethereum blockchain network.

* Infura is what Ethereum calls a **hosted node**, as it hosts all of the services required to interact with the Ethereum blockchain network. This is in contrast to developing your own local node, where you are responsible for engineering requirements associated with Ethereum blockchain integration (i.e., transaction verification and keeping current with the latest blockchain state), which often take up considerable computer memory, bandwidth, and computational resources.

* Infura requires that a developer get an API key, which allows them to monitor who is using services to read from and write to the blockchain. An API key on infura is called a "PROJECT ID".

* Infura allows the developer to determine what Ethereum blockchain they want to connect with&mdash;either the mainnet (the live blockchain) or a testnet like Kovan or Ropsten.

* The primary shortcoming of using a hosted node is that you are centralizing an aspect of your project's infrastructure. If the primary value of blockchain is decentralization, using a hosted node might not make sense.

Explain that each testnet will be a different endpoint listed on Infura, and Infura can host on the mainnet or on testnets.

Remind the class that rather than rely on a testnet to ensure that they can complete their class activities, we use ganache in this course because it is less likely to fail.

Ask the students if they have any questions about the steps we just reviewed. Then, review the following:

* The content in this lesson included a lot of new processes. The point of this discussion was to make sure that we understand the processes for mining and sending transactions on the Ethereum blockchain, definitions of the terms that are used in Ethereum transactions (ether denominations and gas), and key methods used in Web3.py. We also created an environment for testing transactions.

Remind the students that not only are they now able to build a blockchain, they are also able to communicate with them. Today, they were able to connect to a blockchain, read transactions, and send transactions.

* You learned how a transaction is sent on Ethereum blockchain, what a mempool is, and how Ethereum transactions can be “mined in bundles.”

* You learned how miners mine Ethereum in bundles of transactions and how these transactions get prioritized, with the payment being higher or lower based on the amount of gas a sender is willing to send.

* You learned about a new cryptocurrency, ether, and its denominations.

* You addressed some of the benefits of sending transactions on a blockchain rather than through a “brick and mortar” financial institution.

* You created an environment for testing transactions and connected to a faucet to provide ether to test.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
