## 21.3 Lesson Plan: Crowdsales

### Overview

When we create and deploy a real-world blockchain token, minting tokens that comply with ERC-20 is only the first step. The next challenge is to distribute the tokens to other blockchain participants.

In this lesson, you’ll reinforce the students’ knowledge of crowdsales in Ethereum.

In addition to understanding how a crowdsale works, they’ll implement the `ERC20Mintable`, `Crowdsale`, and `MintedCrowdsale` contracts that allow for full crowdsale functionality with fungible tokens.

Once the token and all the required contracts have been successfully written, the crowdsale contracts will be deployed and tested by using Ganache and Metamask.

---

### Class Objectives

By the end of the class, the students will be able to:

* Detail some considerations to take into account when launching tokens via a crowdsale.

* Create a smart contract for a mintable token by using the OpenZeppelin `ERC20Mintable` contract.

* Construct an ERC-20 token crowdsale by using the OpenZeppelin `Crowdsale` and `MintedCrowdsale` contracts.

* Use a single deployer contract to create multiple contracts on a blockchain that are distinct but related.

### Slideshow and Time Tracker

* You can review the slides for this lesson on Google Drive: [Lesson 21.3 slides](https://docs.google.com/presentation/d/1-tcG0DG4sb8oFlL-jVsK26PikTn2bXoMUzVDMErmyRg/edit?usp=sharing).

* To add the slides to the student-facing repository, first download the slides as a PDF. To do that, on the **File** menu, select **Download**, and then select **PDF Document (.pdf)**. Then add the PDF file to your class repository along with other necessary files. You can review these instructions in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

  **Note:** Edit access is not available for this document. If you want to modify the slides, create a copy by selecting **Make a copy** on the **File** menu.

* You can review the Time Tracker for this lesson in the following file: [Time Tracker](TimeTracker.xlsx).

---

## Instructor Notes

* The concept of a crowdsale will be new to some students. Use as many real-world examples as possible to illustrate how a crowdsale works and why it adds value to today's fintech landscape.

* The students will use two Solidity files and three distinct contracts to deploy a crowdsale. This will form their most complicated program that uses Solidity to date. Be clear and patient when explaining how all three contracts work together to create the crowdsale.

* In a later activity (“Introducing the ArcadeToken Crowdsale”), you’ll demonstrate the functionality of the `ArcadeToken` crowdsale contracts for students. The deployment will require integrating Ganache and MetaMask with the application. It will be helpful to have Ganache open and test accounts preloaded in MetaMask before starting the demonstration. This demonstration assumes that you’ve compiled the two Solidity files and deployed the three contracts. But, you can choose to take the students through those steps at that time.

* Reassure the students that as they continue to work with Solidity, they’ll become more comfortable with using both the common patterns in the code and the OpenZeppelin library. Many of the examples that will be shown this week have been used in other smart contract applications.

* For more information about functions, refer to the [OpenZeppelin crowdsale documentation](https://docs.openzeppelin.com/contracts/2.x/crowdsales) and the GitHub pages for [ERC20 Mintable.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol), [Crowdsale.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol), and [MintedCrowdsale.sol](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol).

* **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

* Have your TAs keep track of time by using the [Time Tracker](TimeTracker.xlsx).

---

## Class Activities

### 1. Instructor Do: Crowdsales in Ethereum (15 min)

**Corresponding Activity:** None

In this initial discussion, you’ll introduce the students to the basics of the Ethereum crowdsale. The **crowdsale** is the process of raising capital by creating an initial coin offering, or ICO.

Start by welcoming the students back to class.

* In an earlier lesson, you learned about token fungibility and ERC token standards. You also implemented tokens that were compliant with the ERC-20 standard by using the OpenZeppelin library.

When we create and deploy a real-world blockchain token, minting tokens that comply with ERC-20 is only the first step. The next challenge is to distribute the tokens to other blockchain participants.

* Earlier in this unit, we learned that a blockchain company can distribute tokens via an ICO, which functions much like a traditional IPO. In an ICO, a company sells blockchain tokens that represent an asset or utility that’s relevant to its platform; equity in the company; the promise of a future payment, good, or service; or another form of value.

* In essence, an ICO uses the democratizing features of blockchain to raise the capital that’s needed to support an emerging company or idea.

* But, how does an ICO work from a technical standpoint?

* Smart contract technology, called crowdsales, often power ICOs. A **crowdsale** is defined as a method of funding a project through the sale of digital tokens that give the buyers the right to participate in the idea that the sale is funding.

* Essentially, a crowdsale allows investors to send cryptocurrency to a smart contract and receive tokens in return.

* The crowdsale is a popular method for selling blockchain tokens on the market. Given the functionality of smart contracts, many crowdsales take place on the Ethereum blockchain.

#### Crowdsale Considerations

In this section, you’ll compare the concept of crowdfunding to crowdsales. You’ll also highlight some considerations to take into account when conducting a crowdsale.

* Young companies and startups are often full of innovative new ideas, but executing those ideas can prove expensive.

* Over the last decade, crowdfunding has become a popular way for companies to receive funding that enables them to successfully bring their product or service to production.

* **Crowdfunding** is the process of raising funds by asking a large number of people to each contribute a small amount of money. Usually, those who donate or invest funds in the cause receive the promise of a certain product, service, return on investment, or share in the company in exchange.

* Crowdfunding is often done through an online platform like [Indiegogo](https://www.indiegogo.com/), [StartEngine](https://www.startengine.com/2), or [GoFundMe](https://www.gofundme.com/). In these cases, users are promised a product or service and can then donate money to a particular project in a streamlined manner.

* Blockchain technologies and the rise of tokenomics has enabled a new form of crowdfunding that’s conducted over a blockchain platform. This is known as a crowdsale.

* Unlike in traditional crowdfunding, backers funding the project don’t get promised a particular product or service directly. Instead, they get promised a certain number of tokens at a set price.

* The tokens sold during the crowdsale can then serve as a way for users to take part in the product or service that the company is planning to launch.

* For what purposes might companies running on a blockchain platform use the funds that they raise during a crowdsale? Some possibilities include:

  * Marketing funds

  * Payments to developers

  * Product development

  * Product production

  * Any other initial operating costs

Depending on the student engagement and knowledge of the topic, ask if any students have participated in a crowdsale and if they’re willing to describe the experience.

Shift from the overall concept of crowdsales to the role that tokenomics plays in the process of executing a crowdsale.

* Tokenomics plays an important role in crowdsales.

* Investors backing a crowdsale project might purchase tokens because they believe that the project will succeed. But, they might purchase tokens because they believe that the tokens themselves will increase in value&mdash;even if the project fails.

* For example, recall the cryptokitty tokens that were mentioned earlier in the unit. Even if the CryptoKitties company went out of business, the cryptokitty tokens would remain on the blockchain and could continue to hold their value and be traded.

* Important factors to consider when developing tokens for a crowdsale include:

  * The price and rate configuration of the tokens, which include the following:
  
    - Whether to offer the tokens at a fixed price.

    - Whether to **cap**, or limit, the total number of released tokens.

    - Whether to cap the total number of tokens that a single individual can buy.

  * How to send tokens to crowdsale investors.

  * The time frame associated with the sale&mdash;that is, when the crowdsale will start and when it will end.

  * Whether to distribute the funds that get raised by selling tokens during or after the crowdsale.

  * Whether to have a refund policy if you don’t successfully reach the ultimate goal of the project.

Explain that when implementing a crowdsale, you must first decide how to release tokens to the participants in the sale.

* This process of releasing tokens is known as **token emission**. We normally do this in one of three ways:

  * The crowdsale contract owns a specified number of tokens and transfers ownership of them as users purchase them.

  * The crowdsale contract dynamically mints new tokens as they get purchased.

  * The crowdsale contract has access to a wallet from which it can transfer ownership of tokens as they get purchased.

Mention that it’s also important to consider regulatory factors when making decisions regarding a crowdsale.

* As with IPOs, the US Securities and Exchange Commission (SEC) has regulatory requirements for ICOs in the United States.

* For the activities in this program, we don’t need to be concerned with these regulations. This is because we’ll deploy tokens only on our local network for educational purposes.

* But if you ever launch a real crowdsale across a live blockchain, you must ensure that your crowdsale complies with all the relevant regulations.

Have a TA slack out the link to the SEC ICO webpage for those that might be interested.

* For those who are interested, you can find more information about this on the [Spotlight on Initial Coin Offerings (ICOs)](https://www.sec.gov/ICO) SEC page.

Explain that with all these factors (purpose, timing, distribution, and regulation) now being taken into consideration, it’s time to explore how to prepare a token for a crowdsale on the Ethereum blockchain.

---

### 2. Instructor Do: Preparing a Token for a Crowdsale (15 min)

**Corresponding activity:** [Preparing a Token for a Crowdsale](Activities/01-Ins_Preparing_a_Token_for_a_Crowdsale)

**Files:**

[Starter file](Activities/01-Ins_Preparing_a_Token_for_a_Crowdsale/Unsolved/ArcadeTokenMintable.sol)

[Solution file](Activities/01-Ins_Preparing_a_Token_for_a_Crowdsale/Solved/ArcadeTokenMintable.sol)

In this activity, you’ll introduce the students to the code that’s needed to prepare a token for a crowdsale.

You’ll continue building the code associated with the `ArcadeToken` contract that was created earlier in the unit.

Use the starter file, and live code the demonstration for the students.

Start this activity by explaining to the students that OpenZeppelin also supplies the code that’s needed to prepare the ERC-20 `ArcadeToken` for a crowdsale.

* In the previous lesson, we used OpenZeppelin to leverage contracts that implement the common ERC-20 standard.

* Similarly to how we imported the code for the ERC-20 standard into our `ArcadeToken` contract, we can use other code from OpenZeppelin to help us mint and issue tokens for a crowdsale.

* In the case of `ArcadeToken`, the decision regarding the token emission has been made to dynamically mint new tokens as they get purchased.

* We’ll streamline the crowdsale creation process by creating a smart contract that can automatically mint tokens when a user sends it ether. Anyone who wants to to purchase the `ArcadeToken` in the crowdsale can send ether to the contract from their account address. Then, the contract will automatically mint and send tokens to them in return.

* As we found in the earlier lesson, we create the initial `ArcadeToken` contract by importing the `ERC20` and `ERC20Detailed` contracts, as the following code shows:

  ```solidity
  pragma solidity ^0.5.0;

  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
  ```

#### Add ERC20Mintable

* To provide our contract with all the functionality that it needs for a crowdsale, we’ll now import one more contract from the OpenZeppelin library: `ERC20Mintable`.

Have a TA slack out the links to the [OpenZeppelin crowdsale docs](https://docs.openzeppelin.com/contracts/2.x/crowdsales) and the [ERC20Mintable.sol GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol) so that the students can reference them as needed.

* With this contract, we can inherit code that helps manage those accounts that can mint new tokens. Specifically, this contract creates a `MinterRole` that’s associated with the `mint` function of the `ERC20` contract.

* The following code imports the `ERC20Mintable` contract:

  ```solidity
  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
  ```

* In an earlier lesson, we created an `ArcadeToken` contract that inherited the code from the `ERC20` and `ERC20Detailed` contracts by using the `is` keyword, as the following code shows:

  ```solidity
  contract ArcadeToken is ERC20, ERC20Detailed {
  }
  ```

* Now, we want our contract to also inherit the code from `ERC20Mintable`. So, we add that contract to the `is` statement, as the following code shows:

  ```solidity
  contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
  }
  ```

At this point, the `ArcadeToken` contract file should appear as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
}
```

Explain that when we save the `ArcadeToken.sol` file, Remix will automatically save the `ERC20Mintable.sol` contract and make it available.

In the Remix IDE, in the File Explorers pane, navigate to the `ERC20Mintable.sol` file. Then show the students the information that the file contains.

* Notice that the code of this this contract includes a `mint` function and a `MinterRole`, which adds functionality to the minter accounts.

* By default, when the constructor gets called on deployment of the contract, the account that deploys the contract is the only minter. (We’ll add the constructor shortly.)

* The `ERC20Mintable` code also provides an `onlyMinter` modifier. This modifier restricts the `mint` function so that only accounts with the `MinterRole` can call it.

* Because we imported and inherited this contract by using the `is ERC20Mintable` statement, we can now use these standards to enhance our `ArcadeToken` contract.

#### Add the Constructor Function

In this section, you’ll add the constructor function with the required parameters to the new `ArcadeToken` contract, as the following code shows:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
}
```

* As we did previously, we first add a constructor for the `ArcadeToken` contract.

* The constructor accepts a string `name`, a string `symbol`, and a `uint` that represents the `initial_supply` of tokens.

* When we deploy the contract, we’ll supply values for these parametersin the Remix IDE.

#### Incorporate the ERC20Detailed Constructor

Next, you’ll incorporate the `ERC20Detailed` constructor into the token constructor function, as the following code shows:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
 }
 ```

* Recall from an earlier lesson that because our `ArcadeToken` contract inherits `ERC20Detailed`, we must also call the constructor of `ERC20Detailed`.

* That constructor has three required parameters: `name`, `symbol`, and `decimals`. We’ll continue to use the Ethereum default of 18 decimal places to facilitate the conversion from tokens to ether. Remember that Ethereum defaults to 18 decimal places because one ether equals 10&Hat;18, or 1,000,000,000,000,000,000, wei.

* We make this function public so that the information that’s defined inside it is available for all.

#### Define the ArcadeToken Contract Body

In this section, you’ll define the main body of the `ArcadeToken` contract, as the following code shows:

```solidity
contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        mint(msg.sender, initial_supply);
    }
}
```

* Finally, it's time to define the body of the contract.

* Inside the body, we call the `mint` function of `ERC20Mintable`and pass it the `msg.sender` attribute and the `inital_supply` parameter that our constructor defines.

* Now, when our `ArcadeToken` contract gets deployed, it calls the `mint` function, passing it the current `msg.sender` and our defined `inital_supply`.

* We no longer have to write the `mint` function ourselves, because the `ERC20Mintable` contract now makes it available to us via inheritance.

* Inheriting the `ERC20Mintable` code adds some functionality to our `ArcadeToken` contract that the crowdsale will later need. We’ll explore this further in the following sections as we start to code our crowdsale contracts.

The complete code now appears as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        mint(msg.sender, initial_supply);
    }
}
```

Tell students that in the next activity, they’ll code and deploy their own mintable token that will be ready for a crowdsale!

---

### 3. Student Do: XP_Token Mintable (20 min)

**Corresponding activity:** [XP_Token Mintable](Activities/02-Stu_XP_Token_Mintable)

**Files:**

[Instructions](Activities/02-Stu_XP_Token_Mintable/README.md)

[Starter file](Activities/02-Stu_XP_Token_Mintable/Unsolved/XPTokenMintable.sol)

Have a TA slack the preceding two files out to the students so that they can complete the required steps.

In this activity, the students will generate the code for the `XP_Token` contract.

This contract will inherit functionality from the OpenZeppelin `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts.

---

### 4. Instructor Do: Review XP_Token Mintable (10 min)

**Corresponding activity:** [XP-Token Mintable](Activities/02-Stu_XP_Token_Mintable)

**Files:**

[Instructions](Activities/02-Stu_XP_Token_Mintable/README.md)

[Starter file](Activities/02-Stu_XP_Token_Mintable/Unsolved/XPTokenMintable.sol)

[Solution file](Activities/02-Stu_XP_Token_Mintable/Solved/XPTokenMintable.sol)

In this activity, you’ll generate the code for the `XP_Token` contract. This contract will inherit functionality from the OpenZeppelin `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts.

Focus the review of the activity on the changes to the constructor function since the earlier lesson.

You can use the following video as a basis for this activity review. Note that although the video refers to the `ArcadeToken` contract, the content of the review is the same.

[Arcade Mintable Token Solution Walkthrough](https://fast.wistia.net/embed/iframe/8305xnff4v)

Live code the review for students if possible.

Start the review by creating the pragma version statement and the `import` statements for the `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
```

Pose the following questions to the students. If no one volunteers a response, provide them with the answers.

**Question:** Where can you review the functions that each of the three OpenZeppelin contracts contains? Name two places.

**Answer:** You can navigate to the GitHub page for each of the contracts to review the contained code. Once the contract is compiled, you can also go to the File Explorers pane in the Remix IDE and navigate through the folder structure until you get to the specified Solidity contract files.

**Question:** What function does the `ERC20Mintable` contract contain?

**Answer:** The `ERC20Mintable` contract contains a `mint` function. Additionally, this contract establishes a `MinterRole`. The role will control who will be able to mint tokens for the contract.

Next, create the `XP_Token` contract, as the following code shows (and reference each of the three OpenZeppelin contracts being used):

```solidity
contract XP_Token is ERC20, ERC20Detailed, ERC20Mintable {

}
```

**Question:** What’s the term for what allows the `XP_Token` contract to use functionality from each of the three OpenZeppelin contracts?

**Answer:** The term is **inheritance**. The `XP_Token` contract inherits functionality from each of the OpenZeppelin contracts via the `is` keyword.

Establish the constructor function, and assign it the three attributes that will get defined when the contract is first deployed, as the following code shows:

```solidity
contract XP_Token is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
}
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** Think back to the earlier lesson. What additional attributes are we adding to this constructor function, and when will they get defined?

**Answer:** In addition to the `initial_supply` attribute, we’re adding attributes for `name` and `symbol`. By adding these attributes to the main constructor function, we’ll be able to dynamically define these values when the contract gets deployed.

Add the `ERC20Detailed` constructor, as the following code shows:

```solidity
contract XP_Token is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
}
```

* We make the `ERC20Detailed` constructor function public to make this information available to anyone who interacts with the `XP_Token` contract.

Finally, add the `mint` function to the `XP_Token` contract, as the following code shows:

```solidity
contract XP_Token is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        mint(msg.sender, initial_supply);
  }
}
```

Pose the following question to the students. If no one volunteers a response, provide them with the answer.

**Question:** Our contract inherits the `mint` function from which of the `ERC20` contracts?

**Answer:** Our contract inherits the `mint` function from the `ERC20Mintable` contract. (The `mint` function requires that we specify parameters for an address and an amount. In this case, the address is the `msg.sender` or whoever asks to mint tokens. And, the amount is the `initial_supply` of tokens.)

* It’s important to note that the `ERC20Mintable` contract specifies that the user who makes the request to mint tokens must have the `MinterRole`. At the construction of the contract, the only minter is the deployer.

Compile the `XP_Token` contract, and debug any errors that arise.

Let the students know that we won’t work through deploying the contract until we add some additional crowdsale functionality (although it’s possible to do so sooner).

Before moving on to the next activity, ask the students if they have any additional questions about the `XP_Token` contract as it currently stands.

---

### 5. Instructor Do: Introducing the ArcadeToken Crowdsale (15 min)

**Corresponding activity:** [Crowdsales](Activities/03-Ins_Crowdsales)

**Files:**

[Solution file - ArcadeTokenMintable](Activities/03-Ins_Crowdsales/Solved/ArcadeTokenMintable.sol)

[Solution file - ArcadeTokenCrowdsale](Activities/03-Ins_Crowdsales/Solved/ArcadeTokenCrowdsale.sol)

In this section, you’ll introduce and demonstrate creating the `ArcadeToken` crowdsale smart contract by using the OpenZeppelin library. You’ll first give a short lecture to set the stage for creating the crowdsale contract. You’ll then do a full demonstration of what you’ll build. This demonstration will set the context for the code demonstration that follows.

**Instructor Note:** The `Solved` folder contains two Solidity files. One contains the mintable token contract. The other contains the code for the crowdsale contracts. You’ll need to compile both files and deploy the `ArcadeToken` crowdsale contract for the demonstration.

Start by explaining that distributing tokens via a crowdsale requires more than the token contract. We need to design a contract that can mint tokens by itself whenever a user wants to participate by sending ether.

* To create a crowdsale for our mintable arcade token, we’ll create a new smart contract that can mint tokens by itself whenever a user sends ether to the contract. (That is, the contract rather than the contract owner will mint the tokens.)

Navigate to the [Crowdsales page](https://docs.openzeppelin.com/contracts/2.x/crowdsales) in the OpenZeppelin documentation, and then scroll through the page.

Explain that we’ll create a relatively simple crowdsale contract in this lesson. But, the code that OpenZeppelin makes available via its crowdsale contracts includes a wide variety of features and functionality that help facilitate token sales.

* In addition to having the `ArcadeToken` contract that handles the initial minting, we’ll create a contract named `ArcadeTokenCrowdsale` to oversee the crowdsale functionality.

* This crowdsale contract will inherit functionality, once again, from contracts that OpenZeppelin makes publically available. Specifically, we’ll use the [OpenZeppelin Crowdsale contract](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol) and the [OpenZeppelin MintedCrowdsale contract](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol).

Have a TA slack out the links to the [OpenZeppelin Crowdsale contract](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol) and the [OpenZeppelin MintedCrowdsale contract](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol) to the students for their review.

* We’ll also create one more contract in addition to the `ArcadeToken` and `ArcadeTokenCrowdsale` contracts. This contract will be able to create, configure, and deploy both our `ArcadeToken` contract and our `ArcadeTokenCrowdsale` contract. We’ll name this deployer contract `ArcadeTokenCrowdsaleDeployer`.

* We could manually deploy the token and crowdsale contracts. But, we’ll use the deployer contract to avoid manually calling all the functions and setting all the roles that our other two contracts contain. During deployment, `ArcadeTokenCrowdsaleDeployer` will create the other two contracts and temporarily assume both the contract owner and minter roles. After `ArcadeTokenCrowdsaleDeployer` successfully sets up our crowdsale, it will transfer the owner and minter roles to `ArcadeTokenCrowdsale`.

* By inheriting `ERC20Mintable`, we added minting functionality, including the `MinterRole`, to our `ArcadeToken` contract. With this functionality, our deployer contract can assume the role of minter and then transfer that role. That’s one reason why we enhanced our `ArcadeToken` contract with the `ERC20Mintable` contract before setting up our crowdsale.

Now, you’ll work through the process of demonstrating the functionality of the combined `ArcadeToken` contracts.

For the demonstration, you should have already compiled and deployed the contracts in conjunction with Ganache and MetaMask. It’s best to have three addresses loaded into MetaMask: one for the deployment and two to act as crowdsale participants.

When demonstrating the functionality, be sure to navigate to a different MetaMask account than the one that you used to deploy the contracts.

You can use the following walkthrough video as a basis for your comments about the functionality of this application. Feel free to play around with the application prior to class and to expand the demonstration beyond what the video and the instructions that follow detail.

[ArcadeToken Deployed and Operational Demo Video](https://fast.wistia.net/embed/iframe/edq5lh4ygm)

* Before we explore how to create each of these new crowdsale contracts, let’s review what we want for the end result. This way, we’ll know what we’re working towards.

* We’ll assume the role of investors in the crowdsale. The goal is to purchase tokens that get issued in the crowdsale by using ether.

Start by copying the selected address of the crowdsale participant onto the clipboard.

Next, input a value into the `Value` box and the number of wei that’s associated with the number of tokens to purchase.

In the deployed `ArcadeTokenCrowdsale` contract, paste the address of the crowdsale participant into the `buyTokens` box.

A MetaMask dialog box opens, asking you to confirm the transaction. Confirm it.

Then, navigate to the `ArcadeToken` contract, and paste the participant address into the `balanceOf` box. Clicking the `balanceOf` button should not reveal a number of tokens matching the number of wei that you specified in the `Value` box.

Navigate back to the `ArcadeTokenCrowdsale` contract, and then click the `weiRaised` button. Now, the number should match both the `Value` and `balanceOf` numbers.

Copy a different address from MetaMask, and then purchase a different number of tokens. To do that, enter a new number in the `Value` box, paste the address into the `buyTokens` box, and then click `buyTokens`.

Although the `balanceOf` number should match the `Value` number of purchased tokens, a check of the `weiRaised` balance will show the sum of the values that the two accounts purchased.

Navigate to the `ArcadeToken` contract, and then point out the values for `name`, `symbol` and, now, `totalSupply`.

Once you’ve demonstrated the application, ask the students if they have any questions about the functionality before beginning the process of creating the contracts.

Confirm for the students that you’ll take them through the process of building and deploying the contracts step by step.

---

### 6. Instructor Do: Building Crowdsales with OpenZeppelin (20 min)

**Corresponding activity:** [Crowdsales](Activities/03-Ins_Crowdsales)

**Files:**

[Starter file - ArcadeTokenMintable](Activities/03-Ins_Crowdsales/Unsolved/ArcadeTokenMintable.sol)

[Starter file - ArcadeTokenCrowdsale](Activities/03-Ins_Crowdsales/Unsolved/ArcadeTokenCrowdsale.sol)

[Solution file - ArcadeTokenMintable](Activities/03-Ins_Crowdsales/Solved/ArcadeTokenMintable.sol)

[Solution file - ArcadeTokenCrowdsale](Activities/03-Ins_Crowdsales/Solved/ArcadeTokenCrowdsale.sol)

In this section, you’ll work through the code that’s required to create the `ArcadeToken` crowdsale.

**Instructor Note:** The `Unsolved` and `Solved` folders each contain two Solidity files. One contains the mintable token contract. The other contains the code for the crowdsale contracts. You’ll need both files to deploy the entire crowdsale.

Start this activity by once again highlighting the role of OpenZeppelin in creating crowdsale smart contracts that use ERC-20 standards.

For student reference, ask a TA to slack out the link to the [OpenZeppelin Crowdsale constructor API documentation](https://docs.openzeppelin.com/contracts/2.x/api/crowdsale#Crowdsale-constructor-uint256-address-payable-contract-IERC20-).

* The OpenZeppelin Contracts library provides various crowdsale-related contracts. With these contracts, we can configure the following contract elements (among many others):

  * The token price and the exchange rate (that is, the amount of ether that one token costs).

  * The total number of tokens that can be sold during the crowdsale.

  * Restrictions on who can make purchases during the crowdsale to comply with **know-your-customer (KYC)** and **anti&ndash;money laundering (AML)** regulations. KYC and AML regulations are government regulations that require financial institutions to learn certain information about their customers and the origins of the money that they store and handle. These regulations are designed to prevent entities from illegally using or hiding money.

  * When and how the distribution of funds will occur.

  * The time limits for the sale.

* To set up our arcade token crowdsale, we’ll use the OpenZeppelin [Crowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol) and [MintedCrowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol) contracts. These two contracts contain useful features and code that we can inherit and then use.

Explain that we’ll use these OpenZeppelin contracts to code the `ArcadeTokenCrowdsale` contract.

#### ArcadeTokenCrowdsale Contract

Open the [ArcadeTokenCrowdsale.sol starter file](Activities/03-Ins_Crowdsales/Unsolved/ArcadeTokenCrowdsale.sol). Then begin to code the `ArcadeTokenCrowdsale` contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "./ArcadeTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {

}
```

