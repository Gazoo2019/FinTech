## 21.1 Lesson Plan: Introduction to Tokens

### Overview

In today's class, the students will get an introduction to the concept of tokens on the Ethereum blockchain.

The students will learn what tokens are; how to create them by using more-advanced Solidity data structures; and how to secure them by using third-party libraries, like the OpenZeppelin SafeMath library.

---

### Class Objectives

By the end of the class, the students will be able to:

* Explain what a blockchain token is, what gives it value, and how it can be used.

* Distinguish the general difference between a coin and a token in the context of blockchain.

* Build a Solidity smart contract that creates a simple token.

* Use the mapping data structure to associate customer addresses with their individual information.

* Import third-party OpenZeppelin libraries from GitHub into a Solidity smart contract.

* Use the SafeMath library to perform secure math operations.

* Explain the roles that inheritance and composition play in object-oriented programming (OOP)

### Slideshow and Time Tracker

* You can review the slides for this lesson on Google Drive: [Lesson 21.1 slides](https://docs.google.com/presentation/d/1cSpCWvPgT45PQAbTv3NVkR9HFD5DhKKG9DPY_tCiDKA/edit?usp=sharing).

* To add the slides to the student-facing repository, first download the slides as a PDF. To do that, on the **File** menu, select **Download**, and then select **PDF Document (.pdf)**. Then add the PDF file to your class repository along with other necessary files. You can review these instructions in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

  **Note:** Edit access is not available for this document. If you want to modify the slides, create a copy by selecting **Make a copy** on the **File** menu.

* You can review the Time Tracker for this lesson in the following file: [Time Tracker](TimeTracker.xlsx).

---

## Instructor Notes

* Today's class will be challenging as the students start to dig more deeply into advanced Solidity concepts. Take plenty of time to cover and review the new concepts in today's class.

* Reassure the students that as they practice Solidity, they’ll begin to notice common patterns in the code. Many of the examples shown this week can be reused in other smart contract applications.

* For further information about functions, refer to the OpenZeppelin [SafeMath documentation](https://docs.openzeppelin.com/contracts/2.x/api/math).

* Have your TAs keep track of time by using the [Time Tracker](TimeTracker.xlsx).

* **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

---

## Class Activities
### 1. Instructor Do: Class Welcome (5 min)

Take a few minutes to discuss review questions with the class.

* Before we move on to new and advanced concepts in Solidity, let's review some of the basics that we already know:

  * **Question:** What’s Solidity?

  * **Answer:** A high-level, object-oriented programming language.

  * **Answer:** The language that we use to write smart contracts on the Ethereum blockchain.

  * **Answer:** A strictly typed language.

  * **Question:** What’s a `uint`?

  * **Answer:** An unsigned integer.

  * **Question:** What’s the difference between an `int` and a `uint`?

  * **Answer:** An `int` can be positive, negative, or zero, but a `uint` can be only positive or zero.

  * **Question:** Why is Solidity so strict with its typing?

  * **Answer:** Because that allows for better error handling in code.

  * **Answer:** Because contracts shouldn’t leave room for ambiguity.

  * **Answer:** Because being up front about the data types and the sizes to store them results in less computational overhead and gas costs.

  * **Question:** What’s a `payable` address, and how does it differ from a regular address?

  * **Answer:** A `payable` address resembles a regular address, except that it allows calling the `transfer` function to send ether to it.

  * **Question:** What’s a potential benefit of running code in a virtual machine?

  * **Answer:** Code that runs in a virtual machine can’t directly affect the host machine.

  * **Answer:** The code can run anywhere that the virtual machine can run.

---

### 2. Instructor Do: Introduction to Tokenomics (15 min)

This section will introduce the idea of tokenomics, the nature of tokens on the blockchain and what gives them value, the relationship between tokens and smart contracts, the loose definitions of coins and tokens, and several examples.

* In the traditional financial market, when a company wants to raise capital, they can sell shares of the company to the public through an **initial public offering (IPO)**.

* Blockchain companies have another option available to them: raising funds directly on the blockchain through a similar process, called an **initial coin offering (ICO)**. When a company holds an ICO, they use blockchain technology to generate and sell either blockchain coins or digital tokens.

* **Blockchain coins** are cryptocurrencies that are native to their blockchains, such as Bitcoin.

* **Digital tokens** can represent any asset, utility, service, or currency that has value to the potential buyers.

* Tokens might represent equity in the company (like in a traditional IPO) or a promise of future payment. They might also represent a utility or benefit that relates to the company’s blockchain application or service. These benefits include extra privileges on the system or exclusive or early access. In a gaming system, for example, a token might represent a special or unique item in the game.

* Regardless of the asset that ICO tokens represent, the blockchain uses a particular type of smart contract to encode the details of the token’s value.

* While blockchain tokens are often produced through an ICO, it’s also possible to produce them without undertaking an ICO. In fact, this lesson will teach how to code blockchain token smart contracts without an ICO.

* In short, this lesson is all about tokenomics.

#### Tokenomics

In this section, you’ll explain the concept of tokenomics. 

**Tokenomics**, or the economics of tokens, refers to how blockchain tokens get conceptualized, produced, valued, distributed, traded, and used. A blockchain token represents an asset or utility on a blockchain platform. Essentially, it’s a symbol of value.

Illustrate the concept of tokens by using the example of an arcade as follows:

* Imagine an arcade. When entering the arcade, customers might exchange cash for arcade tokens that are worth 50 cents each.

* Within the ecosystem of the arcade, an arcade token represents a customer’s ownership of 50 cents.

* That customer can exchange the arcade token for a certain amount of time playing a game. Or, they can transfer their ownership of the 50 cents to someone else by giving the arcade token to another customer.

* Blockchain tokens function much the same way. But, blockchain tokens get rendered digitally rather than as physical objects.

* On a blockchain, an asset can be **tokenized**, or represented as a token. Commodities, like gold and silver, and currencies, like the US dollar, can all be represented as tokens. Other types of goods and assets can also be tokenized. These include real-estate properties, cars, and even works of art. In fact, virtually anything that holds value can be represented as a token on a blockchain.

#### Tokens and Smart Contracts

In this section, you’ll establish the relationship between blockchain tokens and Ethereum smart contracts as follows:

* We create tokens on the Ethereum blockchain by using smart contracts.

* The token itself is the symbol of value. The ownership of a token by a blockchain participant (and thus their ownership of the value that the token symbolizes) gets represented in the participant’s wallet.

* The rules and logic that create and maintain the token get encoded in a token smart contract.

* Because we build tokens by using smart contracts, we can program them to do many things besides making payments. Tokens make it easier and more efficient to represent the value of an asset and to trade that asset. Representing commodities as tokens can thus simplify the transfer of ownership.

* Because tokens are powered by blockchain technology, they can be globally traded without involving traditional financial institutions or physical infrastructure. For example, transferring a metric ton of gold requires lots of energy. Transferring tokens that represent that metric ton requires significantly less energy. Furthermore, the borderless nature of blockchain means that the transfer won’t have geographical limitations.

* Imagine a digital wallet that contains records of all the assets that an individual owns, both digital and physical, in a single place. They can manage their home ownership, car payments, artwork, investments, video game items, and more with math that cryptographically proves their ownership of these items and that verifies any transactions associated with them.

* With this system, businesses can also track and transfer assets in a way that improves their liquidity and auditability.

* For example, food items that get purchased at a grocery store could be tokenized. Shoppers could then scan codes on the food items to pull up the entire supply chain history for the purpose of proving exactly where they came from. In fact, some companies have already begun using blockchain technology to track food sourcing in this manner.

#### Coins vs. Tokens

Conclude this section about tokenomics by distinguishing tokens from coins and by introducing the concept of stablecoins, as follows:

* Blockchain tokens often represent cryptocurrency. So, some people in the blockchain community use the terms **token** and **coin** interchangeably. However, they represent two similar but distinct concepts.

* **Coins** represent cryptocurrencies that are native to their blockchains, such as Bitcoin and ether.

* By contrast, **tokens** represent any tangible or intangible asset of value. They get created by deploying smart contracts over existing blockchain platforms.

* Unlike most cryptocurrency coins, a token that holds a currency value can be designed to maintain a stable value. These tokens, called **stablecoins**, are typically backed by a fiat, or government, currency. A stablecoin company often holds a stable currency, like US dollars, in its bank account and then issues tokens that are backed by those dollars.

Ask the students if they have any questions about the concept of tokenomics before proceeding to the next activity.

---

### 3. Instructor Do: Building Tokens with Solidity (20 min)

**Corresponding activity:** [Solidity Tokens](Activities/01-Ins_Solidity_Tokens)


**Files:**

[Starter file](Activities/01-Ins_Solidity_Tokens/Unsolved/ArcadeToken.sol)

[Solution file](Activities/01-Ins_Solidity_Tokens/Solved/ArcadeToken.sol)

In this activity, you’ll demonstrate how to use Solidity to build a smart contract that creates the functionality associated with a simple token.

To accomplish this, you’ll introduce the students to a new data structure, called a **mapping**. You’ll also review the concept of the message object that an earlier module introduced.

Use the starter file to live code the activity for the students.

Explain to the students that the goal of this activity is to build a simple smart contract, named `ArcadeToken`, that allows users to take four actions. Specifically, they’ll be able to check their arcade token balances, transfer tokens between users, purchase new tokens, and mint tokens for the arcade.

To accomplish this task, use Solidity, a new mapping data structure, and the concept of the message object.

#### Explain Mappings

Before diving into the code associated with the token contract, explain the concept of mapping to the students, as follows:

* Think of a **mapping** as an association between two variables.

* For instance, we can map account balances to account addresses. The developer can thus associate a balance with a specific address and then retrieve the current balance for that account at any time.

* A mapping conceptually resembles a Python dictionary with key-value pairs.

* In Solidity, a mapping is a variable type that we define by using the following syntax:

  ```solidity
  `mapping(_KeyType => _ValueType)`
   ```

* To understand the usefulness of mapping for building tokens, let’s return to the arcade example from earlier in the lesson.

* Say that we own the arcade and that we want to switch from a physical-token system to a blockchain-token system. Rather than having customers exchange cash for plastic tokens, we’ll have them exchange ether for blockchain tokens. They can then spend these tokens to play games and redeem prizes at the arcade. We can map the customer account addresses to their account balances&mdash;so that we can track the number of arcade tokens that any customer has at any time.

* We want to convert the concept of the arcade with its arcade tokens into a token smart contract. The token smart contract will contain the logic that creates the tokens, that handles the transactions when arcade customers exchange ether for tokens, and that tracks the token balances in the customer accounts.

Mention that we have just one more feature of Solidity that we need to learn about before coding our token: the message object.

#### Explain the Message Object

Explain that the Solidity message (`msg`) object and its attributes are important concepts for token smart contracts. So, it’s important to take a few minutes to review them.

* The Solidity `msg` object is a **global object**. This means that it’s accessible from any smart contract that we write with Solidity&mdash;without defining the object within our code.

* The `msg` object always refers to the current message that’s being sent to the blockchain. That is, it’s the transaction that’s currently being executed or the smart contract that’s currently being deployed.

* The `msg` object has several attributes, including `msg.sender` and `msg.value`, which we’ll use in this module.

* The `msg.sender` attribute refers to the entity that’s currently sending a message. That is, it’s whoever is executing the current blockchain transaction or deploying the current smart contract.

* It’s important to remember that the value of this attribute can change with each new transaction.

* In the arcade token scenario, for example, when the arcade token smart contract initially gets deployed, the person deploying it becomes the `msg.sender`. When an arcade customer later accesses the token contract to purchase tokens, that customer becomes the `msg.sender`.

* When functionality gets added to the token contract allowing the arcade customers to transfer tokens among themselves, the `msg.value` attribute gets used. This attribute refers to the value of the current transaction, or the amount of ether that the current transaction is transferring.

* Remember that the value of this attribute can change with each new transaction.

Mention to the students that with the concepts of mapping and the message object in mind, it’s time to use Solidity to create arcade tokens!

#### Create a Token Contract

In this section, you'll begin coding the `ArcadeToken` contract.

Start by opening the [starter file](Activities/01-Ins_Solidity_Tokens/Unsolved/ArcadeToken.sol) in the Remix IDE.

In this file, notice the start of a smart contract named `ArcadeToken`, as the following code shows:

```solidity
pragma solidity ^0.5.0;

contract ArcadeToken {

}
```

Next, define three variables inside the `ArcadeToken` contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;

contract ArcadeToken {
  address payable owner = msg.sender;
  string public symbol = "ARCD";
  uint public exchange_rate = 100;
}
```

Let’s go over the three variables in the preceding code:

* The `owner` variable: This variable (of type `address payable`) represents the owner of the `ArcadeToken` contract.

  **Question:** What role does the `payable` modifier play in this variable?

  **Answer:** The `payable` modifier allows the address that `msg.sender` defines to receive ether as part of the contract actions.

  * The contract owner will receive the initial supply of tokens when the contract gets deployed. This owner will also be responsible for transferring those tokens to recipients and creating new tokens as necessary. The contract owner should be the owner of the arcade&mdash;in this case, us!

  * Because this code deploys the contract, `msg.sender` represents the account that creates the smart contract. Because we’ll create the contract, we can set ourselves as the contract owner by setting the `owner` variable equal to `msg.sender`.

* The `symbol` variable: This variable (of type `string public`) represents the ticker of our token.

  * This resembles a stock ticker on a stock exchange. It’s a shorthand representation of the value that the token holds. The token’s ticker will allow other blockchain participants and wallets to recognize it. In this case, we’ll use the “ARCD” ticker to represent our arcade tokens. (“ARCD” consists of letters in “arcade.”) 

* The `exchange_rate` variable: This variable (of type `uint public`) represents the number of tokens that the smart contract will distribute per 1 wei that a customer spends to purchase tokens. We’ll set `exchange_rate` equal to 100. So for every 1 wei that a customer spends, they receive 100 arcade tokens.

The next step is to add a way to track the `ArcadeToken` user balances. Explain that this is where mappings come into play:

* The goal is to create a data container for customer account balances, where we can retrieve the balance for an account by supplying the account number. To do so, we’ll map each account to its current balance.

Now, navigate to the slide that illustrates the following code snippet. Remind the students that to accomplish this in Python, we’d use a dictionary with accounts as the keys, as the following code shows:

```python
# Create a dictionary to store the account balances
balances = {}

# Create an account
account = 123

# Assign that account a balance of 1000
balances[account] = 1000

# Access the account
print(f"The account balance is: {balances[account]}")
```

Next, create a mapping named `balances`. This mapping should accept an account address as the key and store the account balance as the value in the form of an unsigned integer (`uint`), as the following code shows:

```solidity
mapping(address => uint) balances;
```

* It’s possible to create a container for the customer account balances by using a Solidity `mapping` function.

  Navigate to the slide that illustrates an account address mapped to a balance, and explain that this contract might store data that resembles the following:

  ```text
  `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333`.
  ```

* In this example, `0xc3879B456DAA348a16B6524CBC558d2CC984722c` is the account address, and 333 is the account balance.

* The number of values that a mapping can store has no limit. And, we can change or add values to a mapping over time.

Explain that the token contract can now track user balances (that is, arcade customer balances).

The next step is to add a way for the arcade customers to access this information&mdash;so that they can check the number of arcade tokens that are available in their accounts.

#### Fetch an Account Balance

In this section, you’ll write the `balance` function of `ArcadeToken`. This function will use the `balances` mapping that you previously created.

The final code for this function appears as follows:

```solidity
function balance() public view returns(uint) {
    return balances[msg.sender];
}
```

* To allow arcade customers to check their account balances, we’ll write a function named `balance`.

* This function will use the mapping to fetch the balance that’s associated with a particular account address. We’ll make this function public so that the arcade customers can access it.

* With the `balances` mapping, we can access a user’s balance by passing it the user’s account address as a key, as the following code shows:

  ```solidity
  balances[msg.sender]
  ```

* Notice that instead of passing a numerical account address, we passed the `msg.sender` attribute as a key to the `balances` mapping.

* Remember that arcade customers can access this function because it’s public. And, `msg.sender` represents the account that’s currently sending a message. So in this case, `msg.sender` represents the account of whoever is using this function to check their balance.

With the `balances` mapping in place, code the function that uses it.

* The value that our `balance` function outputs is the `uint` account balance that the address of `msg.sender` maps to, as the following code shows:

  ```solidity
  function balance() public view returns(uint) {
      return balances[msg.sender];
  }
  ```

At this point, explain that mappings are flexible data types that allow us to efficiently link pieces of data together.

* To send a transaction to the Ethereum blockchain, we have to pay a gas fee. That is, we have to pay for the computational power that’s required to execute the transaction.

* A smart contract is a type of blockchain transaction. (And normally, it’s one that costs more gas than simply transferring ether!)

* Using a mapping generally requires less gas than using an array.

* For that reason, and because they provide a straightforward way to link user accounts with their token balances, mappings are one of the primary data types used to create token contracts.

Now that our arcade customers can check the number of tokens that they have at any time, it’s time to add some functionality. Specifically, we’ll add the ability to transfer arcade tokens between accounts.

#### Transfer a Balance

In this section, you’ll code the `transfer` function of `ArcadeToken`. This function will allow users to transfer tokens between accounts.

The final code for this function appears as follows:

  ```solidity
  function transfer(address recipient, uint value) public {
      balances[msg.sender] -= value;
      balances[recipient] += value;
  }
  ```

* Next, let's give our customers a way to transfer arcade tokens among themselves. To do so, we can add a new public function, named `transfer`, to our contract. This function will accept a `recipient` parameter and a `value` parameter, as the following code shows:

  ```solidity
  function transfer(address recipient, uint value) public {

  }
  ```

* This function will subtract `value` (that is, the number of tokens being transferred) from the token balance of the sender (that is, `msg.sender`), as the following code shows:

  ```solidity
  balances[msg.sender] -= value;
  ```

* Then, it will add the same value to the token balance of the recipient (that is, `recipient`), as the following code shows:

  ```solidity
  balances[recipient] += value;
  ```

* Essentially, the `transfer` function moves `value` from one address to another.

Explain that `ArcadeToken` is becoming more functional, well, by the function. The next step is to allow users to purchase tokens from the token smart contract.

#### Purchase Tokens

In this section, you’ll code the `purchase` function of `ArcadeToken`.

The final code for the `purchase` function appears as follows:

```solidity
function purchase() public payable {
    uint amount = msg.value * exchange_rate;
    balances[msg.sender] += amount;
    owner.transfer(msg.value);
}
```

* To add the functionality that allows users to purchase arcade tokens by using ether, we add a new `purchase` function to the smart contract and set it to `public payable`, as the following code shows:

  ```solidity
  function purchase() public payable {
  }
  ```

* Inside the new `purchase` function, we multiply `msg.value` (the amount of ether that the customer is spending) by `exchange_rate` (which we set earlier to 100 tokens per wei). This defines `amount` (the number of tokens) that the customer is purchasing, as the following code shows:

  ```solidity
  uint amount = msg.value * exchange_rate;
  ```

* Next, we add the number of tokens being purchased to the token balance of the `msg.sender`. (Remember that in this case, `msg.sender` is the customer who’s currently purchasing tokens.) We do so by adding the value of `amount` to the balance of `msg.sender` in the `balances` mapping, as the following code shows:

  ```solidity
  balances[msg.sender] += amount;
  ```

* Finally, we transfer the ether that the customer spent purchasing tokens to the arcade owner (which is us). We do so by calling `owner.transfer(msg.value)`, as the following code shows:

  ```solidity
  owner.transfer(msg.value);
  ```

* When an arcade customer sends ether to the `purchase` function, they receive tokens based on the exchange rate. And, the ether gets sent to the address of the `ArcadeToken` contract owner (which is us).

* Once customers have tokens, they can call the `transfer` function to send tokens back and forth among one another. They can also call this function to pay for arcade games.

Mention to the students that we have only one more element of this token smart contract left to code&mdash;minting the arcade tokens.

#### Mint Tokens

In this section, you’ll create the `mint` function of `ArcadeToken`.

The final code for the `mint` function appears as follows:

```solidity
function mint(address recipient, uint value) public {
    require(msg.sender == owner, "You do not have permission to mint tokens!");
    balances[recipient] += value;
}
```

* The last thing that the `ArcadeToken` smart contract needs is a way to **mint**, or create, tokens.

* To add this functionality, we add a new public `mint` function, as the following code shows:

  ```solidity
  function mint(address recipient, uint value) public {
      balances[recipient] += value;
  }
  ```

* Notice that this function accepts the same parameters as the `transfer` function: `recipient` and `value`. In this case, `value` represents the number of new tokens to mint. And, `recipient` can represent any blockchain participant.

* This way, we can add newly minted tokens to any customer’s balance as needed. That is, if a customer purchases tokens, we can have the contract mint those tokens and deposit them directly into the customer’s account.

* Next, we add a `require` statement to the `mint` function so that only the contract owner (that is, the arcade owner) can call it. If anyone else tries to call `mint`, the function will return an error message, as the following code shows:

  ```solidity
  require(msg.sender == owner, "You do not have permission to mint tokens!");
  ```

* After all, we want our customers to purchase tokens and not mint them for free!

At this point, the entire, completed `ArcadeToken` contract appears as follows:

```solidity
pragma solidity ^0.5.0;

contract ArcadeToken {
    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        balances[msg.sender] -= value;
        balances[recipient] += value;
    }

    function purchase() public payable {
        uint amount = msg.value * exchange_rate;
        balances[msg.sender] += amount;
        owner.transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        balances[recipient] += value;
    }
}
```

#### Deploy and Test the ArcadeToken Contract

Now that you’ve finished writing the `ArcadeToken` contract, take the students through the process of deploying and testing the contract in the Remix IDE.

Highlight how all the functions that you created in the application get displayed and accessed in the Remix IDE.

Once the contract is deployed, also make the connection between the input values of each function in the code and what appears as the input values that are associated with the functions in the Remix IDE.

Use two addresses in the Remix IDE to test both the transfer of tokens and the `require` function that’s associated with the `mint` function.

Call the `balance` function several times to show how the balances of the different accounts change as different contract functions get used.

Once the demonstration is complete, ask the students if they have any questions about the process of writing, deploying, or testing a smart contract.

Explain to the students that in the next activity, they'll apply all their new knowledge to create their own working `ArcadeToken` contract.

---

### 4. Student Do: Arcade Token (30 min)

**Corresponding activity:** [Arcade Token](Activities/02-Stu_Arcade_Token)

**Files:**

[Instructions](Activities/02-Stu_Arcade_Token/README.md)

[Starter file](Activities/02-Stu_Arcade_Token/Unsolved/ArcadeToken.sol)

Slack out the two preceding activity files to the students.

In this activity, the students will use the mapping data structure to build a token smart contract for use by an arcade&mdash;or for any other business that they’d like!

This contract will allow each student, as the business owner, to collect ether in exchange for tokens that users can spend at the business.

---

### 5. Instructor Do: Review Arcade Token (15 min)

**Corresponding activity:** [Arcade Token](Activities/02-Stu_Arcade_Token)

**Files:**

[Instructions](Activities/02-Stu_Arcade_Token/README.md)

[Starter file](Activities/02-Stu_Arcade_Token/Unsolved/ArcadeToken.sol)

[Solution file](Activities/02-Stu_Arcade_Token/Solved/ArcadeToken.sol)

Focus this activity review as much on the deployment and testing of the `ArcadeToken` smart contract as on the code that’s needed to create it.

Pay particular attention to the `msg` object attributes. Make sure that the students understand who the `msg.sender` is in each instance of the application testing.

As much as time allows, make the review as interactive as possible, asking the students to submit their code for the functions via Slack.

Be sure to leave enough time to demonstrate the integer underflow problem at the end of the review. This will act as the segue to the next section.

Start the review by opening the [starter file](Activities/02-Stu_Arcade_Token/Unsolved/ArcadeToken.sol) and writing the code for the Solidity version, as the following code shows:

```solidity
pragma solidity ^0.5.0;
```

Ask the students if anyone created a contract with a name other than `ArcadeToken`.

If a student volunteers another token name, ask them to slack their code for both the contract and the three variables (`owner`, `symbol`, and `exchange_rate`).

Confirm for the students that using a different contract name, symbol, and/or exchange rate won’t change the rest of the contract code.

Continue building the contract by defining the state variables, as the following code shows:

```solidity
contract ArcadeToken {
    address payable owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

}
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** What value will get assigned to the `owner` variable?

**Answer:** The `owner` variable will contain the address of the user who initially deploys the contract.

Next, code the mapping for the `balances`, as the following code shows:

```solidity
mapping(address => uint) balances;
```

* Stress that the mapping works like a Python dictionary, with key-value pairs. In this case, the key is the address, and the value is the number of tokens associated with that address.

Ask for a volunteer to slack their code for the `balance` function, which should appear as follows:

```solidity
function balance() public view returns(uint) {
    return balances[msg.sender];
}
```

**Question:** What value will get assigned to `msg.sender` when the function gets called in the Remix IDE?

**Answer:** The value that will get assigned to `msg.sender` is the address of the account of the user making the request.

Next, ask for a volunteer to slack their code for the `transfer` function, which should appear as follows:

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] -= value;
    balances[recipient] += value;
}
```

Next, ask for a volunteer to slack their code for the `purchase` function, which should appear as follows:

```solidity
function purchase() public payable {
    uint amount = msg.value * exchange_rate;
    balances[msg.sender] += amount;
    owner.transfer(msg.value);
}
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** What three steps take place inside the `purchase` function?

