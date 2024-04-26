## 22.1 Lesson Plan: Fundamentals of Decentralized Applications

### Overview

In today's lesson, students will be introduced to the concept of DeFi, which is short for decentralized finance. DeFi most commonly refers to financial systems that are built on distributed ledgers and frequently leverage smart contracts. By the end of this class, students will understand that DeFi is a movement within the fintech sector where financial systems are being created and deployed within an open, decentralized, and permissionless architecture.

### Class Objectives

By the end of this lesson, students will be able to:

- Build non-fungible token (NFT) contracts using ERC-721 standards and the OpenZeppelin library.

- Deploy the NFT to a local blockchain using Ganache, MetaMask, and Remix.

- Build a decentralized application for an NFT using Streamlit and Web3.py.

---

### Instructor Notes

- Keep in mind that the contracts you’ll deploy today are relatively large and may take a few minutes to compile.

- Refer to OpenZeppelin’s [ERC-721 documentation](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721) for more information about non-fungible tokens.

- Refer to the [IPFS documentation](https://docs.ipfs.io/) for more information about how IPFS works.

- TAs should keep track of class time by using the [Time Tracker](TimeTracker.xlsx).

- - **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

---

### Slideshow and Time Tracker

- You can review the slides for this lesson on Google Drive: [Lesson 22.1 slides](https://docs.google.com/presentation/d/1FttePmkXG_reotiPi5w3FRtleSLNCEimuc5qoiOq8RQ/edit?usp=sharing).

- To add the slides to the student-facing repository, first download the slides as a PDF. To do that, on the **File** menu, select **Download**, and then select **PDF Document (.pdf)**. Then add the PDF file to your class repository along with other necessary files. You can review these instructions in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

  **Note:** Edit access is not available for this document. If you want to modify the slides, create a copy by selecting **Make a copy** on the **File** menu.

- You can review the Time Tracker for this lesson in the following file: [Time Tracker](TimeTracker.xlsx).

## Class Activities

### 1. Instructor Do: Introduction to Decentralized Applications (10 min)

In this section, you’ll introduce students to decentralized applications, or **dApps**, a concept that was introduced to students in Lesson 20.3.

Remind the students that dApps are software applications that run on the Ethereum blockchain. Review the following points:

- dApps use financial programming and blockchain technology to build new financial capabilities for fintech.

- dApps can even use machine learning, although that’s not required for a dApp to be considered a dApp.

- In today’s lesson, you’ll learn about the structure and components of a dApp and how dApps use blockchain technologies to achieve decentralization.

- We have an exciting day ahead! You’ll create a smart contract for NFTs that uses the Ethereum Request for Comments (ERC)-721 standard. You’ll also build a dApp that can register new digital artwork on a blockchain by minting the NFTs.

Open the lesson slides, move to the “What’s a dApp?” section, and highlight the following.

- Let’s deep dive into what exactly a dApp is. From the perspective of a user, a dApp is just like any other application that they’d use on the internet. What makes a dApp different is that it’s built on a decentralized network, such as a blockchain.

- In this course, we've created many financial applications by using Python. The structure of each application typically consists of a back end and a front end, as shown in the following image.

  ![An illustration depicts an application consisting of a back end and a front end, with data passing between those two parts.](Images/application-front-back-end.png)

- The **back end** consists of the core logic and manages the data.

- The **front end** is the part of the application that a user interacts with (which typically happens through a web browser).

Explain to students that with a traditional application, the entire application might be centralized.

- For example, a server in the cloud might run the code and manage the data. Users then interact with this server through a webpage interface.

- While this approach works, these apps suffer from many of the same centralization limitations that we previously discussed regarding blockchain.

Point out to students that centralized applications are widely used. But, they often suffer from centralization issues, such as having a single point of failure, being susceptible to attack, or even encountering access problems.

- dApps embrace decentralization by using new blockchain technologies, such as smart contracts, so they become robust against these issues.

- The back end of these dApps live on the blockchain and persist despite anything that happens to a single copy (an instance).

Explain that tokens are an essential part of dApps, so we’ll begin by reviewing fungible and non-fungible tokens.

#### Review of Fungible and Non-fungible Tokens

Remind the students of the following:

- You previously implemented a basic token as well as the ERC-721 fungible token standard by using OpenZeppelin libraries. Today, you’ll implement your first ERC-721 non-fungible token by using the OpenZeppelin libraries.

- An ERC, or Ethereum Request for Comment, is a common standard for creating tokens on the Ethereum blockchain. There are several ERCs defined by the Ethereum community.

To review ERCs, OpenZeppelin, and fungibility, ask the class the following questions:

- **Question:** What are some differences between fungible and non-fungible tokens?

  **Answer:**

  - Fungible tokens are not unique, while non-fungible tokens are unique.

  - Fungible tokens are interchangeable with one another, while non-fungible tokens are not.

  - Fungible tokens use ERC-20, while non-fungible tokens use ERC-721.

- **Question:** What are some examples of fungible assets?

  **Answer**: United States Dollars (USD), Ether (ETH), Bitcoin (BTC), gold

- **Question:** What are some benefits of using open source libraries such as OpenZeppelin?

  **Answer**:

  - Open source libraries are freely available to use and contribute to under the MIT license.

  - OpenZeppelin is a community-backed project that has implemented many of the communities agreed-upon standards (EIPS/ERCS).

  - OpenZeppelin provides a secure, standardized starting point for various smart contract standards.

Next, explain that after completing this unit, the students will work on a final capstone project that showcases their fintech skills. Understanding dApps will help them as they develop this final project.

Answer any questions before moving on.

---

### 2. Instructor Do: Build a dApp Back End (30 min)

**Corresponding activity:** [Art Token Back End](Activities/01-Ins_Art_Token_Backend)

In this section, you will build the Solidity smart contract for the Art Token dApp.

The contract will utilize the [ERC-721 standard](https://eips.ethereum.org/EIPS/eip-721) and import the [ERC-721 OpenZeppelin contract](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol).

Additionally, you will deploy the contract using Ganache and Metamask. Although the students should be familiar with these applications, if time permits, demonstrate the process of launching Ganache and adding accounts to MetaMask.

**File:**

[Starter file](Activities/01-Ins_Art_Token_Backend/Unsolved/ArtToken/artwork.sol)

#### Introduce NFTs and ERC-721

Explain to the students that many of the applications that they have built over the last few units have been decentralized applications.

- For example, if the Arcade and XP tokens were launched on the live Ethereum mainnet, they would act as decentralized applications.

Transition to non-fungible tokens (NFTs) and the ERC-721 standard.

- Many of the applications that you already created are considered dApps. This is because they use smart contracts and blockchain to decentralize the core logic and the data behind the application.

- By developing applications for a blockchain, you automatically develop dApps for the Next Generation Web, also known as Web 3.0.

- The `ArcadeToken` and `XP_Token` applications are fungible tokens, but some of the most popular dApps are created for **non-fungible tokens**, or **NFTs**.

- NFTs represent unique assets, such as land, art, or other items with no interchangeable counterpart. This stands in contrast to fungible tokens like cryptocurrencies where, for example, a single bitcoin is easily interchangeable with several ether.

- With dApps specifically designed for NFTs, users can buy or sell artwork NFTs in a decentralized marketplace. They can also play games for which the avatars and game items are NFTs on a blockchain.

- In this lesson, we’ll further explore dApps by learning how to build a new type of smart contract specifically designed for NFTs.

- To build this new type of contract, we’ll use the ERC-721 Non-Fungible Token Standard defined by the Ethereum Improvement Proposal (EIP)-721. ERC-721 is considered the default standard for implementing most NFTs.

Navigate to the [EIP-721](https://eips.ethereum.org/EIPS/eip-721) page. Also, have a TA slack a link to this page out to the students.

Explain to the students that you are going to apply the ERC-721 standard to building an art token contract.

- This contract will use ERC-721 tokens to register new pieces of artwork.

- Building the dApp will start with constructing the back-end contract that will handle the core logic of the `ArtToken` dApp.

#### Build a dApp Back-End Contract

Open Remix and use the starter file to create a file called `artwork.sol`. This file should contain the pragma statement for any Solidity version 0.5.0 through 0.5.17.

```solidity
pragma solidity ^0.5.0;
```

- The `artwork.sol` file contains the contract that will handle the core logic of the dApp.

Navigate to the [ERC-721 GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol) and explain that creating the NFT contract begins with importing the contact standard from OpenZeppelin.

Have a TA slack out the [ERC-721 GitHub page](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol) to the students.

- As with the fungible tokens, first import the code from the OpenZeppelin `ERC721Full` contract, as the following code shows:

  ```solidity
  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
  ```

- The ERC-721 standard contains the constructor that will be used to create the Art Token NFT.

Next, create a new contract named `ArtToken` that inherits code from the `ERC721Full` contract. Here’s the code:

```solidity
contract ArtToken is ERC721Full {
    constructor() public ERC721Full("ArtToken", "ART") {}
}
```

- By creating the `ArtToken` contract and linking it to the ERC-721 GitHub page, the `ArtToken` contract will inherit all the functions that we need to satisfy the requirements of the ERC-721 standard.

- Inside the `ArtToken` contract, a constructor is defined that calls the `ERC721Full` constructor.

- The `ERC721Full` constructor function requires a token name and a token symbol. These can be anything we like, but this token will use the name “ArtToken” and the symbol “ART".

Next, add a separate function named `registerArtwork` that will allow users to register new pieces of artwork, as the following code shows:

```solidity
function registerArtwork(address owner, string memory tokenURI)
    public
    returns (uint256)
{
    // TODO: add code to mint new tokens
}
```

- The `registerArtwork` function will allow users to register new pieces of artwork. Note that this function is included inside the contract, but outside of the constructor functions.

- The `registerArtwork` function accepts an address for the artwork `owner` and a string named `tokenURI`, which will consist of a link to where the digital artwork exists online.

> **Note:** Some students might not be familiar with the term **URI**, or **Uniform Resource Identifier**. Explain that the URI originated from a World Wide Web initiative to standardize the way that files or objects get encoded for the web. The URI is an identifier of a specific resource, like a page, a document, or a book. This is in contrast to the more familiar URL, which is referred to as a locator, as it includes how to access a resource like HTTPs or FTP. The URL is a subset of the URI.

![URI versus URL](Images/uri-versus-url.png)

Ask a TA to slack out the link for the URI standard on the [Universal Resource Identifier (URI)](https://tools.ietf.org/html/rfc3986) page from the Internet Engineering Task Force (IETF).

Return to the `registerArtwork` function.

- The `registerArtwork` function mints the new token and returns the token ID. The token ID takes the form of an unsigned integer.

- Registering new artwork on the blockchain requires us to mint a new token for the artwork. This token will identify the current owner and the uniform resource identifier (URI) of where the artwork resides.

- Inside the `registerArtwork` function, we thus need to accomplish three things: 1) Create a new token ID. 2) Mint a new token for that new token ID. 3) Set the `tokenURI`, which associates the digital artwork with the token.

Develop the code that addresses each of these three aspects. Each of the following four lines of code will be written in the `// TODO:` section of the preceding code block.

Start by explaining the code required to create a new token ID, which is the following:

```solidity
uint256 tokenId = totalSupply();
```

- To create a new token ID, we could use a counter. We’d start the counter at zero and then increment it for each new token.

Highlight the `totalSupply` function as an alternative to the counter. Navigate to the [ERC-721 standards page](https://eips.ethereum.org/EIPS/eip-721) and navigate down to the `ERC721Enumerable` extension.

![ERC721Enumerable section](Images/erc721-enumerable.png)

- However, the `ERC721Full` contract contains an extension called `ERC721Enumerable` that has a function named `totalSupply` that returns the total number of tokens that we have minted. We can use this value as the ID for the new token.

Next, create the `_mint` function that allows us to mint a new token that contains the `owner` address and the new `tokenId` created using the `totalsupply` function, as the following code shows.

```solidity
_mint(owner, tokenId);
```

- Next, we can create a `_mint` function of `ERC721Full`. This function uses the owner address and the token ID to mint a new token.

Finally, create the `setTokenURI` function that takes in the `tokenId` and the `tokenURI`, which was input when the `ArtToken` was constructed. Here’s the code:

```solidity
_setTokenURI(tokenId, tokenURI);
```

- To complete the third step, we create a `_setTokenURI` function to permanently associate the value of `tokenURI` with the token on the blockchain.

- This permanently adds the link to the digital artwork to the token. The art token contract uses the value of `tokenURI` to create the link between the token and the digital artwork. We do this because storing a digital artwork file on the blockchain, or on-chain, is expensive. Instead, we store the URI string that points to where the file resides on the internet.

Explain that, now that the token has been minted and its URI set, the final step is to return the new token, as the following code shows.

```solidity
return tokenId;
```

The full code for the art contract is thus as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtToken is ERC721Full {
    constructor() public ERC721Full("ArtToken", "ART") { }

    function registerArtwork(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        return tokenId;
    }
}
```

Explain that we now have a new art contract that can mint NFTs for the purpose of registering digital artwork.

Ask if the students have any questions about the ERC-721 contract, the code, or why we are linking the `tokenId` to the `tokenURI` (rather than the artwork file) on the blockchain.

The next step is to compile and deploy the contract.

#### Compile and Deploy the Contract

As with the fungible tokens, the next step involves compiling and deploying the `ArtToken` contract by using the Remix IDE, MetaMask, and Ganache.

Although students should now be familiar with this process, if time permits, review the process of launching a Ganache test blockchain and adding the new accounts to MetaMask.

- Ganache's local test blockchain will provide the accounts and the ether that will be needed later to deploy and test the `ArtToken` dApp.

- MetaMask is the wallet that serves as the link between the Remix IDE and the Ganache blockchain. Accounts from the new Ganache instance need to be imported into MetaMask in order to be accessed in Remix.

Once Ganache and MetaMask are up and running, compile the `ArtToken` contract in the Remix IDE.

Explain that there is a new step we must undertake as part of the process of creating our dApp. The details of the contract will need to be saved for use by the front end of the application. This is accomplished by copying its application binary interface (ABI) file, found at the bottom of the Compiler page, into a local JSON file.

Open the [`ArtToken` folder associated with the starter file](Activities/01-Ins_Art_Token_Backend/Unsolved/ArtToken) in Visual Studio Code.

If necessary, copy the code from the `artwork.sol` file from Remix into the `artwork.sol` file contained in the `ArtToken` folder.

Next, inside the `ArtToken` folder in VS Code, create a new file called `artwork_abi.json`. Copy the `abi` file from the compiled file in Remix into the `artwork_abi.json` file and save it.

Review the contents of the ABI file for the students, highlighting the following information.

- An **ABI file** contains contract details that the Web3.py library and Streamlit will use to execute the application in the EVM. Both Web3.py and Streamlit will be used for the front end of our dApp. They’ll use the details contained in the ABI file to connect to the contract and to use its functions and data.

- This is how the Steamlit front-end interface for our dApp will eventually access the details of our contract.

Return to Remix and deploy and test the contract.

Navigate to the Deploy & Run Transactions pane and select “Injected Web 3” as the environment.

When the MetaMask window opens, select at least two Ganache accounts to make available in Remix.

Select the “ArtToken - artwork.sol” contract and click Deploy. Click Confirm when the MetaMask window opens.

Explain that it’s possible that the deployment will fail due to an “out of gas” error. Update the `Gas Limit` to `30000000` and attempt to redeploy the contract.

Click Confirm when the MetaMask window opens.

With the contract deployed, review the `Name`, `Symbol`, and `totalSupply` of the contract. Note that the current value for `totalSupply` is `0`.

Update the `Gas Limit` to `30000000` and attempt to redeploy the contract again.

> **Note:** To test the contract for the students, you can use the URI of the following link to the digital Mona Lisa.
>
> URI Digital Mona Lisa: `https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg`

Explain that the new `tokenId` assigned to our token is `0`, the value of the `totalSupply` category when our token was created.

Navigate to the `tokenURI` field and input the `tokenId` of 0. In the terminal window, highlight how the URI for the Mona Lisa is now reflected, as shown in the following image.

![Token ID and URI](Images/token-id-and-uri.png)

Finally, navigate to the `totalSupply` field and show that it now has a value of `1`.

Ask the students if they have any questions about compiling and deploying the contract before proceeding to the next activity.

---

### 3. Everyone Do: Build the Mint-Condition Artwork Back End (25 min)

**Corresponding activity:** [Build the Mint-Condition Artwork Back End](Activities/02-Evr_Mint_Condition_Artwork_Back_End)

This section focuses on the code required to construct the `ArtToken` contact. Be sure to emphasize the role of the ABI file in the front end of the application, as students will need to understand this for the next activity.

**Files:**

[Starter folder](Activities/02-Evr_Mint_Condition_Artwork_Back_End/Unsolved/ArtToken)

[Solution folder](Activities/02-Evr_Mint_Condition_Artwork_Back_End/Unsolved/ArtToken)

Begin by explaining to the students that this is a collaborative activity where they are expected to code along with you.

Open the Remix IDE and create a new file called `artwork.sol`. Then, copy the code in the provided `artwork.sol` file into the new file.

Spend a few moments reviewing the code and explain to students that they are coding the back-end logic for a non-fungible token.

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtToken is ERC721Full {
    constructor() public ERC721Full("ArtToken", "ART") {}

    function registerArtwork(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        return tokenId;
    }
}
```

Engage the class by asking them to recall the differences between fungible and non-fungible tokens. If no one volunteers a response, provide them with the answer.

**Question:** What are some differences between fungible and non-fungible tokens?

**Answer:** Fungible tokens are easily interchangeable. Cryptocurrencies are the most popular example of fungible tokens. Also, fungible tokens are based on the ERC-20 standard. Non-fungible tokens (NFTs) represent unique assets, like works of art or real estate, and are not easily interchangeable. NFTs are based on the ERC-721 standard.

- The `ArtToken` smart contract is designed to inherit the full functionality of the `ERC721` standard. This is the standard for non-fungible tokens.

- The contract utilizes the `ERC721Full` constructor, which requires a `name` and a `symbol`.

Use the following question as the basis for coding the body of the `registerArtwork` function.

- Aside from the constructor, we will create a function called `registerArtwork`. This function requires the address of the owner and the string value associated with the URI of the item being tokenized. The function will return an unsigned integer in the form of the `tokenId`.

**Question:** What are the four processes that the `registerArtwork` function will perform?

**Answer:** The four processes are:

1. Create a new `tokenId`.

2. Mint a new token for that new `tokenId`.

3. Set the `tokenURI`, which associates the digital artwork with the token.

4. Return the `tokenId`.

Proceed to live code the `registerArtwork` function. Here’s the code:

```solidity
function registerArtwork(address owner, string memory tokenURI)
    public
    returns (uint256)
{
    uint256 tokenId = totalSupply();
    _mint(owner, tokenId);
    _setTokenURI(tokenId, tokenURI);

    return tokenId;
}
```

With the code in place, work through the process of compiling, deploying, and testing the `ArtToken` contract.

As you review the testing process, pose the following question:

**Question:** What back-end processes are performed by the `ArtToken` smart contract?

**Answer:** The `ArtToken` contract controls all of the logic associated with the `ArtToken` NFT. It keeps track of each new token, catalogued by `tokenId`. Each `tokenId` contains references to the owner's address and the URI associated with the asset. All of this information will be stored on the blockchain and can be accessed by making a call to the blockchain.

For the last step in the review, copy the contract ABI from the Remix compiler page.

Open VS Code and navigate to the `ArtToken` folder. Inside the folder, create a `.json` file named `artwork_abi.json` and copy the contents of the ABI from Remix into the file.

> **Note:** Remind students how they can copy the ABI at the bottom of the compiler section in Remix:
![A screenshot depicts the dApp displayed on a webpage.](Images/copying_abi.png)

- The ABI file contains all of the information on the compiled `artwork.sol` file required by the front end of our application. This ABI file, in effect, acts as the link between the front end and back end of the dApp.

Explain that we will start coding the front end of our dApp in the next activity.

Ask students if they have any final questions about the back end of our dApp before moving on.

---

### 4. Break (15 min)

---

### 5. Instructor Do: Build a dApp Front End (30 min)

**Corresponding activity:** [ArtToken Front End](Activities/03-Ins_Art_Token_Front_End)

In this section, you will show the class how to integrate the `ArtToken` smart contract with the Streamlit application in order to build the front-end interface for the dApp. The front end of the `ArtToken` dApp will be built using the Streamlit web application.

The files required for this section are located inside the `ArtToken` folder in the `Unsolved` folder.

> **Note:** This activity assumes that the `ArtToken` contract has been deployed using Remix, Ganache, and MetaMask, and that the ABI file has been copied into a file named `artwork_abi.json`.

**Files:**

[Starter folder](Activities/03-Ins_Art_Token_Front_End/Unsolved/ArtToken)

[Solution folder](Activities/03-Ins_Art_Token_Front_End/Solved/ArtToken)

Explain to students that, with the back-end logic for our `ArtToken` dApp in place, it’s time to focus on building the front end.

- For this dApp's front end, we’ll use Streamlit components and the Web3.py library to provide the capability of interaction with the contract, which resides on the blockchain.

- Specifically, users will be able to select their accounts and register new artwork tokens through a web interface. Users will also be able to display the tokens for their accounts so that they can display the artwork on the webpage.

The first step in the process of building the front end is to set up the application.

#### Set Up the Application

Open the starter folder associated with this activity. At this point, it consists of only the completed `artwork.sol` file and the `artwork_abi.json` file.

Explain that, to set up the front end of our decentralized application, a few files are required: the `artwork_abi.json` file, an environment file (aka a `.env` file), and an `app.py` file.

- The `artwork_abi.json` file, which we already have, contains the content of the compiled contract’s ABI file.

- The environment file named `.env` will store the Web3 provider and the address of the deployed contract.

- The `app.py` file will be the Python application file. It will contain the code that uses Streamlit and Web3.py to allow users to interact with the contract from a webpage.

First, set up the required folder structure.

- Currently, the `artwork_abi.json` file and the `artwork.sol` file are included on the same level inside the `ArtToken` folder.

Create a folder called `contracts`. Move both the `artwork_abi.json` file and the `artwork.sol` file into the `contracts` folder.

Next, inside the `contracts` folder, create a new folder called `compiled`. Move the `artwork_abi.json` file`into the`compiled` folder.

As you create these folders, explain the following to the students:

- Although the front end of the dApp does not use the `artwork.sol` file, it’s integral to the creation of the NFT, so it makes sense to include it as part of the project folder.

- If the application creates more than just an `ArtToken` NFT, the contracts can all be kept together in this folder.

- It’s a best practice to create the `compiled` folder to hold the `artwork_abi.json` file. In this way, the ABI file is kept with its related Solidity file, but in a more easily identifiable location.

- The `artwork_abi.json` file already contains the content of the compiled contract's ABI file. Inside our application, Web3.py will use this file to load the contract.

Next, at the root level of the `ArtToken` folder, create a `.env` file.

- The first entry in the `.env` file specifies the address that the Web3 provider will use for the local Ganache blockchain.

- Because we’ll later use the Ganache Quickstart option to create a local blockchain with a default provider URI, we can use the following code for this line:

  ```text
  WEB3_PROVIDER_URI=http://127.0.0.1:7545
  ```

- The second line specifies the address of the deployed contract. It will appear as follows:

  ```text
  SMART_CONTRACT_ADDRESS=<DEPLOYED TOKEN CONTRACT ADDRESS HERE>
  ```

Navigate to the Remix IDE and locate the address for the smart token contract that was deployed in the first part of the class.

Copy the contract address and put it in place of the text that reads `<DEPLOYED TOKEN CONTRACT ADDRESS HERE>`.

- The address for the deployed smart contract is found in the Remix IDE when displaying the deployed contract. Copy the address to the clipboard and set it equal to the `SMART_CONTRACT_ADDRESS` variable.

The final file to be addressed is the `app.py`. Create an `app.py` file at the root level of the `ArtToken` folder.

- The `app.py` file will contain the Python code needed for the Streamlit web application’s front end.

At this point, the complete folder structure for the `ArtToken` dApp should be in place, as follows:

ArtToken
|
-contracts
|
-compiled
|
-artwork_abi.json
-artwork.sol
-app.py
-.env

Tell students that, with the dApps folder structure in place, the next step in the process is to code the front-end application, starting with the required imports.

#### Import the Required Libraries

Explain that, as always, the first step in creating the Python file is to import the required libraries, as the following code shows:

```python
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
```

- We import libraries for accessing the `.env` file, reading the `artwork_abi.json` file, accessing the Web3 functionality, and Streamlit.

Next, add the `load_dotenv` to load the `.env` file:

```python
load_dotenv()
```

- The `load_dotenv` function allows us to access the values associated with the variables contained in the `.env` file.

Now that we’ve set up the application, the next step is to define and connect a new Web3 provider.

#### Define and Connect a New Web3 Provider

Tell students that the next step is to define and connect to a new Web3 provider, which, in our dApp, will be the Ganache local blockchain.

Remind students that the URI for the Ganache blockchain has been set up in the `.env` file.

```text
WEB3_PROVIDER_URI=http://127.0.0.1:7545
```

Next, create a variable called `w3` that accesses Web3's HTTP provider and passes the code to access the `.env` file variable, as the following code shows.

```python
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI"))
```

- To interact with the smart contract from the Python front end, we define a Web3 instance named `w3` and set it equal to the `WEB3_PROVIDER_URI` environment variable that we stored in our `.env` file.

- Remember, an instance of the `ArtToken` contract has been deployed to and resides on the Ganache blockchain.

Explain that Web3 is also used to load the `ArtToken` smart contract into our Python application. We’ll then be able to use Web3 and Python to interact with the deployed contract directly from the dApp.

#### Load the Contract

Explain that the next step is to write the `load_contract` function. Because we are using Streamlit, write the function with a [Streamlit cache decorator](https://docs.streamlit.io/en/stable/caching.html). Here’s the code:

```python
@st.cache_resource()
def load_contract():
    // TODO: Load the contract’s ABI details next
```

- Recall that Streamlit will run all the code inside an application each time that a Streamlit component changes. To avoid this, we supply a cache decorator.

- Caching the contract tells Streamlit to load this contract only one time, regardless of other changes. This prevents the contract from being reloaded every time content on the page changes.

Have a TA slack out the following link so that students can read more on the Streamlit documentation page about [caching](https://docs.streamlit.io/en/stable/caching.html).

#### Load the Contract’s ABI Details

Explain that the next step is to create the code associated with the `load_contract` function. The `load_contract` function reads the JSON file that contains the contract’s ABI details. Here’s the code:

```python
def load_contract():
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)
```

- The `Path` function and relative path provide the application with access to the smart contract functionality through the ABI file.

- The `json.load` function reads the ABI file and saves it in a variable named `artwork_abi`.

##### Set the Contract Address

Next, the `load_contract` function reads the address of the deployed contract from the `.env` file.

```python
def load_contract():
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
```

- The `os.getenv` function gets this address of our deployed smart contract from the `.env` file and saves it in a variable named `contract_address`

#### Connect to the Contract

Next, the `load_contract` function uses Web3 to connect to the contract. Here’s the code:

```python
def load_contract():
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract
```

Highlight the following to the students:

- Web3 uses the [`eth.contract` function](https://web3js.readthedocs.io/en/v1.2.11/web3-eth-contract.html) along with the `contract_address` and `artwork_abi` variables to create the contract instance.

- The `load_contract` function returns this instance so that we can use it later in the application.

Confirm that the code for the application's `app.py` file appears as follows:

```python
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Load the smart contract into the application
@st.cache_resource()
def load_contract():
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract
```

The final step is to call the contract function.

#### Get the Contract

Explain to the students that now we’ll load the contract and assign it to a new variable named `contract`, as the following code shows:

```python
contract = load_contract()
```

- In the Python application, we’ll use this contract instance to call functions and access attributes that exist in the smart contract.

- For example, if we want to register a new piece of artwork and mint tokens for it, we can call the `registerArtwork` function by using `contract.functions.registerArtwork`.

With the contract details now loaded, it is time to start building the Streamlit application.

#### Register New Artwork

With a contract instance loaded, the next step is to build the Streamlit components and logic for interacting with the smart contract from the webpage.

The first step for building the Streamlit application is to create the necessary components, as the following code shows.

```python
st.title("Register New Artwork")
accounts = w3.eth.accounts
address = st.selectbox("Select Artwork Owner", options=accounts)
artwork_uri = st.text_input("The URI to the artwork")
```

- First, we create a [title](https://docs.streamlit.io/en/stable/api.html#streamlit.title) and [components](https://docs.streamlit.io/en/stable/api.html#api-reference) that allows users to provide two pieces of information.

- Specifically, the application will allow a user to select an account for the contract owner from a list of accounts.

- The user will also be able to enter a URI that links to a piece of digital artwork.

Next, add a Streamlit button. When the user clicks this button, we send the inputs from the two preceding components to the contract by using the Web3 contract instance. Here’s the code:

```python
if st.button("Register Artwork"):
    // Web3 code goes here
```

- When the user clicks this button, we send the inputs from the two preceding components to the contract by using the Web3 contract instance.

Inside this `st.button` function, you will create the transaction to mint a new art token, as shown in the following code.

```python
if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({
        "from": address,
        "gas": 1000000
    })
```

- In order to create the transaction that registers the artwork on the blockchain, we call the smart contract's `registerArtwork` function using the `contract.functions` syntax.

- The function will use the selected owner address and `artwork_uri` from the application's inputs.

- The transaction will need to be sent with gas so that it will update on the blockchain.

Explain how a gas estimate would work in a real-world scenario.

- Each transaction that goes to the smart contract requires gas. Using a test network, we've arbitrarily chosen a value of 1 million (1000000) to ensure that the transaction goes through.

- In a real-world application, the developer would use a more accurate gas estimate for this transaction based on the current gas prices.

- Remember, Web3 offers a `gasEstimate` function to help with this.

- In a real-world scenario, many contracts rely on an external price estimator, called an **oracle**, to get accurate gas prices for each transaction.

For students that want additional information, ask a TA to slack out the following Ethereum documentation page on [Oracles](https://ethereum.org/en/developers/docs/oracles/).

#### Display the Information

Explain that the next step is to create the code for capturing the receipt of the transaction hash, and then displaying it to the dApp page. Here’s the code:

```python
if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
```

- Using the `w3.eth.waitForTransactionReceipt` function, the application will wait for the transaction receipt so that it can be displayed on the application’s webpage.

Confirm that the complete code for registering new artwork with the blockchain is as follows:

```python
st.title("Register New Artwork")
accounts = w3.eth.accounts
address = st.selectbox("Select Artwork Owner", options=accounts)
artwork_uri = st.text_input("The URI to the artwork")

if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({
        "from": address,
        "gas": 1000000
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
```

Tell the students that, at this point, all the code that is needed for the front end of the `ArtToken` dApp is in place.

Ask the students if they have any questions about the code that loads the contract, creates the transaction, or displays the transaction hash to the page.

Once all questions have been addressed, proceed to the next section.

#### Run the Streamlit dApp

Explain that you will now run the dApp.

Open a terminal instance and navigate to the `ArtToken` folder. This folder should contain all of the files associated with the `ArtToken` dApp.

Run the `ArtToken` dApp by typing `streamlit run app.py`, in the terminal.

The following dApp should display on the Streamlit page:

![A screenshot depicts the dApp displayed on a webpage.](Images/artwork-application.png)

Point out that the dApp includes a drop-down list for selecting the artwork owner, a box for typing the URI to the artwork, and a Register Artwork button.

Explain that we can now use our dApp to mint new NFTs to register digital artwork.

Demonstrate the operation of the dApp by selecting an account number and inserting a URI for an artwork that you would like to tokenize.

If you do not have a URI, use the following: `https://www.artic.edu/iiif/2/25c31d8d-21a4-9ea1-1d73-6a2eca4dda7e/full/843,/0/default.jpg`

Once the transaction hash has been returned and recorded to the screen, navigate to Ganache and show the transaction with the same hash value.

Ask the students if they have any questions about the functionality demonstrated in this decentralized application.

Once all questions have been addressed, explain to the students that they will now have the opportunity to expand on this dApp: they’ll add Web3 and Streamlit code to display an art token for a selected account.

- With this code in place, you’ll be able to verify that the dApp correctly minted the token.

---

### 6. Everyone Do: Build a dApp for Mint Condition Artwork (25 min)

**Corresponding activity:** [Build a dApp for Mint Condition Artwork](Activities/04-Evr_Mint_Condition_Artwork_Full)

In this activity, you will live code how to build a dApp that uses NFTs as the students follow along. The goal is to solidify students’ understanding of how to create a fully operational dApp for the artwork token so that they can complete their final project.

**Files:**

[Starter folder](Activities/04-Evr_Mint_Condition_Artwork_Full/Unsolved/ArtToken)

[Solution folder](Activities/04-Evr_Mint_Condition_Artwork_Full/Solved/ArtToken)

Explain to the students that this activity focuses on the Streamlit code required to build a dApp. We will also test the application and observe how the information reflected in the dApp is reflected in the Ganache blockchain. Also, be sure to explain to the students that this activity is collaborative; they should follow along as you live code.

Slack out the `ArtToken.zip` file that’s included in the starter folder. The students should unzip the file on their computers.

This activity is divided into four sections:

- Deploy the Contract
- Prepare the Environment
- Build the dApp
- Run the dApp

> **Important:** As you go through each step, be sure to make a connection between the front-end and back-end functionality of this application.

#### Deploy the Contract

Before showing the code to deploy the contract, review the process of compiling the contract in Remix and deploying it by using Ganache and MetaMask.

Ask the students the following questions about the ABI file.

**Question:** Where is the ABI file located?

**Answer:** Once the contract has been compiled, the ABI file is found at the bottom of the `Solidity Compiler` page.

**Question:** What is the role of the ABI file in the dApp?

**Answer:** The ABI file is loaded as a `.json` file into the front end of the dApp. This provides the front end of the dApp with access to all of the functions contained in the on-chain smart contract.

Show that the `ArtToken` folder that the students are using already contains the `artwork_abi.json` file, including the necessary code.

#### Prepare the Environment

For the next two sections, you will work in the Visual Studio Code IDE.

Review the process of completing the two variables contained in the `SAMPLE.env` file.

- The `WEB3_PROVIDER_URI` should contain the RPC Server URI for Ganache: `HTTP://127.0.0.1:7545`

- The `SMART_CONTRACT_ADDRESS` should contain the address of the deployed contract, as found in Remix on the Deploy & Run Transactions page.

Once both environment variables have been completed, resave the `SAMPLE.env` file as a `.env` file.

#### Build the dApp

In VS Code, open the `app.py` file contained in the `ArtToken` folder.

First, complete the `load_contract` function, as the following code shows.

```python
@st.cache_resource()
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artwork_abi.json')) as f:
        artwork_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=artwork_abi
    )

    return contract

contract = load_contract()
```

- The `cache` decorator and function declaration are included in the starter code.

To complete the `load_contract` function, provide the relative path to the `artwork_abi.json` file to the `with open` function. As everyone is receiving the `ArtToken` starter folder, this relative path should be consistent for all the students.

Next, write the code to load the contract using the `w3.eth.contract` function.

Point out where the `artwork_abi` and `contract_address` variables that are needed to load the contract are found.

In the `Register new Artwork` section of the dApp, you will write the code to register the new artwork. Here’s the code:

```python
st.title("Register New Artwork")
accounts = w3.eth.accounts

# Use a Streamlit component to get the address of the artwork owner from the user
address = st.selectbox("Select Artwork Owner", options=accounts)

# Use a Streamlit component to get the artwork's URI
artwork_uri = st.text_input("The URI to the artwork")

if st.button("Register Artwork"):

    # Use the contract to send a transaction to the registerArtwork function
    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.markdown("---")
```

Explain the following steps to the students:

- First, use the `st.selectbox` component to define the token owner's address.

- Next, use a `st.text_input` component to define the field for inputting the artwork URI.

- Finally, complete the code for the `tx_hash` block inside the `Register Artwork` button.

Then, highlight these points:

- The `contract.functions` syntax references the functions detailed in the `artwork_abi.json` file that was loaded under the variable `contract`.

- `registerArtwork` is one of the functions included in the `ArtToken` smart contract.

- The `registerArtwork` function takes in two parameters: the owner's `address` and the `artwork_uri`, both of which are defined by user input in the Streamlit application.

Finally, demonstrate how to display a token. Review the following code with the students:

```python
st.markdown("## Check Balance of an Account")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} tokens")

st.markdown("## Check  Ownership and Display Token")

total_token_supply = contract.functions.totalSupply().call()

token_id = st.selectbox("Artwork Tokens", list(range(total_token_supply)))

if st.button("Display"):

    # Get the art token owner
    owner = contract.functions.ownerOf(token_id).call()
    
    st.write(f"The token is registered to {owner}")

    # Get the art token's URI
    token_uri = contract.functions.tokenURI(token_id).call()

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)
```

We first want to be able to look up the balance of a given address. We do so by making a call to the `balanceOf` function in the contract. Navigate back to the smart contract and be sure to illustrate the functionality of this function in Remix. Highlight, that our Python frontend allows us to conveniently do this without having to open up Remix by accessing the contract's functions:

```python
tokens = contract.functions.balanceOf(selected_address).call()
```

Point out to students that we also want to be able to look up the owner of any of the existing tokens. We do so by creating a variable called 'total_token_supply' which is calling the `totalSupply()` function in the contract. Navigate to Remix again and show the `totalSupply()` function and point out that it does not require any input. 
We then create dropdown selectbox with a range equal to the `total_token_supply`:

```python
token_id = st.selectbox("Artwork Tokens", list(range(total_token_supply)))
```

To display the contract `owner` address, call the `contract.functions` syntax, and chain the `ownerOf` function from the ERC-721 functionality.

Navigate back to the contract in Remix and show students the `ownerOf` function. Point out that the function requires the `tokenId` to make the call.

The `tokenId` in the smart contract is known by the `token_id` variable in the Streamlit application.

```python
# Get the art token owner
owner = contract.functions.ownerOf(token_id).call()
```

To display the `token_uri`, call the `contract.functions` syntax, and chain the `tokenURI` function from the ERC-721 functionality.

```python
# Get the art token's URI
token_uri = contract.functions.tokenURI(token_id).call()
```

Navigate to Remix again and show the `tokenURI` function. The function call also requires the `tokenId` to make the call.

Ask students if they have any questions about the code to display the token or to build the front-end of the dApp by using Steamlit.

Now that all of the code is written, it’s time to test the application.

#### Run the dApp

Open a terminal instance and navigate to the `ArtToken` folder.

Run the Streamlit application with `streamlit run app.py`.

> **Note:** Application tests seem to work best with one owner and two artworks.

You can use any of the following URIs to test the application:

- `https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg`

- `https://www.artic.edu/iiif/2/25c31d8d-21a4-9ea1-1d73-6a2eca4dda7e/full/843,/0/default.jpg`

- `http://www.minorplanetobserver.com/Albums/Paris/paristhelouvre3.jpg`

- `https://upload.wikimedia.org/wikipedia/commons/c/cd/Pictograma_Arte_rupestre.PNG`

- `https://images.metmuseum.org/CRDImages/mi/original/DP331229.jpg`

Ask the students if they have any questions about their now fully functioning decentralized application.

Congratulate the students on successfully building and testing an end-to-end decentralized application that supports Ethereum's primary NFT standard, ERC-721. This is truly cutting-edge knowledge that’s very valuable in the fintech and blockchain marketplaces!

---

### 7. Instructor Do: Capstone Project Requirements (15 mins)

**Files:**

[Capstone Project Guidelines](Activities/05-Ins_Project_Requirements/Capstone_Project_Guidelines.md)

Present these [Capstone Project slides](https://docs.google.com/presentation/d/170m6HH62_ec7K1gI-N6XwXXQC9gl8JyakvQA8vlmgQg/edit?usp=sharing) of project requirements.

Tell the students that they will work in groups for their capstone project. Each group must submit a project proposal, which needs to be approved by the instructional staff.

Emphasize that this capstone project should ideally align with their future career goals as a fintech professional.

#### Technical Requirements

Explain to students that this project will be graded according to the following rubric:

- Proficiency (&ge; 90% of the points)

- Approaching proficiency (&ge; 80% of the points)

- Progressing (&ge; 70% of the points)

- Emerging (&lt; 70% of the points)

Additionally, they should comply with the following technical requirements for the project:

##### Software Version Control (10 points)

- Repository created on GitHub. (2 points)

- Files frequently committed to repository. (3 points)

- Commit messages with appropriate level of detail included. (2 points)

- Repository organized, and relevant information and project files included. (3 points)

##### Data Collection and Preparation (10 points)

- Data collected, cleaned, and prepared for the application or analysis. (10 points)

##### Development (40 points)

- Jupyter notebook, Google Colab notebook, Amazon SageMaker Studio notebook, or Streamlit application created. (10 points)

- One or more Python modules, machine learning models, or Solidity smart contracts created. (10 points)

- Calculations, metrics, visualizations, or video needed to demonstrate the application included. (10 points)

- One new technology or library used that the class hasn't covered. (10 points)

##### Documentation (15 points)

- Code is well commented with concise, relevant notes. (5 points)

- GitHub `README.md` file includes a concise project overview. (2 points)

- GitHub `README.md` file includes detailed usage and installation instructions. (3 points)

- GitHub `README.md` file includes either examples of the application or the results and summary of the analysis. (5 points)

##### Presentation (25 points)

Explain to the students that each group will prepare a formal 10-minute presentation that should include the following:

- An executive summary of the project and project goals (5 points)

  - Explain how this project relates to fintech.

- The approach that your group took to achieve the project goals (10 points)

  - Include any relevant code or demonstrations of the analysis or application.

  - Describe the techniques that you used to test or evaluate the code.

  - Discuss any unanticipated insights or problems that arose and how you resolved them.

- The results and conclusions from the analysis or application (5 points)

  - Include relevant images or examples to support your work.

  - If the project goal wasn’t achieved, share the issues and what the group tried for resolving them.

- Next steps (5 points)

  - Briefly discuss the potential next steps for the project.

  - Discuss any additional questions that you’d explore if you had more time. Specifically, if you had additional weeks to work on your project, what would you research next?

Finally, remind students of the following:

- **Projects are a professional opportunity.**: Projects are portfolio pieces, so use projects as an opportunity to challenge yourself and showcase your knowledge for potential employers.

- You can develop your project as a **minimum viable product**, also known as **MVP**. An MVP is a version of a product that implements enough features to be usable by early customers or users who can then provide feedback for product enhancement or future product development.

- Keep your MVP simple and add features as you go to avoid **feature creep**. Slack out this article on [feature creep](https://uxdesign.cc/features-creepers-the-customer-experience-horror-story-124c8fa73edf) to the students.

- **Remember the project metrics.**: Projects will be evaluated on their concept, design, functionality, collaboration, and presentation.

Answer any questions before moving on.

---

### 8. Student Do: Project Time (30 min)

Explain to the students that the remaining class time will be spent working in groups on their projects. Announce the project groups, and then highlight the following points:

- Use office hours to ask questions about your project.

- Communication is key when it comes to successfully completing a group project. Be sure to meet with your group regularly.

- Plan to work with your group outside of class. This is your third project that you’ve done for this course, so implement best practices that you learned from your previous two projects.

Students should break into their project groups. If you’re having an online class, you can use the [breakout rooms feature of Zoom](https://support.zoom.us/hc/en-us/articles/206476313-Managing-Breakout-Rooms) for this. You and the TAs should provide support to each group and give a final sign-off on their project proposals. Every group should have an approved proposal by the end of class today.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
