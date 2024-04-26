## 22.2 Lesson Plan: Optimizing Decentralized Applications

### Overview

In this lesson, the students will learn how to optimize a dApp by following the ERC-721 standard. In the first part of today's lesson, the students will learn about events and filters as they relate to the ERC-721 standard. First, they'll optimize their contract by using events and filters to add an appraisal feature to the `ArtToken` contract. Then, they'll apply this feature to the front end of the dApp by using Streamlit.

In the second part of the lesson, the students will incorporate their `ArtToken` dApp with the InterPlanetary File System (IPFS) for decentralized storage.

---

### Class Objectives

By the end of the class, the students will be able to:

- Explain what Solidity events are and how they can be used to enhance a dApp.

- Use filters in Web3.py to react to events from smart contracts.

- Use the InterPlanetary File System (IPFS) to store immutable data off-chain in order to both save gas and ensure the decentralized nature of the dApp.

---

### Instructor Notes

- For more information about the InterPlanetary File System, refer to the [IPFS documentation](https://docs.ipfs.io/).

- The activities in this lesson will use the [Pinata cloud](https://pinata.cloud/) to upload files to IPFS. Sign up for the Pinata cloud application before class. You can sign up for the “Free Plan” that will provide the options required for this lesson.

- Also, one of the activities in this lesson requires your Pinata API keys, so make sure that the account you create can be used for teaching purposes—you will need to show your account details and files to the class.

- **Important:** Pragma requirements are constantly changing. You may come across files that fail to compile due to pragma updates. If so, the error message in Remix will indicate what pragma and compiler version are necessary to resolve the error.

- For today's activities, make sure your Remix compiler is set to at least `0.5.1`.

---

### Slideshow and Time Tracker

- The slides for this lesson can be viewed on Google Drive here: [Lesson 22.2 slides](https://docs.google.com/presentation/d/1wssV_k7gCUDNdObSeNU1gJLxWNU_VSbvsb6rTrXtzHk/edit?usp=sharing).

- To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

- **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting “Make a copy”.

- The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

## Class Activities

### 1. Instructor Do: Welcome the Class (5 min)

In this section, you’ll welcome the students to the class, and then provide a brief refresher on what they learned in the previous class.

Welcome the students to class. Begin by reminding them what they learned previously.

- In the previous lesson, you learned more about decentralized applications, or dApps.

- dApps leverage the decentralized structure of the blockchain in order to build financial systems. dApps also provide the tools that directly enable these systems.

Next, review concepts from the previous lesson by using the following question-and-answer format.

- **Question:** What are some differences between fungible and non-fungible tokens?

  - **Answer:**

    - Non-fungible tokens are unique, fungible tokens are not unique.

    - Fungible tokens are interchangeable while non-fungible tokens are not.

    - Fungible tokens use the ERC-20 standard, while non-fungible tokens use ERC-721.

- **Question:** What are some examples of non-fungible assets?

  - **Answer**: Art, diamonds, land ownership

- **Question:** Which features of blockchain underlie the DeFi movement?

  - **Answer:** Open, decentralized, permissionless

Ask the students if they have any questions before moving on.

---

### 2. Everyone Do: Create an Art Registry Contract (20 min)

**Corresponding activity:** [Art Registry](Activities/01-Evr_Art_Registry)

In this activity, you and the students will build a smart contract that allows the user to add appraisal values and comments to a tokenized piece of art. The focus is on using events and filters to build out the contract. You will live code as the students follow along.

Have a TA slack out the [starter file](Activities/01-Evr_Art_Registry/Unsolved/ArtRegistry.sol) for this activity to the students so that they can code along.

**Files:**

[Starter file](Activities/01-Evr_Art_Registry/Unsolved/ArtRegistry.sol)

[Solution file](Activities/01-Evr_Art_Registry/Solved/ArtRegistry.sol)

Begin by explaining to the students that, in this activity, they will continue to expand their knowledge of the ERC-721 standard that they used to build their `ArtToken` contract.

- You’ll now build an `ArtRegistry` contract that will use the ERC-721 tokens to register new pieces of artwork. This new contract will expand on the prior functionality by providing a way to appraise the artwork.

- To accomplish this, we’ll optimize the smart contract by using events and filters.

- If you choose to focus on blockchain for your final project, you will likely need to use events and filters in order to optimize your smart contract.

#### Create the Art Registry Contract

Start by examining the code included in the starter file:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtRegistryToken", "ART") public { }

}
```

Highlight the following about this code for the students.

- As with the previous `ArtToken` contract, the `ERC721Full` contract is used to implement the token standard.

- This code imports the `ERC721Full` contract and then creates a new `ArtRegistry` contract that inherits code from it.

- “ArtRegistryToken” is the first parameter. This parameter defines the `name` of our non-fungible token. “ART” is the second parameter, which defines the token `symbol`.

Ask the students if they have any questions about the code up to this point.

#### Define a Data Structure for a Piece of Artwork

Explain that the next step is to define the structure, or `struct`, for the artwork information, including the name of the artwork, the name of the artist, and the current appraisal value. Here’s the code:

```solidity
struct Artwork {
    string name;
    string artist;
    uint256 appraisalValue;
}
```

Highlight the following about the code for the students.

- The contract needs a way to represent the artwork information, like the name of the artwork, the name of the artist, and the current appraisal value.

- While it’s possible to create separate variables for each piece of information, we’ll instead group them together into a `struct`, which is short for “structure.” A `struct` is similar to a Python data class. Ethereum developers frequently use the `struct` to organize related pieces of data.

- To define a `struct`, we name and define a unique data type, which consists of a structured collection of data.

- Inside the `struct`, we define the name and the type of each variable that belongs to the `struct`.

- In Solidity, the variables that exist inside a `struct` are called **members** (or, sometimes, **fields**).

- For the `ArtRegistry` contract, we will use the keyword `struct` followed by the name `Artwork`. The `struct` will contain three pieces of data:

  - A string named “name” that contains the name of the artwork.

  - A string named “artist” that contains the name of the artist.

  - An unsigned integer named “appraisalValue” that contains the currently appraised value of the artwork.

- Organizing related pieces of data makes it easier to use them with other data types, such as mappings.

#### Define a Mapping to Associate a Token Identifier with a Piece of Artwork

In this section, you will define the mapping that associates a token identifier, that will be referenced by using the `token_id` variable (which is of type `uint256`) with the `Artwork` struct that was previously defined, as shown in the following code.

```solidity
mapping(uint256 => Artwork) public artCollection;
```

First, remind students that a **mapping** associates (or maps) one piece of data to another. The goal of this piece of code is to map the token ID that is eventually assigned to the data associated with the individual piece of art.

- We want to map each token ID (which is of type `uint256`) to our defined `Artwork` data structure.

- This mapping will provide a way to associate each art token with each instance of an artwork's information (as defined in the `struct`).

- We name our mapping `artCollection`.

- The data that we store on-chain for each art token is contained in this `artCollection` mapping.

#### Define an Event that Logs a New Appraisal to the Blockchain

In this section, you will introduce the concept of the art registry and how events are used to categorize and store a new appraisal value on-chain.

Live code the following and explain it to the students.

```solidity
event Appraisal(uint256 token_id, uint256 appraisalValue, string reportURI);
```

- In the `Artwork` data structure, `appraisalValue` was defined as an unsigned integer. A token can thus have only a single appraisal value at any particular time. With an **art registry**, which is what we are designing, the intention is to keep a full history of the changing appraisal values.

- An **art registry** is a list of the artwork and its metadata (that is, its relevant information) that gets sent to a gallery or to potential buyers.

- We could create a mapping or use another data type to keep a list of the appraisal values, but that would create a cost issue when using a blockchain. The more information that is stored on-chain, or the more transactions that a contract generates, the more gas fees that are paid.

- Instead of storing the appraisal data directly in the smart contract, we want a more efficient and cost-effective way to record that data. We can do so by using events.

Have a TA slack out the Solidity documentation on [events](https://docs.soliditylang.org/en/v0.8.2/abi-spec.html?highlight=events#events) so that the students can learn more.

- With Ethereum and many other blockchains, storing data in the contract and on-chain is expensive. To counter this issue, a new mechanism in Solidity has been created: the event. An **event** in Solidity is an inexpensive way to record data as a log entry on the blockchain. Historical changes in values can be documented without storing them directly in the contract.

- Events work in a similar way as functions. First, an event is defined. In this case, an event named `Appraisal` is defined. The `Appraisal` event has three parameters: `token_id` (of type `uint256`) `appraisalValue` (of type `uint256`), `reportURI` (of type `string`).

- The event can be accessed, or **fired**, from any function inside the contract. When the event is fired, the arguments that get passed to the event will be recorded as a log entry on the blockchain. The `Appraisal` event will be used to log new artwork appraisals to the blockchain.

Transition to the next section by explaining the following:

- Now that the code defines a `struct` that stores the metadata for the `Artwork`, and an `event` that catalogs the new `Appraisal` value, it’s time to focus on the code associated with registering a piece of artwork.

#### Define a Function that Registers a Piece of Artwork

In this section, you will write the code that allows a user to register a new piece of artwork. The `registerArtwork` function will contain variables similar to those defined in the `Artwork` struct, as well as an `initialAppraisalValue`, and the `tokenURI`.

Some of this code should be familiar to the students, as it’s based on the `ArtToken` created in the prior lesson.

```solidity
function registerArtwork(
    address owner,
    string memory name,
    string memory artist,
    uint256 initialAppraisalValue,
    string memory tokenURI
) public returns (uint256) {

    // TODO: register new artwork here

}
```

As you live code, highlight the following for the students.

- The next step is to create a function to register a piece of artwork. The function is named `registerArtwork`. It’s defined as a `public` function that’s responsible for registering a new piece of artwork on the chain. Finally, it returns the ID of the newly minted token as a `uint256`.

The function consists of the following parameters:

- `owner`: The Ethereum address of the owner of the artwork

- `name`: The name of the artwork

- `artist`: The name of the artist

- `initialAppraisalValue`: The initial appraisal value of the artwork

- `tokenURI`: The URI to where the artwork resides on the internet. Because the `tokenURI` argument will link to a file that resides on the internet, this will be a point of centralization. But, we’ll solve that issue later in the lesson. For now, we just need to store a string.

Explain to the students that, after defining the parameters of the `registerArtwork` function, we’ll write the body of the function.

#### Code the Body of the Registered Artwork

In this section, you will code the body of the `registerArtwork` function. Similar to the prior `ArtToken` smart contract, this will consist of generating the `tokenId`, minting a new token, and setting the token URI.

This code will also set the `tokenId` equal to the metadata associated with the new registered artwork: the name of the artwork, the artist, and the initial appraisal value.

Finally, the token ID is returned from the function. Here’s the code:

```solidity
uint256 tokenId = totalSupply();
_mint(owner, tokenId);
_setTokenURI(tokenId, tokenURI);

artCollection[tokenId] = Artwork(name, artist, initialAppraisalValue);

return tokenId;
```

- As with the `ArtToken`, the next `tokenId` is generated by using the ERC-721 `totalSupply` function.

- The `_mint` method of `ERC721Full` is used to mint a new token for the owner address.

- The `_setTokenURI` method of `ERC721Full` is called and passed two arguments. The first argument is the generated `tokenId` value, and the second argument is the `tokenURI` value that was passed to the `registerArtwork` function. This call permanently associates the `tokenURI` value with the `tokenId`.

- Now that the token URI is set, it needs to be associated with all the other arguments that were passed to `registerArtwork` with the token. This is done using `artCollection` mapping and the `Artwork` data structure that we defined earlier. Specifically, the `tokenId` is used as the key in the `artCollection`, and the members of the `Artwork` structure are used as the values to link.

- Finally, we return the new token.

Confirm that the `registerArtwork` function appears as follows:

```solidity
    function registerArtwork(
        address owner,
        string memory name,
        string memory artist,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        artCollection[tokenId] = Artwork(name, artist, initialAppraisalValue);

        return tokenId;
    }
```

Ask the students if they have any questions regarding the newly coded `registerArtwork` function, and how it relates to both the `Artwork` struct and the mapping to the `artCollection.

Ask for a student volunteer to review the code step by step, explaining what happens when the `registerArtwork` function is called. If no one volunteers, explain to the students that the code we just wrote allows us to register a piece of artwork.

Ask if there are any questions about the code up to this point. Then, proceed to the next step: defining a function that allows us to add a new appraisal for an art token.

#### Define a Function that Adds a New Appraisal

In this section, you will generate the code that tracks a new appraisal value for the registered artwork. The `newAppraisal` function will take in three parameters: the token ID, the new appraisal value, and the appraisal report URI. The public function will return an unsigned integer. Here’s the code:

```solidity
function newAppraisal(uint tokenId, uint newAppraisalValue, string memory reportURI)
    public
    returns (uint256) {
    // TODO: Add appraisal code here
}
```

As you live code, highlight the following to the students:

- To define a function that allows us to add a new appraisal, a second public function is defined and named `newAppraisal`.

- Our `newAppraisal` function has three parameters: `tokenId` (of type `uint256`), `newAppraisalValue` (of type `uint256`), and `reportURI` (of type `string memory`).

- This function is responsible for firing an event that will log the full appraisal report to the blockchain. The event will log this report as a URI that points to the appraisal report file.

Then, explain that the next step is to write the body of the `newAppraisal` function. Once the `appraisalValue` is updated with the `newAppraisalValue`, the `Appraisal` event that was created earlier is fired. Here’s the code:

```solidity
artCollection[tokenId].appraisalValue = newAppraisalValue;

emit Appraisal(tokenId, newAppraisalValue, reportURI);

return artCollection[tokenId].appraisalValue;
```

As you live code, highlight the following to the students.

- First, the `appraisalValue` of the artwork is updated with the `newAppraisalValue` of the token that was passed to our function.

- This new appraisal value is logged to the blockchain by firing the `Appraisal` event created earlier. The `emit` keyword is used to fire the event and log the value.

- In the next section, we’ll use `Web3.py`'s **filter** functionality to read the event log created by the appraisal event.

- Finally, the updated appraisal value is returned.

Confirm that the complete code for the `ArtRegistry` contract is now as follows:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtRegistry is ERC721Full {
    constructor() public ERC721Full("ArtToken", "ART") {}

    struct Artwork {
        string name;
        string artist;
        uint256 appraisalValue;
    }

    mapping(uint256 => Artwork) public artCollection;

    event Appraisal(uint256 token_id, uint256 appraisalValue, string reportURI);

    function registerArtwork(
        address owner,
        string memory name,
        string memory artist,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        artCollection[tokenId] = Artwork(name, artist, initialAppraisalValue);

        return tokenId;
    }

    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {
        artCollection[tokenId].appraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        return artCollection[tokenId].appraisalValue;
    }
}
```

Ask the students if they have any questions about the process of logging the new appraisal value to the blockchain or how the appraisal event functions.

Review the concepts covered in the lesson so far by asking the students the following questions:

- **Question:** Why is a `struct` a useful data structure?

  - **Answer:** A `struct` allows you to create new dynamic data structures, data structures that contain multiple types, and objects.

- **Question:** What is the purpose of Solidity events?

  - **Answer:** Events are an inexpensive way of logging information on the blockchain. They allow dApps to update and monitor given values on the blockchain.

Ask if there are any questions about any of the code or concepts covered up to this point.

Then, congratulate the students on creating a smart contract that can both mint new artwork tokens and add new appraisals for each piece of art.

- The contract also uses a cost-effective method of logging historical data and external appraisal reports via the `Appraisal` event that we created.

Explain that, in the next section, you’ll demonstrate how the Web3.py filter functionality is used by the front end of the dApp to read the event log.

---

### 3. Instructor Do: Creating the dApp Filters (10 min)

**Corresponding activity:** [dApp Filters](Activities/02_Ins_dApp_Filters)

In this demonstration, you will show students how to apply Web3.py filters to the front end of a decentralized application.

**Files:**

[Starter file](Activities/02_Ins_dApp_Filters/Unsolved/app.py)

[Solution file](Activities/02_Ins_dApp_Filters/Solved/app.py)

#### Introduce Web3.py Filters

Start by explaining that, because our contract can store data in the event log, we need to build a way to access that historical data. The ERC-721 standard provides the tools needed for managing these events.

- Solidity automatically inherits all the code for managing events from the `ERC721Full` contract. To access the event data, a filter for the event needs to be created in the front end of a dApp.

- Why a filter? The reason is that more than one type of event might get logged for the smart contract. We want to be able to choose the event type that we desire to access.

- Web3.py offers the [`createFilter` function](https://web3py.readthedocs.io/en/stable/contracts.html#web3.contract.Contract.events.your_event_name.createFilter) that can be used to create the necessary filter.

Open the documentation and share it on your screen. Ask a TA to slack out the [`createFilter`](https://web3py.readthedocs.io/en/stable/contracts.html#web3.contract.Contract.events.your_event_name.createFilter) section of the Web3.py documentation.

#### Filter the Events to Access Historical Data

Explain that, for the `ArtRegistry` contract, the dApp will require using only the `fromBlock` and `argument_filters` parameters of the Web3.py `createFilter` function.

Open the [starter file](Activities/02_Ins_dApp_Filters/Unsolved/app.py) for the front end of what will eventually be the `ArtRegistry` dApp.

Show students that the `load_contract` function is identical to the contract from the `ArtToken` dApp built in the prior lesson. But, in this case, the contract is the deployed `ArtRegistry` contract.

If students ask about the missing code in the "Register New Artwork" and "Appraise Art" sections in the starter code, assure them that they will get the opportunity to both deploy the `ArtRegistry` smart contract and fill in the missing code in the next activity.

Scroll down to the "Get Appraisals" section of the file. Below the Streamlit "Get Appraisal Reports" button, add the following code that creates the filter.

```python
appraisal_filter = contract.events.Appraisal.createFilter(
    fromBlock=0,
    argument_filters={"tokenId": art_token_id}
)
```

As you live code, highlight the following for the students:

- This code creates a new filter for the `Appraisal` event in the `ArtRegistry` contract that finds all the events in the chain for a specified token ID.

- For the `fromBlock` parameter, we specify the starting block in the chain of blocks that we want to access. We want to access all the events in the chain of blocks, so we use zero for this value. This starts the filter at the first block in the chain (that is, at the genesis block).

- With the `argument_filters` parameter, filter the data to just the blocks that contain relevant data. Specifically, we use the token ID to get all the events for a specific token.

#### Apply the Filter

Tell students that, now that we created our filter, we can get all the events by using the [`get_all_entries` function](https://web3py.readthedocs.io/en/stable/filters.html?highlight=get_all_entries#web3.utils.filters.Filter.get_all_entries) from Web3.py. Here’s the code:

```python
appraisals = appraisal_filter.get_all_entries()

for appraisal in appraisals:
    print(dict(appraisal))
```

Explain to the students that calling the filter on the entries results in a Python dictionary. Then, say we’ll now explore the `args` key in order to examine the data that the event originally recorded.

#### Examine the Event Arguments

Explain that, because we converted the appraisal reports to Python dictionaries, we can also use the `args` key to read the arguments that were passed to the event.

Update the code inside the `appraisals` for loop to print the detail of the `args`.

```python
appraisals = filter.get_all_entries()
for appraisal in appraisals:
    report_dictionary = dict(appraisal)
    print(report_dictionary)
    print(report_dictionary["args"])
```

Running this code generates a series of appraisal reports that each resemble the following code snippet. Show students this code (it’s provided in the slides) so that they can examine the output.

```text
{
  "args": "<class 'web3.datastructures.AttributeDict'>",
  "event": "Appraisal",
  "logIndex": 0,
  "transactionIndex": 0,
  "transactionHash": "<class 'hexbytes.main.HexBytes'>",
  "address": "0x27da73d2A832a6EcA6c4Fcaa38354a595C196dE8",
  "blockHash": "<class 'hexbytes.main.HexBytes'>",
  "blockNumber": 9
}

AttributeDict({'tokenId': 0, 'appraisalValue': 100, 'reportURI': 'This art is great!'})
```

Highlight the following for the students:

- The result is output that shows the `tokenId`, `appraisalValue`, and the `reportURI`. In other words, we can review the event dictionary and the arguments that were passed to the event.

- Events and filters provide an efficient way to record historical data for a smart contract, without the expense of storing that data directly in the contract.

Ask the students if they have any questions about how filters and events are used to access historical data associated with a smart contract.

Once all questions have been answered, explain to the students that they will use the `ArtRegistry` contract that was built earlier in the lesson in order to create a dApp that both logs new appraisal events and shows the full history of the appraisals.

---

### 4. Everyone Do: Appraising the Situation (15 min)

**Corresponding activity:** [Appraising the Situation](Activities/03-Evr_Appraising_the_Situation)

This activity focuses on the Streamlit functionality that is required to make the dApp operational. The students will create and deploy a dApp by using the `ArtRegistry` contract and Streamlit.

> **Note:** The students should be increasingly familiar with the process of compiling and deploying a contract by using Remix, Ganache, and MetaMask. So, have these tools launched and ready to go prior to beginning the demonstration.
>
> Also, keep in mind that some students may find it challenging to complete the Streamlit code in the `app.py` file. Therefore, make sure that the TAs are available to assist students who need the support. If many students find this section to be challenging, complete this section as a code-along (you live code, and the students follow along).

First, explain to the students that the starter file contains the code to create the complete `ArtRegistry` contract. The students will be tasked with compiling and deploying it by using Remix, Ganache, and MetaMask.

**Files:**

[Starter folder](Activities/03-Evr_Appraising_the_Situation/Unsolved/ArtRegistry)

[Solution folder](Activities/03-Evr_Appraising_the_Situation/Unsolved/ArtRegistry)

#### Compile and Deploy the Art Registry Contract

The first part of the activity is to compile and deploy the `ArtRegistry` contract by using Remix, Ganache, and MetaMask. The students should be familiar with this process. Be sure to answer questions as they arise.

#### Prepare the Environment File

The next step is to define and connect to a new Web3 provider. In our dApp, this is the Ganache local blockchain.

Remind the students that the URI for the Ganache blockchain should be set up in the `.env` file as follows:

```text
  WEB3_PROVIDER_URI=http://127.0.0.1:7545
```

Navigate between Visual Studio Code and Remix, and review how to access the address of the deployed `ArtRegistry` contract from the Remix IDE and then copy it to the `SAMPLE.env` file that has been provided.

Finally, rename the file from `SAMPLE.env` to `.env` and save it.

#### Build the dApp

In this section, the class will complete the code required to make the `ArtRegistry` dApp function.

Briefly review the code included in the `app.py` file, specifically, the imports and the `load_contract` function. These should be familiar to students, as they encountered them when they built the `ArtToken` dApp.

Also highlight that the `ArtRegistry` ABI code, which is generated when the contract is compiled, is already included in the folder inside the `artregistry_abi.json` file.

Next, point out the three sections of `app.py` that we need to complete: "Register New Artwork," "Appraise Artwork," and "Get Appraisals.”

##### Register New Artwork

Begin with the "Register New Artwork" section. Here’s the code:

```python
st.markdown("## Register New Artwork")

artwork_name = st.text_input("Enter the name of the artwork")
artist_name = st.text_input("Enter the artist name")
initial_appraisal_value = st.text_input("Enter the initial appraisal amount")
artwork_uri = st.text_input("Enter the URI to the artwork")

if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        int(initial_appraisal_value),
        artwork_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")
```

As you live code, ask the students to provide both the variable names and Streamlit components for each element that is required to register the artwork: artwork name, artist name, initial appraisal value, and artwork URI. Each of these variables should use the `st.text_input` function.

Next, create the “Register Artwork” button by using Streamlit.

- In order to register the artwork, use the `contract.functions` syntax followed by the smart contract's `registerArtwork` function.

Navigate to the `registerArtwork` function in the smart contract so that the students can review the information.

- The smart contract's `registerArtwork` function requires five variables: the `owner` address plus the four variables we just created with Streamlit components.

Navigate back to VS Code and explain the following:

- To the `registerArtwork` function call, we will chain the Web3.py `transact` function, passing in parameters for the `from` address and the amount of `gas` to cover the fee.

- All of this is set equal to a variable called `tx_hash`, which is the transaction hash that is returned from the function call.

- The transaction receipt is captured by using the Web3.py’s `w3.eth.waitForTransactionReceipt` function and passing it the `tx_hash`.

- The `st.write` function is used to display the `receipt` to the application page.

Ask the students if they have any questions about the code so far. Once all questions have been answered, move on to the “Appraise Art” section.

##### Appraise Artwork

Next, explain that the following code—which is in the starter code—allows us to input a new appraisal.

```python
st.markdown("## Appraise Artwork")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
new_appraisal_value = st.text_input("Enter the new appraisal amount")
report_uri = st.text_area("Enter notes about the appraisal")
if st.button("Appraise Artwork"):

    # Use the token_id and the report_uri to record the appraisal
    tx_hash = contract.functions.newAppraisal(
        token_id,
        int(new_appraisal_value),
        report_uri
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")
```

The goal of this section is to complete the code that records the new appraisal value to the blockchain when the "Appraise Artwork" button is clicked. Highlight the following to the students:

- Again, the `contract.functions` syntax is used in conjunction with the call to the `newAppraisal` function.

Navigate to Remix to show the students the `newAppraisal` function in the smart contract.

- The `newAppraisal` function takes in three parameters: the token id, the new appraisal value, and the report URI (or the notes about the appraisal).

Return to VS Code and complete the `newAppraisal` function call.

- After defining the three parameters of the `newAppraisal` function, the `transact` function is chained by using the parameter `{"from": w3.eth.accounts[0]}`.

- Based on the [Web3.py contract functions `transact` documentation](https://web3py.readthedocs.io/en/stable/contracts.html?highlight=.transact#web3.contract.ContractFunction.transact), if `gas` is not explicitly provided, the `web3.eth.estimate_gas` method will automatically be invoked.

  > **Note:** Slack out the link to the [Web3.py contract functions `transact` documentation](https://web3py.readthedocs.io/en/stable/contracts.html?highlight=.transact#web3.contract.ContractFunction.transact) to the students.

Ask the students if they have any questions about the code so far.

Once any questions are answered, move on to the “Get Appraisals” section.

##### Get Appraisals

Finally, complete the code for the "Get Appraisals" section of the dApp. Here’s the code:

```python
st.markdown("## Get the appraisal report history")
art_token_id = st.number_input("Artwork ID", value=0, step=1)
if st.button("Get Appraisal Reports"):
    appraisal_filter = contract.events.Appraisal.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": art_token_id}
    )
    appraisals = appraisal_filter.get_all_entries()
    if appraisals:
        for appraisal in appraisals:
            report_dictionary = dict(appraisal)
            st.markdown("### Appraisal Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Appraisal Report Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This artwork has no new appraisals")
```

Explain that the first step is to get the token ID for the artwork whose appraisal history we want to access. Highlight the following:

- The [Streamlit `number_input` component](https://docs.streamlit.io/en/stable/api.html?highlight=number_input#streamlit.number_input) allows us to input an integer value. The `value` parameter will determine the starting value, and we can increase input values by 1 using the `step` parameter.

- Inside the button, a `appraisal_filter` is created calling the `contract.events` function. It references the `Appraisal` event from the smart contract, and then chains the `createFilter` function. The search will start at the Genesis block and will filter based on the artwork token ID.

- A **Genesis block** refers to the first block a token ever created.

- Once all of the appraisals associated with the artwork token ID are accessed, we create a loop that writes each of the reports to the screen.

At this point, stop and ask if there are any questions. This code was likely challenging for the students. Ask if they need clarification about any of the code.

Once all questions have been answered, proceed to the testing phase.

#### Run the dApp

Navigate to the `ArtRegistry` folder in the terminal and run the dApp by using `streamlit run app.py`.

Input the information for a piece of artwork, and then update the appraisal. (Update it twice if time permits, and validate that the appraisal value was updated.)

- The appraisal update, per the resulting output, includes a `gasUsed` parameter, despite the fact that we did not include it with the `transact` function.

Finally, get a list of appraisal information back from the blockchain.

Congratulate the students on navigating one of the most challenging activities they have encountered in the course. It required them to integrate a number of new concepts and functions.

- You have just built another NFT that is compliant with the ERC-721 standard, complete with on-chain, custom members and several linked token URIs.

- You used Solidity events and URIs that allow you to connect both data and a front end to your Solidity smart contract from outside the blockchain.

- You created a sophisticated dApp for this contract, but it’s not quite finished.

Explain that, in the next part of the lesson, we’ll explore how to use decentralized file storage with smart contracts in order to reduce costs while ensuring the integrity of the digital asset.

---

### 5. Instructor Do: Introduction to Decentralized Storage (10 min)

In this section, you will introduce IPFS technology and how it can be used to store immutable, hash-based, content-routed data. The students will observe firsthand how, when combined with blockchain technology, IPFS can store large datasets with the same level of integrity as on-chain data.

Begin by providing some background about IPFS and how it works.

- **IPFS** stands for **InterPlanetary File System**. It’s a protocol, a network, and a file system. But what exactly does this mean and how does it all fit together?

- For two users to exchange data with one another across the internet, they need a common set of rules for how the information is sent between them; this is a communication protocol.

- **Communication protocols** are usually organized as a **protocol suite**. For example, the internet protocol suite is widely used today, and of the protocols that make up that suite, **HyperText Transfer Protocol**, or **HTTP**, is the foundation for communication.

- Another important piece is known as the system's **architecture**, or how the actual computers within the network can communicate with one another. Traditionally, this is done in a **client-server model**. IPFS uses a **peer-to-peer network model**.

- In a typical client-server model, centralized servers store data that is accessed via **location-based addressing**. This provides an easy way to secure and manage data in a scalable manner, though it doesn't come without its drawbacks.

- Because data is stored on centralized servers, anyone with access to those servers, whether an authorized administrator or a hacker with malicious intent, can alter and remove data. This poses problems in both the realms of privacy and security because, in this model, control of the server is equal to control of the data.

- In location-based addressing, a piece of data is recognized by location as opposed to its content. This means that in order to access a piece of data, you must go to its specific location, even if the same data is available from a closer source.

- This also means a client has no de facto way to determine if the data that it has received has been altered, because the client isn't concerned with _what_ the data is but rather _where_ it is.

- The client-server model works well for websites and small pieces of data, but it's not the most efficient when it comes to big pieces of data.

- IPFS aims to address these issues with the traditional client-server model by using a distributed peer to peer file-sharing system.

Now that the students have a general idea of what IPFS is and its goal, explain that, in the next section, they will learn about the [Pinata service](https://www.pinata.cloud/) and how IPFS is a valuable tool for building dApps and decentralized systems.

#### Introducing the Pinata IPFS Service

In this section, you’ll explain IPFS technology and how to use it to store decentralized data.

Begin by reminding the students that blockchain offers a powerful way to maintain the integrity of data. However, storing data on a chain is expensive. This is where a decentralized file system, like IPFS, comes into play. When combined with blockchain, IPFS can store large datasets with the same degree of integrity as on-chain data.

Next, explain IPFS technology in more detail.

- IPFS stores and retrieves files from a decentralized system.

- Instead of using centralized storage, like a database, IPFS distributes each file across multiple nodes in its own network. That is, it breaks down the file into pieces of data and then distributes the pieces across multiple nodes. It does this by using a custom data structure and rules for storing and retrieving the data pieces.

- Participants in the IPFS network can thus share their files. And, smart contracts and dApps can thus store and retrieve their files directly from the nodes that have the data pieces. This means that they store and access their data by using a decentralized technology—without the expense of storing that data on the chain.

- One of the most popular ways for dApps to access IPFS services is through the Pinata IPFS cloud service.

Navigate to the [Pinata webpage](https://pinata.cloud/), and explain that Pinata is a file pinning service for IPFS. We'll learn how to use Pinata to pin files in the next section.

Remind the students that they were asked to create an account in Pinata and access the required API keys as part of the setup for this unit.

If students have previously signed up for a Pinata account and have their API keys accessible, they can begin their break a few minutes early.

Students who have NOT already signed up for a Pinata account and gotten their API keys will need to complete the process by using the [dApp Install Guide](../Supplemental/dApp_Install_Guide.md). The process should take only a few minutes.

Answer any questions before moving on.

---

### 6. Break (15 min)

---

### 7. Instructor Do: Pinning Files with IPFS and Pinata (10 min)

**Corresponding activity:** [IPFS and Pinata](Activities/04-Ins_Pinata)

In this section, you will introduce the Pinata cloud service and demonstrate how to pin a file. Use the `.json` file located in the `Solved` folder. For the sake of this demonstration, it may be helpful to have a copy of this `.json` file on your desktop for easy access.

**File:**

[Mona Lisa Image](Activities/04-Ins_Pinata/Solved/mona_lisa.json)

#### Storing Decentralized Data with IPFS

Explain that, for the integrity of our dApps, we need the data that they reference to always be available. One way to achieve this is to use decentralized storage technologies that are designed to work with dApps.

Remind the students that centralization issues include having a single point of failure, being susceptible to attack, and even encountering access problems.

Slack out the [IPFS website URL](https://ipfs.io/) to the students and explain that it’s used throughout the blockchain community to build robust dApps that use decentralized file storage.

- Note that the techniques for using decentralized storage aren't limited to blockchain. Decentralized storage is applicable to any financial application, machine learning dataset, or blockchain application that can benefit from the robust storage that IPFS provides. You might consider using IPFS for your final project.

One of the most popular ways for dApps to access IPFS services is through the [Pinata](https://pinata.cloud/) IPFS pinning service.

#### Pinning Files with IPFS and Pinata

Navigate to the [Pinata webpage](https://pinata.cloud/), and reiterate that Pinata is a file pinning service for IPFS.

- With IPFS, computers can communicate directly with other computers on the network to store and access files. This differs from the way that web browsers work.

- Pinata provides a web service, called a **gateway**, that allows access to files through a web browser without installing IPFS on a computer. This gateway acts as a bridge between any single computer and the IPFS network.

Have a TA slack out the documentation on the [IPFS gateway](https://docs.ipfs.io/concepts/ipfs-gateway/) so that the students can learn more if they’re interested.

Next, explain the concept of pinning.

- **Pinning** is the act of storing a file on the decentralized IPFS network. Files can be pinned through either the Pinata webpage or the Pinata API.

- With Pinata, files can be hosted on the IPFS network and then referenced by a hash.

Next, you’ll pin a file and review its details.

#### Pin a File and Review Its Details

In this section, you will demonstrate how to pin a file in Pinata and then review the details of the pinned file.

> **Note:** The descriptions and screenshots of the Pinata user interface in this demo reflect how it exists at the time of this writing. However, there might be slight differences because of updates.

To begin, navigate to the [Pinata website](https://pinata.cloud/). The welcome page is shown in the following screenshot.

![A screenshot depicts the Pinata welcome page.](Images/pinata-start-page.png)

Explain that Pinata accounts are free to create, and they allow you to pin files up to a total of 1 gigabyte in IPFS.

The following image should reflect the Pinata dashboard once you have logged in:

![A screenshot depicts the Pinata dashboard.](Images/pinata-user-interface.png)

Highlight that the dashboard initially displays the Pin Manager app. Use the Pin Manager to upload a file to Pinata.

- Recall that each ERC-721 token typically has an associated token URI. This URI is intended to link to an off-chain storage provider, such as IPFS.

- Specifically, the token URI is intended to link to a `.json` file that contains metadata about the artwork file that we store in IPFS.

- The metadata includes information like the name of the artwork, a description, and the address of the artwork. In this case, the address of the digital artwork is also located in IPFS.

Open the file, named [`mona_lisa.json`](Activities/04-Ins_Pinata/Solved/mona_lisa.json), that contains metadata about the _Mona Lisa_ painting and a link to where a digital copy of the painting exists in IPFS. Here’s the metadata shown in the file:

```json
{
  "name": "Mona Lisa",
  "description": "One of the most famous works of art by Leonardo da Vinci",
  "image": "ipfs://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq/I/m/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
}
```

Remind students that a gateway is needed to act as a bridge between our computers and the IPFS network, so in order to access the image in our browser we'll need to prepend `https://ipfs.io/ipfs` to the artwork's ipfs hash. Thus, the link to the Mona Lisa image is as follows:

```
https://ipfs.io/ipfs/bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq/I/m/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg
```

Input the above link to the IPFS Mona_Lisa image into your browser and show the image to the students.

Explain that the piece of artwork—in this case, the digital image of the Mona_Lisa—is located at the IPFS hash address that is detailed in the image link.

Now that the students have observed the metadata in a pinned file, explain that you will now demonstrate the process of uploading a digital artwork to IPFS via Pinata.

On the Pin Manager page, click the Upload menu, as shown in the following screenshot.

![A screenshot points out the Upload menu on the Pin Manager page.](Images/pinata-upload-button.png)

Explain that the Upload menu expands, listing the Folder, File, and CID menu items:

![A screenshot points out the expanded Upload menu.](Images/pinata-upload-folder-file.png)

- Click Folder or File to navigate to an entire folder or a single file, respectively, to upload from our local computer.

- Alternatively, click `CID` to provide a hash for a file that’s already pinned to IPFS. The CID, which stands for **content identifier** for a file, includes a hash of the file and additional information, depending on the CID version. IPFS can then use the hash to retrieve the file from its network.

Have a TA slack out the [Identifier formats documentation](https://docs.ipfs.io/concepts/content-addressing/#identifier-formats) so that the students can review more information about different CID versions.

Because we want to upload the `.json` file containing metadata for the _Mona Lisa_ painting, click File. This displays the Upload File dialog box, as shown in the following image.

![A screenshot depicts the Upload File dialog box.](Images/pinata-upload-window.png)

In the Upload File dialog box, click “Click to upload.” You can then navigate to and select the file on your computer that you want to upload, which is `mona_lisa.json` file.

Next, in the "Name” box, type "Artwork".

- "Artwork" is the descriptive name for the pinned file that will display later in the Pinata dashboard.

Finally, click the Upload button to upload the file, as shown in the following screenshot.

![A screenshot depicts the Upload File dialog box after we select a file and type the custom name for the pin.](Images/pinata-artwork-upload.png)

- When the upload completes, the dialog box closes, and you will be taken back to the Pin Manager page.

Navigate to the My Pins section. Show the students that the upload is now displayed, which means that it’s been pinned to Pinata.

- The name that we typed in the “Name” box displays in the Name column.

- The IPFS CID hash that Pinata generated displays in the IPFS CID column.

- Additional file data is displayed in the remaining columns.

- The CID for a file includes the hash for the file and additional information, depending on the CID version. However, only the hash displays in the IPFS CID column.

- The hash from the IPFS CID column can be used in our dApps and smart contracts to refer to the pinned file. Storing this hash in a smart contract is more memory efficient (that is, it uses less space) than storing the entire file. Less required memory means smaller transaction fees associated with storing information on-chain.

- Rather than storing the image on-chain, the image is stored in the decentralized IPFS network. The on-chain information associated with the artwork is then just the hash associated with the `.json` file containing the appropriate artwork metadata.

Finally, demonstrate that the pinned file is a clickable link.

![A screenshot points out the name of our pin in the Name column of the My Pins section.](Images/pinata-pin-name.png)

- The IPFS CID column displays the IPFS CID hash of our pinned file. Clicking that hash saves it to the clipboard for later use in an application.

- Clicking the name of the pinned file opens the Pinata gateway in the web browser, searches for the pinned file in the IPFS network, and then displays the `.json` file in our web browser.

![A screenshot depicts our JSON file about the Mona Lisa displayed in a web browser.](Images/pinata-gateway-file.png)

- Displaying the file in our web browser, the Pinata gateway created a standard web URL. This URL is always `gateway.pinata.cloud/ipfs/` followed by the hash.

Summarize this demonstration by explaining that Pinata allows developers to pin any file to the IPFS network and to reference that file by its IPFS CID hash.

- In smart contracts and dApps, the hash can be used to associate the file—which the IPFS network stores—with a smart contract that resides on the blockchain.

Recap this section by asking students the following questions:

- **Question:** What is IPFS?

  - **Answer:** IPFS stands for InterPlanetary File System, which is a protocol, a network, and a file system. It allows users to store almost any type of data on the file system in a decentralized manner.

- **Question:** How does uploading data to a decentralized storage system aid dApps?

  - **Answer:** Using a decentralized storage system reduces the size of the information that is required to be kept on-chain. This greatly reduces any gas fees associated with creating and maintaining the token.

- For example, rather than associating the digital artwork with a token, the artwork can be stored on IPFS. Additionally, the metadata associated with the artwork, including the name, artist, description, and hash of the IPFS address for the artwork, can also be stored in a `.json` file on IPFS. This way, the only information that needs to be associated with the token is the IPFS address associated with the `.json` file.

- **Question:** How does Pinata work with IPFS?

  - **Answer:** Pinata is an application that allows a developer to easily upload files to the IPFS. Users can upload folders or files, or provide a CID. The result of uploading data to Pinata is an IPFS CID or URL that can be copied and used in an application.

Now that students have an understanding of how to upload files to decentralized storage for our files, tell them that it’s time to explore using these pinned files in our `ArtRegistry` dApp.

---

### 8. Instructor Do: Using IPFS and Pinata in a dApp (20 min)

**Corresponding activity:** [Art Registry and IPFS](Activities/05_Ins_Art_Registry_IPFS)

In this activity, you will demonstrate how to incorporate a Pinata file into the decentralized `ArtRegistry` application so that it uses IPFS to store the artwork files and appraisal reports.

> **Note:** For this demonstration you **MUST** first complete the following two tasks:
>    - Use the included solved files to _recompile_ and _redeploy_ the `ArtRegistry` contract. The updated contract includes an image retrieval component that requires the contract's redeployment.
>    - Update your `.env` file with the newly redeployed contract address.
>    - Copy your Pinata API keys into the same `.env` file. (Make sure that your Pinata account can be used for teaching purposes and that the content can be shared with the class.)

This demo may be challenging for students, as you’ll be creating the helper functions required to integrate Pinata and IPFS into the `ArtRegistry` dApp. If you need more time, you can use up to 10 additional minutes, but be sure to adjust the time of the last student activity in this lesson (work on final projects).

**Files:**

[Unsolved folder](Activities/05_Ins_Art_Registry_IPFS/Unsolved/ArtRegistry)

[Solved folder](Activities/05_Ins_Art_Registry_IPFS/Solved/ArtRegistry)

Explain to the students that we'll now update our dApp so that it uses the Pinata API to pin artwork files and appraisal reports. Highlight the following:

- Rather than using the Pinata webpage to upload files, we’ll reconfigure our dApp so that it pins the artwork files and appraisal reports through the Pinata API.

- Users will then be able to directly upload their files and reports through the dApp. They won’t need to visit the Pinata webpage.

- The API will also return the hashes for the pinned files. So, the dApp will be able to permanently attach them to the tokens and events in the blockchain.

- To ease pinning files and reports from the dApp, we’ll build a new Python file that has helper functions for interacting with the Pinata API.

- A **helper function** is a regular function that codes some of the complexity that using a service, like the Pinata API, requires. All the code for formatting and sending the Pinata API request will be added to helper functions. These helper functions, with the required data, can be called anytime that we need to use this code. This helps the code to use the Don’t Repeat Yourself (DRY) principle.

The first step in the process is updating the `.env` file for the Pinata API information.

#### Update the Environment File

Open the `SAMPLE.env` file contained in the `Unsolved` folder, and explain that the `.env` file needs to include our Pinata API keys. Demonstrate the process of accessing the keys and updating the file for the students. Here’s the code:

```env
PINATA_API_KEY='<YOUR PINATA API KEY HERE>'
PINATA_SECRET_API_KEY='<YOUR PINATA SECRET KEY HERE>'
WEB3_PROVIDER_URI=http://127.0.0.1:7545
SMART_CONTRACT_ADDRESS=<YOUR_DEPLOYED_CONTRACT_ADDRESS_HERE>
```

- Pinata API keys are accessed by going to the Pinata [API Keys](https://pinata.cloud/keys) page and then copying the keys into your `.env` file. **Note:** The secret key is only revealed at the time of key pair creation, and cannot be retrieved when revisiting the page.

Next, add the address of the deployed `ArtRegistry` contract to the `SMART_CONTRACT_ADDRESS` environment variable.

- Given that the smart contract code will not change, the address of the `ArtRegistry` contract deployed earlier in the lesson can be used.

#### Create the Pinata Helper Functions

Next, open the file named `pinata.py`. This is where you’ll write the helper functions for pinning files to IPFS via Pinata.

Start by importing the required libraries.

```python
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()
```

- We need the os and dotenv libraries for loading our Pinata API keys.

- We need the requests library so that we can use the API from Python.

- We need the json library so that we can convert data to the JSON format for the API requests.

- The Pinata API keys are loaded by using the environment variables in our `.env` file via the `load_dotenv` function.

#### Pin an Artwork File to IPFS via Pinata

Pinata requires authentication headers for any request to the API, as shown in the following code.

```python
file_headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}
```

- The file headers need to include only the Pinata API keys. So, we create a `file_headers` variable that includes those keys as loaded from the `.env` file via the dotenv library.

- File headers can also be created to contain other metadata for the API, but more on that later.

Next, these new headers are used to create a Python `post` request that can send files to Pinata via the API.

The following code uses the pinFileToIPFS API endpoint to pin a file:

```python
def pin_file_to_ipfs(data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash
```

- To make it easier to use the code associated with the post request, a helper function named `pin_file_to_ipfs` is created.

- This new function accepts a `data` argument that represents the file to upload.

```python
file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])

file_ipfs_hash = pin_file_to_ipfs(file.getvalue())

print(f"The IPFS file hash is {file_ipfs_hash}")

print(f"The IPFS file URI is ipfs://{file_ipfs_hash}")
```

- Remember, the `app.py` file contains the code that uses Streamlit and Web3.py to allow users to interact with the contract from a webpage, so this`file_uploader` component will be added to that file.

- The uploader component lets users upload files and send them to Pinata. With this component, we can specify the types of files that we want to allow for upload. In this case, we want only digital images for the artwork. So we specify a list of types that consists of “jpg”, “jpeg”, “png”.

- The user can upload an image of one of these types, and we then call the `pin_file_to_ipfs` function with the file data. We do so by using the `getvalue` function to get the file data from the Streamlit `file_uploader` component.

- The `pin_file_to_ipfs` function then sends the file to Pinata and returns the IPFS hash for that file.

- We can then use the hash as the URI for the tokens.

The output of the preceding code will resemble the following:

```text
The IPFS file hash is Qmd16NKbYJXaMQczba3D1rDHG74393nS5D6LZqiPEhiCpT
The IPFS file URI is ipfs://Qmd16NKbYJXaMQczba3D1rDHG74393nS5D6LZqiPEhiCpT
```

- The `pin_file_to_ipfs` function can be called anytime that we need to upload and pin a file to IPFS through a dApp.

- However, we can make an additional enhancement by including metadata for the file.

#### Pin the Metadata for the Artwork File

To send metadata for the artwork file, a new helper function is created that allows us to pin a JSON metadata file directly to IPFS via the Pinata API.

- The process for sending JSON data to Pinata slightly differs from the one for sending artwork files (.jpg, .jpeg, .png).

- Specifically, we’ll need to create the headers for the Pinata API, create a function that posts the metadata to Pinata, and then specify the CID version.

- These tasks will take place back in the `pinata.py` file.

#### Create the Headers for the Pinata API

To send JSON data to Pinata, we first need to create a new header dictionary for the Pinata API by using the following code:

```python
json_headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}
```

- The dictionary contains the required values for our JSON headers.

- The key:values pairs associated with the `json_headers` are as follows:

  - The “Content-Type” header key uses “application/json” to specify that JSON data is being sent.

  - A “pinata_api_key” header: We use the Pinata API key from our account.

  - A “pinata_secret_api_key” header: We use the Pinata secret API key from our account.

Have a TA slack out [common examples](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) so that the students can learn more about `Content-Type` headers.

- For the last two values, it uses the API keys that we previously defined in our `.env` file. This dictionary is used for the request header when sending JSON data to IPFS via our account.

#### Create a Function that Posts the Metadata to Pinata

The next step is to create a function that posts the JSON metadata to Pinata.

- To create a helper function that posts the JSON metadata to Pinata, we first need to know the endpoint for pinning JSON data to Pinata.

Navigate to the [pinJSONToIPFS](https://docs.pinata.cloud/api-pinning/pin-json) page in the Pinata documentation.

Have a TA also slack the link out to students: [pinJSONToIPFS](https://docs.pinata.cloud/api-pinning/pin-json)

- Reviewing the documentation, the endpoint is `https://api.pinata.cloud/pinning/pinJSONToIPFS`.

![Pinata JSON endpoint](Images/pinata-json-endpoint.png)

Explain that we also want to know the response that Pinata will send back when we post the JSON metadata.

- Scrolling down to the "Response" section of the same page, this Pinata endpoint will return a JSON object that includes a key named `IpfsHash`. The value of this key will be the IPFS hash of the JSON data that we sent. This hash will later be used for the URIs in our dApp.

![Pinata JSON to IPFS response format](Images/pinata-json-response.png)

Next, define the helper function, named `pin_json_to_ipfs`, by using the following code:

```python
def pin_json_to_ipfs(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json,
        headers=json_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash
```

- The function accepts JSON data as an argument.

Compare this to the `pin_file_to_ipfs` function that took in `data` as an argument.

- It then sends a `post` request to the `pinJSONToIPFS` endpoint in Pinata with that JSON data.

- The `data` is the `json` file.

- The function also uses the `json_headers` dictionary that we defined earlier to authorize the request.

- Finally, it returns the `IpfsHash` value from the Pinata response.

Explain that, before this function can be called by the front end of the dApp, we need to take care of one last item that’s related to Pinata. We need to include the CID version with the JSON data that we send.

#### Specify the CID Version

To use the Pinata API, we need to specify the content identifier (CID) version for the JSON data that we send. Here’s the code:

```python
data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
```

- This code tells IPFS what kind of hash to generate. So, we’ll use Version 1, which is the latest available version.

- We set this option by creating a new variable, named `data`, that includes the version number and assigns our metadata content to the `pinataContent` key.

Explain that the `data` variable just created is a Python dictionary. The dictionary needs to be converted to a JSON string before it can be sent to the API.

- The code can be used to create the third and final helper function, named `convert_data_to_json` that accepts our content, adds the CID version, and then returns a JSON string.

- The `json.dumps` function returns the data in the appropriate format, as shown in the following code.

```python
def convert_data_to_json(content):
    data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
    return json.dumps(data)
```

To confirm, the final version of the `pinata.py` file appears as follows:

```python
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()


file_headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

json_headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}

def convert_data_to_json(content):
    data = {"pinataOptions": {"cidVersion": 1}, "pinataContent": content}
    return json.dumps(data)

def pin_file_to_ipfs(data):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinFileToIPFS",
        files={'file': data},
        headers=file_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash

def pin_json_to_ipfs(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS",
        data=json,
        headers=json_headers
    )
    print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return ipfs_hash
```

Show the students the completed code and ask if they have any questions about the structure of the helper functions or what each function is designed to do.

If time permits, ask the students to explain what each function does as a way to review what they just learned.

Finally, tell the students that with all of the helper functions in place, the next step is to put them all together in a working dApp.

#### Put It All Together: Pin an Artwork File and Its Metadata

Start by confirming that, using the helper functions, we can now pin an artwork file to IPFS, build a JSON metadata file for the artwork, convert the metadata to the JSON string that Pinata requires, and then pin the JSON string to IPFS.

##### Pin an Artwork File

The complete code for the dApp is put together in the `app.py` file by creating a new front-end `pin_artwork` helper function. Note that this code is already loaded into the "Helper functions to pin files and json to Pinata" section of the `app.py` file.

```python
def pin_artwork(artwork_name, artwork_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(artwork_file.getvalue())

    # Build a token metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash, token_json
```

Ask for a student volunteer to review the code line by line and explain what is happening in each line.

Ask the students if they have any questions before moving on to the second front-end helper function: pinning an appraisal report for the artwork file.

##### Pin a Report for the Artwork File

The JSON helper function can also be used to pin appraisal reports for the artwork.

The following helper function, named `pin_appraisal_report`, accepts a string of report content, converts it to the JSON format that Pinata requires, and then pins the JSON file.

```python
def pin_appraisal_report(report_content):
    json_report = convert_data_to_json(report_content)
    report_ipfs_hash = pin_json_to_ipfs(json_report)
    return report_ipfs_hash
```

Ask for a student volunteer to review the code line by line and explain what is happening in each line.

Ask the students if they have any questions about the two front-end helper functions that we integrated into the `app.py` file.

Congratulate the students on writing a lot of sophisticated code in this lesson. Explain that they can reuse this code whenever they’re working with a dApp that needs to pin an image or JSON file to Pinata.

Tell the class that, in the next activity, they’ll practice using these helper functions by adding IPFS file storage to the `ArtRegistry` dApp.

---

### 9. Everyone Do: Art Registry with IPFS (15 min)

**Corresponding activity:** [Art Registry with IPFS](Activities/06-Evr_Art_Registry_with_IPFS)

In this section, you’ll demonstrate the fully functioning `ArtRegistry` dApp, including integration with Pinata and IPFS.

This demo requires that the updated `ArtRegistry` contract from the previous activity be compiled and deployed with Remix, Ganache, and MetaMask.

> **Note:** Be sure to have your `.env` file in place before beginning this demonstration. This file requires your Pinata API keys and the address of the deployed `ArtRegistry` contract in Remix. Also, be aware that this activity assumes that you have compiled and deployed the `ArtRegistry` smart contract, as well as updated the `.env` file with the necessary information.

Use the [solution folder](Activities/06-Evr_Art_Registry_with_IPFS/Solved/ArtRegistry) to demo the dApp.

**Files:**

[Starter folder](Activities/06-Evr_Art_Registry_with_IPFS/Unsolved/ArtRegistry)

[Solution folder](Activities/06-Evr_Art_Registry_with_IPFS/Solved/ArtRegistry)

Begin by explaining to students that this demo will work in reverse: first, you’ll demo the full application, and then you’ll review the code.

Open a terminal instance and launch the solved version of the `ArtRegistry` application by running `streamlit run app.py`.

Upload one or more image files using the launched app. For each image, appraise its value using the Appraise Value controls and then retrieve each appraisal using the Appraisal Report History controls. Note that in the Appraise Value widget, the art token ID is auto-generated starting at 0.

Then, navigate to your Pinata account to show the students that the files uploaded from the dApp are now included among your list of pinned items. You can also navigate to Ganache and show them the list of transactions associated with running the application.

Both of these steps should help to tie together all of the different applications that have been part of building, deploying, and running this `ArtRegistry` dApp.

Once the demonstration is complete, review the code from the `app.py` file with the students as shown in the following sections.

#### Import the Helper Functions from pinata.py

The statement to import the three helper functions from the `pinata.py` file into `app.py` is relatively straightforward. Here’s the import statement:

```python
from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json
```

#### Register New Artwork

Next, there are two code snippets that need to be completed in the "Register New Artwork" section.

Explain that the first code snippet uses the [Streamlit `file_uploader` function](https://docs.streamlit.io/en/stable/api.html?highlight=file_uploader#streamlit.file_uploader) to create the type of digital file that will be uploaded into Pinata. Here’s the code:

```python
# Use the Streamlit `file_uploader` function to create the list of digital image file types (jpg, jpeg, or png) that will be uploaded to Pinata.
file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])
```

- We’ll incorporate two parameters listed in the `file_uploader` function documentation.

  - The first parameter `Upload Artwork` is a label describing what the function is being used for.

  - The second, for the parameter `type`, is a list of digital file types that will be accepted for upload.

Explain that the second code snippet in the "Register New Artwork" section involves using the `pin_artwork` helper function to pin the created file to IPFS. Here’s the code:

```python
# Use the `pin_artwork` helper function to pin the file to IPFS
artwork_ipfs_hash, token_json = pin_artwork(artwork_name, file)
```

- The `pin_artwork` helper function, defined earlier in the `app.py file`, takes in two parameters, the artwork name and the artwork file.

- The `file` that should be pinned is the one we created by using the Streamlit `file_uploader` function.

#### Appraise Art

Now, explain that there are also two code snippets required to complete the "Appraise Art" section.

The first uses Pinata to pin an appraisal report for the report contents, called the report URI.

```python
# Use Pinata to pin an appraisal report for the report content
appraisal_report_ipfs_hash =  pin_appraisal_report(appraisal_report_content + image_uri)
```

- The `pin_appraisal_report` helper function takes in one parameter, the content of the appraisal report.

To complete the second code snippet, we need to copy and save the URI to this report for later use as the smart contract’s `reportURI` parameter.

```python
# Copy and save the URI to this report for later use as the smart contract’s `reportURI` parameter.
report_uri = f"ipfs://{appraisal_report_ipfs_hash}"
```

Although students might not be familiar with this code, almost the exact same line can be found in the "Register New Artwork" section of code:

```python
artwork_uri = f"ipfs://{artwork_ipfs_hash}"
```

- The code creates an f-string, references the syntax to call the IPFS, and passes it the transaction hash that results from pinning the appraisal to Pinata. This f-string can be used to access the report from the browser.

#### Get Appraisals

If time permits, review the code contained in the "Get Appraisals" section, even though students are supplied with the entire code block.

Once all of the code has been reviewed, ask the students if they have any questions about the now fully operational `ArtRegistry` dApp.

Remind the students that they learned a lot of code in this lesson; it’s a good idea to continue to review the solution file for this application in order to familiarize themselves with the processes and steps.

Assure the students that they’ll continue to practice these new skills in the next class before they begin their final project.

Assure them that they will get another opportunity to put all of these pieces together in the following class, just before they get the opportunity to switch focus to their capstone project.

---

### 10. Student Do: Project Time (60 min)

Explain to the students that the remaining class time will be spent working in groups on their projects. Highlight the following points from the previous class:

- Use office hours to ask questions about your project.

- Communication is key when it comes to successfully completing a group project. Be sure to meet with your group regularly.

- Plan to work with your group outside of class. This is your third project that you’ve done for this course, so implement best practices that you learned from your previous two projects.

Students should break into their project groups. If you’re having an online class, you can use the [breakout rooms feature of Zoom](https://support.zoom.us/hc/en-us/articles/206476313-Managing-Breakout-Rooms) for this. You and the TAs should provide support to each group.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