**Answer:**

1. The amount of tokens being purchased gets calculated by multiplying the amount of wei being sent times the exchange rate that was established when the contract was created.

2. The amount of tokens gets transferred to the address making the purchase request.

3. The amount of wei associated with the purchase gets transferred to the account address of the owner (that is, whoever deployed the contract).

Finally, ask for a volunteer to slack their code for the `min` function, which should appear as follows:

```solidity
function mint(address recipient, uint value) public {
    require(msg.sender == owner, "You do not have permission to mint tokens!");
    balances[recipient] += value;
}
```

**Question:** What role does the `require` function play in this function?

**Answer:** The `require` function ensures that only the owner (that is, whoever deployed the contract) can mint tokens.

Before deploying and testing the application in the Remix IDE, ask the students if they have any additional questions about the way that the code was written.

Deploy and test the contract for the students.

* As the contract owner, check the balance of tokens.

* As the contract owner, mint tokens.

* Transfer tokens to a second address.

* Check the balance of tokens for both the owner and the second address.

* As the second address, try to mint tokens. Point out the error in the Remix IDE.

* As the second address, purchase tokens, and display the token balance.

* Show how the ether balance of the owner account has changed since the purchase.

As you work through the testing process, ask the students if anyone noticed a flaw in the way that the code was written.