* To create the `ArcadeTokenCrowdsale` contract, we’ll first import the mintable `ArcadeToken` contract created earlier in today's lesson. This is so that our crowdsale contract can mint the tokens that `ArcadeToken` creates.

* Next, by using the `is` keyword, the `ArcadeTokenCrowdsale` contract will inherit the functionality of the OpenZeppelin `Crowdsale` and `MintedCrowdsale` contracts.

Next, add a constructor to the `ArcadeTokenCrowdsale` contract that accepts the same parameters as the constructor of the OpenZeppelin `Crowdsale` contract.

Navigate to the [Crowdsale.sol GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol), and then show the students the constructor function.

* We’ll use the contract's constructor to call the `Crowdsale` constructor with the same parameters, as the following code shows:

  ```solidity
  contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
      constructor(
          uint rate,
          address payable wallet,
          ArcadeToken token
      )
          Crowdsale(rate, wallet, token)
          public
      {
          // constructor body can stay empty
      }
  }
  ```

* The OpenZeppelin `Crowdsale` constructor requires three parameters. (Note that we’ll set the values for these parameters in the Remix IDE on deployment of the contract.)

* The first parameter, `rate`, is the conversion rate between our token and the ether currency.

  * Because our code performs all transaction calculations with the smallest possible units of currency, the `rate` is really the conversion rate between one bit of our token and one wei. Remember that a bit is the smallest unit of a token. Because our arcade token, ARCD, has 18 decimal places, 1 bit of ARCD equals 1/10&Hat;18 of an ARCD token.

  * Today, we’ll keep our exchange rate simple and set a value of 1 for the `rate`. Because both ARCD and ether have 18 decimal places, 1 ARCD bit costs 1 wei&mdash;and 1 ARCD token costs 1 ether.

  > **Instructor Note:** For students that inquire, this exchange rate differs from the one that we originally set for the first version of the arcade token contract. We’re changing the rate today to simplify the exchange rate calculation.

