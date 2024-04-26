## 19.2: Digital Signatures and Keys

---

### Overview

In today's class, students will begin to sign and send transaction blockchains using Python libraries Web3.py and `bit`. They will also learn how BIP-44 works in preparation for the homework.

The goals for today's class are for students to understand how to talk to Ethereum and Bitcoin nodes using Python and how wallets work across the blockchain ecosystem.

### Objectives

By the end of this lesson, students will be able to:

* Summarize asymmetric and symmetric cryptography and how they can both increase security.

* Describe the process in which digital signatures authorize blockchain transactions.

* Evaluate the roles of hot and cold wallets.

* Detail how wallets use public- and private-key pairs and store cryptocurrency.

* Articulate the role of Bitcoin improvement proposals (BIPs), specifically BIP-39 and BIP-44, and how to use them to generate mnemonic phrases.

* Develop an Ethereum account by using BIP-44, BIP-39, and Python.

* Use mnemonic phrases and Web3.py to create a verifiable transaction.

* Create, sign, and send a transaction using their Ethereum account.

### Instructor Notes

* In this section, students will begin to learn about cryptography. This is important because it ties together many moving parts, such as digital wallets, Web3.py for sending and receiving transactions, wallet addresses, and blockchain security. These concepts are new and may be difficult for students.

* Today is a heavy cryptography day. Take time to answer questions and thoroughly explain the differences between symmetric and asymmetric (public key) cryptography as well as digital signatures.

* If the students are having trouble connecting with the real-world examples, they will likely have a better understanding when sending encrypted messages to each other.

* BIP-44 and BIP-39 will need to be installed; this process is straightforward and explained in the lesson content.

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1eLHPQauaFZhv0VbP2Tx3HSQAXA-kHqkfkFjLXPHlorU/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Briefly recap the previous class, reminding students about Web3.py and Ethereum functionality. Then, you’ll explain digital signatures.

Begin by recapping the previous unit and lessons:

* At this point in the course, you should have a good understanding of the methodology behind blockchain transactions.

* The previous unit covered how to build a blockchain-based ledger system from scratch. In your `PyChain`, each block on the chain is stored data for the ledger.

* Blockchain blocks can store any type of data&mdash;the transfer of cryptocurrency funds, the text of a complex legal document, or even a simple sentence such as “Jeremy owes Sue $20.” Regardless of content, each of these records represents a basic blockchain transaction.

* The lessons have covered how to execute and verify such transactions, but there’s one question we haven’t considered:

   If anyone can create a transaction and store data on the blockchain (as long as they pay the transaction fee), how do the ledger’s participants know who is adding what? How do we know that “Jeremy owes Sue $20” was, in fact, written onto the ledger by Sue?

* Blockchain developers have created a mechanism for identifying participants in a blockchain and associating those identities with transactions: the **digital signature**.

* A participant’s digital signature proves that they authorized a given transaction on the blockchain. Like most features of a blockchain, digital signatures are designed to make the blockchain system more secure and verifiable.

Cover the following points, which lay out the plan for the remainder of the lesson.

* In this lesson, you will learn about the cryptography that powers digital signatures. Then, you will learn about other technical components of a blockchain digital signature, including digital wallets.

* You will generate your own digital signature by using Web3.py as well as two additional popular Python libraries, mnemonic and BIP-44. The digital signature will allow you to authorize messages and transactions on an Ethereum-based blockchain.

* Wallets are important because they provide security for these transactions, and it is important for developers to understand how to safely send and receive cryptocurrency.

