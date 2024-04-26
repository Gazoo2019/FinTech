## 20.2 Lesson Plan: Interacting with Smart Contracts

### Overview

Today's class will introduce practical uses of the Solidity programming language for the Ethereum blockchain. Students will learn about decision making, managing ether, the `require` function, trading, and enforcing terms of a smart contract.

The goal of this lesson is for students to understand how to manipulate smart contracts by using Solidity, so that they can build smart contracts on their own terms. 

### Class Objectives

By the end of this lesson, students will be able to:

* Define the `payable` function's role in smart contracts.

* Develop the syntax in Solidity to withdraw and deposit ether.

* Explain the purpose of using the keyword `public` in smart contracts.

* Use the `this` keyword in smart contracts.

* Create a public `getter` function to manipulate trades by sending different denominations of coins.

* Write conditional statements in Solidity.

* Use conditional statements in Solidity in order to obtain the desired results in your smart contract.

* Demonstrate how the `require` function works in Solidity smart contracts.

* Develop a smart contract using the `require` function to enforce smart contract terms.

### Instructor Notes

* This unit marks the first time that students will encounter a strictly typed programming language. This may be a difficult adjustment for the students, as they will have to remember to specify data types everywhere, as well as use semicolons to end expressions.

* If the students get frustrated, remind them that they are learning something that few are skilled at. By learning a strictly typed language now, they’ll more easily learn any programming language in the future.

* Make sure your Remix compiler version is set to match your pragma. Otherwise, unexpected errors may occur.  The pragma and compiler versions should match, as observed in the following image:

  ![pragma_compiler_match](Images/pragma_compiler_match.png)

* **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