* The second parameter, `wallet`, is the account address where all the ether that the crowdsale raises will go.

  * In this case, our tokens will raise funds for the arcade. So, we set this parameter to the main wallet address of the arcade owner (who is also the contract deployer).

* The third parameter, `token`, defines the token that this crowdsale contract will launch. In this case, we set our `ArcadeToken` contract as the value for `token`. This will allow the `ArcadeTokenCrowdsale` contract to interact with `ArcadeToken` and to mint new tokens once the contracts exist on the blockchain.

* The constructor functions will allow `ArcadeTokenCrowdsale` to initialize all the variables that the `Crowdsale` contract requires.

* Finally, the body of the constructor can stay empty. This is because the `Crowdsale` and `MintedCrowdsale` contracts that `ArcadeTokenCrowdsale` inherited already contain all the logic.

Explain that we need to create one more contract in our file: `ArcadeTokenCrowdsaleDeployer`.

#### The ArcadeTokenCrowdsaleDeployer Contract

Just after the `ArcadeTokenCrowdsale` contract, create the code for `ArcadeTokenCrowdsaleDeployer` as follows:

```solidity
contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
  // ...
}

contract ArcadeTokenCrowdsaleDeployer {

}
```

Explain the `ArcadeTokenCrowdsaleDeployer` contract in the following way:

* We’ll use the `ArcadeTokenCrowdsaleDeployer` as a temporary helper contract that will help us set up, configure, and deploy our `ArcadeToken` and `ArcadeTokenCrowdsale` contracts with all the correct information.

* After the deployment and initial setup of our crowdsale, `ArcadeTokenCrowdsaleDeployer` will turn control of the crowdsale over to `ArcadeTokenCrowdsale`.

* The deployer contract will create our new `ArcadeToken` and `ArcadeTokenCrowdsale` contracts by calling the constructor functions of those contracts.

Explain that before that happens, however, we must accomplish one more step. We need to account for the addresses that get assigned to both the `ArcadeToken` and `ArcadeTokenCrowdsale` contracts, as the following code shows:

```solidity
contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
  // ...
}

contract ArcadeTokenCrowdsaleDeployer {

    address public arcade_token_address;
    address public arcade_crowdsale_address;

}
```

* When the `ArcadeToken` and `ArcadeTokenCrowdsale` contracts get deployed, they’ll each get assigned an address on the blockchain. This is so that they can mint and distribute tokens and receive ether from purchasers.

* We need to keep track of these contract addresses. So, we’ll first create two new public `address` variables inside the deployer contract. (We’ll make them public to make them accessible from an application like Remix.) Later, we’ll assign the contract addresses to these variables.