* Some major [companies using cryptocurrency](https://finance.yahoo.com/news/15-biggest-companies-accept-bitcoin-165115491.html) include Whole Foods, PayPal, Microsoft, and many more!

Be sure that there are no questions before moving forward.

---

### 2. Instructor Do: Symmetric and Asymmetric Cryptography (10 min)

This section provides a brief explanation of asymmetric cryptography for students. In order to complete this lesson, it is important that they understand what they are doing and why.

Reference the slides and then begin explaining asymmetric cryptography and digital signatures.

* Before using a digital signature to authorize blockchain transactions, it is important that we understand the components of a digital signature and how they all work together.

* Let's explore the encryption technology that powers digital signatures, which is known as **asymmetric cryptography**. But, before we can dive too deeply into asymmetric cryptography, we must first understand symmetric cryptography. So, let’s get started.

#### Symmetric Cryptography

Reference the slides as you define symmetric cryptography. Explain the security risks associated with it, and establish why asymmetric cryptography is helpful.

* **Symmetric cryptography** essentially means that for one lock, there is one key. This one-to-one relationship provides the symmetry.

* Consider this concept in physical terms: If you have a lockbox, you have one key that opens it. If you want to share the contents of the lockbox, you have to give away the one key (or an identical copy of it).

* Here are some real-word examples: This same concept is used to digitally encrypt a hard drive or password-protect a document. One set password&mdash;or **key**&mdash;can open it, and anyone with that password can access your computer or the document. We use this technique primarily to protect **data at rest**, or data that is not moving across a network.

* A possible downside to symmetric cryptography: if you send a user an encrypted message, you also have to send them the key to decrypt it.

* This means that a malicious hacker could have an opportunity to intercept the key and use it to decrypt your secret data.

#### Asymmetric Cryptography

* Blockchain needs a way to share confidential data without having to also share the data’s password, or key. This is where asymmetric cryptography comes in.

Reference the slides as you transition into explaining asymmetric cryptography and how it is used on the blockchain:

* In symmetric cryptography, encrypted data has just one key. Asymmetric cryptography, on the other hand, splits up this key into a **key pair**. Each key pair includes a **public key** and a **private key**.

* The public key is like a bank account number. If Devon stores money in her bank account, anyone with the account number&mdash;the public key&mdash;can deposit money into the account. However, withdrawing funds from the account requires not just the account number but also Devon’s PIN&mdash;the private key. No one knows this PIN except for Devon.

* The following diagram illustrates key pairing in asymmetric cryptography:

  ![A diagram depicts the asymmetric encryption process with a public-private key pair.](Images/19-2-asymmetric-cryptography.png)

* Notice that User 1 uses User 2’s public key to encrypt the secret data. Doing so ensures that only User 2 will be able to access the secret data. This is because User 2’s private key is the only key that can decrypt data that is encrypted with User 2’s public key. Once User 1 has encrypted the data, they send it to User 2. Then, User 2 uses their private key to decrypt the message and read the secret data.

* Asymmetric cryptography makes it much harder for malicious hackers to read data by getting hold of a key because you never have to send a private key over a network or share it with anyone.

* In the next section, we’ll learn how blockchain leverages public-private key pairs to create secure digital signatures for all network participants.

---

### 3. Students Do: Secretbox Demo (10 min)

This brief activity will help solidify encoding a message for students.

**Corresponding activity:** [Secretbox](Activities/01-Stu_Secretbox)

Slack out this link, and ask students to open a browser and navigate to it.

**Link:** [Secretbox demo](https://tweetnacl.js.org/#/secretbox)

Explain a bit about the activity before students get started, using the following talking points.

* TweetNaCl.js is a JavaScript library that developers often use to implement encryption into an application’s user interface. The Secretbox demonstration tool allows us to test symmetric and asymmetric cryptography, as well as hashing, signing, and verifying messages.

* There are more capabilities, but for this activity, we’ll just use the Secretbox demo tool to practice some basic symmetric cryptography.

Be sure that there are no questions before moving forward.

---

### 4. Instructor Do: Review Secretbox Demo (10 min)

**Corresponding activity:** [Secretbox Demo](Activities/01-Stu_Secretbox)

In this activity, you will walk students through the Secretbox demo. Share your screen with the class. Be sure to answer any questions about asymmetric cryptography as you do this activity. The purpose of this activity is to help students understand asymmetric cryptography. Explain each step thoroughly as you complete it.

Once you’ve navigated to the site, there are four text boxes on the screen. The boxes are labeled Key, Nonce, Message, and Box, as shown in the following image:

![A screenshot depicts the Secretbox demo window.](Images/19-2-secretbox-demo.png)

Type an arbitrary message into the Message text box on the lower-left side of the screen. This message is a secret!

Next, click the Random button that is located to the right of the Key text box. This button will generate a key, or a random alpha-numeric series of characters, in the Key text box, as shown in the following image:

 ![A screenshot depicts the Secretbox window with a note typed in the Message box, and a key in the Key box.](Images/19-2-secretbox-generate-key.png)

Once your secret message is encrypted, you will be able to use this symmetric key just like a password to access the message.

Secretbox also requires that you add a nonce to your message.

* Recall that a "nonce" (number used once) is a number added to a hash, or encrypted block, in a blockchain that, when rehashed, meets the difficulty level restrictions.

* You added a nonce to each block’s data to alter the hash (the encryption output) of the block’s data.

* The Secretbox tool will similarly add a nonce to your Message data. Without the nonce, encrypting the same data with the same key would return the same encrypted output every time.

* Adding the nonce to your message data randomizes the data and ensures that a unique encrypted output is returned. Ultimately, using the nonce just makes it harder for a bad actor to break your data’s encryption.

To generate the nonce, click the Random button that is located to the right of the Nonce text box. Explain that a random alpha-numeric series of characters should appear in the Nonce text box, as shown in the following image:

![ A screenshot depicts the Secretbox window with a none added to the Nonce box.](Images/19-2-secretbox-generate-nonce.png)

Next, click the blue Encrypt button found beneath the Message box. This will encrypt the message.

* The Secretbox tool returns the encrypted message in the Box text box on the lower-right side of the screen, as the following image shows:

  ![A screenshot depicts the Secretbox window with an encoded message in the Box text box.](Images/19-2-secretbox-encrypt.png)

Congratulate students on creating and using symmetric cryptography to encode a message.

Explain that now they have an encoded message and the key&mdash;the “password”&mdash;that will decode it.

* To decode the message later, we can copy the encrypted message, the key, and the nonce to a secure place for storage.

* The encrypted data now includes the nonce, so in addition to the encrypted message and the key, we’ll also need to tell Secretbox what nonce to include with our data.

For now, leave the key, nonce, and encoded message in their respective text boxes. Delete the original message from the Message box.

Then, click the green Decrypt button, which is located beneath the Box text box. The original message should reappear in the Message box.

Be sure that there are no questions before moving forward.

---

### 5. Instructor Do: Signatures and Wallets (10 min)

In this activity, you will introduce digital signatures and explain how they relate to wallets as they are used on the blockchain.

Share the following diagram and explain how it illustrates key pairing with asymmetric cryptography:

![A diagram depicts the asymmetric encryption process with a public-private key pair.](Images/19-2-asymmetric-cryptography.png)

* Blockchain leverages public-private key pairs to secure communications or transactions by using asymmetric cryptography.

* The user's private key is used to create a digital signature that secures all blockchain transactions.

In the next few talking points, discuss digital signatures with the students and make connections with real-life examples and blockchain. Mention examples of when the students may have used digital signatures in the past. Maybe they have signed a digital document or used a digital document-signing service before.

* These services use cryptography to create digital signatures that prove that a document or transaction has been authorized by the proper individual(s) and that the signed document has not been tampered with.

* Similarly, blockchains use asymmetric cryptography to generate a digital signature, or a public-private key pair, for each participant.

* Each participant on the blockchain has one private key. This private key is used to sign documents, messages, or transactions that they send to the blockchain&mdash;in other words, to **authorize** transactions (this is akin to Devon using her PIN to authorize the withdrawal of funds from her bank account).

* For example, when a blockchain participant&mdash;like the example, Devon&mdash;signs a transaction with her private key, it generates a public key that appears as a publicly viewable digital signature on the transaction.

* Only Devon’s private key can generate her public key. So, if Devon’s digital signature appears on a transaction, other blockchain participants can independently verify Devon’s public key and be sure that she authorized the transaction.

* In this way, blockchain participants can check any transaction's digital signature to verify the transaction.

* Private keys play an important role in the blockchain transaction-authorization process. They provide security and the ability to send transactions. For this reason, private keys should never be shared with anyone&mdash;just as you would never share your bank account PIN with anyone. They might empty your wallet!

* Cryptography is used in almost every industry that uses computers&mdash;specifically the type used to generate public and private keys.

* In the context of cryptocurrency, users use their private key to send funds, ensuring that no one else can access the money in their account. You use your public key to receive funds.

* Recall from the previous lesson that every blockchain participant has an account address, like a bank account number, where other participants can send funds. On Ethereum blockchains, a participant’s account address is a shortened version of their public key.

* It is common that a blockchain participant has one private key and one associated public key, but it’s possible to associate more than one public key with a given private key.

* Some blockchain participants choose to associate multiple public keys with their private key in order to increase privacy.

* It’s also possible for one blockchain participant to use multiple private keys. Again, some individuals do this to increase privacy and data security.

* For this lesson, you will create your blockchain accounts with one private key and one associated public key.

* The same private key can be used across multiple blockchains if they use the same protocols. For example, a blockchain participant could use the same private key for their accounts on both Bitcoin and Ethereum.

The next few talking points explain cryptocurrency wallets.

* Digital wallets and physical wallets both store important information.

* A **cryptocurrency wallet** is a software program or physical hardware device that securely stores and manages a blockchain participant’s payment information. This includes the participant’s private key as well as their cryptocurrency balance. The wallet also allows the participant to make cryptocurrency transactions on a blockchain.

* A blockchain, a participant's actual balances, and a transaction history are stored in the distributed ledger&mdash;in other words, on the blockchain itself.

* A blockchain participant uses their wallet to store their private key, confirm their cryptocurrency balance, create cryptocurrency transactions, and then authorize the transactions using their private key.

* After the transaction has been created and authorized from within the wallet, it is sent to the blockchain. Then, as you know, it waits in the mempool to be validated by a miner and added to a new block on the chain.

* Some digital wallets can only hold the information for a single cryptocurrency, but multicurrency wallets exist that can accommodate several cryptocurrencies.

* In short, a digital wallet allows you to both spend your cryptocurrency and verify your ownership of it.

* IMPORTANT: Highlight to students the important distinction between Custodial vs. Non-Custodial Wallets and share this [link](https://academy.binance.com/en/articles/custodial-vs-non-custodial-wallets-what-s-the-difference). A custodial wallet owns the private key to your wallet and holds these assets in custody similar to a regular bank account. This comes with its own risks also similar to a regular bank account (which for instance may or may not be covered by a form of deposit insurance), and it is up to the user to be aware of these risks. In contrast, a non-custodial wallet (such as Metamask, which we will use in class) grants you alone access and control over the funds. The term digital wallet is often used synonomysly for both types of wallets.

* You can also code your own wallet&mdash;which we’ll do later in this lesson.

* Wallets have various levels of security, depending on how they’re constructed and how they store keys.

* **Hardware wallets** store the cryptographic keys inside of a special chip. Some hardware wallets are **cold wallets**. This type of wallet rarely, if ever, connects to the internet.

* The keys stored in a hardware wallet are completely disconnected from the digital world, except in the rare moments when they are used to withdraw or transact with the participant’s funds. This makes these wallets extremely difficult for bad actors to tamper with. Several providers of hardware wallets exist, including Ledger, Trezor, and KeepKey.

* A **hot wallet**, on the other hand, is a digital wallet that connects to the internet directly through a computer or cell phone.

* A hot wallet can be a software application on your phone or computer, or it can be a hardware wallet that connects to the internet via the USB port on your computer. Hot wallets are less secure than cold wallets. This is because their internet connection can present opportunities for bad actors to access the programs, if they’re not properly secured, and gain access to the stored digital keys.

* The following image visualizes the differences between a hot wallet and a cold wallet:

  ![An illustration compares hot and cold wallets.](Images/19-2-wallet-types.png)

* As the image shows, a hot wallet’s features include:

  * Software or hardware device
  * Often or always connected to internet
  * Easier to access account information
  * Less secure

* On the other hand, a cold wallet’s features include:

  * Hardware device
  * Rarely connected to internet
  * More difficult to access account information
  * Extremely secure

Explain that we’ll use hot wallets in this course because they are easier and more convenient to use, and they are also free.

Emphasize the importance of caution when integrating a software wallet into a production system. If we are not careful, we could inadvertently put the information stored inside the wallet at risk.

Answer any questions before moving on.

---

### 6. Instructor Do: Generating a Private Key (10 min)

In this section, students will learn how to generate an Ethereum private key. They will also learn about *Bitcoin improvement proposals (BIPs)* and how they are utilized by blockchain.

The following talking points explain BIPs and how students will use them. Reference the slides and allow students the opportunity to ask questions as you proceed.

* A BIP is a proposed standard that would alter current Bitcoin protocols or processes. In other words, it proposes changes to the protocol.

* The procedure that we’ll use to generate our `mnemonic seed phrase`, which will be used to generate our `private key`, involves two different BIPs.

* New BIPs are voted on by the Bitcoin blockchain community. If a majority favors the BIP, it is adopted and implemented.

* BIPs can include changes to the process of validating transactions within the Bitcoin ecosystem or improvements to the core process of running the Bitcoin ecosystem. Like many aspects of Bitcoin, many BIPs are also adopted by other blockchains, including Ethereum.

Slack out the following link, and then begin to explain mnemonic phrases and how students will use them.

**Link:** [Bitcoin BIPs Github](https://github.com/bitcoin/bips)

* We will use two widely adopted BIPs today, **BIP-39** and **BIP-44**. These will help us generate our Ethereum private key.

* BIP-39 sets a standard for using a **mnemonic phrase**, or **seed phrase**, which serves as a backup that can recover your private key if your wallet is compromised, lost, or destroyed.

* A mnemonic seed phrase is a string of randomly selected words that is used to generate a private key. Generating a private key from a random string of words enhances the security of the private key by making it harder to guess. It also makes it harder to lose your private key.

* If a private key is lost, its owner loses the ability to access all account information and funds associated with the account. A list of words is generally easier for humans to copy and retain than the key itself.

* Since the same seed phrase will always generate the same private key when the same hashing algorithm is applied, using seed phrases can help blockchain participants maintain access to their wallets and private keys.

* BIP-39 includes a list of 2,048 words that can be included in seed phrases. To generate a seed phrase, a digital wallet typically selects either 12 or 24 words from this list at random.

* People tend to be bad at generating randomness when selecting their own words; BIP-39 has become one of the most common standards for randomly creating seed phrases.

* Letting the wallet software generate the 12- or 24-word seed phrase means that the participant’s only responsibility is to write the phrase down and keep it somewhere safe&mdash;both from being lost and from malicious hackers.

The following image shows an example of a 24-word seed phrase created using BIP-39:

![A screenshot depicts the seed phrase.](Images/19-2-example-seed-phrase.png)

Ask students to pay attention to the words the phrase contains; they are relatively simple words like “toe,” “miss,” “bonus,” “bicycle,” and “wave.”

Ask if there are any questions about mnemonic seed phrases. Once it is clear that the class fully understands the concept, tell them it’s time to generate one.

The next few talking points detail how to use our seed phrase to generate the private key for working on the Ethereum blockchain.

* Explain that the first step is to derive a private key from a seed phrase using BIP-44, which is similar to BIP-39.

* BIP-44 will convert the seed phrase to a corresponding private key that we can use to authorize transactions on a blockchain network.

* Remember, blockchain participants store private keys in their wallets. Like BIP-39, BIP-44 was designed for hierarchical deterministic wallets, or HD wallets.

* HD wallets automatically generate the public-private key pair from the seed phrase rather than having the user do it manually. Most blockchains now use BIP-44 as the standard for generating public-private key pairs. BIP-44 has been widely adopted because it allows a single wallet to handle multiple coins, multiple accounts, and even multiple public-private key pairs.

Be sure that there are no questions before moving forward.

---

### 7. Everyone Do: Creating an Ethereum Account (25 min)

**Corresponding activity:** [Creating a Mnemonic and Generating a Private_Key](Activities/02-Evr-Creating_a_Mnemonic_and_Generating_a_Private_Key)

In this activity, demonstrate how to use Python libraries based on BIP-39 and BIP-44 to create a new Ethereum account. The activity starts with generating a new seed phrase and then creating a wallet and public-private key pair for a new Ethereum account.

**File:**
[Creating a Mnemonic and Generating a Private_Key](Activities/02-Evr-Creating_a_Mnemonic_and_Generating_a_Private_Key/Solved/Private_Key_from_a_Mnemonic.ipynb)

**Links:**

[mnemonic PyPI documentation page](https://pypi.org/project/mnemonic/)
[BIP-44 PyPI documentation page](https://pypi.org/project/bip44/)
[PyPI.org](https://pypi.org/)

Slack out the above links. Explain that they include documentation about the BIP-39 and BIP-44.

* We’ll need to use new packages in conjunction with Web3.py for this activity. We will use the mnemonic package, which is based on BIP-39, and the BIP-44 package; both can be found in the PyPI.org documentation.

Explain how to install `mnemonic`. Ensure that the TA is able to help students as needed, and encourage students to help each other. Use the following code:

  ```bash
  pip install mnemonic
  ```

Explain how to install the bip44 package. Ensure that students have support, and feel free to demonstrate the code below in your terminal.

  ```bash
  pip install bip44
  ```

Then, instruct the class to open the `Unsolved` folder and begin coding in Jupyter Notebook.

* We'll also import `os` and `dotenv` so that once our new seed phrase is generated, we can store it in a variable called `MNEMONIC` and load it from an `.env` file.

  ```bash
  pip install python-dotenv
  ```

* An `.env` file allows a developer to store sensitive information that is needed to run a program but should not be revealed to the public.

* In previous activities, we used `.env` files to store personal API keys for sites like Alpaca and Mapbox. An `.env` file in conjunction with a `.gitignore` file can prevent the sensitive information stored in the `.env` file from getting out to sites like GitHub.

* Importing `os` and `load_dotenv` from `dotenv` allows developers to import the information contained in a `.env` file into a Jupyter notebook, which runs the program that requires the information.

* In addition, we must import the `Account` module from Web3.py. This will allow the creation of an `Account` object, which enables Web3 to interact with our Ethereum account on the Ethereum blockchain.

The following code shows all of our imports:

  ```python
  # Imports
  import os
  from dotenv import load_dotenv
  load_dotenv()
  from mnemonic import Mnemonic
  from bip44 import Wallet
  from web3 import Account
  ```

In the next few steps, students will generate an initial seed phrase using the mnemonic package. The next few talking points detail this process:

* Ideally, one would generate a seed phrase only once. This seed phrase will eventually generate our private key, and we do not want to create a new seed phrase and new private key every time we run our program&mdash;that would be equivalent to wiping our wallet.

* Generating and storing a new seed phase would overwrite the seed phrase that preceded it&mdash;and that would also overwrite the private key.

* That means that, whenever the code was rerun, the user would lose access to the funds and transactions associated with the previous private key. To prevent this, we’ll save our seed phrase to a `.env` file after we generate it. Then, we can load the phrase from the `.env` file each time we run our program.

The next few steps detail how to generate a seed phrase with BIP-39. Explain each step to students as they code along with you:

* The function `os.getenv` is used to check the environment for the environment variable `MNEMONIC`.

  ```python
  # Load the value of the MNEMONIC variable from the .env file
  mnemonic = os.getenv("MNEMONIC")
  ```

Save the contents stored in the `.env` file’s `MNEMONIC` variable to a program variable named `mnemonic`.

Use an `if` statement to check if `mnemonic` is `None`.

  ```python
  # Evaluate the contents of the mnemonic variable
  # Create a new mnemonic seed phrase if the value of mnemonic equals None
  if mnemonic is None:
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate(strength=128)
  ```

* If the program variable `mnemonic` is not `None`, then that means there is already a mnemonic phrase saved in an associated `.env` file. We would then print the contents of the variable to return our mnemonic seed phrase.

* On the other hand, if the value of `mnemonic` is `None`, then there is no mnemonic phrase saved in an associated `.env` file, and we need to generate a new mnemonic. This can be done by calling the function `Mnemonic` and passing it the string “english” (for English words). We will save the function as a variable named `mnemo`.

Then, on the `mnemo` variable, call the function `generate` and pass it a parameter of `strength=128`.

* This parameter is used to generate a new 12-word seed phrase and that the parameter `strength=256` would generate a 24-word seed phrase.

Save this as a new variable named `mnemonic`, then print out the value of the `mnemonic` variable.

* This variable will return our newly generated mnemonic seed phrase.

  ```python
  # Display the value of the mnemonic variable
  display(mnemonic)
  ```

* Upon printing out our new `mnemonic` variable, we should see a 12-word phrase that looks something like this:

  ```text
  “ide fiscal agent shield tail wing mix sight friend leg situate near”
  ```

Now, copy this phrase into our `.env` file so that the next time this notebook is run from the beginning, it uses this same phrase for our wallet.

  ```text
  MNEMONIC= “ide fiscal agent shield tail wing mix sight friend leg situate near”
  ```

Recommend that students save their mnemonic seed phrase to another secure and accessible location on their computer.

Remind them that they will utilize several different notebooks throughout this module, and therefore, they will also use several different `.env` files. The process of creating `.env` files will be much easier if students can easily access their mnemonic seed phrase.

Congratulate students and explain that they now have a mnemonic seed phrase, which allows them to create a wallet and our private and public keys.

In the next few steps, live code to generate a wallet with the class. Be sure to mention the following talking points:

* Wallets can be developed in many different ways with a variety of structures and characteristics. In this demonstration, we are coding a hierarchical deterministic (HD) wallet.

* Remember that an HD wallet generates the public-private key pair.

* The first thing we need to do is generate our wallet; then, we pass the mnemonic seed phrase into it as a parameter so the wallet can use our seed phrase to generate a unique public-private key pair.

* To generate our HD wallet, we'll call the function `Wallet()`, which is imported from the BIP-44 package.

Pass this function our `mnemonic` variable, and save the HD wallet that we generated as a new variable named `wallet`. The following code shows this step:

```python
wallet = Wallet(mnemonic)
wallet
```

* The `wallet` variable should now be a **`bip44.wallet`** object, which means that the digital wallet instance meets the standards defined in BIP-44.

* The wallet currently contains the seed phrase that was created using the mnemonic package.

Demonstrate that the output of our `Wallet()` function, the `bip44.wallet` object, looks like this:

```text
<bip44.wallet.Wallet at 0x7f94a84bdd10>
```

Take the next few minutes to explain the importance of a mnemonic seed phrase. Instead of live coding, it is acceptable to reference slides during this time.

* One way this wallet could be used along with the mnemonic seed phrase is to create multiple private keys for a variety of different blockchains.

* The `wallet` instance that the `Wallet` function creates is often called “universal” because it can be utilized with more than one blockchain provider or cryptocurrency.

* Unlike digital wallet applications that you download to your phone or computer, or the ones that exist as hardware devices (e.g., Coinbase, Trezor, Ledger), the `wallet` instance that you create in this program is not persistent. It only exists while the program is open.

* This means that programmers need to recreate the `wallet` object every time they write a program that interacts with a blockchain. This is why they need to save their mnemonic to a `.env` file and recreate their `wallet` instance with the same mnemonic each time.

* Remember, mnemonic seed phrases represent the master key to their wallet and, ultimately, their blockchain account.

The next few talking points explain seed phrases.

* The next step is to use our wallet and seed phrase to create one Ethereum account&mdash;with one public-private key pair.

* We will create code to generate a wallet with the same mnemonic seed phrase. This will generate the same private key and account information every time the program is run.

* Every Ethereum transaction that we create will then be discoverable through the same account address.

Next, demonstrate how to create an Ethereum account with a public-private key pair. It’s important that you transition to live coding and explain each step to students as you proceed.

Begin to explain the steps to create an Ethereum account:

* The first step is to generate the public-private key pair that we will use to transact on the Ethereum blockchain.

Define the code you are about to write by explaining each step.

* Call the `derive_account` function on our wallet instance, and pass it the string “eth”. The `derive_account` function uses the mnemonic seed phrase that is stored in the `wallet` object instance to generate a public-private key pair.

* Store the private key and public key that this function returns as variables named `private` and `public`, respectively. The string “eth” associates this private-public key pair with the Ethereum blockchain.

The following code generates the keys:

  ```python
  # Create the public and private keys associated with a new Ethereum account
  private, public = wallet.derive_account("eth")

  # Display the private key
  private
  ```

Demonstrate and explain that this code will return your private key in the form of a **byte string**.

* A byte string is a series of encoded characters, or bytes, that are readable only by the computer.

* The byte string is identified by the “b” preceding the string. Your private key, returned in the form of a byte string, looks like this:

  ```text
  b'G_4e:\xdf\xf4\xe7\xaa\xfaX\xaex\xfc\n$\xdcs\x05\x0f\x06\xb8\x8d\x80Zus\xd3\xf7&\xb2&'
  ```

Congratulate the class on creating a private key, and remind them that they imported an `Account` object from Web3.py earlier. Then, make a connection to the previous activities by explaining that now they can call the `Account.privateKeyToAccount` function and pass it their private key as an argument.

* This will return a new Ethereum `account` object, and a variable named `account` can be assigned to it.

* The `account` object will allow us to send transactions to the Ethereum blockchain using our private key. The `account object` will also allow other participants to send cryptocurrency funds to the owner.

Call `account.address` and print the result.

* It should return a new Ethereum address that other blockchain participants can use to send us funds. Remember that in Ethereum, an account address is a shortened version of the participant's public key.

* The following code creates our account and prints our Ethereum account address:

  ```python
  # Create an Ethereum account by passing the private key via the Account object
  account = Account.privateKeyToAccount(private)

  # Print the account address associated with the Ethereum account
  print(account.address)
  ```

The new blockchain account address is a string that looks like this:

  ```text
  0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396
  ```

* This is the address to receive funds on any Ethereum-based blockchain. Because our Ethereum account address is a shortened version of our public key, it is safe for us to share our account address with other blockchain participants.

Allow time for students to ask questions before the break.

---

### 8. BREAK (15 min)

---

### 9. Students Do: From Mnemonic to Ethereum Account (20 min)

**Corresponding activity:** [From Mnemonic to Ethereum Account](Activities/03-Stu-From_Mnemonic_to_Ethereum_Account)

In this activity, students will use the mnemonic and BIP-44 packages and the Web3.py library to generate a `wallet` instance and a new, secure public-private key phrase from a mnemonic seed phrase.

Tell the class to open `from_mnemonic_to_ethereum_account.ipynb` in the Unsolved folder and to code in Jupyter Notebook.

Ensure that the TA is available to help students resolve any issues that they may encounter and to encourage them to ask questions.

**Instructions:**

* [README.md](Activities/03-Stu-From_Mnemonic_to_Ethereum_Account/README.md)

**File:**

* [From_Mnemonic to Ethereum Account](Activities/03-Stu-From_Mnemonic_to_Ethereum_Account/Unsolved/from_mnemonic_to_ethereum_account.ipynb)

---

### 10. Instructor Do: Review From Mnemonic to Ethereum Account (10 min)

**Corresponding Activity**[From Mnemonic to Ethereum Account](Activities/03-Stu-From_Mnemonic_to_Ethereum_Account)

In this part of the lesson, you will review the activity that the students just completed. Be sure to have the TA circulating the class to aid any students who may be struggling and to ensure that the class understands the activity before moving forward. Explain each action item to students as you move through each step.

**File:**
[From_Mnemonic to Ethereum Account](Activities/03-Stu-From_Mnemonic_to_Ethereum_Account/Solved/from_mnemonic_to_ethereum_account.ipynb)

First, begin discussing the purpose of each of the imports listed below:

```python
# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account
```

* `dotenv` will hide our mnemonic phrase.

* `Mnemonic` to produce our phrase.

* `web3` to talk to blockchain.

* `Wallet` to produce our wallet.

Explain the following steps as you create the mnemonic seed phrase for this activity:

* Call `os.getenv("MNEMONIC")`, and save its value as a variable named `mnemonic`.

  ```python
  mnemonic = os.getenv("MNEMONIC")
  ```

* The `if` statement is used to check if the mnemonic variable is `None`. Then, if the mnemonic variable is `None`, initialize a new `Mnemonic()` instance and pass it a string value of “english” so that it will use the English word list.

Save the instance as a variable named `mnemo`.

* Then, we generate a mnemonic seed phrase by creating a variable named `mnemonic` and calling `mnemo.generate(strength=128)`.

Finally, print out the mnemonic phrase.

  ```python
  if mnemonic is None:
       mnemo = Mnemonic("english")

      mnemonic = mnemo.generate(strength=256)
  ```

Create a `.env` file in the same folder as the Jupyter notebook, and create an environment variable named `MNEMONIC`. Copy the new mnemonic seed phrase that you just generated and set it equal to the `MNEMONIC` variable.

In the new `.env` file, add the following:

```text
MNEMONIC = 'YOUR MNEMONIC SEED PHRASE HERE'
```

Instantiate a new instance of `Wallet` and pass it the `mnemonic` variable. Then, review the `wallet` instance.

* This is a variable that uses our `wallet` import and then passes in `mnemonic`.

  ```python
  wallet = Wallet(mnemonic)

  wallet
  ```

Derive public and private keys from your `wallet` instance by completing the following steps:

Create two variables, `public` and `private`, and set their values by calling the `derive_account` method on your `wallet` instance. To associate the account with Ethereum, pass the string “eth” to the `derive_account` method.

* We can set the same value for both `private` and `public` on one line by separating them with a comma. Then, we call the `derive_account()` method and place “eth” inside the parentheses.

  ```python
  private, public = wallet.derive_account("eth")
  ```

Review the byte string for your private key by calling the `private` variable that we just created.

```python
private
```

Create a new variable named `account`, and construct the Ethereum account by calling `Account.privateKeyToAccount` and passing it your `private` key variable.

```python
account = Account.privateKeyToAccount(private)
```

Call `account.address` to access the address associated with your new Ethereum account. By using this address, other participants can send you ether on the Ethereum blockchain.

  ```python
  account.address
  ```

The bonus step can be completed by calling `account.privateKey` to access the private key associated with your new Ethereum account.

* We set `account` to `Account.privateKeyToAccount(private)`, giving it access to the information in the account.

  ```python
  account.privateKey
  ```

Ask the class if they have any questions or if they would like to review any of the steps once more before moving on.

---

### 11. Everyone Do: Signing and Verifying Messages with Web3.py (20 min)

**Corresponding activity:**
[Signing and Verifying Messages with Web3](Activities/04-Evr-Signing_and_Verifying_Messages_with_Web3.py)

In this portion of the lesson, perform a live code demonstration. Have students follow along as you explain each step. This activity is important because it provides students with context for digital signatures and the role they play in blockchain transactions.

Tell the class to open `Unsolved_Signing_a_Message_With_Web3.ipynb` in the `Unsolved` folder.

**File:**
[Signing and Verifying Messages with Web3](Activities/04-Evr-Signing_and_Verifying_Messages_with_Web3.py/Unsolved/Unsolved_Signing_a_Message_With_Web3.ipynb)

Tell the class that in this portion of the lesson, they will use Web3.py to authorize&mdash;or sign&mdash;and then verify transactions that we send to a blockchain.

Then, explain that the functions they will use from the Web3.py library include the `encode_defunct` function from the `eth_account.messages` module. An instance of `w3` will also need to be imported using Web3.py’s `auto` function.

* State that the purpose of the activity is to access Ethereum functions without having to specify a connection method or provider for the Ethereum blockchain.

* You will use your keys from the previous activity.

Tell students that this means we can use some of the code from the previous activity:

```python
# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from eth_account import Account


mnemonic = os.getenv("MNEMONIC")

type(mnemonic)

private, public = wallet.derive_account("eth", account=0)
private

account = Account.privateKeyToAccount(private)

print(account.address)
```

Explain that the following code imports our functions:

```python
from web3.auto import w3

from eth_account.messages import encode_defunct

```

Tell students that we can also create a message; for this demonstration, we’ll use the string “Zach owes David $20.” The following code saves our string as a variable named `msg`:

```python
msg = "Zach owes David $20"
```

Explain the next few steps to students:

* After writing a message, the next step is to encode it from a text format into a byte format. In a byte format, the message can be read by computers and signed using our private key.

* To do this, use the `encode_defunct` function that we imported. Pass `msg` in to the function as the text argument, and save it as a new variable named `message`, as shown in the following code:

  ```python
  message = encode_defunct(text=msg)
  ```

Tell students that they can now sign the message using the `w3.eth.account.sign_message` function. This function accepts our message as the first argument and our private key as an argument named `private_key`. Then, it returns the encoded, signed message.

  ```python
  signed_message = w3.eth.account.sign_message(message, private_key=private)

  signed_message
  ```

Expect that upon printing the `signed_message` value, the following object will be returned:

  ```text
  SignedMessage(messageHash=HexBytes('0xb4aac7e826ed228d4aca4c19e090daf7744dcab152eb82450b3493e6d8b1e9e2'), r=86463783249892389545395593721538729131000973963063013048526836494924568441848, s=22180326548204491458663314535893580599255069685716856960705135400662501223845, v=27, signature=HexBytes('0xbf28c45e6c0b65ddb896c0cebae0ab595a434f25d66010fd9a0889ae65c9b3f831099eb4918ce327526792d39f59483111846b7cd90c3cdd3eae65ccb120eda51b'))
  ```

Make sure that students notice that the `SignedMessage` object consists of several parts.

* The signature consists of a HexBytes hash code. Together, the `r`, `s`, and `v` variables that the object contains can be used to independently verify the signature.

* To validate this transaction’s signature against our public key, we must call `w3.eth.account.recover_message()`.

Pass this function our original encoded message as well as the digital signature contained within our `SignedMessage` object.

```python
w3.eth.account.recover_message(message, signature=signed_message.signature)
```

Illustrate that this returns the account address (a shortened version of the public key) of the participant who signed the message.

* Only the participant whose private key pairs with the message public key (and therefore, the account address) could have signed the message.

* The value returned from the `recover_message` function should match the value of the `account.address` function associated with the participant's Ethereum account. If they match, then we’ve verified who sent the message.

* The previous code returns the following output:

  ```text
  ‘0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396’
  ```

Tell the class that now that they've learned how to sign and send authorized transactions from our local machines to an Ethereum blockchain node, they’ll practice signing and authorizing a message independently!

Give students a chance to ask any questions that they may have before moving on to the next activity.

---

### 12. Students Do: Signing Ethereum Transactions (20 min)

**Corresponding activity:** [From Mnemonic to Ethereum Account](Activities/05-Stu-Signing_Ethereum_Transactions)

In this activity, students will use the Web3.py library to sign and authorize messages with their public-private key pair.

Tell the class to open `signing_ethereum_transactions.ipynb` in the `Unsolved` folder.

**Files:**
[Signing Ethereum Transactions](Activities/05-Stu-Signing_Ethereum_Transactions/Unsolved/signing_ethereum_transactions.ipynb)

**Instructions:** [README.md](Activities/05-Stu-Signing_Ethereum_Transactions/README.md)

---

### 13. Instructor Do: Review Signing Ethereum Transactions (20 min)

**Corresponding activity:** [From Mnemonic to Ethereum Account](Activities/05-Stu-Signing_Ethereum_Transactions)

This activity is designed to ensure students are comfortable with the concepts they've learned by reviewing the activity they just completed. As you complete each step, provide encouragement and support to students.

**Files:**
[Signing Ethereum Transactions](Activities/05-Stu-Signing_Ethereum_Transactions/Solved/signing_ethereum_transactions.ipynb)

Add the `.env` file and make sure it contains the mnemonic seed phrase that you generated in the first activity. Be sure to save this as the variable `MNEMONIC`.

Then, point out all of the imports and provide some brief details.

```python
import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from eth_account import Account
from web3.auto import w3
from eth_account.messages import encode_defunct
```

Call `os.getenv("MNEMONIC")` and save its value as a variable named `mnemonic`.

Confirm that your seed phrase is available by checking the `type` of your `mnemonic` variable.

```python
mnemonic = os.getenv("MNEMONIC")
```

View the data type of mnemonic to confirm its availability.

```python
type(mnemonic)
```

From the bip44 package, generate a `Wallet` instance and pass your `mnemonic` variable as the parameter.

Review your `wallet` instance afterwards.

```python
wallet = Wallet(mnemonic)

wallet
```

Use the `derive_account` method on the `wallet` instance. Pass the string “eth” to the method. Review the byte string of the private key.

```python
private, public = wallet.derive_account("eth")

private
```

Use the `Account` object, the `privateKeyToAccount` function, and the private key to generate an Ethereum account. To confirm the account was successfully initiated, print the account’s address.

```python
account = Account.privateKeyToAccount(private)
```

Print the account's address by using the `account` instance and adding `address` at the end.

```python
account.address
```

Create a new string variable named `msg`, and set its value equal to any message you would like to sign&mdash; .e.g.,“Zach owes Glenna $40.”

```python
msg = "Zach owes Glenna $40"
```

Use `encode_defunct(text=msg)` from Web3.py to byte encode your message. Save the output as a variable named `encoded_msg`.

```python
message = encode_defunct(text=msg)
```

Call the `w3.eth.account.sign_message` method. Pass it your encoded message variable and your private key.

The private key will “sign” your new message. Save the returned signed message as a variable named `signed_message`.

```python
signed_message = w3.eth.account.sign_message(message, private_key=private)
```

Then, review your signed message by calling the variable `signed_message`.

```python
signed_message
```

Then, call the `w3.eth.account.recover_message` method. Pass it your encoded message variable and the message’s signature from the `signed_message.signature`.

* It’s important to confirm that the returned value matches the account address that was printed.

  ```python
  w3.eth.account.recover_message(message, signature=signed_message.signature)
  ```

Address any questions that the class may have. Then, congratulate them on everything they did in this class&mdash;they accomplished a lot!

Let the class know that in the next lesson, they will use their private key to sign real transactions on a real blockchain network!

Then, summarize what the class has learned:

* Today, the class learned asymmetric cryptography and how it applied to blockchain.

* Students were able to use BIPs and learned about how they impact the blockchain.

* Remind students that they should be very proud of what they've achieved in class. Learning to sign and send transactions can be difficult, but they've made major progress.

Be sure that there are no questions before ending the class.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
