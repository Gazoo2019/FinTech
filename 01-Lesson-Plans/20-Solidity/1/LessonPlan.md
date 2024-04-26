## 20.1 Lesson Plan: Smart Contracts Fundamentals

---

### Overview

Today's class will introduce the students to smart contracts.

In essence, **smart contracts** are computer programs that allow credible transactions of digital assets under certain conditions without third parties. In this unit, the students will learn what a smart contract is. They’ll also build smart contracts by using [Solidity](https://solidity.readthedocs.io/en/latest/index.html), which is an object-oriented language for implementing smart contracts in Ethereum.

Today's class will introduce the students to the fundamental concepts of smart contracts. It will also introduce them to the development tools and the environment that they’ll use to write basic contracts, create functions, utilize getters and setters, experiment with the Remix IDE, and compile their smart contracts.

---

### Class Objectives

By the end of this lesson, the students will be able to:

* Explain what a smart contract is and explain its applications in fintech and other business areas.

* Explain how Solidity works and how it differs from Python as a programming language.

* Explain how the Ethereum Virtual Machine (EVM) is an isolated environment and how Solidity code can access only on-chain data.

* Recognize that a smart contract is a program that runs in the EVM.

* Identify the kinds of smart contracts and their top use cases.

* Explain how Remix supports blockchain development.

* Create three types of functions in Solidity: a deposit function that adds ether, a withdraw function that withdraws ether, and a fallback function that captures ether.

* Create getters and setters, including their return types, in Solidity.

---

### Instructor Notes

* Smart contracts involve lots of math and computing complexity that are beyond the scope of today's class. The goal of this lesson is to show the students how smart contracts work and what tools we use to create, compile, and deploy them.

* Smart contracts have several applications beyond the financial sector, such as those in the medical, industrial (supply chain), and cybersecurity sectors. Feel free to include additional use cases or applications that you believe are suitable for the class.

* This lesson marks the first time that students will encounter a strictly typed programming language. This may be a difficult adjustment for the students, as they will have to remember to specify data types everywhere, as well as use semicolons to end expressions.

* If the students get frustrated, remind them that they are learning something that few are skilled at. By learning a strictly typed language now, they’ll more easily learn any programming language in the future.

* Set your Remix compiler version to match your pragma. Otherwise, unexpected errors may occur.  The pragma and compiler versions should match, as observed in the following image:

  ![pragma_compiler_match](Images/pragma_compiler_match.png)

* **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

---

### Slideshow and Time Tracker

* You can review the slides for this lesson on Google Drive: [Lesson 20.1 slides](https://docs.google.com/presentation/d/1wNAHET1NzFtpokVMm3MwwRh7symrbDgjcO3QJ9tzqzk/edit?usp=sharing).

* To add the slides to the student-facing repository, first download the slides as a PDF. To do that, on the **File** menu, select **Download**, and then select **PDF Document (.pdf)**. Then add the PDF file to your class repository along with other necessary files. You can review these instructions in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

  **Note:** Edit access is not available for this document. If you want to modify the slides, create a copy by selecting **Make a copy** on the **File** menu.

* You can review the Time Tracker for this lesson in the following file: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome and Class Introduction to Smart Contracts (10 min)

Welcome the class to Unit 20 of the FinTech Boot Camp! This unit will teach the students a new programming language: Solidity. It’s important that the students feel excited to learn this language for blockchain development. This introduction will prepare the students for this lesson that explains the role of Solidity in blockchain.

* Congratulations on learning how to use Web3 both to interact with Ethereum nodes and to send transactions! And, congratulations on making it this far in the boot camp!

* In this unit, you’ll learn how to use Solidity.

Remind the class that blockchain is used to establish trust with a network that maintains an immutable ledger.

Define the role of Solidity in blockchain.

* Solidity enhances our transaction processes, allows us to establish the terms of a financial contract, and gives us the ability to create applications and services on the blockchain.

* We can use smart contracts to define the parameters for a purchase, an auction, voting, banking transactions, and more. So, a developer that can program in Solidity is valuable to institutions that are involved with blockchain transactions.

* **Smart contracts** are like computer programs that can run on a blockchain. This means that people can use them to build decentralized applications (dApps) that can run code in a trustworthy way.

Give a brief explanation of dApps in the following talking points. This will help highlight the importance of smart contracts and Solidity:

* You will develop dApps in upcoming units.

* dApps are software that has decentralized operations and that uses decentralized storage.

* Compare dApps to traditional software applications. The latter generally run on a centralized server and use centralized storage. By contrast, dApps run in a decentralized environment that the blockchain nodes provide.

The next few talking points are meant to explain the characteristics of smart contracts to the students:

* Smart contracts exist on a blockchain, so they automatically inherit two valuable properties:

  * Smart contracts are immutable. This means that once a smart contract is created and validated, it can never be changed (see section below on `Upgradable Smart Contracts`).

  * Smart contracts are distributed. This means that everyone on the blockchain network validates the terms of the contract.

* Here’s an example: if one party to the contract or member of the blockchain network tries to override the terms of the contract by trying to trigger an early release of funds, the other network members will recognize the change to the contract as invalid and prevent the action.

`Upgradable Smart Contracts`: Smart contracts are immutable by design as this is a necessary feature that enables decentralization and security but it does have drawbacks as it prevents any updates to the business logic or criticical security updates once the contract is deployed. An attempt to get the best of both worlds, i.e. immutable yet improvable contracts, has led to the introduction of so called `Upgradable Smart Contracts`. These are created using so called proxy contracts that enable developers to modify contract's functionality post deployment —without causing any harm to security or decentralization.  It is important to make students aware that upgradeability and mutability are not the same. Particularly, you still cannot change a program deployed to an address on the Ethereum blockchain but you can change the code that is executed when a user interact with that smart contract. Encourage students to read more about this on the [Ethereum website]((https://ethereum.org/en/developers/docs/smart-contracts/upgrading/)).

* The immutable and distributed nature of smart contracts makes them almost impossible to change once they’re deployed.

* That’s why in addition to the financial sector extensively using them, people are using them to solve problems in healthcare, real estate, supply chains, and other industries. People can even use dApps to build decentralized games, voting applications, and marriage contracts.

Go over the principles of smart contracts with the students in the following talking points:

* Smart contracts need to allow application development and credible transactions that involve assets without a third-party overseer. So, smart contracts rely on the following building blocks:

  * A robust, reliable and industry-supported blockchain technology

  * A robust and reliable programming language

  * An isolated execution environment

  * Robust encryption mechanisms

  * A suitable set of development tools for creating and deploying the smart contracts

* These building blocks involve a lot, but as you work with smart contracts, they’ll all start to make more sense.

* Developers like us write smart contracts by using Solidity, which is a human-readable programming language. It's like Python in the sense that its syntax comes close to human language (as opposed to the bits and bytes of a more computer-friendly language). This eases our ability to read, write, and understand Solidity code.

Let the class know that in the upcoming sections, they’ll learn about the differences between Solidity and Python. This will involve how they create, compile, and use the code. Then, they’ll build their very first smart contract by using this new language!

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

* **Question:** In a few words, how would you define a smart contract to someone who’s new to blockchain technology?

  * **Answer:** Smart contracts are just computer programs that run on a blockchain. People use them for credible transactions of digital assets without third parties.

---

### 2. Instructor Do: Solidity and Remix (10 min)

This section provides a continued overview of Solidity&mdash;the programming language that people use for smart contract development on the Ethereum blockchain. This portion of the class also introduces the students to Remix, which is the IDE that we use for Solidity development and later deployment.

In the next talking point, explain how Solidity can be used professionally and how it’s currently being used in the industry:

* Solidity will help us develop smart contracts that work on Ethereum-compatible blockchains. These include [Hyperledger Fabric](https://www.hyperledger.org/) from the Linux Foundation, [Quorum](https://consensys.net/quorum/) from ConsenSys, and [Ethereum Classic](https://ethereumclassic.org/).

Before getting into the fundamentals of Solidity coding, we need to discuss the how of writing and running Solidity code:

* Solidity code is considered particularly human readable, with characteristics that resemble those of both Python and JavaScript.

* Here’s a summary of what happens when a Solidity smart contract runs: The program first gets compiled. This means that it’s converted from human-readable syntax into a computer-friendly version of the code, called **bytecode**. Once compiled, the code runs in the EVM.

* The **EVM** is a software platform that’s embedded in each node of the Ethereum blockchain network. The EVM runs the bytecode that results from running a Solidity smart contract.

Explain a key benefit of using the EVM: It offers an isolated environment in which Solidity code can run&mdash;without accessing the computer network, files, or other resources of the host computer. This means that by using that same instructions, each decentralized node on the Ethereum blockchain can validate the smart contract. The EVM is thus essential to the consensus mechanism of the Ethereum blockchain.

Explain to the students that in general, a **consensus mechanism** allows the nodes in the Ethereum blockchain to work together to both stay secure and reach an agreement on the current state of the blockchain.

Slack out the link to the [Remix IDE](https://remix.ethereum.org/) to the students and highlight the following:

* We use an IDE for Solidity, just like we use an IDE for Python. But instead of using Visual Studio Code or JupyterLab, we’ll use the Remix IDE.

* The Remix IDE is an open-source application for developing, deploying, and administering smart contracts that run on Ethereum-based blockchains. We can use this IDE for the entire development cycle of smart contracts and as a playground for teaching and learning Ethereum.

* The Remix IDE is available in both web and desktop versions For better compatibility among operating systems. In our class, we’ll use the web version of the Remix IDE.

* Because Remix is an open-source application, the Remix IDE is under constant development, and its user interface often gets updated. So, the interface in the current live version might vary from the slides that appear in this lesson.

Slack out the link to the [Remix Project Website](https://remix-project.org/) to the students. Let them know that if they want to learn more about the entire Remix Project or even join its development community, this is an excellent resource.

---

### 3. Instructor Do: Coding Our First Smart Contract (20 min)

**Corresponding activity:** [First Smart Contract activity](Activities/01-Ins_First_Smart_Contract)

**File:** [First Smart Contract file](Activities/01-Ins_First_Smart_Contract/Solved/First_Smart_Contract.sol)

**Link:** [Remix IDE](https://remix.ethereum.org/)

In this activity, you as the instructor will demonstrate to the students how to code a basic smart contract by using the Remix IDE. Be sure to take your time and explain each step as you go through it.

Slack out the link to the [Remix IDE](https://remix.ethereum.org/). Then navigate to the [Remix IDE](https://remix.ethereum.org/) in a browser before beginning the demonstration.

To start creating our first smart contract, first open the Remix IDE. Then, in the Featured Plugins area, click the Solidity button, as the following image shows:

![A screenshot points out the Solidity button.](Images/20-1-remix-ide-first-launch.png)

Explain the Solidity development environment display: this environment includes two new buttons, named **Solidity static analysis** and **Solidity unit testing**, as the following image shows:

  ![A screenshot points out the two buttons.](Images/20-1-solidity-environment-enabled.png)

Explain that now that the IDE is set up, the students can start coding.

Go through the steps to create a smart contract by coding a Solidity script that defines the structure of the contract.

* In this demonstration, we’ll start with a basic smart contract that will store an Ethereum address and a message.

* To create a new Solidity script in the Remix IDE, first click the **File Explorers** button (which appears in the upper-left area of the window). This causes the Solidity Compiler pane to change to the File Explorers pane, as the following image shows:

![A screenshot points out the File explorers button and includes the File Explorers pane.](Images/20-1-open-remix-file-browser.png)

* In the File Explorers pane on the toolbar, click the Create New File button, as the following image shows:

![A screenshot points out the Create New File button.](Images/20-1-new-file-icon.png)

* A new box appears, where we can type a file name for our new smart contract. Type `message_contract.sol`, and then press Enter, as the following image shows:

![A screenshot points out the text “message_contract.sol” in the new box.](Images/20-1-set-new-filename.png)

Explain that just like `.py` is the file extension for our Python scripts, `.sol` is the file extension for our Solidity smart contracts.

Point out that a new, empty Solidity script, named `message_contract.sol`, opens in the code editor pane, as the following image shows:

  ![A screenshot points out the empty code editor pane.](Images/20-1-remix-code-editor.png)

Explain to the students that the first aspect that we need to define when creating a smart contract is the pragma version.

* **Pragma** refers to the version of Solidity that we’ll use. This module will use version 5.0.0, which we’ll define in the first line of our code. Type the following code into the Remix IDE editor:

  ```solidity
  pragma solidity ^0.5.0;
  ```

Explain the following scenario to the students. Suppose that we want to ask someone we know to send us some money to help pay the rent for an apartment. We can create a basic smart contract that contains a relevant message. To do so, we type our code in the code editor pane.

* Start by typing the word `contract`, followed by the text `MessageContract`, followed by a set of curly braces ({}). Explain that this defines the name of the contract, as well as the portion of the code where we’ll write the smart contract.

* Next create a variable named `myAddress` by using the `address` keyword, and set it to `0xc3879B456DAA348a16B6524CBC558d2CC984722c`.

* Finally, create a variable by using the `message` keyword, and set it to "Send me money!". The entire code block is as follows:

  ```solidity
  contract MessageContract {
    address myAddress = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
      string message = "Send me money!";
  }
  ```

Explain the preceding code, starting with how the syntax differs a bit from Python syntax. 

* We specify a smart contract by using the `contract` keyword and a set of braces ({ }) that defines the start and the end of the contract’s code. So, we defined a contract named `MessageContract` that has two lines of code inside the braces.

* Note that we use the **CapWords** style for the contract name. With this style, we capitalize the first letter of each word.

Close the browser instance, and then refer to the slides to begin discussing the Solidity data types:

* Solidity is a programming language that’s **statically typed**. This means that we need to specify a data type for each Solidity variable. By contrast, we don’t need to do this for Python variables.

* The code from the smart contract that we just created has two variables: `myAddress` and `message`.

* We specified `address` as the type of the `myAddress` variable and `string` as the type of the `message` variable.

* Like Python, Solidity uses string variables to store text values.

Identify the difference in the naming style for variables.

* In Solidity, the standard practice is to use the **mixedCase** style for naming variables. This means that we use lowercase for the first word and capitalize the first letter of each subsequent word. (Because the `message` variable name consists of only one word, it’s all lowercase.) 

* By contrast, the Python style is to separate the words of a variable name with underscores.

* Solidity coding styles originated from the [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

* When we define the data types up front, the Solidity compiler doesn’t have to use resources to figure them out. In Python, the interpreter runs the code and figures out the types as it goes along.

* While this makes writing Python code easier, it also makes it more expensive to run. This is because the Python interpreter has to figure out the types every time the code runs.

* When code that’s written in any programming language runs, a certain component takes charge of performing the code execution. This component is either a compiler or an interpreter.

Reference the slides as you explain the different Solidity data types to the students:

* Solidity includes several data types. The following image lists the main ones, which you can use for smart contracts, and includes Python and Solidity examples of using them:

  ![A table depicts the data types and examples of them.](Images/20-1-solidity-data-types.png)

* The main data types in Solidity are string, positive number, negative number, wallet address, and boolean value.

* Note the following about the Solidity data types:

  * A variable of type `string` stores a text value.

  * A variable of type `uint` stores a positive number. The keyword `uint` stands for “unsigned integer.”

  * A variable of type `int` stores a number. This type of variable can store a positive or a negative integer.

  * A variable of type `address` stores an Ethereum address. This is a special Solidity data type for storing an Ethereum address in a way that’s computationally more efficient than storing a string.

  * A variable of type `bool` stores a Boolean value&mdash;that is, `true` or `false`.

Go back to the Remix IDE, and open the first contract that you wrote earlier in this demo. Then go through the steps to compile the contract and highlight the following:

* After creating a smart contract, the next logical step is to compile it for testing purposes. After we compile it, we can run it to send the message.

* First, in the Remix IDE, we click the **Solidity compiler** button, as the following image shows:

  ![A screenshot points out the Solidity compiler button.](Images/20-1-open-solidity-compiler.png)

* Next, in the Compiler drop-down list, we select the Solidity compiler version that we want to use. The version number is 0.5.0. Note that the commit ID that follows the version number isn’t relevant for our purposes. The drop-down list will include only one version 0.5.0 to select. The following image shows the selection of 0.5.0:

  ![A screenshot points out 0.5.0 selected in the list.](Images/20-1-choosing-compiler.png)

* Finally, we click the **Compile message_contract.sol** button to pass our Solidity script through the compiler, as the following image shows:

  ![A screenshot points out the “Compile message_contract.sol” button.](Images/20-1-compile-program-button.png)

* If the program successfully compiles, a green check mark indicating “compilation successful” will appear next to the **Solidity compiler** button, as the following image shows:

  ![A screenshot points out a green check mark indicating “compilation successful”.](Images/20-1-compilation-succeed.png)

Explain that now, we have a successfully compiled Solidity contract.

* Remember, because this is a new programming language, it’s normal for typos to become an issue. For example, one might forget the semicolon at the end of a Solidity code line.

* The compiler is a useful tool: it detects any compilation errors and displays an error indication and specific error messages. The following image shows a compilation error indication and a specific message that resulted from a missing semicolon at the end of Line 5:

  ![A screenshot points out an error message at the end of the Solidity Compiler pane.](Images/20-1-compilation-error.png)

* The red circle next to the **Solidity compiler** button in the sidebar indicates **compilation failed with 1 error**. In the Solidity Compiler pane, an error message prints at the end of the pane. This message explains that the program expected a semicolon (;) but got a brace (}). Error messages like this one will help you debug your Solidity contracts.

Ask the class if they have any questions regarding variables, the Remix IDE, smart contracts, or Solidity. Then introduce the next activity.

---

### 4. Students Do: Create a Customer Contract (20 min)

**Corresponding activity:** [Create a Customer a Contract activity](Activities/02-Stu_Create_a_Customer_Contract)

**File:** [Create a Customer a Contract file](Activities/02-Stu_Create_a_Customer_Contract/Unsolved/customer_contract.sol)

**Instructions:** [README.md](Activities/02-Stu_Create_a_Customer_Contract/README.md)

Slack out the preceding files to the students, and advise them to begin coding in the Remix IDE.

In this activity, the students will create a Solidity smart contract. This is the first project in which the students will independently use Solidity.

Be sure to provide insight for confused students and ensure that any available TA is present for the students to get support.

The students will begin by creating their first Solidity file. It’s okay to remind them how to do this if they struggle. It’s also okay to remind them that Solidity files have the `.sol` file extension.

---

### 5. Instructor Do: Review Create a Customer Contract (10 min)

**Corresponding activity:** [Create a Customer a Contract activity](Activities/02-Stu_Create_a_Customer_Contract/)

**File:** [Create a Customer Contract file](Activities/02-Stu_Create_a_Customer_Contract/Solved/customer_contract.sol)

In this part of the lesson, you as the instructor will review the first smart contract that the students independently wrote by live coding it. Solidity is new to them, so they might have questions. Be sure to allow time for them to ask questions after each step.

First, tell the compiler the version of Solidity that we’re using: `pragma solidity ^0.5.0;`. Then, begin by using the `contract` keyword and the `CustomerAccount` contract name to create the contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;

contract CustomerAccount {}
```

Emphasize that this is how we begin to write every smart contract.

Next, create the following variables in the body of the smart contract, and emphasize the appropriate data types:

* The `owner` variable: Holds the Ethereum address of the main customer (for example, 0xaaaaaaaaaaaaaaaaa).

* The `isNewAccount` variable: Represents whether the account is new (that is, `true` or `false`).

* The `accountBalance` variable: Holds the account balance (for example, 10000).

* The `customerName` variable: Holds the first name of the customer (for example, "Jordan").

* The `customerLastName` variable: Holds the last name of the customer (for example, "Habib").

The following code shows these variables:

```solidity
    address owner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    bool isNewAccount = true;
    uint accountBalance = 10000;
    string customerName = "Jordan";
    string customerLastName = "Habib";
```

Compile the smart contract. If an error occurs, review the code, and make the necessary changes for a successful compilation.

Ask the class if they have any questions, and offer to review the steps before sending them on their break.

---

### 6. Break (15 min)

---

### 7. Instructor Do: Solidity Functions (15 min)

**Corresponding activity:** [Crypto Trading Functions activity](Activities/03-Ins_Crypto_Trading_Functions/Solved/Crypto_Trading_Functions.sol)

**File:** [Crypto Trading Functions file](Activities/03-Ins_Crypto_Trading_Functions/Solved/Crypto_Trading_Functions.sol)

**Link:** [Remix IDE](https://remix.ethereum.org/)

This portion of the lesson introduces Solidity functions to the students before they begin to independently write more-complex smart contracts by using functions.

You will demonstrate how to effectively use functions in Solidity by creating a basic smart contract. Then, you’ll explain how to write all the parts of a function. This will also provide a deeper dive into Solidity data types.

To engage the class, begin by explaining a scenario in which this contract might be used:

* Say that you’re a famous crypto trader who wants to publish your latest buy order, including the price that you paid.

* A **buy order** refers to the action of buying a certain amount of financial assets. In this case, we’re referring to buying cryptocurrencies.

* To prove that you made a cryptocurrency purchase at the execution price, you want to build a smart contract that publishes your latest trade to the blockchain. The **execution price** is the price at which the trade was executed.

* Explain that we need to define a function to enable a smart contract to interact with the blockchain or even with other smart contracts. The function will capture the business rules that we want to implement. As we did in Python, we can define functions in Solidity&mdash;but with some nuances, as we’ll learn next.

Open the Remix IDE, and then begin to code a contract.

Before creating a function, ensure that the compiler is using version 5, and name the smart contract `LatestTrade`.

This contract will store the following data that relates to a trading operation: the coin type, the price, and a `bool` identifier to ensure that it’s a buy order.

Define the variable as follows: a `string` named `coin` that contains "BTC", a `uint` number named `price`, and a `bool` (that is, Boolean) identifier named `isBuyOrder`, as the following code shows:

```Solidity
pragma solidity ^0.5.0;

contract LatestTrade {
    string coin = "BTC";
    uint price;
    bool isBuyOrder;
}
```

Review the code with the students.

* First, we define a `string` variable named `coin` that contains “BTC” as its default text. The `coin` variable will store the name of the last coin that we purchased.

* Next, we define a `uint` variable named `price`. This will store the last price that we paid for the coin. 

* Finally, we define a `bool` variable named `isBuyOrder`. If the order was a buy order, we’ll set this to `true`. If it was a sell order, we’ll set it to `false`.

Call attention to the next part of the lesson as you add a function to the smart contract. This is the most important takeaway from this portion of the lesson for the students.

Explain that to add interaction capabilities to our smart contract, we’ll add a function named `updateTrade`. This function will update the trading price of our last buy or sell operation, as the following code shows:

```Solidity
pragma solidity ^0.5.0;

contract LatestTrade {
    string coin = "BTC";
    uint price;
    bool isBuyOrder;

    function updateTrade(string memory newCoin, uint newPrice, bool isBuy) public {
       coin = newCoin;
       price = newPrice;
       isBuyOrder = isBuy; // Is this a buy or a sell order?
   }
}
```

Point out that in the preceding code, we used the CapWords style for the contract name. And, we used the mixedCase style for the function name, just like we do when we name variables.

Add that we used the mixedCase style for the function argument names. Despite the fact that Solidity doesn’t require this style, following this practice creates more readable code&mdash;and makes the code seem more professional.

Point out that the `updateTrade` keyword follows the `function` keyword and defines and names the function.

* In Solidity, we have the `function` keyword followed by the function name. Then, the following syntax can specify many function arguments or none.

* This function has three arguments, and we specify the data type for each.

Discuss the `memory` keyword that precedes the `newCoin` argument.

* This keyword tells the Solidity compiler to temporarily store the value of the `string` argument in memory.

* Doing this uses a smaller amount of resources by keeping it in the data area called storage.

Recall that before running the code of a smart contract, the first step is to compile it to make sure that it’s free of errors and to convert it into machine code.

Ensure that the students are aware that the `memory` keyword is available only for the function arguments of a contract.

Explain that strings are complex data types. Thus, they’re more expensive than integers and addresses. This is because they consume more computational resources, such as memory or storage. And, that’s why the EVM requires us to specify where to store an argument.

Over the next few talking points, explain how the EVM can store items in three areas: in storage, in memory, and on the stack. Reference the slides as needed.

* The contract variables all reside in storage and that temporary values reside in memory. The EVM clears this memory area between function calls. So, it’s less expensive to use than storage.

* The third storage solution for the EVM is the stack, which holds small local variables and argument values. It’s almost free to use but can store only a limited number of values.

Remind the students that a great way to learn more about these storage areas is to read the [Storage, Memory and the Stack](https://docs.soliditylang.org/en/v0.5.11/introduction-to-smart-contracts.html?highlight=storage#storage-memory-and-the-stack) section of the Solidity documentation. Take a moment to slack out this link, and advise the students to bookmark it.

Point out that the last item of the function to pay close attention to is the `public` keyword at the end of the function definition.

* By default, Solidity functions are public. This means that the function can be called from outside the contract&mdash;by either users or other contracts. This is known as **access control** in the object-oriented programming paradigm.

* Despite `public` being the default access control value, the language syntax requires us to specify it.

Answer any questions before moving on.

---

### 8. Students Do: Travel Expenses Contract (30 min)

**Corresponding activity:** [Travel Expenses Contract activity](Activities/04-Stu_Travel_Expenses)

**File:** [Travel Expenses Contract file](Activities/04-Stu_Travel_Expenses/Unsolved/TravelExpenses.sol)

**Instructions:** [README.md](Activities/04-Stu_Travel_Expenses/README.md)

Slack out the preceding files to the students, and remind them to begin coding in the Remix IDE.

In this activity, the students will practice variable declarations in Solidity by creating a travel expenses smart contract. This will be slightly more complicated than the function that the instructor explained to the class.

Ensure that the students are supported throughout the activity, and allow them to ask questions.

---

### 9. Instructor Do: Review Travel Expenses Contract (10 min)

**Corresponding activity:** [Travel Expenses Contract activity](Activities/04-Stu_Travel_Expenses)

**File:** [Travel Expenses Contract file](Activities/04-Stu_Travel_Expenses/Solved/TravelExpenses.sol)

Begin this section by asking the students for feedback on the previous activity&mdash;to assess how comfortable they’re feeling about Solidity. Allow a moment for the students to ask questions.

Remind them that this is their first day with a new programming language and that despite any challenges they might be facing, they are supported.

Open the Remix IDE, and then begin live coding for the class, explaining each step while coding.

As we’ve done previously, set up the contract. Specifically, add the Solidity version for the compiler by using the `pragma` keyword, and then add the contract by using the `contract` keyword, as the following code shows:

  ```solidity
  pragma solidity ^0.5.0;

  contract TravelExpenses {
  ```

Create an `address payable public` variable named `corporate_account`, and assign a valid Ethereum address to it, as the following code shows:

  ```solidity
  address payable public corporate_account = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;
  ```

* This is `address payable` so that it can be used to transfer ether.

Create an `address payable` variable named `personal_account`, and assign a valid Ethereum address to it, as the following code shows:

  ```solidity
  address payable personal_account = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;
  ```

Define a `string` variable named `employee_name`, and assign your name to it, as the following code shows:

```solidity
string employee_name = "<your name>";
```

Create a 256-bit unsigned integer constant named `daily_expenses_eth` that has a value of 1, as the following code shows:

  ```solidity
  uint256 constant daily_expenses_eth = 1;
  ```

Remind the class we need to specify the data type.

Create a 256-bit unsigned integer named `current_expenses_wei` that has an initial value of 0, as the following code shows:

```solidity
uint256 current_expenses_wei = 0;
```

Create an unsigned integer named `current_taxes_wei` that has an initial value of 0, as the following code shows:

```solidity
uint current_taxes_wei = 0;
```

Create a 16-bit unsigned integer named `expenses_count`, and that has an initial value of 0, as the following code shows:

```solidity
uint16 expenses_count = 0;
```

Create an 32-bit unsigned integer named `eth_usd_rate`, and assign it the current value in US dollars (USD) of one ether (ETH), as the following code shows:

```solidity
uint32 eth_usd_rate = 143;
```

Create a 256-bit unsigned integer constant named `eth_wei_rate`, and assign it the number of wei in one ether, as the following code shows:

  ```solidity
  uint256 constant eth_wei_rate = 1000000000000000000;
  ```

Explain that 256 bits (vs. 32 or 16) will allow us to assign a larger number, because the number of bits refers to the allocated memory capacity.

Create a new 256-bit unsigned integer public variable named `daily_expenses_wei`, and assign it the value of `daily_expenses_eth` times `eth_wei_rate`, as the following code shows:

  ```solidity
  uint256 public daily_expenses_wei = daily_expenses_eth * eth_wei_rate;
  ```

Explain that this variable is calculating the expenses.

Create an unsigned 256-bit unsigned integer named `expense_usd_no_tax`, and assign it the value of the `new_net_expense_usd` minus the taxes, as the following code shows:

```solidity
function RecordExpense(uint32 new_net_expense_usd, uint tax_rate) public {
  //    minus taxes.
  uint256 expense_usd_no_tax = new_net_expense_usd - new_net_expense_usd * tax_rate / 100;
```

Create an 256-bit unsigned integer named `taxes_usd`, and assign it the taxes in USD from `new_net_expense_usd`, as the following code shows:

```solidity
uint256 taxes_usd = new_net_expense_usd * tax_rate / 100;
```

Explain that we’re calculating the tax costs.

Update `current_expenses_wei` by adding the value of `expense_usd_no_tax` converted to wei, as the following code shows:

```solidity
current_expenses_wei += expense_usd_no_tax * eth_wei_rate / eth_usd_rate;
```

Update `current_taxes_wei` by adding the value of `taxes_usd` converted to wei, as the following code shows:

```solidity
current_taxes_wei = taxes_usd * eth_wei_rate / eth_usd_rate;
```

Increase `expenses_count` by one unit to complete the contract, as the following code shows:

```solidity
    expenses_count += 1;
  } 
}
```

Compile the contract by using the Remix IDE.

Remind the students that using the compiler is an excellent way to check for errors, because the compiler will point them out.

Check the code for errors. If any exist, explain how to fix them.

Then allow the students time to ask questions and provide feedback.

---

### 10. Instructor Do: Getters and Setters (10 min)

**Corresponding activity:** [Getters and Setters activity](Activities/05-Ins_Getters-and-Setters)

**File:** [Getters and Setters file](Activities/05-Ins_Getters-and-Setters/Solved/GettersAndSetters.sol)

This activity will add getters and setters to the code that the students wrote earlier in this lesson. The purpose of this activity is to define getters and setters and to give an example of how to use them.

Copy the code from the `Unsolved` folder, open a new file in the Remix IDE, and then paste the code in the new file. Alternatively, if the code from the Solidity Functions activity is still present in the Remix IDE, you can start with that.

Briefly review the code with the class:

```solidity
pragma solidity ^0.5.0;

contract LatestTrade {
    string coin = "BTC";
    uint price;
    bool isBuyOrder;

    function updateTrade(string memory newCoin, uint newPrice, bool isBuy) public {
        coin = newCoin;
        price = newPrice;
        isBuyOrder = isBuy; // Is this a buy or a sell order?
    }
```

Explain that now that we’ve defined our first function, we can add another function that gets the current values of all the defined variables&mdash;and, all at once.

* Create a new function named `getLatestTrade`, as the following code shows:

  ```solidity
      function getLatestTrade() view public returns (string memory, uint, bool) {
          return (coin, price, isBuyOrder);
      }
  }
  ```

Explain to the class that `public` functions are part of the contract interface. So, they can be called either internally in the contract or via messages.

Explain that the `getLatestTrade` function returns values that are based on the user's input.

After coding this function, pause to explain each part of the function and the rules of Solidity to the students as follows:

* The `getLatestTrade` function doesn’t have any arguments.

* This is because we use this function only to get the current values of the `coin`, `price`, and `isBuyOrder` variables. Because these variables are defined within the scope of the smart contract, they’re inaccessible to other users or contracts. (This would be different if we created the `getLatestTrade` function to allow us to set or manipulate their values.)

* As just mentioned, the `getLatestTrade` function only gets values and doesn’t change them. That’s why we have a `view` access modifier to specify to the Solidity compiler that this is a read-only function.

* An advantage of only getting data is that calling this function is almost free! It has only an associated cost to write data to the blockchain or to perform calculations on Solidity objects in memory.

* Solidity requires us to specify the types of data that this function returns. In this case, the function returns a `string` value, a `uint` value, and a `bool` value. (Note that the `string` value will be stored in memory, because we’re only getting the value of the variable.) These data types refer to the contract variables that we read to get their values.

* A common practice in object-oriented programming languages is to define functions that only update the value of variables or that only get the current values.

Define a **setter** by explaining that the `updateTrade` function sets the values of the variables. So, this function is called a setter.

Define a **getter** by explaining that the `getLatestTrade` function gets the current values of the variables. So, this function is called a getter.

Feel free to reference the slides for the students while diving more deeply into the definitions of getters and setters.

Remind the students that they now know how to add a function to a smart contract and that they can define two special types of functions:

* Setter functions, which can set or update the value of any variable.

* Getter functions, which can get the current value of a variable.

Ask the students to take a moment to answer a coding question by using the Remix IDE. Ask the question, and then give the students a moment to code the answer. Then, code the answer yourself so that students can visualize or conceptualize it.

* **Question:** Suppose that you want to create a smart contract that allows people to transfer funds between two Ethereum addresses. So, you need a function that sets the transfer amount, the sender, and the recipient. How would you define the function’s signature (that is, the function name and its arguments)?

  * **Answer:** You might name your function `setTransferInfo` and define its signature as follows:

    ```solidity
    function setTransferInfo(address sender, address recipient, uint amount) public {
      // set user data here
    }
    ```

Before transitioning to the next activity, provide the students with encouragement.

* The key to learning is practice. Learning a new programming language is like learning a new human language.

* You’ll have the opportunity to practice these new Solidity skills throughout the remainder of this unit.

---

### 11. Students Do: Adding Getters and Setters (20 min)

**Corresponding activity:** [Adding Getters and Setters activity](Activities/06-Stu_Adding_Getters_and_Setters)

**File:** [Adding Getters and Setters file](Activities/06-Stu_Adding_Getters_and_Setters/Unsolved/customer_contract.sol)

**Instructions:** [README.md](Activities/06-Stu_Adding_Getters_and_Setters/README.md)

**Link:** [Remix IDE](https://remix.ethereum.org/)

Slack out the preceding files to the students, and remind them to begin coding in the Remix IDE

In this activity, the students will create a smart contract and independently add getters and setters to it for the first time.

---

### 12. Instructor Do: Review Adding Getters and Setters (10 min)

**Corresponding activity:** [Adding Getters and Setters activity](Activities/06-Stu_Adding_Getters_and_Setters)

**Files:** [Adding Getters and Setters file](Activities/06-Stu_Adding_Getters_and_Setters/Solved/customer_contract.sol)

**Link:** [Remix IDE](https://remix.ethereum.org/)

In this activity, you will review the activity that the students just completed. The purpose will be to provide clarity on how to use getters and setters. You can do this by adding a getter and a setter to the `CustomerAccount` contract that the students created earlier.

Open the Remix IDE, and then either paste the code from the starter file into a new Solidity file or open the `customer_contract.sol` file that the students created earlier. The starter code should contain the following:

```solidity
pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    bool isNewAccount = true;
    uint accountBalance = 10000;
    string customerName = "Jordan";
    string customerLastName = "Habib";
}
```

Create a `view public` getter function named `getInfo` as follows:

```solidity
function getInfo() view public returns(address, bool, uint, string memory, string memory) {
        return (owner, isNewAccount, accountBalance, customerName, customerLastName);
    }
```

In `returns`, specify the types of data that the `getInfo` function will return.

* This function returns the values of all the variables that you specified before&mdash;specifically, the values of `owner`, `isNewAccount`, `accountBalance`, `customerName`, and `customerLastName`.

Remove the default values for the customer info, as they are no longer needed.

Next, create a setter function named `setInfo` as follows:

```solidity
function setInfo(address newOwner, bool newAccountStatus, uint
    newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
```

* The setter function updates the values of each variable in the object.

* The values of all the variables that you specified before&mdash;specifically, the values of of `owner`, `isNewAccount`, `accountBalance`, `customerName`, and `customerLastName`, are retrieved from the `getInfo` function to get the current value of each variable.

The final code for this lesson should be as follows:

```solidity
pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner;
    bool isNewAccount;
    uint accountBalance;
    string customerName;
    string customerLastName;

    function getInfo() view public returns(address, bool, uint, string memory, string memory) {
        return (owner, isNewAccount, accountBalance, customerName, customerLastName);
    }

    function setInfo(address newOwner, bool newAccountStatus, uint
      newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }
}
```

Compile the smart contract. If an error occurs, review the code, and make the necessary changes for a successful compilation.

Give the students some time to ask questions before ending the class.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