Next, create the public constructor function that’s associated with the `ArcadeTokenCrowdsaleDeployer` contract, as the following code shows:

```solidity
contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
  // ...
}

contract ArcadeTokenCrowdsaleDeployer {

    address public arcade_token_address;
    address public arcade_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
}
```

* With the address variables in place, we add a constructor function to the deployer contract that accepts `name`, `symbol`, and `wallet` values.

* When we deploy `ArcadeTokenCrowdsaleDeployer`, this constructor function will use the values that we supply here and the `ArcadeToken` and `ArcadeTokenCrowdsale` constructors to create those two contracts.

Next, create the `ArcadeToken` contract within the constructor function of the deployer, as the following code shows:

```solidity
contract ArcadeTokenCrowdsale {
  // ...
}

contract ArcadeTokenCrowdsaleDeployer {

    address public arcade_token_address;
    address public arcade_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
    }
}
```

* We create `ArcadeToken` within the constructor function.

* Just as we did in the `Crowdsale` contract, we store `ArcadeToken` in a variable named `token`.

* We pass in `name`, `symbol`, and `initial_supply` parameters.

* We set `initial_supply` to 0. That’s because this deployer contract will just initialize and configure our contracts. It will then turn over the minting capabilities to the `Crowdsale` contract. We designed that contract to mint new tokens on demand, so we don’t need an initial supply.

* Notice that the syntax that creates `ArcadeToken` uses the `new` keyword. This keyword allows a contract to create another contract. In this case, it allows the `ArcadeTokenCrowdsaleDeployer` contract to create the `ArcadeToken` contract.

