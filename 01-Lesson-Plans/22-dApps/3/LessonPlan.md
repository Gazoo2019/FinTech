## 22.3 Lesson Plan: Building Certificate Smart Contracts

### Overview

In this class, the students will have the opportunity to review the previous lessons regarding the ERC-721 implementation of non-fungible tokens (NFTs).

They’ll spend the first part of the class building and deploying a certificate NFT.

They’ll spend the latter part of the class beginning the work on their Capstone projects.

### Class Objectives

By the end of the class, the students will be able to:

- Define a smart contract based on the ERC-721 NFT standard to issue certificates.

- Build a dApp using the Streamlit library.

- Start working on their Capstone project.

### Slideshow and Time Tracker

- You can review the slides for this lesson on Google Drive: [Lesson 22.3 slides](https://docs.google.com/presentation/d/1UQeaAG1rzNE4yA_McHxvvzkNhgWMkq_tcBDzIQWAq20/edit?usp=sharing).

- To add the slides to the student-facing repository, first download the slides as a PDF. To do that, on the **File** menu, select **Download**, and then select **PDF Document (.pdf)**. Then add the PDF file to your class repository along with other necessary files. You can review these instructions in the [Sharing Slides with Students](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing) document.

  **Note:** Edit access is not available for this document. If you want to modify the slides, create a copy by selecting **Make a copy** on the **File** menu.

- You can review the Time Tracker for this lesson in the following file: [Time Tracker](TimeTracker.xlsx).

### Instructor Notes

- This class won’t cover any new material. It will be heavily driven by the student activity, which focuses on building a certificate NFT.

- **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

## Class Activities

### 1. Instructor Do: Welcome the Class (10 min)

Welcome the students back to class! By the end of today’s lesson, they’ll have begun work on their Capstone project. This is a major milestone in their quest to become fintech professionals and should be celebrated (but not too much). They still have much work to do.

Remind the students that the previous class introduced them to two concepts: Solidity events and the use of IPFS and Pinata for decentralized storage.

Ask the class the following recall questions. If no one volunteers a response, provide them with the answers:

- **Question:** What are some benefits of Solidity events?

  - **Answer:** They may have a lower cost for gas than functions do.

  - **Answer:** They allow you to keep an on-chain log of information.

  - **Answer:** They’re significantly cheaper than contract storage.

  - **Answer:** They’re the built-in way in Solidity to interact with something external, like a UI.

- **Question:** What are some potential issues that IPFS seeks to solve?

  - **Answer:** Web inefficiencies. These include duplicate files and the need to route to a distant server to get a needed file when that file might exist nearby.

  - **Answer:** File integrity issues, like not knowing whether files accessed over the web have changed.

  - **Answer:** Security issues, like the fact that centralized servers provide a centralized attack vector.

- **Question:** Having written many smart contracts and now deployed a decentralized application, or dApp, what are some contracts that you believe a dApp can use?

  - **Potential Answer:** A contract that tracks the unchanging locations of historical landmarks.

  - **Potential Answer:** A contract that transfers tokens between two users in a decentralized product-swapping website.

  - **Potential Answer:** A contract that maintains an unchanging list of user achievements in an online course dApp.

  - **Potential Answer:** Any smart contract that one can think of. The Ethereum blockchain is a globally distributed data store and supports the development of any type of software application that uses the Solidity programming language.

---

### 2. Everyone Do: Certificate Contract (30 min)

**Corresponding activity:** [Certificate Contract](Activities/01-Evr_Certificate_NFT)

**File:** [Certificate NFT](Activities/01-Evr_Certificate_NFT/Solved/certificate.sol)

In this code-along activity, you’ll guide the students step by step through building a certificate token based on the ERC-721 NFT standard.

Propose the following thought experiment, giving students the opportunity to discuss the problem and solution:

- Suppose that the administrators of this course decided to issue your fintech certificate of completion on the Ethereum blockchain. Would you consider this certificate a fungible or a non-fungible token? What kinds of information might the certificate include? Would you include this information inside or outside the token?

Give the students an opportunity to discuss the preceding questions, and be sure that the following points get highlighted:

- Because certificates are unique to each individual, they’re non-fungible assets.

- Each certificate will likely include the program title, the date of completion, and the individual's name.

- Although this information can be stored directly in the token, storing on-chain data has an associated cost. This is because Ethereum [charges fees for smart contracts](https://ethereum.org/en/developers/docs/gas/).

- For the short term, we’ll ignore those extra storage costs and focus on building a simple certificate token. Later, with time permitting, we can expand the contract to use more-efficient methods of data storage.

Start the code-along by asking the students to open a [Remix IDE](https://remix.ethereum.org/) session and then create a new contract named `certificate.sol`.

You’ll take the students line by line through building a certificate token smart contract. These instructions are divided into the following subsections:

1. Add the Pragma and Import Statements

2. Define the Contract

3. Define the Constructor

4. Define a Function to Award Certificate Tokens

5. Complete the Function

Here’s the complete code of the certificate token smart contract:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract Certificate is ERC721Full {
    constructor() public ERC721Full("Certificate", "CERT") {}

    function awardCertificate(address student, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newCertificateId = totalSupply();
        _mint(student, newCertificateId);
        _setTokenURI(newCertificateId, tokenURI);

        return newCertificateId;
    }
}
```

**Note:** When you deploy the contract later, you might need to adjust the Gas Limit parameter in Remix by increasing it over the amount that Remix details by default. Adjusting it from 3000000 to 5000000 usually works.

#### Step 1: Add the Pragma and Import Statements

First, add the pragma statement to define the compiler version to use for this token contract, as the following code shows:

```solidity
pragma solidity ^0.5.0;
```

Next, import the `ERC721Full` contract, as the following code shows:

```solidity
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
```

Explain the following about the `import` statement:

- The `ERC721Full` contract is an [OpenZeppelin implementation](https://docs.openzeppelin.com/contracts/2.x/erc721) of the [ERC-721 NFT standard](https://eips.ethereum.org/EIPS/eip-721).

- The `ERC721Full` version specifically includes all the token extensions that we’re likely to need for this type of token.

- If we import the file in Remix, the file downloads to the files list in Remix. The code at the Github URL then matches this downloaded code.

  - **Important:** Other IDEs might not be able to import contracts this way. Instead, we’d need to manually copy the file to a local version.

#### Step 2: Define the Contract

Define the certificate contract and explain the following:

```solidity
contract Certificate is ERC721Full {

}
```

- The `Certificate` contract `is` an `ERC721Full` contract because it inherits the smart contract code using the `is` keyword.

- Inheritance is a way to derive all of the code from the parent contract (ERC721Full in this case) and then extend it with custom code and configuration.

#### Step 3: Define the Constructor

Define the constructor for the certificate contract, as the following code shows:

```solidity
constructor() public ERC721Full("Certificate", "CERT") {}
```

Explain the following about this constructor:

- The certificate contract requires a constructor. Because we don't have anything yet that needs to be configured on contract deployment, we create a constructor that just calls the constructor of `ERC721Full` with the required values for the token name and token symbol.

  - We can find the `ERC721Full` constructor parameters in the [OpenZeppelin documentation](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721#ERC721Full-constructor-string-string-) and in the [contract code](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/837828967a9831e4333d5fb9edefb200a357d24d/contracts/token/ERC721/ERC721Full.sol#L15).

- The constructor of the certificate calls the constructor of `ERC721Full` to set the name to "Certificate" and the symbol to "CERT" for the token.

- The constructor of the certificate is public. So, it can be called externally from tools like Remix. In our case, we call the constructor whenever we click the Deploy button in the Remix IDE.

#### Step 4: Define a Function to Award Certificate Tokens

Explain that the last thing we need to do is create a function that can mint new certificate tokens and assign them to a recipient.

Define the function at a high level to start, as the following code shows:

```solidity
function awardCertificate(address student, string memory tokenURI)
        public
        returns (uint256)
    {
        // TODO: we will complete this in a moment

        return newCertificateId;
    }
```

Explain the following about this function:

- The `awardCertificate` function is a public function that accepts the address for the recipient (which is the student) and a URI for the certificate.

- For now, `tokenURI` can be just a string that we enter. Later, we can enhance this part of the contract by using decentralized file storage.

- The function will mint (that is, create) a new token and return its ID.

#### Step 5: Complete the Function

To complete the function, start by adding the following line of code:

```solidity
uint256 newCertificateId = totalSupply();
```

Explain the following:

- The first thing that we need to do is create a new token ID. We could use a counter for this. But, a common trick is to use a function that the `ERC721Full` contract already includes&mdash;specifically, the function named [totalSupply](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721#ERC721Enumerable-totalSupply--).

- The `totalSupply` function returns the total number of tokens that the contract has created. If we start our token IDs at zero, we can use the value that `totalSupply` returns as the new token ID. For example, if no tokens exist, `totalSupply` will return zero, which we can use as the first token ID. If we then mint a second token, `totalSupply` will return 1 (because we already have our first token). We can then use 1 as the ID of the second token, and so on. This is a clever way to increment the token ID based on the total supply of tokens.

- Once we have the new token ID, we can call the `_mint` function of `ERC721Full` to mint a new token with this ID, as the following code shows:

  ```solidity
  _mint(student, newCertificateId);
  ```

- The [\_mint](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721#ERC721Enumerable-_mint-address-uint256-) function accepts the recipient address (in our case, the student address) and the new token ID and creates the token.

- Finally, we call the [\_setTokenURI](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721#ERC721Metadata-_setTokenURI-uint256-string-) function to permanently associate the token URI with the token, as the following code shows:

  ```solidity
  _setTokenURI(newCertificateId, tokenURI);
  ```

- This token URI can be a real URI or URL to a certificate file on the internet. But for now, we can send just a string of text to this function. 

Show the final contract to students, and slack out this code so that everyone has a working version:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract Certificate is ERC721Full {
    constructor() public ERC721Full("Certificate", "CERT") {}

    function awardCertificate(address student, string memory tokenURI)
        public
        returns (uint256)
    {
        uint256 newCertificateId = totalSupply();
        _mint(student, newCertificateId);
        _setTokenURI(newCertificateId, tokenURI);

        return newCertificateId;
    }
}
```

Ask for any remaining questions before moving on to testing and deploying the contract in Remix, MetaMask, and Ganache.

---

### 3. Everyone Do: Building Decentralized dApps (20 min)

**Corresponding activity:** [Certificate dApp](Activities/02-Evr_Certificate_dApp)

**Files:**

[Solution folder](Activities/02-Evr_Certificate_dApp/Solved)

[Starter folder](Activities/02-Evr_Certificate_dApp/Unsolved)

In this code-along activity, the class will build the Streamlit application that allows for interaction with the `awardCertificate` contract from a front-end interface.

Ask the students if anyone can explain what a dApp is and how it differs from a normal application. After a brief class discussion, introduce the students to dApps by using the following talking points:

- One of the main features that’s related to the success of Ethereum is dApps.

- Most applications are centralized, with a central computer that runs the programming logic for the application. Centralized applications suffer from many of the same limitations and issues as centralized financial systems. These include having a single point of failure and ownership and governance issues.

- Even though dApps often behave like regular applications, they run their core logic on the blockchain in a decentralized manner. In fact, web applications themselves can become decentralized by using blockchain web hosting services.

Explain to the students that they’ve been building dApps all along with Streamlit and Web3.py. Highlight the following points:

- With Streamlit and Web3.py, we can build web applications that allow the public to easily interact with smart contracts on the blockchain.

- The dApps act as the bridge between the users and the contracts.

Explain that to use Streamlit and Web3.py to interact with the contract, we need to import a compiled version of the contract from Remix that’s an Application Binary Interface, or ABI, file.

In the Remix IDE, first compile the `certificate.sol` file, then copy the ABI file from the **Solidity compiler** pane as the following image shows:

![A screenshot shows how to copy the ABI file in the Remix IDE.](Images/remix-copy-abi.png)

Next, paste it into the `certificate_abi.json` file, located in the compiled folder of the repo, as the following image shows:

![A screenshot shows the certificate.abi.json file.](Images/abi-json.png)

Then highlight the following points:

- The ABI file has information about the functions and data that Web3.py needs to connect.

- We can load the ABI file into a Python program by first using the `with-open` statement and then using `json.load` to parse the JSON file into a Python dictionary, as the following code shows:

  ```python
  with open(Path('./contracts/compiled/certificate_abi.json')) as f:
      certificate_abi = json.load(f)
  ```

- Web3.py can use the ABI dictionary and the address to connect to the smart contract, as the following code shows:

  ```python
  # Set the contract address (this is the address of the deployed contract)
  contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

  # Get the contract
  contract = w3.eth.contract(
      address=contract_address,
      abi=certificate_abi
  )
  ```

- We can then use the contract object to call functions and perform transactions on the contract&mdash;just like we do by using the buttons and boxes in the Remix IDE. The following example calls the `totalSupply` function, which is part of the token, and then prints the total number of certificate tokens that have been created:

  ```python
  print(contract.functions.totalSupply().call())
  ```

- Highlight another example of a `contract.functions` call&mdash;specifically, a call from the Display Certificate portion of the Streamlit code. The following function makes a call to retrieve the address of the certificate owner:

  ```python
  certificate_owner = contract.functions.ownerOf(certificate_id).call()
  ```

- Finally, to use this code in Streamlit, the contract needs to be cached. Otherwise, any change to any input in the application would result in the contract getting reloaded, which would be inefficient. The following code shows how to cache the contract when its loaded:

  ```python
  ## Cache the contract on load
  @st.cache(allow_output_mutation=True)
  # Define the load_contract function
  def load_contract():

  # Contract functions here

  # Return the contract from the function
  return contract
  ```

Now, show the following code in its entirety:

```python
# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load Art Gallery ABI
    with open(Path('./contracts/compiled/certificate_abi.json')) as f:
        certificate_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=certificate_abi
    )
    # Return the contract from the function
    return contract


# Load the contract
contract = load_contract()
```

Explain the following points”

- The cache decorator with `allow_output_mutation=True` allows us to load the contract only once.

- The `allow_output_mutation=True` parameter tells Streamlit not to hash the contract. This resembles the Streamlit recommendation for handling database connections, which the [advanced caching](https://docs.streamlit.io/en/stable/caching.html#advanced-caching) page in the Streamlit documentation describes.

Explain that for our purposes, we can simply reuse the preceding code anytime that we need to load a contract with Web3.py and Streamlit.

Tell the students that they’ll use what they've learned so far to build their own dApp for the certificate contract in the next activity.

---

### 4. Student Do: Building a Certificate dApp (25 min)

**Corresponding activity:** [Certificate dApp](Activities/03-Stu_Certificate_dApp)

**Files:** [Starter folder](Activities/03-Stu_Certificate_dApp/Unsolved)

**Instructions:** [Instructions](Activities/03-Stu_Certificate_dApp/README.md)

Slack out the preceding files and instructions to the students.

In this activity, the students will build a dApp that’s capable of awarding certificate tokens.

---

### 5. Instructor Do: Review Building a Certificate dApp (10 min)

**Corresponding activity:** [Certificate dApp](Activities/03-Stu_Certificate_dApp)

**Files:** [Starter folder](Activities/03-Stu_Certificate_dApp/Solved)

This activity review should revolve around the code in the `app.py` file. Prior to starting the review, be sure to have Ganache accounts loaded into MetaMask and to have Metamask linked to the `certificate.sol` contract in Remix. This contract will need to be deployed so that the address can be copied into the local `.env` file.

Open the solution, and then take the students through the code. Highlight the following points:

- Once we have the contract loaded, we can use any of the functions and attributes that Web3.py provides for contracts. This gives us lots of flexibility with how we design and choose the Streamlit components for the application.

- First we complete the code in the `load_contract()` function:

  ```
  # Load Art Gallery ABI
  with open(Path('./contracts/compiled/certificate_abi.json')) as f:
      certificate_abi = json.load(f)

  # Set the contract address (this is the address of the deployed contract)
  contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

  # Get the contract
  contract = w3.eth.contract(
      address=contract_address,
      abi=certificate_abi
  )
  ```

- The following code gets a full list of the available accounts and then uses it in a drop-down selection list. We could also have created this as a text input box. Building dApps is open to creativity!

  ```python
  accounts = w3.eth.accounts
  account = accounts[0]
  student_account = st.selectbox("Select Account", options=accounts)
  ```

- Inside the Streamlit button, we can then call our `awardCertificate` function by using Web3.py and supply the arguments for the function by using the Streamlit component values.

  - Remember that the `awardCertificate` function requires a transaction for us to mint the certificate token, as the following code shows:

  ```python
  if st.button("Award Certificate"):
      contract.functions.awardCertificate(student_account, "FinTech Certificate of Completion").transact({'from': account, 'gas': 1000000})
  ```

- Other Web3.py functions don’t require a transaction. That's because Web3.py allows us to call certain functions just to access the values.

- The following code uses the Web3.py `contract.functions` object together with the `ownerOf` and `tokenURI` functions to display the values in the application:

  ```python
  certificate_id = st.number_input("Enter a Certificate Token ID to display", value=0, step=1)
  if st.button("Display Certificate"):
      # Get the certificate owner
      certificate_owner = contract.functions.ownerOf(certificate_id).call()
      st.write(f"The certificate was awarded to {certificate_owner}")

      # Get the certificate's metadata
      token_uri = contract.functions.tokenURI(certificate_id).call()
      st.write(f"The certificate's tokenURI metadata is {token_uri}")
  ```

Use the following talking point to discuss the token URI and to set up a discussion around decentralized file storage:

- Now, let's chat for a minute about that token URI. We were cheating by using strings of text for it. What we really need is a secure and robust way to associate digital files with the transactions on the blockchain. That way, we’ll store them neither directly in the smart contract nor in a centralized location. Ideally, this would be done with a peer-to-peer, decentralized file storage system that works directly with the blockchain such as IPFS.

Answer any remaining questions about Ganache, Metamask, Remix, Solidity and the integration with Web3.py and Streamlit before moving to the break.

---

### 6. Break (15 min)

---

### 7. Students Do: Project Work Time (70 min)

Explain to the students that the remaining class time will be spent working in groups on their projects. Highlight the following points from the previous class:

- Use office hours to ask questions about your project.

- Communication is key when it comes to successfully completing a group project. Be sure to meet with your group regularly.

- Plan to work with your group outside of class. This is your third project that you’ve done for this course, so implement best practices that you learned from your previous two projects.

Students should break into their project groups. If you’re having an online class, you can use the [breakout rooms feature of Zoom](https://support.zoom.us/hc/en-us/articles/206476313-Managing-Breakout-Rooms) for this. You and the TAs should provide support to each group.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