* One of the most common errors is the `Gas estimation failure` error. It can be frustrating to encounter, as it serves as a kind of "catch-all" error, delivering a vague message that offers little guidance on what actually caused it. In these instances, check the [Troubleshooting Gas Estimation Errors](../Supplemental/StudentGuide.md#troubleshooting-gas-estimation-errors) section of the [Student Guide](../Supplemental/StudentGuide.md) for helpful tips.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 20.2 slides](https://docs.google.com/presentation/d/1RwkHHvONvfAK5G9Hk2wLdzOr2xl1FoCBgM_PCLcyrsA/edit#slide=id.gf1cfbdfd60_0_0).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this section, you’ll provide a brief refresher of what students learned in the previous lesson. Then, you’ll introduce the concept of smart contract fulfillment and explain the role of the `payable` keyword in smart contracts.

Give a brief recap of the previous lesson and connect what they learned to today’s class:

* In the previous lesson, we defined the basic structure of a smart contract, and wrote a function as well as variables for storing data.

* In this lesson, we’ll create functions that add functionality to a smart contract.

* Remind the class that in previous units they wrote Python functions.

Explain that in Solidity, a developer can add custom business rules to a smart contract. These rules verify whether a person is authorized to make a transaction.

Give an example of how business rules defined in a smart contract can be useful in the real world.

* Let’s say that you’re a famous crypto trader who wants to publish your latest buy order, including the price that you paid. A **buy order** refers to the action of buying a certain amount of financial assets. In this case, we’re referring to buying cryptocurrencies.

* In order to prove that you made a cryptocurrency purchase at the execution price, you want to build a smart contract that publishes your latest trade to the blockchain. The **execution price** is the price at which the trade was executed.

* In order to enable a smart contract to interact with the blockchain or even with other smart contracts, we need to define a function that captures the business rules that we want to implement.

* As we did in Python, we can define functions in Solidity&mdash;but with some nuances.

The next few talking points explain the `payable` function in Solidity. Refer to the slides if needed and answer questions for students.

* In order to trade, we must be able to send and receive currency. The currency we’re using is ether. In order for our functions to receive ether, they must be attached to a modifier called `payable`. `payable` is a reserved keyword in Solidity.

* `payable` is a mandatory keyword for trading because, without it, the function will be rejected, and no ether will be sent.

* Usually, there is a `no name` function that accepts ether that is to be sent to a contract. This is called a fallback function, which we’ll explain in more detail in the next section.

  ```Solidity
  function () payable {}
  ```

* An exception is when you have more than one `payable` function that is used to perform different tasks, such as registering a deposit to your contract:

  ```Solidity
  function deposit() payable {
    deposits[msg.sender] += msg.value;
  };
  ```

Answer any questions before moving on to the next section.

---

### 2. Instructor Do: Making Transactions in the Ethereum Blockchain (20 min)

**Corresponding Activity:** [Making Transactions in the Ethereum Blockchain](Activities/01-Ins-Transactions_on_Ethereum_Blockchain)

In this section, review how to make transactions on the Ethereum blockchain by using Solidity and smart contracts. Live code brief examples and explain core concepts. Focus on withdrawing ether, collecting ether without a `deposit` function, depositing ether to a smart contract, and paying gas on contracts.

**File:** [Making Transactions in the Ethereum Blockchain](Activities/01-Ins-Transactions_on_Ethereum_Blockchain/Solved/transactions.sol)

Before diving into the concepts, remind the class of the bigger picture:

* Blockchain is a technology that records and shares data. By using functions, as we did in the previous section, you now know how to store data in a contract. One application of this in the fintech realm is keeping track of asset transactions.

* In this section, you’ll learn how to add special functions to smart contracts that will allow us to deposit or withdraw ether.

Remind the students that ether is the native cryptocurrency of the Ethereum network and one of the largest cryptocurrencies by market capitalization.

Continue with the following talking points:

* Besides depositing and withdrawing ether, we’ll also build functions that allow us to catch ether that’s sent from outside a function call. These functions make up the core building blocks for managing digital assets in smart contracts.

* Sending currency is an important part of a blockchain developer's role. It allows them to be an asset when dealing with transactions and building applications on the Ethereum blockchain.

#### Withdraw Ether from a Smart Contract

In this section, you’ll demonstrate how to withdraw ether from a smart contract. 

Open the Remix IDE and begin to code.

To introduce the withdraw function, create a new smart contract that represents a bank account balance. Start with the main contract structure, as the following code shows:

```solidity
pragma solidity ^0.5.0;

contract BankAccount {
}
```

* Like we did previously, we specify the version of the Solidity compiler that we want to use by setting the `pragma`. We then define the contract and name it `BankAccount`.

* The first step to making ether transactions is to add a `withdraw` function to the contract, as the following code shows:

  ```solidity
  pragma solidity ^0.5.0;

  contract BankAccount {
      function withdraw(uint amount, address payable recipient) public {
          return recipient.transfer(amount);
      }
   }
  ```

* The `withdraw` function allows us to take ether from a smart contract. This function accepts the following arguments:

* A `uint` argument representing the amount of ether, in its smaller denomination named wei, that we want to withdraw. We name it `amount`.

* An `address` argument representing the Ethereum address that we want to send the funds being withdrawn to. We name it `recipient`.

Tell the students to pay special attention to the new modifier, named `payable`, that we use for the `address` argument.

* By setting an address or function as `payable`, we unlock special functions that allow us to collect and manage ether.

Explain both of Solidity's address types:

* The `address` type can store a 20-byte value, which is the size of an Ethereum address.

* The `address payable` type is the same as `address` but includes functions, like `send` and `transfer`, that allow us to perform operations with ether.

Slack out the [Solidity documentation](https://docs.soliditylang.org/en/v0.5.0/types.html#address) and encourage students to review it.

#### Deposit Ether to a Smart Contract

In this section, you’ll demonstrate how to deposit ether to a smart contract.

Begin by explaining that each time you deploy a smart contract, a public Ethereum address is assigned to it.

* So, a smart contract can store and send ether like a cryptocurrency wallet with its Ethereum account address.

* It’s up to developers to create functions that manage this address, just like we did with the `withdraw` function.

Tell the class that you will create a function that adds ether to our smart contract.

Name this function `deposit`, and set it as `public` so that users and contracts can access it. Also, add the `payable` modifier so that the contract can accept ether that gets sent to this function. The following code shows our `deposit` function:

```solidity
pragma solidity ^0.5.0;

contract BankAccount {
    function withdraw(uint amount, address payable recipient) public {
        return recipient.transfer(amount);
    }

    function deposit() public payable {}
 }
```

Point out that the body of the `deposit` function is empty. This is because we create this function only to accept and hold the ether that we send to the contract, and this is done by adding the `payable` modifier.

#### Collect Ether Without a Deposit Function

In this section, you’ll demonstrate how to collect ether without a `deposit` function.

Tell the class that this is the final function that will be added to the end of our contract’s code. Then, cover the following points:

* The purpose of the function is to make sure that ether gets sent to the contract without using the `deposit` function (that is, by sending ether directly to the contract's address).

* The contract still collects the ether in the contract wallet. It’s important not to lose even one wei.

* The following code shows the addition of this final function:

  ```solidity
  pragma solidity ^0.5.0;

  contract CustomerSavings {

  function withdraw(uint amount, address payable recipient) public {
    return recipient.transfer(amount);
  }

  function deposit() public payable {}

  function() external payable {}
  }
  ```

Keep the code on display for students. Before moving on, review the following talking points to ensure students understand the code.

* The function without a name is known as a **fallback function**.

* A fallback function is used in two scenarios: (1) if the function identifier doesn't match any other function in the contract, or (2) if the sending function doesn't supply any data, so we have to add the `external` keyword so that other contracts or transactions can call this contract. We also add  the `payable` keyword so that the contract can collect any amount of ether that gets sent to it via the contract address.

Explain the purpose of the fallback functions: If we don't add the fallback function, and ether gets sent to our contract address, the ether will be returned. This forces other users to send ether via the `deposit` function.

Establish that the contract is now complete, which means that anyone can add ether via the contract address or the `deposit` function. Anyone can also send any amount of ether to any address that we specify to the `withdraw` function, as long as we have enough in our balance.

#### Paying Gas to Run Your Contracts

In this section, define the concept of gas and explain how gas is related to smart contracts.

* Moving ether in the Ethereum blockchain implies a cost that’s known as gas.

* **Gas** is a kind of fee that a user pays for each instruction that the Ethereum Virtual Machine (EVM) runs.

Compare Bitcoin transaction fees to Ethereum's by identifying a few key differences:

* Instead of a plain transaction fee, like Bitcoin has, Ethereum blockchain users pay fees that are based on running different computations. Each computation has a different gas cost.

* Each time that you run a function within a smart contract, you have to pay a gas fee to run that function in the blockchain.

* The blockchain miners determine the precise gas fee. In fact, they occasionally update the gas fee when certain code executions become too expensive for average nodes to process. This is to keep the blockchain network fair.

* Gas is essential to the Ethereum network. It’s the energy that it needs to work&mdash;in the same way that a bulb needs electricity to light up.

Slack out [Ethereum’s documentation on gas and fees](https://ethereum.org/en/developers/docs/gas/). This is a good resource for students to learn more about how gas costs operate.

Pose the following question to the class:

* **Question:** As you know, moving ether around in the blockchain implies a cost. What if we don't have enough gas to complete a transaction? Do we lose the gas that we were charged?

  * **Answer:** We do lose the gas that we were charged. But, the transaction will be reversed, and we’ll get our ether back. This is like turning on the engine of a car and staying parked. The engine already consumed some gasoline, even though we didn’t go anywhere (and even if we have an electric car). We used some gasoline to start the car&mdash;just like we used some gas to start an ether transaction!

---

### 3. Everyone Do: Implement Ether Management Functions (15 min)

**Corresponding Activity:** [Implement Ether Management Functions files](Activities/02-Evr_Implement_Ether_Management_Functions)

In this section, you will demonstrate how to add functions to a smart contract that deposit and withdraw ether while students follow along. Be sure to tell students that they should code as you demonstrate.

Explain that, after creating a smart contract that stores customer information, the next step is to create a remittances application.

* This will allow people to both deposit ether into the contract and withdraw funds to send to friends and family members that have an Ethereum address.

The first step is to add new functions to the `CustomerAccount` contract.

**File:** [Implement Ether Management Functions files](Activities/02-Evr_Implement_Ether_Management_Functions/Solved/customer_account.sol)

Use `customer_account.sol` in the `Unsolved` folder to write your code, using the `Remix` IDE. As you live code, be sure to explain each step and leave time for feedback and questions.

Change the scope of the `accountBalance` variable to `public` to allow other users or contracts to access it. Making this variable public will allow you and others to check the balance of ether in the contract when depositing or withdrawing ether.

```solidity
pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner;
    bool isNewAccount;
    uint public accountBalance;
    string customerName;
    string customerLastName;

    function getInfo() view public returns(address, bool, uint, string memory, string memory) {
        return (owner, isNewAccount, accountBalance, customerName, customerLastName);
    }
}
```

Inside the body of the contract, create a new function named `sendRemittance`. Make this a withdrawing function that takes ether from the current contract balance. This function should accept a `uint` argument named `amount` and an `address payable` argument named `recipient`.

Inside the `sendRemittance` function, call the `transfer` method on the passed `recipient` argument, and specify the `amount` to transfer. Then, declare an  `accountBalance` variable and set it equal to the balance of the contract. The body of the `sendRemittance` function should resemble the following:

```solidity
    function sendRemittance(uint amount, address payable recipient) public {
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }
```

Point out the `this` keyword in the preceding code. It refers to the smart contract itself. The `this` keyword helps you distinguish a contract's own balance from any other balance.

Next, implement a `public payable` function named `deposit` within the body of the contract. Inside this function, declare an `accountBalance` variable and set it equal to the balance of the contract as follows:

```solidity
      function deposit() public payable {
        accountBalance = address(this).balance;
    }
```

* By declaring the `accountBalance` variable and setting it equal to the contract's balance inside both the `sendRemittance` and `deposit` functions, it can update the contract’s ether balance with each deposit or withdrawal.

Finally, insert the basic fallback function so that the contract can store ether that’s sent from outside the `deposit` function.

```solidity
    function() external payable {}
```

Compile the smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

---

### 4. Student Do: Trading and Savings Contracts (30 min)

**Corresponding Activity:** [Trading and Savings Contracts](Activities/03-Stu_Trading_And_Savings)

In this activity, students will practice writing functions in order to create more enhanced smart contracts in Solidity. Students will create two contracts: one for trading, and another to define a savings account.

**Files:**

* [latest_trade.sol](Activities/03-Stu_Trading_And_Savings/Unsolved/latest_trade.sol)

* [person_savings.sol](Activities/03-Stu_Trading_And_Savings/Unsolved/personal_savings.sol)

**Instructions:** [README.md](Activities/03-Stu_Trading_And_Savings/README.md)

---

### 5. Instructor Do: Review Trading and Savings Contracts (10 min)

**Corresponding Activity:** [Trading and Savings Contracts](Activities/03-Stu_Trading_And_Savings)

In this section, you will review the two contracts that students created independently in the previous activity.  

**Files:**

* [latest_trade.sol](Activities/03-Stu_Trading_And_Savings/Solved/latest_trade.sol)

* [person_savings.sol](Activities/03-Stu_Trading_And_Savings/Solved/personal_savings.sol)

First, take a moment to check in with the class and find out how comfortable they are creating smart contracts by using Solidity and the `Remix` IDE.

Then, begin to review the steps of the activity.

Use the `latest_trade.sol` file to create a contract named `LatestTrade` that contains:

* A string variable `coin` with the value `XRP` assigned to it.

* An unsigned integer variable `price`.

* A boolean variable `is_buy_order`.

```solidity
pragma solidity ^0.5.0;
contract LatestTrade {

  string coin = "XRP";
  uint price;
  bool is_buy_order;

}
```

Next, add a function named `updateTrade` to the `LatestTrade` contract and highlight the following:

* We define an in-memory string variable `new_coin` as the first parameter.

* Next, we define an unsigned integer variable `new_price` as the second parameter.

* Then, we define a boolean variable `is_buy` as the third parameter.

* Into the body of the function, we set the contract variables `coin`, `price`, and `is_buy_order` to the inputs of the `updateTrade` function. This function will update the contract variables via the `updateTrade` function.

```solidity
  function updateTrade(string memory new_coin, uint new_price, bool is_buy) public {
    coin = new_coin;
    price = new_price;
    is_buy_order = is_buy;
    }
```

Explain that in Step 3 in the activity, a public `getter` function should be added that’s called `getTrade`. 

* The `getTrade` function should return the `coin`, `price`, and `is_buy_order` variables of the `LatestTrade` contract.

The completed contract can be seen below:

```solidity

contract LatestTrade {

  string coin = "XRP";
  uint price;
  bool is_buy_order;


  function updateTrade(string memory new_coin, uint new_price, bool is_buy) public {
    coin = new_coin;
    price = new_price;
    is_buy_order = is_buy;
  }

  function getTrade() public returns (string memory, uint, bool) {
    return (coin, price, is_buy_order);
  }

}

```

Now navigate over to the `personal_savings.sol` file.

* As before the verison of pragma is 5 and the word contract is needed to declare the contract.

  ```solidity
  pragma solidity ^0.5.0;
  contract PersonalSavings {
  ```
* Next we define two address varlaibles as `payable` and a name for the account holder.
    
    ```solidity
    address payable public public_savings = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
    address payable private_savings = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
    string account_holder = "Jane Doe";
    ```

* Finally we create a withaw function passing in the amount and a `payable` address who is the reciepent.

* This function should return a transfer to the `recipient` the value of this transfer should be the amount.

    function withdraw(uint amount, address payable recipient) public {
      return recipient.transfer(amount);
    }

* Then create a simple deposit function and a fallback function. Both of which should be `payable`.

  ```solidity
    function deposit() public payable {
    }

    function() external payable {
    }
  }
  ```
  
Ask the class to rate their level of understanding by raising their hand for a "Fist-to-Five" check. A closed fist (0) means they are lost and need much more help. An open hand (5) means they could create and compile the contact successfully and feel confident and ready to go.

Answer any questions before sending students on break.

---

### 6. Break (15 min)

---

### 7. Instructor Do: Decision Making in Smart Contracts (10 min)

**Corresponding Activity:** [Decision Making in Smart Contracts](Activities/04-Ins_Solidity_Decision_Making)

In this section, you will explain conditionals in Solidity while coding examples.

Welcome students back from break. Then, open the Remix IDE to begin the coding demonstration.

**File:** [Decision Making in Smart Contracts](Activities/04-Ins_Solidity_Decision_Making/Solved/solidity_decision_making.sol)

First, get students thinking about how decision making affects their lives. Examples include deciding whether to adopt a dog, or whether to buy or sell stocks.

* We can implement this mental decision-making process in most programming languages by using conditionals&mdash;as we learned when using Python earlier.

* Solidity provides a set of statements to implement conditionals. These statements can be used to define the terms of a smart contract.

* For example, we can restrict the ability to withdraw ether from a smart contract, depending on the requested amount and the current balance. In this section, we’ll learn more about the conditional statements that we can use to add decisions to a smart contract.

Next, explain **`if` statements** and code an example.

* In Python, the `if` statement can be used to implement decision-making in smart contracts. The operating logic is the same in Solidity. However, the syntax slightly differs, as the following code shows:

  ```solidity
  if (a < 10) {
      a = a + 1;
  }
  ```

* In this code, notice that we place the condition for the `if` statement inside a set of parentheses. We also use braces ( {} ) to enclose the code block that should run as part of the conditional statement.

Next, explain **`else` statements** and code an example.

* Solidity also provides an `else` statement for when the condition of the `if` statement is false. It works like the same statement in Python. Adding braces is needed to enclose the code block for the `else` portion of the entire `if-else` conditional statement, as the following code shows:

  ```solidity
  if (a < 10) {
      a = a + 1;
  }
  else {
      a = a - 1;
  }
  ```

Next, explain **stacked conditionals** and code an example.

* In Solidity, conditionals can be “stacked,” or chained together. However, there is no equivalent of the Python `elif` statement. Instead, we need to define a new `if` statement as part of the `else` code block. The following code shows a simple contract with a stacked `if` structure:

  ```solidity
  pragma solidity ^0.5.0;

  contract IfElse {
      uint y;

      function exampleIfElse(uint x) public {
          if (x < 10) {
              y = 0;
          }
          else if (x < 20) {
              y = 1;
          }
          else {
              y = 2;
          }
      }
  }
  ```

* Note that the relational operators that the conditions use match the ones in Python. In fact, in Solidity, we use the same syntax for six of these operators: `<=`, `<`, `==`, `!=`, `>=`, and `>`. Only the `not` operator differs. In Solidity, we use the exclamation point (`!`) to denote the negation of a conditional statement.

Pose the following question to the class.

* **Question:** In the preceding code, can you figure out a way to restructure the nested `if` statements by using different, correct syntax?

  * **Answer:** Recall that the `else` statement needs to enclose its code block in braces. So, you can rewrite the code as follows:

    ```solidity
    pragma solidity ^0.5.0;

    contract IfElse {
        uint y;

        function exampleIfElse(uint x) public {
            if (x < 10) {
                y = 0;
                        }
            else {
                if (x < 20) {
                    y = 1;
                }
                else {
                    y = 2;
                }
                          }
        }
    }
    ```

* The second `if` statement belongs to the code block of the first `else` statement. This nesting style can get messy. That’s why we mainly use the simplified nesting syntax of the original code. That way, we can omit the braces around any single-statement code blocks.

Answer any questions before moving on to the next activity.

---

### 8. Student Do: Trade Controllers (20 min)

**Corresponding Activity:** [Trade Controllers](Activities/05-Stu_Trade_Controllers)

In this activity, students will gain practical experience with using conditional statements in Solidity. They’ll use basic logical operators and a control flow—an order of statements and functions—to build a smart contract that tracks trades in the Ethereum blockchain.

For this activity, students can either create a new Solidity file named `trade_controller.sol` or use the provided starter file.

**Files:**

[Trade Controllers file](Activities/05-Stu_Trade_Controllers/Unsolved/README.md)

[README.md](Activities/05-Stu_Trade_Controllers/README.md)

---

### 9. Instructor Do: Review Trade Controllers (10 min)

**Corresponding Activity:** [Trade Controllers](Activities/05-Stu_Trade_Controllers)

In this section, you’ll review the solution to the previous activity, Trade Controllers.

**File:** [Trade Controllers](Activities/05-Stu_Trade_Controllers/Solved/trade_controller.sol)

Open the Remix IDE and begin to live code. Explain each step to students.

* Create a basic smart contract named `TradeController`.

* Define two variables: a `uint` variable named `previousPrice` and a `string` variable named `tradeType`.

At this point, explain to the class that we’re defining our contract parameters. A number variable will hold the previous price and a string to signify the type of trade—for example, “buy” or “sell.”

```solidity
pragma solidity ^0.5.0;

contract TradeController {
    uint previousPrice;
    string tradeType;
}
```

Continue explaining the steps.

* Create a `public` function named `makeTrade`. This function should take a `uint` argument named `currentPrice` that represents the current price of the asset.

* Add a new `bool` argument to the `makeTrade` function, and name it `buyAnyway`.

  * `bool` represents a `boolean` and is a `variable` that can be true or false. This `buyAnyway` will tell our program to buy ether.

    ```solidity
        function makeTrade(uint currentPrice, bool buyAnyway) public {


        }

    ```

* In the body of the `makeTrade` function, define a conditional statement that checks if the current price is less than the previous price. If this condition is true, set the `tradeType` variable to “Buy” and the previous price equal to the current price.

* Place `|| buyAnyway` at the end of the conditional. This will allow the function to return `true` even if the current trade price is greater than the previous price. You might want to buy anyway, regardless of the previous price. 

   ```solidity
       function makeTrade(uint currentPrice, bool buyAnyway) public {
           if (currentPrice < previousPrice || buyAnyway) {
               tradeType = "Buy";
               previousPrice = currentPrice;
           }
   ```

At this point, explain that an`if-else`statement can be useful when writing a program to buy or sell. Here, we can set a conditional to compare the `currentPrice`to the `previousPrice`. If it is higher, you tell your program to `Sell` to make a profit.  

* Add an `else if` statement with a condition that checks if `currentPrice` is less than `previousPrice` so that we know when to sell.

* Add a final `else` statement for the case when the first two conditions evaluate to `false`. In this statement, set `tradeType` to “Hold”, because you don’t want to buy or sell in this scenario. 

  ```solidity
           else if (currentPrice > previousPrice) {
                   tradeType = "Sell";
                   previousPrice = currentPrice;
           }
           else {
              tradeType = "Hold";
          }
       }
   ```

Here’s the completed contract:

   ```solidity
   pragma solidity ^0.5.0;

   contract TradeController {
       uint previousPrice;
       string tradeType;

       function makeTrade(uint currentPrice, bool buyAnyway) public {
           if (currentPrice < previousPrice || buyAnyway) {
               tradeType = "Buy";
               previousPrice = currentPrice;
           }
           else if (currentPrice > previousPrice) {
                   tradeType = "Sell";
                   previousPrice = currentPrice;
           }
           else {
               tradeType = "Hold";
           }
       }
   }
   ```

* Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

Answer any questions students have about the activity before moving on.

---

### 10. Instructor Do: The Require Function (10 min)

**Corresponding Activity:** [The Require Function](Activities/06-Ins_Require_Function)

In this section, you will explain an alternative to conditionals in Solidity called the `require` function.

For this demonstration, you will need to open the Remix IDE.

**File:** [The Require Function](Activities/06-Ins_Require_Function/Solved/require.sol)

Introduce the `require` function and a use case.

* Solidity provides an alternative to using conditional statements to define the contract terms before allowing its fulfillment: it’s called the `require` function.

* Use cases  for the `require` function include:

  * Verifying that a recipient is someone you know after completing a withdrawal transaction  

  * Verifying that the sender smart contract has enough ether to cover the requested amount

* As a fintech professional, you can strengthen your contract policies by using the `require` function.

To demonstrate how the `require` function works, start by copying and pasting with the following `BankAccount` contract:

```solidity
pragma solidity ^0.5.0;

contract BankAccount {
    address payable accountOwner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;

    function withdraw(uint amount, address payable recipient) public {
        if (recipient == accountOwner) {
            return recipient.transfer(amount);
        }
    }

    function deposit() public payable {}

    function() external payable {}
}
```

* This contract resembles the one that we created earlier. However, we added an `address payable` variable to set the Ethereum address of the account owner. We also added an `if` statement to the `withdraw` function to ensure that the ether gets withdrawn to the account owner’s address.

* This contract is logically accurate. But, we can confirm the account owner by using the `require` function instead of the `if` statement.

Next,  explain how the `require` function works and then code an example. 

* The `require` function checks a condition just like an `if` statement does. But if the condition is false, it will return the unused gas and any ether and roll back the entire transaction. Consider it a hard stopping point: you require a specific condition to be true to continue.

* Let’s put the `require` function into action. In the `BankAccount` contract, we’ll replace the `if` statement with a call to the `require` function, as the following code shows:

   ```solidity
   pragma solidity ^0.5.0;

   contract BankAccount {
       address payable accountOwner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;

       function withdraw(uint amount, address payable recipient) public {
           require(recipient == accountOwner, "You don’t own this account!");
           return recipient.transfer(amount);
       }

       function deposit() public payable {}

       function() external payable {}
   }
   ```

* Like an `if` statement, the `require` function checks if a conditional expression is true. If it is, then the code appearing after the declaration will run. Otherwise, the function returns an exception message, and any further execution halts.

* In the preceding code, we use the `require` function to check if the recipient is the account owner. If the conditional statement is false, the recipient isn’t the account owner. So, the code **raises** (returns) an exception that **throws** (displays) a message reading "You don't own this account!"

* Unlike with the `if` statement, when the conditional statement of the `require` function is false, the contract immediately stops running. It returns the remaining gas to the contract or to the account that ran the contract. You can think of the `require` function as a type of error handling. Notice that we can even declare a custom error message for the user.

* If the `withdraw` function receives an address that doesn’t match the value of `accountOwner`, which our contract defines, the function raises an error and displays an error message reading, "You don’t own this account!"

Slack out the [Solidity documentation on error handling](https://docs.soliditylang.org/en/v0.5.0/control-structures.html#error-handling-assert-require-revert-and-exceptions).

Answer any questions before moving on to the next activity.

---

### 11. Student Do: Enforcing Contract Terms (25 min)

**Corresponding Activity:** [Enforcing Contract Terms](Activities/07-Stu_Enforcing_Contract_Terms)

In this activity, students will use the `require` function to enhance the `sendRemittance` function of the `CustomerAccount` contract that they created in the previous lesson.

Tell students to use the Solidity file in the `Unsolved` folder to write their code. Alternatively, they can use the `customer_account.sol` contract created in the previous lesson to write their code.

**File:** [Enforcing Contract Terms](Activities/07-Stu_Enforcing_Contract_Terms/Unsolved/customer_account.sol)

**Instructions:** [README.md](Activities/07-Stu_Enforcing_Contract_Terms/README.md)

---

### 12. Instructor Do: Review Enforcing Contract Terms (10 min)

In this section, you’ll review the solution to the previous activity.

**Corresponding Activity:** [Enforcing Contract Terms](Activities/07-Stu_Enforcing_Contract_Terms)

Open the Remix IDE and begin to code the solution to the activity. Use the following file:

**File:** [Enforcing Contract Terms](Activities/07-Stu_Enforcing_Contract_Terms/Unsolved/customer_account.sol)

Review each step.

* Define an `address payable` variable named `authorizedRecipient`. This Ethereum address will represent a third-party account that’s authorized to receive withdrawal payments.

* To allow the account owner to receive withdrawal payments at their Ethereum address, change the `owner` variable to become `payable`.

   ```solidity
   pragma solidity ^0.5.0;

   contract CustomerAccount {
       address payable owner;
       bool isNewAccount;
       uint public accountBalance;
       string customerName;
       string customerLastName;
       address payable authorizedRecipient;
   ```

* Modify the type of the `newOwner` variable in the `setInfo` function to `address payable`. The purpose of doing this is to avoid compilation errors from the change that you made to the `owner` variable.

   ```solidity
       function getInfo() view public returns(address, address payable, bool, uint, string memory, string memory) {
           return (owner, authorizedRecipient, isNewAccount, accountBalance, customerName, customerLastName);
       }
   ```

* Change the `sendRemittance` function by adding a `require` function. The `require` function will enforce the rule that only the account owner or the authorized recipient can receive ether from the contract balance. The `require` function is therefore protecting the ether from being stolen.

  ```solidity
    function sendRemittance(uint amount, address payable recipient) public {
        require(recipient == owner || recipient == authorizedRecipient, "The recipient address is not authorized!");
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }
  ```

* Ensure there is a `deposit` function and an external payable `fallback` function. This ensures that the ether can be deposited.

  ```solidity
    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
    }   
  ```

* Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

Give the class time to ask any questions before ending the class. If time permits, offer to go over any parts of the activity or the code that students may need help with.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