Explain to the students that the deployer contract and the crowdsale contract both have a variable named `token` of type `ArcadeToken`. The deployer contract will create a new token by using the values that we supply for `name`, `symbol`, and `initial_supply`. It will later pass this object into the crowdsale contract. There, the object will get assigned to the `token` variable that we created in the crowdsale contract. The crowdsale contract will accept the `token` object because our token meets ERC-20 standards. If it didn’t, the crowdsale contract would return an error.

Next, store the token’s address in the public variable that you previously set up for this purpose, as the following code shows:

```solidity
contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint rate,
        address payable wallet,
        ArcadeToken token
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor body can stay empty
    }
}

contract ArcadeTokenCrowdsaleDeployer {
    address public arcade_token_address;
    address public arcade_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
        arcade_token_address = address(token);
    }
}
```

* Finally, we store the address of `ArcadeToken`in the public variable named `arcade_token_address` that we previously set up for this purpose.

* Now, the `ArcadeTokenCrowdsaleDeployer` contract can create the `ArcadeToken` contract (and thus our arcade token) on deployment.

Ask the students if they have any questions about how both the `ArcadeTokenCrowdsale` and `ArcadeTokenCrowdsaleDeployer` contracts are using the original `ArcadeToken` contract. Find out if any students are willing to explain how the process works.

If no one volunteers, use both Solidity files to follow the `ArcadeToken` contract through the code.

Once you feel that the students grasp the flow of the `ArcadeToken` contract, explain that the deployer contract also needs to create the `ArcadeTokenCrowdsale` contract (and thus our crowdsale) on deployment, as the following code shows:

```solidity
contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
    // ...
}
contract ArcadeTokenCrowdsaleDeployer {
    address public arcade_token_address;
    address public arcade_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
        arcade_token_address = address(token);

        ArcadeTokenCrowdsale arcade_crowdsale = new ArcadeTokenCrowdsale(1, wallet, token);
        arcade_crowdsale_address = address(arcade_crowdsale);
    }
}
```

* We use a similar process to create `arcade_crowdsale`. We set the `arcade_crowdsale` variable of type `ArcadeTokenCrowdsale` equal to our `ArcadeTokenCrowdsale` contract.

* We pass the `rate`, `wallet`, and `token` parameters to the new contract. (Remember that we use 1 for `rate` so that we can exchange 1 token for 1 ether.)

* Once again, we use the `new` keyword to allow the deployer contract to create another contract.

* Finally, we store the address of the crowdsale contract in the variable that we set up earlier.

Explain that the last step is to allow `ArcadeTokenCrowdsaleDeployer` to pass minting authority over to `ArcadeTokenCrowdsale` after deployment, as the following code shows:

```solidity
contract ArcadeTokenCrowdsale is Crowdsale, MintedCrowdsale {
    // ...
}
contract ArcadeTokenCrowdsaleDeployer {
    address public arcade_token_address;
    address public arcade_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        ArcadeToken token = new ArcadeToken(name, symbol, 0);
        arcade_token_address = address(token);

        ArcadeTokenCrowdsale arcade_crowdsale = new ArcadeTokenCrowdsale(1, wallet, token);
        arcade_crowdsale_address = address(arcade_crowdsale);

        token.addMinter(arcade_crowdsale_address);
        token.renounceMinter();
    }
}
```

* Remember that `msg.sender` is the default minter when we deploy `ERC20Mintable` tokens (which `ArcadeToken` now is).

* The `ArcadeTokenCrowdsaleDeployer` contract is the `msg.sender` when we create the token.

* This makes `ArcadeTokenCrowdsaleDeployer` the default minter. But, we want only the crowdsale contract to control the minting. So, we need to make the `ArcadeTokenCrowdsale` a minter and renounce the minter role from `ArcadeTokenCrowdsaleDeployer` at the end of the constructor.

* Because the `ArcadeTokenCrowdsale` contract will now be responsible for minting and distributing tokens, we can remove the `mint` function from the `ArcadeToken` contract.

* In fact, because we were minting to `msg.sender`, keeping the `mint` function here would cause us to lose tokens. This is because the `ArcadeTokenCrowdsaleDeployer` contract initially creates the `ArcadeToken`. So, `msg.sender` would be the address of the `ArcadeTokenCrowdsaleDeployer` contract. Because that contract has no function to withdraw tokens, they’d get **burned** (or lost) from the usable supply.

* Note that we could add a withdrawal function to `ArcadeTokenCrowdsaleDeployer`/ But, that’s unnecessary and would ultimately use more energy. Therefore, it would cost us more gas on the Ethereum blockchain. Instead, we’ll have `ArcadeTokenCrowdsale` mint tokens on demand and deliver them directly to the specified recipients.

* To remove the `mint` function from `ArcadeToken`, we navigate back to that contract and remove the `mint` call that the constructor contains.

Navigate back to the [ArcadeTokenMintable.sol starter file](Activities/03-Ins_Crowdsales/Unsolved/ArcadeTokenMintable.sol) and the `ArcadeToken` contract, and then remove the `mint` function.

