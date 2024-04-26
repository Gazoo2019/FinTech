## 21.2 Lesson Plan: Token Standards

### Overview

In today's class, the students will learn about two types of blockchain tokens: fungible and non-fungible. They’ll learn how to use the ERC-20 token standard to create non-fungible tokens in an efficient and secure manner.

In addition, the students will use the Ganache application for blockchain testing and the MetaMask digital wallet. They’ll incorporate both of these applications into the Remix IDE. They’ll then be able to deploy and test their tokens.

---

### Class Objectives

By the end of the class, the students will be able to:

* Differentiate fungible from non-fungible tokens.

* Explain that the Ethereum Request for Comments (ERC) standards are official smart contract implementations for various use cases.

* Explain which ERC token standards correspond with fungible vs. non-fungible tokens.

* Implement the ERC-20 standard to create a fungible token by using the OpenZeppelin library.

* Deploy and test a token that uses the ERC-20 standard by using MetaMask and a Ganache blockchain.

* Define the terms **initial coin offering (ICO)** and **crowdsale**.

### Slideshow and Time Tracker

* You can review the slides for this lesson on Google Drive: [Lesson 21.2 slides](https://docs.google.com/presentation/d/10OPVlCRiJLPOGnwBSYPM9_FTA3x5DsGwBUhisk73sFc/edit?usp=sharing).

* To add the slides to the student-facing repository, first download the slides as a PDF. To do that, on the **File** menu, select **Download**, and then select **PDF Document (.pdf)**. Then add the PDF file to your class repository along with other necessary files. You can review these instructions in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

  **Note:** Edit access is not available for this document. If you want to modify the slides, create a copy by selecting **Make a copy** on the **File** menu.

* You can review the Time Tracker for this lesson in the following file: [Time Tracker](TimeTracker.xlsx).

---

## Instructor Notes

* For today's class, it will be important that the students understand how the OOP concept of inheritance enables their smart contracts to use all the features that the ERC-20 token standard defines (as the OpenZeppelin library details).

* The use of token standards (ERC-20 and eventually ERC-721), as OpenZeppelin defines, will form the foundation of their coding for the remainder of the course.

* The students will also be introduced toMetaMask in this lesson. Be sure to take the necessary time to explain how MetaMask acts as the link between Ganache and the deployed application in the Remix IDE.

* Reassure the students that as they continue to work with Solidity, they’ll become more comfortable with using both the common patterns in the code and the OpenZeppelin library. Many of the examples that will be shown this week have been used in other smart contract applications.

* For more information about functions, refer to the [OpenZeppelin ERC-20 documentation](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) and the [OpenZeppelin ERC20.sol GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol).

* **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

* Have your TAs keep track of time by using the [Time Tracker](TimeTracker.xlsx).

---

## Class Activities

### 1. Instructor Do: Fungible and Non-Fungible Tokens (10 min)

In this activity, the students will get introduced to the concepts of fungible and non-fungible tokens along with their differences.

You’ll start with real-world examples and move to digital examples. For additional documentation, refer to [Tokens - OpenZeppenlin Docs](https://docs.openzeppelin.com/contracts/2.x/tokens#_different_kinds_of_tokens).

Start by welcoming the students back to class for another fabulous day learning about blockchain tokens.

* As previously discussed, we can use tokens to represent any potential store of value. These include votes, currency, property and, as we found in an earlier class, arcade games.

* Some tokens represent assets that have interchangeable and exchangeable values. These are called **fungible** tokens. Tokens that represent fiat currency or cryptocurrency often fall into this category.

* A token that represents one ether or one bitcoin, for example, holds the same value as another token that represents one ether or one bitcoin. And, these tokens are interchangeable with each other.

* As with fiat currencies, an exchange rate exists between cryptocurrencies. Individuals can thus exchange a single bitcoin for the appropriate amount of ether.

* Tokens that represent other types of assets can also be fungible. For example, consider tokens that represent votes. Any individual’s vote holds power that’s equal to that of any other individual’s vote. So, the tokens that represent their votes have equal values.

* The practice of representing assets as tokens on a decentralized blockchain is called **tokenomics**. This is a powerful concept. But, it goes deeper than representing the values of interchangeable assets.

* Tokens representing stores of value that aren’t directly comparable and interchangeable are called **non-fungible tokens**, or **NFTs**.

* NFTs depend more on **which** assets someone owns rather than on **how many**. The values of NFTs are more difficult to determine. And, they’re not interchangeable with other NFTs.

* Examples of non-fungible goods include parcels of land, diamonds, and collectibles.

  * A person might own one parcel of land in California and another in Pennsylvania. These parcels differ, so they don’t hold the same value. They’re thus not interchangeable with one another. The same is true for two collectible figures, like a Pop Vinyl and a Beanie Baby. Each collectible is unique.

Take this opportunity to discuss some real-world implementations of NFTs on the blockchain with the students.

* NFTs have recently gained a lot of popularity among artists and art collectors.

* Christie's recent sale of an NFT by the artist Beeple for $69 Million set a new record for digital art.

* Jack Dorsey, the founder of Twitter, auctioned off an NFT that represents his first tweet for $2.9 million.

Have a TA slack out the link to the [CryptoKitties website](https://www.cryptokitties.co/), and give the students a minute or two to explore the site.

* [CryptoKitties](https://www.cryptokitties.co/) is a popular NFT application on the Ethereum blockchain. Users can buy, sell, and breed virtual cats in the form of NFTs. At the cryptocurrency peak in 2017, some cryptokitties were valued at over $130,000 USD.

If possible, share your own experience with NFTs to facilitate the discussion.

Ask if any of the students have had an experience either buying or creating an NFT that they’d like to share with the class.

Finally, have a TA slack out the following the short video by Reuters that explains the concept of NFTs:

[Explained: What are Non-fungible tokens or NFTs?](https://www.youtube.com/watch?v=X_AugmQpwho)

Conclude the discussion by explaining that NFTs, such as cryptokitties, fundamentally differ from fungible tokens.

* Both types have value, but the value of each NFT is unique. This leads to different sets of rules, processes, and implementations for fungible and non-fungible tokens.

* The smart contracts that create NFTs follow different standards than those that create fungible tokens.

* Today, we’ll discuss and use some of the standards that the Ethereum community has created for implementing both fungible and non-fungible tokens.

---

### 2. Instructor Do: Token Standards and ERC-20 (10 min)

In this section, you’ll introduce the students to Ethereum Improvement Proposals (EIPs) and the ERC-20 token standard that they’ll use to build Ethereum tokens.

#### Token Standards

* Ethereum continues to grow and rapidly evolve as the blockchain community expands on the concepts of Web 3.0 and blockchain development.

* During periods of change like this one, developers form **standards** that outline best practices for the platform to prevent bugs and security vulnerabilities.

* In Ethereum, these standards are known as [Ethereum Improvement Proposals](https://eips.ethereum.org/), or **EIPs**. The Ethereum Foundation officially refers to an EIP as “a design document providing information to the Ethereum community, or describing a new feature for Ethereum or its processes or environment.”

* Remind the student that in an earlier module, we used Bitcoin Improvement Proposals (BIPs) to generate a mnemonic seed phrase and to then transform our seed phrase into a private key for our blockchain account. EIPs resemble BIPs. But, the proposed standard in an EIP is developed specifically for the Ethereum blockchain rather than for the Bitcoin blockchain.

* Although there are several categories of EIPs, we’ll focus on **Ethereum Request for Comments (ERC)**. This type of EIP sets standards at the application level. This means that the standards apply to the code for applications, such as smart contracts and tokens.

* Most EIPs, including ERCs, follow a similar workflow, which includes the following stages:

  * **Work in progress (WIP):** An EIP creator formulates an EIP and can ask for input on community forums.

  * ** Draft:** The initial EIP draft and any changes get merged into the Ethereum EIP GitHub repository via a pull request. The EIP must then be implemented or, written as code, progress to the next phase.

  * ** Last Call:** The EIP gets listed on the [Ethereum Improvement Proposals](https://eips.ethereum.org/) website in the Last Call section. If no unaddressed technical complaints or required changes to the source material exist, the EIP will become final. This means that the standard won’t change after this point.

  * ** Final:** The Ethereum blockchain and its participants begin using the processes that the EIP lays out.

Have a TA slack out the link to the list of [some ERCs in various stages of development](https://eips.ethereum.org/erc).

Explain that many ERC token standards exist, but we’ll focus on two of the most popular:

* The [ERC-20 Token Standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) for creating fungible tokens.

* The [ERC-721 Non-Fungible Token Standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/) for creating NFTs.

Have a TA slack out the preceding two links to the students. Give them a few minutes to examine the contents, especially the ERC-20 documentation.

Explain that today’s class will focus on implementing the ERC-20 token standard. And, we’ll focus on the ERC-721 standard in a later unit.

#### ERC-20

Explain why we’ll use ERC-20:

* Although other standards apply to fungible tokens, we’ll use ERC-20 for the following reasons:

  * Compared to some other standards, it’s simpler to understand and implement.

  * It has the widest adoption and support among blockchain explorers, wallets, and developer libraries.

  * ERC-20 tokens are common in the real world. And, many popular stablecoins implement them. These include USD Coin (USDC) by Coinbase and Gemini dollar (GUSD) by Gemini. So, it’s important to understand how ERC-20 tokens are structured.

  * Unlike some other standards for fungible tokens, ERC-20 doesn’t require us to incorporate any additional EIPs.

* ERC-20 essentially defines the code for a simple smart contract for a fungible token.

* Using standards to write contracts ensures consistency and predictability across various contracts. One ERC-20 token contract should work just like any other ERC-20 token contract. This is particularly important in the finance realm. After all, no one wants unexpected behavior from contracts that handle their money.

Explain that using standards also makes it easier to write, use, and build applications. This is because we know which functions are available for use in the applications and how they’ll behave.

* We use the ERC-20 standard for fungible Ethereum tokens that store value. The ERC-20 standard defines rules for how the tokens get used, how transactions get made, and how new tokens get created (or minted).

* The ERC-20 standard serves as the basis for many cryptocurrencies and coins, especially stablecoins, that exist today. These include Chainlink (LINK), Wrapped Bitcoin (WBTC), Binance Coin (BNB), USD Coin (USDC), and Dai (DAI).

Explain that in an earlier lesson, we implemented a basic token smart contract by writing custom logic.

* In this lesson, we’ll instead learn how to use community-accepted ERC-20 standards to implement fungible tokens. This will not only make our tokens more secure but also save us some work!

Explain that by keeping track of the most recently accepted EIPs, we can stay up to date on the current Ethereum standards, practices, and technologies.

* Now that we understand what token standards are and why we use them, let’s learn how to implement an ERC-20 token contract by using OpenZeppelin!

---

### 3. Instructor Do: OpenZeppelin ERC20 Contracts (20 min)

**Corresponding activity:** [OpenZeppelin ERC20](Activities/01-Ins_OZ_ERC20)

**Files:**

[Starter file](Activities/01-Ins_OZ_ERC20/Unsolved/ArcadeTokenERC20.sol)

[Solution file](Activities/01-Ins_OZ_ERC20/Solved/ArcadeTokenERC20.sol)

In this activity, you’ll build the `ArcadeToken` smart contract by using the `ERC20` and `ERC20Detailed` contracts from the OpenZeppelin library.

Start this demonstration by explaining that we’ll rewrite the `ArcadeToken` smart contract that we developed in an earlier lesson. The purpose will be to enhance it by using the ERC-20 token standard.

#### ERC20 and ERC20Detailed Contracts

* The arcade tokens are fungible. (Remember that every token holds a value that’s equal to the value of every other token). So, we want to reimplement our `ArcadeToken` contract by using the official ERC-20 standard. To do that, we’ll use ERC-20 contracts that the OpenZeppelin library provides.

Navigate to the [OpenZeppelin ERC-20 contracts](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) in the OpenZeppelin documentation.

Have a TA slack out the [same link](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) to the students so that they can review this documentation.

* The OpenZeppelin library provides a wide variety of contracts that relate to the ERC-20 token standard. Each of the OpenZeppelin ERC-20 contracts is designed to accomplish something slightly different. And, we can further customize each contract for our particular purposes.

* We’ll use several OpenZeppelin ERC-20 contracts throughout this unit. Today, we’ll start with the basic OpenZeppelin `ERC20` contract. With that, we can begin re-creating our `ArcadeToken` contract.

In the Remix IDE, open the [starter file](Activities/01-Ins_OZ_ERC20/Unsolved/ArcadeTokenERC20.sol), and then import the `ERC20` contract into the application, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
```

* Like we import functions from the SafeMath library, we must first import the `ERC20` contract from the OpenZeppelin library before we can use it. This tells the compiler that the `ArcadeToken` contract will inherit the functions and properties of the `ERC20` contract.

Remind the students of the discussion about inheritance that took place in an earlier previous lesson.

* **Inheritance** is a technique that brings in new functionality to our contract from an existing contract. That is, our contract inherits this functionality from the existing contract.

Navigate to the [ERC20.sol GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol) that the previous `import` statement references. Show the students the functions that the code specifies, including the import of the SafeMath library.

* By inheriting from the `ERC20` contract, our `ArcadeToken` contract has all the same functions and code that the `ERC20` contract has&mdash;just as if we had written the code ourselves.

* The OpenZeppelin `ERC20` contract contains functions like `_transfer`, `balanceOf`, and `_mint`.

* By inheriting this contract, our `ArcadeToken` contract will be able to use these functions, too! This means that we don’t have to write the entire contract from scratch like we did in an earlier lesson.

Next, add the `ArcadeToken` contract, including the `ERC20` contract, as the following code shows:

```solidity
contract ArcadeToken is ERC20 {

}
```

* In Solidity, we can inherit a contract by using an `is` statement. To inherit `ERC20`, we thus define our `ArcadeToken` contract with the `ArcadeToken is ERC20` statement.

* The Ethereum ERC-20 standard defines some mandatory functions for a fungible token contract, including `_transfer`, `_mint`, `balanceOf`, and `totalSupply`. These functions provide critical functionality for any ERC-20 token.

* Other functions, such as `name`, `symbol`, and `decimals`, are considered optional. OpenZeppelin separates the optional functions into an extension contract, which is named `ERC20Detailed`.

Add the `import` statement for [ERC20Detailed.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol) and the `ERC20Detailed` reference to the `ArcadeToken` contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {

}
```

* We want our `ArcadeToken` contract to become a version of the OpenZeppelin `ERC20` contract. But, we also want `ArcadeToken` to include the optional functions from `ERC20Detailed`. So, we’ll import and inherit both the `ERC20` and `ERC20Detailed` contracts. This will tell Solidity that `ArcadeToken` is a version of the `ERC20` contract and that it’s also a version of the `ERC20Detailed` contract.

Next, compile the `ArcadeToken` contract in the Remix IDE.

* After we save or compile our contract in the Remix IDE, the `ERC20.sol` and `ERC20Detailed.sol` contracts that we imported will get downloaded and listed in the Remix files list.

In the Remix IDE, in the File Explorers pane, open the `ERC20.sol` contract, as the following image shows:

![A screenshot depicts ERC20.sol selected in the File Explorers pane.](Images/oz-erc20.png)

In the preceding image, notice that to get to **ERC20.sol** in the File Explorers pane, you need to expand **github**, expand **OpenZeppelin**, expand **openzepellin-contracts**, expand **contracts**, expand **token**, expand **ERC20**, and then select **ERC20.sol**.

Opening `ERC20.sol` displays the complete code of the contract for the students. Point out that the code in the Remix file matches that on the [ERC20.sol GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol).

Make the connection between the code that the `ERC20` contract provides and the code that the students wrote in their original `ArcadeToken` contract.

* You might notice that the `ERC20` code resembles the code that we wrote for `ArcadeToken` in an earlier lesson.

* It contains a mapping named `_balances` that keeps track of user balances. The `balanceOf` function pulls the `uint` value that corresponds to a specified address from the `_balances` mapping. And, it does so in the same way that our `balance` function previously did this.

* This contract also contains a `_mint` and a `_transfer` function. The `_transfer` function differs a bit from our earlier one. But, it has the same parameters and general logic.

* The `ERC20` contract also uses the SafeMath library. And, the `_transfer` function is coded to prevent the type of integer underflow error that we discussed earlier.

* By using the `ArcadeToken is ERC20`, statement, our `ArcadeToken` contract inherits all the variables, functions, and code directly from the `ERC20` contract.

Next, you’ll examine the `ERC20Detailed` contract by opening `ERC20Detailed.sol` from the File Explorers pane.

Navigate to the `constructor` function inside the `ERC20Detailed` contract. This function should appear as follows:

```solidity
constructor (string memory name, string memory symbol, uint8 decimals) public {
     _name = name;
     _symbol = symbol;
     _decimals = decimals;
 }
```

* The constructor is a programming technique that many programming languages use. With constructors, you can quickly customize code with your own initial values.

Have a TA slack out the link to the [Constructors](https://docs.soliditylang.org/en/v0.5.0/contracts.html#constructor) page of the Solidity documentation, which displays the Solidity `constructor` function.

* Notice that `ERC20Detailed` includes a function named `constructor`, which establishes the `name`, `symbol`, and `decimals` parameters.

* The constructor creates a new contract by using the supplied parameters. Using a constructor simplifies the process of creating custom versions of the `ERC20Detailed` contract. The `name` parameter contains the human-friendly name of the token, the `symbol` parameter contains the ticker symbol of the token, and the `decimals` parameter contains the number of decimal places that this token will use.

Explain that using decimal places allows customers to purchase or transfer fractions of a token.

* Think of the way that we use fractions of a US dollar, for example. The dollar has two decimal places. This means that we can divide one dollar into increments of 10&Hat;2 (that is, increments of 100). So, the smallest denomination of a dollar is one hundredth of a dollar, which we call one cent.

* By contrast, ether uses 18 decimal places. This means that we can divide one ether into increments of 10&Hat;18 (that is, increments of 1 followed by 18 zeros). So, the smallest denomination of an ether is one divided by 10&Hat;18, which we call a wei.

* As we learned in earlier units, all ether transactions get conducted in wei. Similarly, all token transactions get conducted in the smallest denomination of a token, which OpenZeppelin calls a **bit**.

* This is because Solidity can perform these calculations only with whole numbers and not with fractions. For example, say that we set two decimal places for a token. This means that each token contains 10&Hat;2, or 100, bits. If we want to transfer 3.45 tokens to a friend, the code will transfer 3.45 &times; 10&Hat;2, or 345, token bits.

* Most tokens use 18 decimal places. This is because ether uses 18 decimal places. And, using the same number of decimal places simplifies the conversion between ether and tokens. For this reason, we’ll use 18 decimal places for our arcade token.

Have a TA slack out the link about token decimal places in the OpenZeppelin documentation: [A Note on decimals](https://docs.openzeppelin.com/contracts/2.x/erc20#a-note-on-decimals).

Explain that by importing `ERC20` and `ERC20Detailed`, we made lots of helpful code available to use in our own contract.

Now, we can use these OpenZeppelin contracts to create an enhanced version of the `ArcadeToken` contract.

#### Apply the ERC-20 Standard to the ArcadeToken Contract

Start the contract creation process by defining the `ArcadeContract` owner, as the following code shows:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed {
  address payable owner;
}
```

* As in an earlier lesson, we start by defining the owner of our contract.

* Remember that the `owner` variable is of type `account payable`. This is so that the owner of the contract can get paid ether when customers purchase tokens.

#### Add the Constructor

Explain that in the original contract, we created the `symbol` and `exchange_rate` variables along with `owner`. With the `ERC20` contract, that process changes. Specifically, we use the constructor to define these two variables.

* We now need to add a `constructor` function below the owner address.

* As we just learned, a constructor is a special type of function that we can use to pass initial values to our contract. So, we’ll create a constructor for our `ArcadeToken` contract and pass it some initial parameters.

* In this case, the `constructor` function will accept a `uint` named `initial_supply`, which represents the supply of tokens that this contract will create on deployment.

* Note that we won’t set the value for `initial_supply` until we deploy the contract. When we deploy, Remix will allow us to enter this value.

The next step is to incorporate the `ERC20Detailed` constructor information into the `ArcadeToken` contract, as the following code shows

```solidity
contract ArcadeToken is ERC20, ERC20Detailed {
  address payable owner;

  constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
  }
}
```

* We’ll also use our constructor to call the constructor that we inherited from `ERC20Detailed`.

* Next, because the `ArcadeToken` contract inherits the `ERC20Detailed` contract, we need to call the `constructor` function of `ERC20Detailed`. Solidity allows us to call this `constructor` function by using our `constructor` function and passing it the three parameters that it requires.

* Recall that the `ERC20Detailed` constructor takes the `name`, `symbol`, and `decimals` parameters. We’ll pass `ArcadeToken` as the name and “ARCD” as the symbol. And, remember that we decided to use the Ethereum default of 18 decimal places for our token.

Next, set the `owner` variable and call the `_mint` function inside the body of the constructor function, as the following code shows:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }
}
```

* In the body of the constructor, we set `owner` to `msg.sender`, as we did for our contract in an earlier lesson.

Remind the students that `msg.sender` is the person who’s currently sending the message. So, the owner will end up being the person who deploys the contract&mdash;that is, the arcade owner.

* Next, we call the `_mint` function that the OpenZeppelin `ERC20` contract provides to us. As detailed in the docs, the `_mint` function requires two parameters: `address` and `amount`.

* By passing the `owner` and `initial_supply` parameters to the `_mint` function, we can create an initial number of tokens and have them sent to the contract owner on the contract deployment.

* With this code, the `constructor` function of the token contract will mint an initial supply of tokens and send them to the arcade owner on deployment of the contract.

Pose the following question to the class:

* What happens when the owner needs to mint more tokens in the future?

#### Add Minting Capability

Now, add the a separate `mint` function to the `ArcadeToken` contract, as the following code shows:

```solidity
function mint(address recipient, uint amount) public {
  _mint(recipient, amount);
}
```

* The `_mint` function of the `ERC20` contract, which we inherited from `ERC20` and used for our contract, is an internal function. We can call this function only from within the `ArcadeToken` contract. To use this code outside the contract&mdash;for example, in an application like Remix&mdash;we need to wrap in a public function.

* To do this, we’ll create a new public `mint` function that calls the internal `_mint` function of `ERC20`.

* We can supply recipients and amounts to the public `mint` function.

* The public function will then provide the specified amount of tokens to the specified recipient by calling the internal `_mint` function of `ERC20`. This is a nifty trick that programmers use to control the ways in which people can interact with particular code.

* But as in the earlier lesson’s contract, only the arcade owner should be able to mint new tokens. Customers need to purchase tokens and not mint their own for free.

* We’ll restrict the public `mint` function to the contract owner by using a `require` statement. But this time, we’ll do so by creating our own modifier. This will make our code simpler to reuse. Rather than typing the `require` statement each time, we’ll be able to apply this modifier to any other functions or variables that we want to restrict to only the contract owner.

Add the `onlyOwner` modifier code to the `ArcadeToken` contract (between the `owner` variable and the `constructor` function), as the following code shows:

```solidity
modifier onlyOwner {
    require(msg.sender == owner, "You do not have permission to mint these tokens!");
    _;
}
```

* We’ll name the modifier `onlyOwner`.

* Inside the modifier, we’ll add the same `require` statement that we used in the earlier lesson’s contract to ensure that `msg.sender` equals the address of the contract owner.

* On the last line of the modifier, we’ll add an underscore ( `_` ) to tell Solidity to return to the function that called the modifier.

Once you’ve created the `onlyOwner` modifier, you can add the `onlyOwner` modifier to the public `mint` function, as the following code shows:

```solidity
function mint(address recipient, uint amount) public onlyOwner {
    _mint(recipient, amount);
}
```

* Now, if anyone besides the arcade owner (that is, us) tries to mint new tokens, the smart contract won’t mint them. Instead, it will return the following error message:

  “You do not have permission to mint these tokens!”

The final contract now appears as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
}
```

* That's it! Now, our arcade token is a fully functioning ERC-20 token. We even created an `onlyOwner` modifier for the `mint` function of the contract.

Ask the students if they have any questions about re-creating the `ArcadeToken` contract by using the ERC-20 standards.

Let the students know that in the following activity, they’ll have the opportunity to practice building their own `ArcadeToken` contract that uses the ERC-20 standards.

---

### 4. Student Do: ERC-20 Arcade Token (30 min)

**Corresponding activity:** [ERC20 Arcade Token](Activities/02-Stu_ERC20_Arcade_Token)

**Files:**

[Instructions](Activities/02-Stu_ERC20_Arcade_Token/README.md)

[Starter file](Activities/02-Stu_ERC20_Arcade_Token/Unsolved/ArcadeTokenERC20.sol)

Have a TA slack out the preceding files to the students so that they can complete the activity.

In this activity, you’ll create an `ArcadeToken` smart contract by using the `ERC20` and `ERC20Detailed` smart contracts that the OpenZeppelin library provides.

---

### 5. Instructor Do: Review ERC-20 Arcade Token (10 min)

**Corresponding activity:** [ERC20 Arcade Token](Activities/02-Stu_ERC20_Arcade_Token)

**Files:**

[Instructions](Activities/02-Stu_ERC20_Arcade_Token/README.md)

[Starter file](Activities/02-Stu_ERC20_Arcade_Token/Unsolved/ArcadeTokenERC20.sol)

[Solution file](Activities/02-Stu_ERC20_Arcade_Token/Solved/ArcadeTokenERC20.sol)

In this activity, you’ll review the creation of `ArcadeToken` by using the `ERC20` and `ERC20Detailed` smart contracts that the OpenZeppelin library provides.

Be sure to focus on the concept of inheritance as it applies to the `ERC20` and `ERC20Detailed` contracts in relation to the `ArcadeToken` contract.

Also, be sure to emphasize the role that the constructor plays in creating the `ArcadeToken` contract.

You can use the following walkthrough video as a guide for this review:

[ERC-20 Arcade Token Solution Review ](https://fast.wistia.net/embed/iframe/4z0ejwnynf)

Start the review by focusing on the `import` statements for the `ERC20` and `ERC20Detailed` contracts and the creation of the `ArcadeToken` contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {

}
```

In the Remix IDE, navigate to the pages that contain the code for each of these two contracts. (The folder path for the first contract is **.deps** > **github** > **OpenZeppelin** > **openzeppelin** > **contracts** > **contracts** > **token** > **ERC20** > **ERC20.sol**. The folder path for the second contract is the same, except that you go to **ERC20Detailed.sol** at the end instead of **ERC20.sol**.)

Explain that by importing the statements into the Solidity file and tying them to the `ArcadeToken` contract with the `is` keyword, the `ArcadeToken` contract inherits, or has access to, all the functionality that the pages for the `ERC20` and `ERC20Detailed` contracts detail.

* This functionality includes access to the SafeMath library, the mapping functionality for the balances, and the `ERC20Detailed` constructor function.

The next step is to add the code for the `owner` attribute, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
  address payable owner;

}
```

Next, add the `constructor` function, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
  address payable owner;

  constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
      owner = msg.sender;
      _mint(owner, initial_supply);
  }

}
```

Explain that a constructor function is a special function that we can use to construct our `ArcadeToken` by passing some initial values to it.

* In this case, we can use the constructor function to create an initial supply of tokens when the contract gets deployed.

* By referencing the constructor function of the `ERC20Detailed` contract, we can also establish the values of some initial parameters for the contract. Specifically, these are the values of `name`, `symbol` and `decimals`.

* The value of `decimals` determines the smallest fraction of ether that someone can use to buy a single arcade token. The smallest denomination of ether is the wei. One ether equals 10&sup1;18 wei. So, setting the `decimals` value to 18 simplifies the token conversion process ,because one wei will equal one arcade token.

As you’re discussing the `_mint` function of the constructor, be sure to open the `ERC20` contract page. This is so that you can tie the parameters that get assigned in the `ArcadeToken` contract (`owner` and `initial_supply`) to those that the `ERC20` contract details (`address` and `amount`).

Be sure to stress that the underscore ( `_` ) at the beginning of the `_mint` function name tells the program to return to its place inside the program (after the referenced function executes).

* Inside the constructor function, we’ll also establish the owner of the contract as `msg.sender`, or the person who initially deploys the contract.

* Finally, we call the `mint` function of `ERC20`, assigning it `owner` as the `address` and `initial_supply` as the `amount`.

Next, work through the process of creating the `mint` function. This function will allow the contract owner to mint tokens beyond the initial supply that’s set at the time of the contract deployment.

This will include the creation of the `onlyOwner` modifier as it relates to the public `mint` function, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
  address payable owner;

  modifier onlyOwner {
      require(msg.sender == owner, "You do not have permission to mint these tokens!");
      _;
  }

  constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
      owner = msg.sender;
      _mint(owner, initial_supply);
  }

  function mint(address recipient, uint amount) public onlyOwner {
      _mint(recipient, amount);
  }

}
```

* This public `mint` function takes the same parameters as the `mint` function of `ERC20`: `address` and `amount`.

* To ensure that the functionality of the `mint` function gets reserved only for the contract owner, we’ll create and reference an `onlyOwner` modifier. The `onlyOwner` modifier will incorporate a `require` modifier. This `require` modifier will evaluate whether `msg.sender` equals `owner` and, if it doesn’t, return an error message.

With all the code in place, compile the contract.

Navigate to the contract page, and then deploy the contract with an initial supply of tokens.

In the Remix IDE, review values like those of `decimal`, `name` and `symbol`.

Copy the address used to deploy the contract, and check the contract `balance`. The value of the tokens from the balance check should match that of the initial deployment.

**Question:** Ask the students how the `ArcadeToken` contract has access to  functions that haven’t been defined within  the contract, such as `balanceOf`, `transfer`, and `transferFrom`?

**Answer:** The `ERC20` contract contains the code for all of these functions. The `ArcadeToken` contract inherited them from the `ERC20` contract.

Before moving on to the next section, ask the students if they have any additional questions about the using the `ERC20` and `ERC20Detailed` contracts to create the `ArcadeToken` contract.

---

### 6. Break (15 min)

---

### 7. Instructor Do: Introducing MetaMask (10 min)

**Corresponding activity:** [Ganache & MetaMask Demo](Activities/03-Evr_Deploying_Tokens)

**File:** [Solution file](Activities/03-Evr_Deploying_Tokens/Solved/ArcadeTokenERC20.sol)

In this activity, you’ll perform a high-level demonstration of the Ganache and MetaMask applications by deploying them together with the `AcradeToken` contract.

Be sure that both applications are installed on your machine. MetaMask should be installed as an extension in your Chrome browser.

You’ll use the `ArcadeToken` contract that you reviewed in the previous activity to demonstrate these applications and how they integrate with a contract that’s hosted in Remix.

The purpose of this demonstration is to familiarize the students with the high-level integration among Ganache, MetaMask, and Remix.

In the activity after this one, you’ll have time to work with the students to ensure that they understand the role of each application, how each application operates, and how they work together in the contract deployment and testing process.

Start this activity by explaining that it’s possible to deploy the `ArcadeToken` contract on the main Ethereum blockchain network, which is also called the `mainnet`.

* Because the `ArcadeToken` contract uses industry standards, we can deploy it to the main Ethereum blockchain network (the `mainnet`). In this case, we can have our “ARCD” token listed on a **cryptocurrency exchange**, or a public marketplace where people can trade tokens. Many wallets and block explorers could then automatically detect it .

* But, like with all applications (regardless of whether we wrote them in Solidity or Python), it’s always a good idea to deploy and test a smart contract to catch any potential issues.

* To deploy and test our contract, we will use the test blockchain application Ganache and an integrated wallet called MetaMask.

Encourage the students to just observe this initial demonstration. Let them know that you’ll work through the steps in detail together as a class in the next activity.

Open the Ganache application on your machine, and then select the **Quickstart Ethereum** button, as the following image shows:

![A screenshot points out the the Quickstart Ethereum button on the Ganache start page.](Images/ganache-start.png)

The Ganache application opens the Accounts page, which lists all the available test accounts, as the following image shows:

![A screenshot depicts the the Accounts page.](Images/ganache-test-accounts.png)

* Ganache provides the user with 10 test accounts, each of which starts with a 100-ether balance.

Click the Show Keys button (which looks like a key icon) for the first account, as the following image shows:

![A screenshot points out the Show Keys button, one of which exists for each account.](Images/ganache-key-icon.png)

An **Account Information** dialog box opens that lists the account address and the private key that’s associated with the account, as the following image shows:

![A screenshot depicts the Account Information dialog box.](Images/ganache-private-key.png)

* Besides having a unique Ethereum address, each account also has a private key.

Explain that another application, called MetaMask, will use both the address and the private key information.

Open the MetaMask extension in your Chrome browser.

* MetaMask is a wallet that people can use to interact with the Ethereum blockchain or with various Ethereum-related test blockchains. We’ll integrate MetaMask with Ganache.

First, show the students how to create a new network that’s associated with Ganache.

* We can connect MetaMask to different networks, such as the Ethereum Mainnet. Today, we’ll connect MetaMask with Ganache to test transactions. To do this, we’ll use Ethereum Mainnet, which is the default network. So, we click the Ethereum Mainnet button, which opens the Networks menu. On this menu, we click Custom RPC. Then in the Network Name box, we type **devNetwork**. We copy the RPC Server link from Ganache into the New RPC URL box. In the Chain ID box, we type 1337 and then click the Save button. MetaMask connects with Ganache!

Now, work through the process of adding the first two Ganache test accounts to MetaMask, as the following image shows:

![A screenshot points out the My Accounts menu and the Import Account option.](Images/metamask-account-import.png)

* We can import an account from Ganache into MetaMask. To do that, we first click the My Accounts button, and then on the menu that displays, we select Import Account. We make sure that Private Key is selected on the Select Type drop-down menu. We then copy the private key from the Account Information page in Ganache and paste it into the **Paste your private key string here** box. We then click the Import button.

* Notice that MetaMask lists each resulting account with 100 ether, which matches the amount that Ganache details.

With the test accounts now in MetaMask, navigate to Remix, and then compile the `ArcadeTokenERC20.sol` contract.

When it finishes compiling, open the deployment page, and then deploy the contract using by the **Injected Web** environment.

* Earlier, we compiled and deployed the `ArcadeTokenERC20.sol` file by using the JavaScript VM that Remix supplies. The JavaScript VM gave us a series of account addresses that we could use to test our application. But, all the testing happened inside the Remix IDE.

* By selecting **Injected Web3** as the environment, we can establish a connection between Remix, MetaMask and Ganache.

* Once we select **Injected Web3**, the MetaMask Chrome extension automatically opens and displays accounts from which we can choose for testing.

Select each of the accounts that you just imported from Ganache to import into Remix.

Point out that one of the accounts selected in MetaMask now appears in the **Deploy & Run Transactions** box for the account in the Remix IDE.

To get the second selected account to appear in Remix, navigate to MetaMask, and then choose the alternate account.

Contrast this with the list of 10 accounts that automatically appears in Remix when we use the JavaScript VM. With the **Injected Web3** environment, a user must first select the account in MetaMask.

Next, deploy the contract by using one of the available MetaMask accounts. Point out that the MetaMask window for the account opens and asks you to confirm the transaction.

* The integration with MetaMask asks you to confirm the validity of the transaction. Notice that MetaMask also details the cost of deploying the contract as the gas fee.

In MetaMask, click Confirm to deploy the contract.

Once the contract is deployed in Remix, navigate back to Ganache, and then click the Transactions button (which appears along the top of the page). The Transactions page opens and displays the transaction details. This includes the transaction hash, the account address, and the created contract address, as the following image shows:

![A screenshot points out the Transactions button and displays the transaction details.](Images/ganache-transaction.png)

Explain to the students that once the contract is deployed, they’ll be able to use the other MetaMask accounts to test the deployed contract. And, the Transactions page in Ganache will detail the resulting transactions.

Summarize the interaction among Remix, Ganache, and MetaMask by making the following points:

* We use Remix to develop, compile, deploy, and test the contract operations.

* Ganache mimics the Ethereum blockchain but in the local environment. Ganache creates the account that we use to test the application. It also creates a record of the transactions that occur in the contract.

* MetaMask is the wallet. It functions as the go-between, routing information between Ganache and Remix. MetaMask stores the information that’s associated with each account. This includes the private key, the address, the ether balance, and the balance of other tokens that the account has purchased (including the `ArcadeToken` if set up properly).

Ask the students if they have any high-level questions about the integration among Remix, Ganache, and MetaMask. Then proceed with the next activity, which takes everyone through the process of deploying a smart contract by using these two new applications.

---

### 8. Everyone Do: Deploying Tokens with Ganache and MetaMask (20 min)

**Corresponding Activity:** [03-Evr_Deploying_Tokens](Activities/03-Evr_Deploying_Tokens)

**File:** [Starter file](Activities/03-Evr_Deploying_Tokens/Unsolved/ArcadeTokenERC20.sol)

In this activity, you’ll lead a code-along, where the entire class will deploy the `ArcadeToken` contract by using Ganache and MetaMask.

The students should be able to use their `ArcadeTokenERC20.sol` file from the previous activity. But, you can slack out the preceding starter file to any students who had difficulty getting their contract to deploy and run properly.

Explain to the students that in this activity, they’ll deploy their ERC-20 `ArcadeToken` to a test network by using the two tools just demonstrated: MetaMask for the wallet and Ganache for a test blockchain.

* Ganache should be set up as an application on each student’s machine.

* MetaMask should be set up as an extension on each student's browser.

The students were instructed to install both of these applications as part of the [Tokenomics Install Guide](../Supplemental/Tokenomics-Install-Guide.md).

If any students haven’t installed one or both of these applications, have them identify themselves so that they can work with a TA to install them on their machines.

Start by having each student confirm that they have an operational ERC-20 `ArcadeToken` up and running in Remix. Have the TA slack out the appropriate starter file code to those students who don’t.

At this point, have the students reload the Remix page. This should close any deployed versions of the contract that they have running, giving them a fresh start. The Remix page with the contract code should be open, as the following image shows:

![A screenshot depicts the XP Token contract displayed in the Remix IDE.](Images/xptoken-remix.png)

The next step in the process is to launch Ganache.

#### Launch Ganache

Remind the students that Ganache is an application that launches a personal blockchain for the development and testing of applications that are designed for use on the Ethereum blockchain. With Ganache, a user can develop, deploy, and test their decentralized applications in a safe environment. 

Have the students launch Ganache and then select **Quickstart Ethereum**, as the following image shows:

![A screenshot points out the the Quickstart Ethereum button on the Ganache start page.](Images/ganache-start.png)

The result is a list of 10 account addresses, each with a balance of 100 ether, as the following image shows:

![A screenshot depicts the Accounts page.](Images/ganache-test-accounts.png)

Clicking an account’s Show Keys button (which looks like a key icon and appears at the right side of each account entry) opens the Account Information dialog box, which reveals the private key and the address of the test account, as the following image shows:

![A screenshot depicts the Account Information dialog box, including the icon described as “Show Keys”.](Images/ganache-private-key.png)

Let the students know that each time they launch Ganache, a new list of accounts with different addresses and keys gets created. This will become important later.

The last piece of important information is the RPC server address. This is the local host location of the Ganache instance. This location remains the same every time that Ganache gets launched, and it appears in the RPC Server box, as the following image shows:

![A screenshot points out the RPC Server box on the Accounts page.](Images/ganache-rpc-server.png)

Let the students know that they’ll use all this information in MetaMask, which they’ll work with next.

#### Add Ganache to the MetaMask Network List

Explain to the students that MetaMask is a software cryptocurrency wallet that we use to interact with the Ethereum blockchain.

We can identify the MetaMask browser extension by an icon that looks like a fox. Because the students will frequently use MetaMask over the next several lessons, suggest that the they pin their MetaMask extension to the browser extension list, as the following image shows:

![A screenshot points out MetaMask in the browser extension list.](Images/metamask-browser-icon.png)

Open MetaMask by clicking the icon.

Explain to the students that they’ll connect MetaMask to Ganache by setting up the Ganache RPC server location as a MetaMask network.

Click the Network button (which appears at the top of the MetaMask window), and then in list of MetaMask networks, select **Custom RPC**, as the following image shows:

![A screenshot points out Custom RPC in the Networks list.](Images/metamask-custom-rpc.png)

Explain that they need to do this process only once, because the RPC URL for Ganache doesn’t change when it gets launched.

Open your own Ganache network, and point out the relevant boxes for the students. Have the students enter text in these boxes to create their custom Ganache network, as follows:

* Network Name: Anything that the students want. Suggestions are **Ganache** or **Dev**.

* New RPC URL: The RPC URL from Ganache, which is `HTTP://127.0.0.1:7545`. They can copy it from Ganache and then paste it into MetaMask.

* Chain ID: The value **1337**, which is specific to Ganache.

Have the students scroll down and then click Save, as the following image shows:

![A screenshot points out the Save button.](Images/metamask-ganache-network.png)

Their new network is now saved to the list. To select it for use, they can click the Networks button that appears at the top of the MetaMask page.

#### Import Ganache Accounts into MetaMask

The next step for the students is to import test accounts from Ganache into MetaMask.

Inform the students that they’ll need to complete this process every time that they’re likely to deploy and test an application in Remix. This is because the Ganache account list changes every time that the application gets relaunched.

Explain to the students that once they’ve established the network, the next step is to import Ganache accounts to MetaMask.

To import a Ganache account to MetaMask, click the “My Accounts” icon in the upper-right part of the MetaMask window, and then select **Import Account**, as the following image shows:

![A screenshot points out the “My Accounts” button and the Import Account option.](Images/metamask-account-import.png)

Stress to the students that they want to import rather than add an account. By importing an account, they can specify the account's private key. And, they can delete imported accounts from MetaMask.

Navigate back to Ganache, and then click the Show Keys button (which looks like a key icon) for the first account. When the Account Information dialog box appears, copy the private key, as the following image shows:

![A screenshot depicts the private key selected in the Account Information dialog box.](Images/ganache-private-key-copied.png)

Paste the private key into MetaMask in the **Paste your private key string here** box, and then click Import, as the following image shows:

![A screenshot points out the Import button.](Images/metamask-private-key-string.png)

If the account got imported properly, a new account will appear in MetaMask. This account will have an address with the same first and the same last digits as those that appear in the Account Information dialog box in Ganache, as the following image shows:

![A screenshot points out the first and last digits in both MetaMask and Ganache.](Images/matching-address-info.png)

Repeat the process to import a second Ganache account.

Finally, explain to the students that they can delete accounts. They do that by clicking Account Options (the three dots) next to the account name and then selecting **Remove account**, as the following image shows:

![A screenshot points out the Account Options button and the Remove account item in the list.](Images/metamask-delete-account.png)

Explain to the students that they’ll need to do this process of deleting old accounts from MetaMask and adding new ones every time that they relaunch Ganache. This is because the accounts (that is, the addresses and the private keys) change each time that Ganache gets launched.

Confirm that all the students now have at least two active Ganache accounts loaded into MetaMask. Have the students that aren’t this far along work with a TA to bring them up to speed.

Now that we have our Ganache accounts imported into MetaMask, it’s time to link MetaMask with our `ArcadeToken` contract in Remix.

#### Link MetaMask and the ArcadeToken Contract

Have everyone navigate back to Remix and compile the `ArcadeTokenERC20.sol` contract.

With the contract compiled, go to the **Deploy & Run Transactions** pane. This time, instead of selecting the JavaScript VM environment, select **Injected Web3**.

The Connect With MetaMask dialog box appears, allowing you to select the accounts that you want to link to the Remix instance. Select the accounts that you imported from Ganache into MetaMask, and then click Next, as the following image shows:

![A screenshot points out the selected accounts and the Next button.](Images/remix-injected-web3.png)

A confirmation page appears. Click Connect, as the following image shows:

![A screenshot depicts the Connect to 2 accounts page.](Images/metamask-connect.png)

When the connection completes, the **Account** box in the **Deploy & Run Transactions** pane in Remix contains an address. And, this address matches the one for the selected and active account in MetaMask (that is, the account that indicates **Connected**), as the following image shows:

![A screenshot points out matching addresses in Remix and in MetaMask.](./Images/remix-active-account.png)

With a Ganache account now linked to Remix via MetaMask, we can focus on deploying our `ArcadeToken` contract.

#### Deploy the ArcadeToken Contract

In the **Deploy & Run Transactions** pane, in the **initial_supply** box, type an arbitrary amount, like `3333333333333`. This sets the value of the `initial_supply` constructor parameter. Then click the **transact** button, as the following image shows:

![A screenshot depicts the initial_supply box and the transact button.](Images/arcade-token-erc20-deploy.png)

A MetaMask notification appears, allowing you to confirm the transaction. Before doing so, point out the following:

* We can use the estimated price to check how much deploying this token to the `mainnet` would cost.

Now, in the notification, click Confirm to confirm the contract deployment in MetaMask, as the following image shows:

![A screenshot points out the Confirm button.](Images/deploy-confirm.png)

Confirm that all the students have followed along and deployed their tokens by using MetaMask and Ganache.

When everyone has deployed their contracts, everyone should navigate to Ganache and then click the Transactions button (which appears along the top of the Ganache window). Everyone should then notice their transaction recorded in their own personal blockchain, as the following image shows:

![A screenshot points out the Transactions button and displays a transaction.](Images/ganache-transaction.png)

Next, point out that you can interact with this contract in the **Deploy & Run Transactions** pane in Remix as usual, as the following image shows:

![A screenshot depicts the XP_Token contract in the Deployed Contracts area.](Images/arcade-token-deployed.png)

Explain the following to the class:

* We should copy the contract address and store it in a convenient place. We can always look it up on the blockchain by checking our transaction history, but we want to have it readily available.

Copy the contract address, and then refresh the page, clearing the Remix session. Navigate back to the contract code, compile the contract, and then redeploy it by using **Injected Web3** and the contract owner address from MetaMask.

Finally, in the **Deploy & Run Transactions** pane, in the **At Address** box (which appears just after the Deploy button), paste the contract address, as the following image shows:

![A screenshot depicts an address in the At Address box.](Images/arcade-token-reappear.png)

Click the **At Address** button to fetch the contract from the Ganache blockchain. The contract's interactive menu reappears, as the following image shows:

![A screenshot depicts the options for the contract in the Deployed Contracts section.](Images/arcade-token-deployed.png)

Demonstrate that it’s even possible to paste the address of the contract owner into the **balanceOf** box to confirm that the initially deployed tokens, all 3333333333333 of them, are still available.

Ask the students again if they have any questions about the integration among Remix, Ganache, and MetaMask.

Let them know that they’ll next have the opportunity to put all the pieces together by both building another token that’s ERC-20 compliant and deploying it by using Ganache and MetaMask.

---

### 9. Student Do: Build and Deploy XP_Token (30 min)

**Corresponding activity:** [Build and Deploy XP_Token](Activities/04-Stu_Build_Deploy_XP_Token)

**Files:**

[Instructions](Activities/04-Stu_Build_Deploy_XP_Token/README.md)

[Starter file](Activities/04-Stu_Build_Deploy_XP_Token/Unsolved/XP_TokenERC20.sol)

Have a TA slack out the preceding two files to the students so that they can work through the activity.

In this activity, the students will first implement `XP_Token` by using the `ERC20` contract that the OpenZeppelin library provides. They’ll then deploy and test the `XP_Token` functionality by using Ganache and MetaMask.

---

### 10. Instructor Do: Review Build and Deploy XP_Token (10 min)

**Corresponding activity:** [Build and Deploy XP_Token](Activities/04-Stu_Build_Deploy_XP_Token)

**Files:**

[Instructions](Activities/04-Stu_Build_Deploy_XP_Token/README.md)

[Starter file](Activities/04-Stu_Build_Deploy_XP_Token/Unsolved/XP_TokenERC20.sol)

[Solution file](Activities/04-Stu_Build_Deploy_XP_Token/Solved/XP_TokenERC20.sol)

Focus this review on deploying the `XP_Token` contract by using Ganache and MetaMask.

Be sure that the students understand the process of importing accounts into MetaMask from Ganache. Because the students have now launched Ganache at least twice, show them how to delete old Ganache accounts from MetaMask.

Finally, be sure that the students understand the process for linking Remix with MetaMask via the Injected Web3 environment.

Engage the students as much as possible regarding the code that’s associated with `XP_Token`, which is based on the `ERC20` and `ERC20Detailed` contracts. This code should seem familiar to the students. That’s because it basically matches the code that they created for the `ArcadeToken` contract, also by using `ERC20` and `ERC20Detailed`. 

The final `XP_Token` contract code appears as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract XP_Token is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("XP_Token", "XPT", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
}
```

Engage the students by asking them the following questions. Depending on the student responses, be sure to cover the concepts that the answers provide.

**Question:** Which OOP concept influences the way that the `ERC20` and `ERC20Detailed` contracts get applied to the `XP_Token` contract?

**Answer:** This OOP concept is inheritance. The concept of inheritance proves useful when a certain type of relationship exists between two classes. Specifically, we can use inheritance when we consider one class to be a specialized version of the other, more-general one. In this case, `ERC20` is the general class. And, `XP_Token` is the specialized version of that class.

**Question:** What’s a constructor, and what role does it play in the `XP_Token` contract?

**Answer:** A constructor is a specialized function that we can use to pass initial values to our contract. In the case of `XP_Token`, we can use the constructor to pass values for the `initial_supply` of tokens, the `name`, the `symbol`, and the number of `decimals` that are associated with the token distribution.

**Question:** What’s significant about the value of 18 that leads to its selection as the `decimals` number in our constructor?

**Answer:** The smallest denomination of either is the wei. Each wei is an 18-decimal-place fraction of an ether. Also, setting the `decimals` value of `XP_Token` to 18 means that each wei can buy one `XP_Token`. This greatly simplifies the token calculation and distribution.

With the `XP_Token` contract in place, work through the process of deploying the contract by using Ganache and MetaMask.

Be sure to relaunch Ganache so that you can demonstrate the process of setting up the new Ganache accounts in MetaMask.

Pose the following questions to the students. If no one volunteers a response, provide them with the answers.

**Question:** What’s Ganache?

**Answer:** Ganache is a desktop application that developers can use to locally implement a test version of the Ethereum blockchain.

**Question:** How many times do you need to set up the Ganache network in MetaMask?

**Answer:** You need to set up the Ganache network only once in MetaMask. That’s because the RPC server location for Ganache (`HTTP://127.0.0.1:7545`) doesn’t change.

Stress that the students should import new accounts into MetaMask as opposed to adding them.

* By importing accounts, the students can control the private keys for the accounts.

* Also, they can delete imported accounts.

Take the students through the process of deleting accounts from MetaMask. Let them know that this might become valuable knowledge&mdash;because their list of Ganache accounts in MetaMask might grow quite long depending on how much testing they do.

As you set up the new Ganache accounts in MetaMask, point out how the address (especially the last four digits) that MetaMask displays for each account matches the address in Ganache.

Once the accounts have been set up in MetaMask, navigate to Remix, and then compile the `XP_Token` contract.

Deploy the contract by using the Injected Web3 environment. Be sure to add an `initial_supply` of tokens when deploying the contract.

Confirm the transaction in MetaMask when the dialog box opens. Be sure to point out the gas fee for the transaction.

Point out that this gas fee has been deducted from the ether balance of the deploying account. Also, call the `balanceOf` function to check that the balance of tokens available to the owner matches that in `initial_supply`.

Now, navigate back to Ganache, and then review the Transactions page. Point out the address that’s associated with the contract.

Demonstrate how to use this address to access the contract&mdash;even if the Remix window has been reloaded and the contract no longer appears there. You need to both compile the `XP_Token` contract and reestablish the link with MetaMask before this will work.

Confirm for the students that the contract now lives at the specified address on the Ganache test blockchain. And, it will continue to do so until the Ganache window is closed and that version of the blockchain is terminated.

Ask the students if they have any additional questions regarding the integration between MetaMask and Ganache and how we use them to test smart contract applications.

---

### 11. Instructor Do: Real-World Token Examples (15 min)

This activity is a facilitated discussion about fungible and non-fungible tokens in the current blockchain environment.

Start by reviewing the following basic questions about tokens and tokenomics:

**Question:** What things can a token represent?

**Answers:**

* Property

* Currency

* Votes

* Art

* Potentially any other store of value

**Question:** What are some common aspects of a token?

**Answers:**

* It has a fixed or an infinite supply.

* It represents a store of value.

* It can be programmed with a smart contract.

**Question:** What are some generally accepted differences between coins and tokens?

**Answers:**

* We commonly build tokens on an existing blockchain. By contrast, coins commonly make up a fundamental component of a blockchain.

* People typically use coins just as a currency for buying and selling things. By contrast, tokens have broader use cases.

* Sometimes, they don’t differ. Many people in crypto communities use the terms interchangeably.

**Question:** What are some potential benefits of tokenizing an asset on an open blockchain?

**Answers:**

* The ability to globally trade the asset without any additional infrastructure.

* The easy transfer of ownership with improvements in liquidity and auditability.

* The open blockchain benefits: open, public, borderless, censorship resistant, and neutral.

**Question:** What’s the difference between fungible and non-fungible tokens?

**Answers:**

* With fungible tokens, we ask "how many.” With NFTs, we ask "which one."

* Fungible tokens are interchangeable. That is, each token can be exchanged with another token of the same value. By contrast, NFTs are unique, per-token assets. That is, each token has its own properties and value, like artwork and legal certificates. An NFT can’t be exchanged with another NFT.

With the concepts of fungible and non-fungible tokens established, facilitate a discussion about the use of tokens in the world today, especially as it relates to finance and fintech. Encourage the students to share their understanding of fungible tokens, decentralized finance (DeFi), and even NFTs as the discussion progresses.

* Blockchain and the use of coins and tokens are changing the way that that world conducts transactions.

* Blockchain has the ability to revolutionize any industry that involves either transactions or recordkeeping. These industries include finance and investing, medicine, shipping and receiving logistics, and beyond.

* Once of the most common uses cases for fungible tokens&mdash;also known as coins or stablecoins&mdash;is finance. The term for these evolving financial systems that use fungible tokens is **decentralized finance**, or **DeFi**.

* Firms building DeFi applications use smart contract functionality to perform many traditional financial services. Rather than conducting their business by using fiat currency (such as the US dollar, the Euro, or the Chinese Yuan), DeFi applications all use blockchain tokens, coins or, most likely, stablecoins. Examples of coins are the Dai by MakerDao and the COMP by Compound. Examples of stablecoins are the Tether (USDT), the USD Coin (USDC), and the Binance USD (BUSD).

* Companies operating in the DeFi space include payments processors (such as Terra, Acala, and Ampleforth), lending firms (such as Maker, Aave, and Compound), decentralized assets exchanges (such as Uniswap, Ox, and FTX), and even decentralized derivative exchanges (such as Vega and Injective Protocol).

Encourage the students to share the names and operating spaces of any DeFi companies that they’ve explored or might be interested in working for.

* Blockchain and smart contracts underlie DeFi applications, which are anchored on the concept of **composability**. That is, fintech entrepreneurs can use the public functions of existing smart contracts to create, or compose, new smart contracts.

* Blockchain tokens are gaining popularity in areas well beyond financial services.

In this next part of the discussion, you’ll introduce the students to the concepts of utility tokens, ICOs, and crowdsales. If possible, use an example of a blockchain token that you have a particular interest in.

* [Brave](https://brave.com/) is a security- and privacy-focused internet browser that issues [Basic Attention Tokens (BATs)](https://brave.com/brave-rewards/). The goal is to revolutionize the digital advertising industry. A user earns BATs for using the Brave browsing software to surf the web or to display specific advertisements. Users can spend the BATs to buy products or to tip content creators with Brave Rewards.

* [Golem](https://www.golem.network/) is a company seeking to create an economic system that allows individuals to rent excess computing power. Participants in the network can earn [Golem tokens (GLMs)](https://www.golem.network/glm) for renting idle digital resources. Participants can then use GLM tokens to purchase computing resources when needed.

* We refer to tokens like the BAT and the GLM as **utility tokens**. People can redeem utility tokens in the future to access the product or service of the issuing company. We do not consider utility tokens as financial investments but more as blockchain-based IOUs.

* Utility tokens and other fungible tokens and coins get issued through an **initial coin offering**, or **ICO**. An ICO is a fund-raising mechanism, where new coins or tokens are offered in exchange for more-popular cryptocurrencies, like Bitcoin or ether.

* The process of conducting an ICO is called a crowdsale. A **crowdsale** is a blockchain-focused process for capitalizing or financing projects for startups or other companies. Rather than issuing shares in a company, like an initial public offering (IPO) does, an ICO issues tokens.

* Because they’re conducted on a blockchain, ICOs offer immutable contract guarantees. In some cases, they also offer quicker liquidity than other funding sources, which are often subject to a long holding period.

* More importantly, because of the nature of blockchain, ICOs democratize access to investment capital for projects that need funding. Both the capital markets and venture capital are available to only a few. But, anyone with a good idea and access to a computer can conduct an ICO.

Conclude the discussion by introducing the concept of the token crowdsale as the topic for the next class.

* In fact, the next class will focus on updating our `ArcadeToken` so that it can get distributed via a crowdsale. We’ll use the ERC-721 standard to accomplish that.

Ask the students if they have any questions about fungible tokens, the ERC-20 standard, Ganache, or MetaMask before releasing them for the day.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.