Depending on the answer, demonstrate the integer underflow problem, as the following animation shows:

![An animation depicts an integer underflow error.](Images/integer-underflow.gif)

Use this demonstration as a segue to the next section about securing contracts with Solidity libraries.

---

### 6. Instructor Do: Securing Contracts with Solidity Libraries (15 min)

**Corresponding activity:** [Securing Contracts](Activities/03-Ins_Securing_Contracts)

**Files:**

[Starter file](Activities/03-Ins_Securing_Contracts/Unsolved/ArcadeTokenSafeMath.sol)

[Solution file](Activities/03-Ins_Securing_Contracts/Solved/ArcadeTokenSafeMath.sol)

In this activity, you’ll explain how developers can use third-party libraries&mdash;specifically, the [OpenZeppelin SafeMath library](https://docs.openzeppelin.com/contracts/2.x/api/math)&mdash;to secure smart contracts.

Start by explaining that although smart contracts and the resulting tokens are relatively easy to create, we can use third-party libraries to make our smart contracts both more secure and more efficient to write.

#### Writing Secure Contracts with Solidity Libraries

In this section, you’ll demonstrate how to write secure smart contracts by using the external SafeMath library from OpenZeppelin.

Have a TA slack out the following pages to the students:

[OpenZeppelin Docs page for SafeMath](https://docs.openzeppelin.com/contracts/2.x/api/math)

[OpenZeppelin Contracts GitHub page for SafeMath](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol)

* OpenZeppelin is a company that specializes in developing secure smart contracts that use Ethereum community standards. They provide several libraries for smart contract development.

* The OpenZeppelin project includes many standardized smart contracts that the blockchain development community can adapt, customize, and build from. Developers can thus write more-secure and more-efficient Solidity code.

* As demonstrated, the arcade tokens that we created earlier in this lesson aren’t secure. The contract is vulnerable to rewarding an infinite number of tokens to a customer via an integer underflow error.

Further explain the concepts of integer overflows and underflows by using the following examples:

* Imagine that the odometer on a car has reached the maximum value that it supports. What happens after it reaches Mile 999,999? The odometer runs out of higher numbers and resets back to zero. That's an example of an **integer overflow**.

* An **integer underflow** is the opposite. For example, we know that the minimum possible value of a `uint` is zero. And, say that we try to subtract an amount from zero. The value will roll back to the maximum value that the `unit` can contain. In the case of `ArcadeToken`, say that an arcade customer has zero tokens and tries to spend tokens&mdash;that is, to subtract tokens from the zero balance. Instead of getting a negative `uint` balance, the customer gets a new balance that’s the highest number a `unit` can hold. That represents an enormous number of tokens!

The following animation shows the `ArcadeToken` contract demonstrating an integer underflow error in action:

![An animation depicts an integer underflow error.](Images/integer-underflow.gif)

If time allows, again demonstrate the integer underflow error by deploying your `ArcadeToken` contract in the Remix IDE. Encourage the students to duplicate the integer underflow error when they deploy their own `ArcadeToken` contracts.

Demonstrate the integer underflow error in the following way:

* The account owner begins with a balance of zero. Then, they try to transfer 1 token from their account to the recipient account. The `transfer` function subtracts that value of 1 from the current balance of zero. But, the function doesn’t return a new balance of &minus;1. Instead, an integer underflow error occurs. The function should thus return the following account balance, which you can point out to the students in the Remix IDE:

  ```text
  115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,935
  ```

Obviously, this is a problem!

Explain that by default, most programming languages behave this way. It's up to the developer to make sure that this doesn’t happen in their programs.

Introduce using the OpenZeppelin SafeMath library as a way to keep integer overflow and underflow errors from occuring.

* The SafeMath library provides the guardrails that we need to prevent integer underflows and overflows and similar vulnerabilities from occurring in our token smart contracts.

Note that [SafeMath.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol) is accessed from the [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) GitHub repository.

Import the SafeMath library directly into the `ArcadeToken` contract by inserting the link as the following code shows, and point out that the address being imported matches that of the SafeMath GitHub page:

```solidity
pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract ArcadeToken {
  // ...
}
```

* We access Solidity libraries in much the same way that we access Python libraries: by importing them. We can use the SafeMath library by importing the code directly into our smart contracts.

Navigate back to the [SafeMath GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol), and point out the list of functions that are now available to the students.

* By importing the GitHub page into the program, we gain access to all the functions that the page lists, including `add`, `sub`, and `mult`.

* Stress that the Remix IDE supports importing libraries directly from GitHub. So, we can just supply the URL of the `SafeMath.sol` library. Not all IDEs can import libraries in this way.

#### Using SafeMath

In this section, you’ll incorporate SafeMath library functions to secure the `ArcadeToken` contract. You'll replace existing code with SafeMath functions.

Start by adding `using SafeMath for unit` to the smart contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract ArcadeToken {
    using SafeMath for uint;

    // ...
}
```

* Now that we've imported SafeMath, we can use it to build a more secure version of our `ArcadeToken` contract.

* On the first line of the contract, we add `using SafeMath for uint;` to link the SafeMath library to the `uint` data type.

* This adds special functions to any object that uses the `uint` type. These functions include `.add`, `.sub`, `.mul`, and `.div`, which we can use instead of the plus (`+`), minus (`-`), times (`*`), and divided by (`/`) operators.

* Unlike the operators that we used previously, these SafeMath functions don’t allow integer underflows or overflows to occur.

Next, you’ll modify the `transfer` function to incorporate the `sub` and `add` functions from SafeMath.

The following code replaces the minus (`-`) and plus (`+`) operators with `.sub` and `.add`:

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] = balances[msg.sender].sub(value);
    balances[recipient] = balances[recipient].add(value);
}
```

* Now, we can modify the `transfer` function so that it uses the SafeMath assignments instead of the standard minus (`-`) and plus (`+`) operators. Notice that we can now call `.sub` and `.add` on the `uint` values that the `balances` mapping returns.

Once you’ve made the update to the `transfer` function, recompile and deploy the `ArcadeToken` contract. Try to transfer 1 token from an address that doesn’t hold any tokens. That should generate an error message in the Remix IDE, as the following result shows:

```shell
transact to ArcadeToken.transfer pending ...
transact to ArcadeToken.transfer errored: Error: [ethjs-rpc] rpc error with payload {"id":559065790857,"jsonrpc":"2.0","params":["0xf8ab1a843b9aca00832dc6c094aa6b6a74aec9a4d05484c9841dd911b35838bb4180b844a9059cbb000000000000000000000000a29f7e79ecea4ce30dd78cfeb9605d9aff5143a50000000000000000000000000000000000000000000000000000000000000001822d45a0dc029786c5cb8efb0c75ed6d6c86db6f75e5e51af57e584f0df168e6d4fffbf0a069cabf26a54d320aaea8d68d98d02d296fbf80335200c6434b021f9324058ef7"],"method":"eth_sendRawTransaction"} [object Object]
```

* By using SafeMath to perform math operations, we prevent integer underflows! We can retry the same transaction that the earlier animation showed (that is, transferring 1 token from an account with a zero balance) with this new code.

* Notice that instead of processing the transaction, the function returns an error message that the Remix IDE displays.

* Voila! We’ve secured our contract against integer underflows and overflows. Keep in mind that based on our current code, this will work only for `uint` types. But, we could also declare it for the `int` type if we wanted to.

* The next step is to replace every instance of an operator like plus (`+`), minus (`-`), times (`*`), and divided by (`/`) with its SafeMath alternative. In fact, it’s a good practice to use the SafeMath library by default. The majority of smart contract developers do so, because this library has prevented many tokens from becoming compromised.

Ask the students if they have any questions about incorporating the SafeMath library into the `ArcadeToken` contract.

Depending on the time, you can release the students for a break now, confirming that you’ll update the remainder of the `ArcadeToken` contract together upon their return. Or, you can proceed with the next activity and give them a break after it’s completed.

---

### 7. Break (15 min)

---

### 8. Everyone Do: SafeMath (15 min)

**Corresponding activity:** [SafeMath](Activities/04-Evr_SafeMath)

**Files:**

[Instructions](Activities/04-Evr_SafeMath/README.md)

[Starter file](Activities/04-Evr_SafeMath/Unsolved/ArcadeTokenSafeMath.sol)

[Solution file](Activities/04-Evr_SafeMath/Solved/ArcadeTokenSafeMath.sol)

Welcome everyone back from the break.

Explain that for this next activity, you’ll work together to incorporate the SafeMath functions into all the functionality of the `ArcadeToken` contract that involve mathematical computations.

Slack the starter file out to the students so that they can code along with the activity.

Encourage the students to provide as much of the code that’s related to this activity as possible.

Start the activity with everyone navigating to the Remix IDE and then creating a new file named `ArcadeTokenSafeMath.sol`.

Have everyone copy the contents of the starter file into the new file. Alternatively, they can use the code from their earlier Arcade Token activity.

Next, ask if everyone can access the link to the SafeMath GitHub page that you slacked out earlier in the lesson.

Have a TA resend the link for those students that can’t access it.

Instruct each student to copy that link and and then paste it into the beginning of their `ArcadeTokenSafeMath.sol` file, as the following code shows:

```solidity
import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** What role will this `import` statement play in the `ArcadeToken` contract?

**Answer:** This link will give the contract access to all the functions that the SafeMath GitHub page includes. With these functions, we’ll be able to secure the `ArcadeToken` contract from errors like the integer overflow and the integer underflow.

Next, incorporate the code that makes the SafeMath library available to all variables of type `uint`, as the following code shows:

```solidity
using SafeMath for uint;
```

**Question:** What role does this statement play in the `ArcadeToken` smart contract?

**Answer:** This statement will link the SafeMath library to the `uint` type. We’ll then be able to call functions like `.add`, `.sub`, `.mul`, and `.div` directly from a `uint` rather than using operators like plus (`+`), minus (`-`), times (`*`), and divided by (`/`).

The next steps involve replacing every math operation in the contract with its SafeMath equivalent.

For example, the following code:

```solidity
balances[msg.sender] -= value;
```

becomes the following code:

```solidity
balances[msg.sender] = balances[msg.sender].sub(value);
```

Ask for volunteers to provide the updated statements for the `transfer` function. If you don’t have volunteers, supply the following code for the initial `transfer` function:

```solidity
function transfer(address recipient, uint value) public {
    // using .sub and .add prevents integer underflow
    balances[msg.sender] = balances[msg.sender].sub(value);
    balances[recipient] = balances[recipient].add(value);
}
```

Encourage the students to provide the code for the remaining statements, because the updates are all similar.

* Each statement must include variable reassignments, because SafeMath doesn’t change the variable that it operates on. For the function to work properly, each variable must be reassigned with an equal sign (`=`). An example is `balances[recipient] = balances[recipient].add(value);`.

Ask for a volunteer to provide the updated statement for the `purchase` function, as the following code shows:

```solidity
function purchase() public payable {
    uint amount = msg.value.mul(exchange_rate);
    balances[msg.sender] = balances[msg.sender].add(amount);
    owner.transfer(msg.value);
}
```

Ask for a volunteer to provide the updated statement for the `mint` function, as the following code shows:

```solidity
function mint(address recipient, uint value) public {
    require(msg.sender == owner, "You do not have permission to mint tokens!");
    balances[recipient] = balances[recipient].add(value);
}
```

Once all the statements have been updated, have everyone deploy and test the contracts. Everyone should try to duplicate the integer underflow error, checking for the resulting message in the console.

The `ArcadeToken` contract should now be safe from any integer underflows and overflows!

Ask the students if they have any questions about the OpenZeppelin SafeMath library and how it works to secure the `ArcadeToken` smart contract from possible mathematical problems like the integer underflow error.

---

### 9. Student Do: Creating an XP-Token (30 min)

**Corresponding activity:** [XP-Token](Activities/05-Stu_XP_Token)

**Files:**

[Instructions](Activities/05-Stu_XP_Token/README.md)

[Starter file](Activities/05-Stu_XP_Token/Unsolved/XP_Token.sol)

Slack out the preceding two files to the students so that they can complete the XP-Token activity

In this activity, the students will use their knowledge of Solidity to build an `XP_Token` smart contract.

In addition to creating the smart contract, they’ll use the OpenZeppelin SafeMath library to secure the contract from integer underflow errors.

The `XP_Token` contract will allow students to collect ether in exchange for XP tokens, which they will create in this activity, that users can then spend at a company website that accepts only XP-tokens.

---

### 10. Instructor Do: Review Creating an XP-Token (10 min)

**Corresponding activity:** [XP-Token](Activities/05-Stu_XP_Token)

**Files:**

[Instructions](Activities/05-Stu_XP_Token/README.md)

[Starter file](Activities/05-Stu_XP_Token/Unsolved/XP_Token.sol)

[Solution file](Activities/05-Stu_XP_Token/Solved/XP_Token.sol)

This activity reviews all the material that the class covered today. It involves both creating an `XP-Token` smart contract and incorporating the OpenZeppelin SafeMath library into it.

The code for this activity almost matches that of the `ArcadeToken` contract.

Start by importing the SafeMath library directly from GitHub at the beginning of the file, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract XP_Token {

}
```

Reiterate to the students that only the Remix IDE supports importing libraries directly from GitHub. Other IDEs require a different method of importing the `SafeMath.sol` library, such as copying the code from the file that’s hosted on GitHub into the new contract file before creating your contract..

Next, work through the content of the `XP_Token` smart contract.

Start with the following statement:

```solidity
using SafeMath for uint;
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** What role does the preceding line of code play for the smart contract?

**Answer:** The statement links the SafeMath library to the `uint` data type. We can then call functions like `.add` and `.sub`on any `uint` that the smart contract references. By replacing all the math operations with their SafeMath alternatives, we prevent potential underflow errors that might give customers an infinite amount of tokens.

Next, copy and paste the following code for the three contract variables for the students:

```solidity
address payable owner = msg.sender;
string public symbol = "XPT";
uint public exchange_rate = 100;
```

Pose the following questions to the students. If no one volunteers a response, provide them with the answer.

**Question:** How does the role of the contract owner get assigned?

**Answer:** The role of the contract owner gets assigned to the address of whoever initially deploys the contract.

**Question:** Given what we know about the `XP_Token` contract, what’s unique about the owner role? And, how does the contract specify the properties of the owner role?

**Answer:** The contract owner is the only user who can mint tokens. The `require` statement in the `mint` function specifies this.

Follow this with the code for the `mapping` data structure:

```solidity
mapping(address => uint) balances;
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** What Python data structure does the Solidity mapping data structure correspond to, and why?

**Answer:** The mapping data structure corresponds to the Python dictionary. This is because it uses key-value pairs. In the case of the `XP_Token` contract, the key is the address, and the value is the `uint` balance of tokens for that address.

Finally, work through each function (`balance`, `transfer`, `purchase` and `mint`) with the students, ensuring that they incorporate the SafeMath library where appropriate, as the following code shows:

```solidity
function balance() public view returns(uint) {
    return balances[msg.sender];
}

function transfer(address recipient, uint value) public {
    balances[msg.sender] = balances[msg.sender].sub(value);
    balances[recipient] = balances[recipient].add(value);
}

function purchase() public payable {
    uint amount = msg.value.mul(exchange_rate);
    balances[msg.sender] = balances[msg.sender].add(amount);
    owner.transfer(msg.value);
}

function mint(address recipient, uint value) public {
    require(msg.sender == owner, "You do not have permission to mint tokens!");
    balances[recipient] = balances[recipient].add(value);
}
```

Once the code is complete, deploy and test the contract in the Remix IDE. Be sure to confirm that no integer underflow error occurs by reviewing the account balance of the deployed contract in the IDE.

Ask for any remaining questions about how SafeMath works to secure smart contracts before moving on.

---

### 11. Instructor Do: Inheritance and Composition (15 min)

Point out to the students that writing smart contracts (like many programming activities) heavily relies on the object-oriented programming (OOP)  principles of inheritance and composition.

To familiarize the students with this programming paradigm (that is, OOP), you’ll introduce these concepts at a high level in this activity.

Rather than getting lost in the (potentially vast) details of OOP, focus on two core targets that we want to achieve by using these principles:

* **The ability to easily scale or reuse code:** Once we or others have designed robust and efficient code, we want to use it for other use cases without having to modify the code.

* **The reduction of the potential for bugs:** Being able to reuse well-tested code allows us to become more efficient and reduce the chance for bugs in our code.

Go over the following two principles as they pertain to the approach that the upcoming lessons use (although we’ll use only inheritance, it will be helpful to contrast inheritance with composition):

**Inheritance:**

* In OOP, we use inheritance when a particular type of relationship exists between classes. Specifically, this happens when one class is a specialized version of the other, more-general class. Here are some examples:

  * Start with a vehicle. A vehicle has an engine, the ability to carry passengers, and a color.

  * A truck is a vehicle. Because it’s a vehicle, it inherits having an engine, the ability to carry passengers, and a color. But, it also has unique characteristics. Specifically, the engine is a diesel one, the truck can carry two passengers, the color is blue, and the truck has a flatbed.

  * A car is also a vehicle. Because it’s a vehicle, it inherits having an engine, the ability to carry passengers, and a color. But, it also has unique characteristics. Specifically, the engine is a six-cylinder one, the car can carry four passengers, the color is red, and the car has a trunk.

  * Another example involves a CPU. A CPU has a collection of circuits that run the instructions from a program.

  * The Intel Core i9 is a CPU. Because it’s a CPU, it inherits having circuits. But, these circuits are specialized ones that can work with the iOS operating system.

  * The AMD Ryzen 9 is also a CPU. Because it’s a CPU, it inherits having circuits. But these circuits are specialized ones that can work with the Windows operating system.

* In each case, the **subclass** is a specialized version of the **superclass**. In our case, our `XP_Token` might be a specialized version of a general type of reward token that a parent corporation issues.

* With inheritance, **is a** is the key phrase. A truck **is a** vehicle. The Intel Core i9 **is a** processor.

**Composition**:

* In OOP, we use composition for cases where a class or object has elements of another class or object. Here’s an example:

  * A computer has a processor but also a graphics card, a hard drive, and a cooling element.

* As the name suggests, composition emphasizes the composition of a class or object based on elements of other types. By contrast, inheritance emphasizes being of a certain type. Composition contains elements of other classes that provide the desired functionality.

* With composition, **has a** is the key phrase. A computer **has a** processor. Contrast this with inheritance, where the key phrase is **is a**.

Which one is the better approach?

* As always, the answer is that it depends on the use case.

* Both approaches have their strengths and work better or worse for certain use cases. Inheritance makes sense when a large overlap (like 80%) exists between two classes&mdash;and one class is a specialized case of the more-general class. By contrast, composition is more flexible. With composition, we can choose the components that we want to use to construct a new class.

For the upcoming lessons, we’ll use inheritance to design our tokens. This is generally true for most implementations of tokens within smart contracts.

Explain that the tokens we’ll design in an upcoming class will inherit characteristics from tokens that Ethereum standards define and that OpenZeppelin makes available.

* Open the [OpenZeppelin ERC-20 docs](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20). Point out some of the familiar contract variables (`name` and `symbol`) and functions (`balance` and `transfer`).

* Explain that the tokens we’ll build next will inherit the smart contract features and functionality that the ERC-20 specifications lay out. We’ll thus be able to build robust and more secure smart contracts in less time.

Finally, wrap up the class with a few basic review questions to the class:

* **Question:** What’s the solution that we used to fix our underflow and overflow issues?

* **Answer:** The OpenZeppelin SafeMath library.

* **Question:** Who is ultimately responsible for the cybersecurity of an organization?

* **Answer:** Everyone is responsible for carrying the burden of security.

* **Question:** Why not just offload this stuff to the security team?

* **Answer:** The security team is already overwhelmed with other things to patch and is constantly fighting a uphill battle.

* **Answer:** Every bit of effort towards security helps.

* **Answer:** We can't be lazy when developing and leave security as an afterthought. That's how the technology industry became so vulnerable in the first place!

Clarify any outstanding questions that the students might have about the Remix IDE, Solidity, tokenomics, OpenZeppelin, and SafeMath.

Reassure the students that their exploration of the cutting-edge technology underlying tokenomics is only just beginning. More fun lies ahead over the next several lessons!

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