The complete `ArcadeToken` contract now appears as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract ArcadeToken is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        // constructor can stay empty
    }
}
```

Explain to the students that all the necessary code is now in place for launching the `ArcadeToken` crowdsale.

Ask the students if they have any immediate questions about what they just observed regarding the `ArcadeToken`, `ArcadeTokenCrowdsale`, and `ArcadeTokenCrowdsaleDeployer` contracts.

Assure them that it will all make more sense as you work through the process of deploying and testing the code.

Give the students two options. They can digest what they learned over the break and then go through the deployment activity on their return. Or, they can go through the deployment activity now and take the break after.

---

### 7. Break (40 min)

---

### 8. Instructor Do: Deploying the ArcadeToken Crowdsale (15 min)

**Corresponding activity:** [Crowdsales](Activities/03-Ins_Crowdsales)
**Files:**

[Starter file - ArcadeTokenMintable](Activities/03-Ins_Crowdsales/Unsolved/ArcadeTokenMintable.sol)

[Starter file - ArcadeTokenCrowdsale](Activities/03-Ins_Crowdsales/Unsolved/ArcadeTokenCrowdsale.sol)

[Solution file - ArcadeTokenMintable](Activities/03-Ins_Crowdsales/Solved/ArcadeTokenMintable.sol)

[Solution file - ArcadeTokenCrowdsale](Activities/03-Ins_Crowdsales/Solved/ArcadeTokenCrowdsale.sol)

In this section, you’ll work through the process of deploying and testing the `ArcadeToken` crowdsale.

**Instructor Note:** The `Unsolved` and `Solved` folders each contain two Solidity files. One contains the mintable token contract. The other contains the code for the crowdsale contracts. You’ll need both files to deploy the entire crowdsale.

To successfully conduct this demonstration, you need to refresh the Remix IDE. This removes the previously deployed versions of the code that you used earlier to demonstrate the functionality of the application.

Although you’ve likely already completed this step, you need to launch Ganache and load accounts into MetaMask.

It might also help to have the solved versions of both the `ArcadeTokenMintable.sol` and the `ArcadeTokenCrowdsale.sol` contracts open and compiled in Remix.

You can use the following walkthrough video as the basis for this demonstration:

[Deploying and Launching the ArcadeToken Crowdsale](https://fast.wistia.net/embed/iframe/929kyjgd0o)

Depending on the order of activities, welcome the students back to class.

If they’ve taken a break, ask them if they’ve come up with any questions regarding the code for the `ArcadeTokenCrowdsale` and `ArcadeTokenCrowdsaleDeployer` contracts during their break.

They’ll likely have new questions from the additional time to digest all the information that the previous activity detailed.

Once you’ve answered all the questions, proceed to the process of deploying the `ArcadeToken`, `ArcadeTokenCrowdsale`, and `ArcadeTokenCrowdsaleDeployer` contracts.

Start by confirming for the students that you’ve launched Ganache and loaded several accounts into MetaMask. Additionally, you’ve opened and compiled the complete versions of both the `ArcadeTokenMintable.sol` and `ArcadeTokenCrowdsale.sol` contracts in Remix.

Begin the deployment demonstration by navigating to the **Deploy & Run Transactions** pane in the Remix IDE.

Make sure that you select **Injected Web3** as the environment and choose one of the MetaMask account addresses.

Deploy the `ArcadeTokenCrowdsaleDeployer` contract first.

* By deploying the `ArcadeTokenCrowdsaleDeployer` contract first, we can launch the token and crowdsale contracts and configure them appropriately.

Next, fill in the values for `name` (ArcadeToken), `symbol` (ARCD), and `wallet` (the account address that’s selected, which appears at the top of the page).

* The values that we input at the time of deploying `ArcadeTokenCrowdsaleDeployer` are all parameters that the constructor function specified.

* The selected wallet will be the beneficiary of the sale&mdash;that is, the owner of the contract.

When you click the **transact** button, MetaMask opens a dialog box that requires you to confirm the transaction.

Explain that the `ArcadeTokenCrowdsaleDeployer` contract creates the crowdsale and token contracts and launches them.

In the **Deploy & Run Transactions** pane, scroll down to where the deployed `ArcadeTokenCrowdsaleDeployer` contract is listed, and point out the buttons that are associated with `arcade_crowdsale_address` and `arcade_token_address`, as the following image shows:

![A screenshot points out the arcade_crowdsale_address and arcade_token_address buttons.](Images/arcd-deployer-addresses.png)

* Per the code, the `ArcadeTokenCrowdsaleDeployer` contract created two contracts, each with an associated address. The `arcade_token_address` is associated with the `ArcadeToken` contract, and the `arcade_crowdsale_address` is associated with the `ArcadeTokenCrowdsale` contract.

* The next step is to associate the contracts and addresses with the functionality in the code that we created.

Copy the `arcade_crowdsale_address` address. Navigate to the Contract box, and then select the `ArcadeTokenCrowdsale` contract file. Paste the address into the AtAddress box, and then click the AtAddress button.

* By associating the `arcade_crowdsale_address` contract address with the `ArcadeTokenCrowdsale` contract code, we link the functionality in the code with the deployed contract.

Scroll down to the end of the Remix window, and point out the functionality that’s associated with the now-functional `ArcadeTokenCrowdsale` contract, as the following image shows:

![A screenshot depicts the buttons and a drop-down list for the ArcadeTokenCrowdsale contract.](Images/arcd-crowdsale-deployed.png)

* In the image, notice that we have buttons named buyTokens, rate, token, wallet, and weiRaised and a drop-down list named **address beneficiary**.

Repeat the same process with the `arcade_token_address` and the `ArcadeToken` contract, as the following image shows:

![A screenshot depicts buttons and drop-down lists for the ArcadeToken contract.](Images/arcd-token-deployed.png)

* In the image, notice that we have the buttons and drop-down lists for the `ArcadeToken` contract.

* At this point, the `ArcadeTokenCrowdsaleDeployer` contract has done its job. The contracts for the `ArcadeToken` and `ArcadeTokenCrowdsale` have been created on the blockchain.

* By using the addresses provided for those contracts, we were able to link the on-chain contracts with the Solidity code that we wrote to define the functionality for those contracts.

Ask the students if they have any questions about how the contracts got deployed and linked.

Now, run through a quick demonstration of the functionality of the contracts. Make this a shorter version of the demonstration that you did in an earlier activity. The students should now have more context for the crowdsale functionality.

Be sure to navigate to a different MetaMask account than the one that you used to deploy the contracts.

* Once again, we assume the role of investors in the crowdsale. The goal is to purchase tokens that get issued in the crowdsale by using ether.

Start by copying the selected address of the crowdsale participant onto the clipboard.

Next, input a value into the `Value` box and a denomination of wei that’s associated with the number of tokens to purchase.

In the deployed `ArcadeTokenCrowdsale` contract, paste the address of the crowdsale participant into the `buyTokens` box.

A MetaMask dialog box opens, asking you to confirm the transaction. Confirm it.

Then, navigate to the `ArcadeToken` contract, and paste the participant address into the `balanceOf` box. Clicking the `balanceOf` button should not reveal a number of tokens matching the number of wei that you specified in the `Value` box.

Now that they’ve observed the code, the deployment process, and a demonstration of the functionality, ask the students if they have any questions about creating Ethereum crowdsales.

Ask the students the following two questions to confirm their understanding of the deployment process:

**Question:** What role does the `ArcadeTokenContractDeployer` contract play in the deployment process?

**Answer:** The `ArcadeTokenContractDeployer` creates the on-chain contracts for both the `ArcadeToken` and the `ArcadeTokenCrowdsale` contracts.

**Question:** What purpose does associating `arcade_token_address` with the `ArcadeToken` contract serve?

**Answer:** The `ArcadeTokenContractDeployer` contract created an `ArcadeToken` contract on the blockchain. The address details the location of that contract. At the time of deployment, however, the on-chain `ArcadeToken` contract doesn’t do anything, because it doesn’t have any code that’s associated with it. Linking the address to the `ArcadeToken` contract ensures that the on-chain contract has access to the intended functionality.

Let the students know that the best way to understand both the code and the deployment process is to do it themselves. Up next: they’ll have the opportunity to do exactly that.

---

### 9. Student Do: XP_Token Crowdsale (40 min)

**Corresponding activity:** [XP_Token Crowdsale](Activities/04-Stu_XP_Token_Crowdsale)

**Files:**

[Instructions](Activities/04-Stu_XP_Token_Crowdsale/README.md)

[Starter file - XPTokenMintable.sol](Activities/04-Stu_XP_Token_Crowdsale/Unsolved/XPTokenMintable.sol)

[Starter file -XPTokenCrowdsale.sol](Activities/04-Stu_XP_Token_Crowdsale/Unsolved/XPTokenCrowdsale.sol)

**Instructor Note:** Students will need to set their compiler versions to `0.5.5` for this activity.

Have the TAs slack out the preceding three files out the students so that they can complete the activity steps.

In this activity, the students will code, deploy, and test the contracts for launching a crowdsale to distribute `XP_Tokens`.

This is a challenging activity that integrates lots of moving pieces. Be sure that the TAs circulate to assist those students that seem to have trouble working through the steps.

The activity is broken down into three phases: code the contracts, deploy the contracts, and test the application.

If you find that multiple students or groups seem challenged by the same step, especially in the coding section, feel free to bring everyone together for a quick code-along. Encourage the students that are further along in the activity to supply the code and their reasoning for it.

---

### 10. Instructor Do: Review XP_Token Crowdsale (15 min)

**Corresponding activity:** [XP_Token Crowdsale](Activities/04-Stu_XP_Token_Crowdsale)

**Files:**

[Instructions](Activities/04-Stu_XP_Token_Crowdsale/README.md)

[Starter file - XPTokenMintable.sol](Activities/04-Stu_XP_Token_Crowdsale/Unsolved/XPTokenMintable.sol)

[Starter file - XPTokenCrowdsale.sol](Activities/04-Stu_XP_Token_Crowdsale/Unsolved/XPTokenCrowdsale.sol)

[Solution file - XPTokenMintable.sol](Activities/04-Stu_XP_Token_Crowdsale/Solved/XPTokenMintable.sol)

[Solution file - XPTokenCrowdsale.sol](Activities/04-Stu_XP_Token_Crowdsale/Solved/XPTokenCrowdsale.sol)

Focus this review on the integration between the`XP_TokenCrowdsaleDeployer` contract and the `XP_Token` and `XP_TokenCrowdsale` contracts.

Before beginning the review, make sure that you’ve opened Ganache and loaded at least three accounts into MetaMask.

As much as possible, live code the solution for students.

Start this review with the `XPTokenMintable.sol` file. The first step in the activity asks the students to remove the `mint` function from the `XP_Token` contract.

It’s possible to just comment out that line of code, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

contract XP_Token is ERC20, ERC20Detailed, ERC20Mintable {
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        // mint(msg.sender, initial_supply);
    }
}
```

* We remove the `mint` function from the body of the `XP_Token` constructor function because the `XP_TokenCrowdsale` contract will eventually handle the functionality.

Open the `XPTokenCrowdsale.sol` file, and then work through the steps that create all the code, starting with the `pragma` and `import` statements, as the following code shows:

```solidity
pragma solidity ^0.5.0;

import "./XPTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
```

* In addition to adding the `pragma` statement and importing the OpenZeppelin `Crowdsale` and `MintedCrowdsale` contracts, we also need to import the `XPTokenMintable.sol` file. To do that, we use a relative path. The `import` statement gives the code in this file access to the `XP_Token` contract.

Next, move on to coding the `XP_TokenCrowdsale` contract, as the following code shows (encourage the students to volunteer as much of the code as possible):

```solidity
contract XP_TokenCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint256 rate,
        address payable wallet,
        XP_Token token
    )
      Crowdsale(rate, wallet, token)
      public
    {
        // constructor can stay empty
    }
}
```

Pose the following questions to the students. If no one volunteers a response, provide them with the answer.

**Question:** Why must we declare the `Crowdsale` constructor as a public function?

**Answer:** We make the `Crowdsale` constructor a public function so that the eventual participants will be able to access the functionality that’s associated with the `Crowdsale` contract.

**Question:** Why does the body of the constructor function stay empty?

**Answer:** We don’t need to include the `mint` functionality in the body of this constructor because the `Crowdsale` constructor accounts for it.

Before moving on, answer any additional questions that the students might have concerning the `XP_TokenCrowdsale` contract.

Next, code the `XP_TokenCrowdSaleDeployer` contract as follows:

```solidity
contract XP_TokenCrowdsaleDeployer {
    address public xp_token_address;
    address public xp_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
    public
    {
        XP_Token token = new XP_Token(name, symbol, 0);
        xp_token_address = address(token);

        XP_TokenCrowdsale xp_crowdsale =
            new XP_TokenCrowdsale(1, wallet, token);
        xp_crowdsale_address = address(xp_crowdsale);

        token.addMinter(xp_crowdsale_address);
        token.renounceMinter();
    }
```

Before moving on, answer any additional questions that the students might have concerning the `XP_TokenCrowdsaleDeployer` contract.

When you’ve completed all three contracts, compile the two files.

The next step in the review process is to deploy all three contracts, starting with `XP_TokenCrowdsaleDeployer`.

Encourage the students to supply the steps for deploying the contracts.

Have the students volunteer the order in which the contracts should be deployed.

Pose the following questions to the students. If no one volunteers a response, provide them with the answer.

**Question:** What role does the `XP_TokenCrowdsaleDeployer` contract play?

**Answer:** The `XP_TokenCrowdsaleDeployer` contract creates the `XP_Token` and `XP_TokenCrowdsale` contracts on the blockchain. It also makes sure that the individual deploying the contracts has access to the addresses for the on-chain contracts. The deployer also assigns the minter role to the `XP_TokenCrowdsale` contract so that participants can buy tokens.

**Question:** What’s the process for linking the on-chain contracts that the deployer created with the code in the Solidity files?

**Answer:** In Remix, the compiled `XP_Token` contract of Solidity code gets deployed at the address assigned to the on-chain `XP_Token` contract that the deployer created. The same process gets repeated for the `XP_TokenCrowdsale` contract.

Answer any additional questions that students might have concerning contract deployment before moving on to crowdsale testing.

Using a MetaMask address that differs from the one that you used for contract deployment, purchase XP_Tokens.

For that address, evaluate both the `balanceOf` value for the tokens and the `totalSupply` value for the tokens.

Execute a purchase of tokens by using a third address, again reviewing the `balanceOf` and `totalSupply` values.

Encourage the students to share the results of any additional testing that they undertook.

When the testing is complete, ask the students if they have any final questions about the integration among the Solidity contracts, about how the contracts inherit functionality from OpenZeppelin, or about how the deployment process worked to link the separate contracts into a cohesive application.

If possible, use these questions as the basis for the structured review to take place in the next activity.

---

### 11. Instructor Do: Structured Review (35 min)

**Note:** If you’re teaching this lesson on a weeknight, please save this review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

**Suggested format:**

* Ask the students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow the students to start the homework with extra TA support.

* Take your time with these questions! This is a great time to reinforce concepts and address misunderstandings.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.