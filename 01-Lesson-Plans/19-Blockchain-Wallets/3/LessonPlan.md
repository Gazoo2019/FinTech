## 19.3: Testing Blockchain Transactions

---

### Overview

In today's lesson, the students will learn how to use new Python libraries to send transactions and even build applications. They'll use the mnemonic phrase generated from Ganache that will give them practice in signing and sending transactions on a live blockchain network. Then, finally, they will use Streamlit in conjunction with Web3.py to create both the front and back ends of a blockchain application.

### Class Objectives

By the end of this lesson, the students will be able to:

* Use a blockchain explorer to visualize each part of a transaction.

* Develop code by using Python and Web3.py to connect to a local Ganache blockchain.

* Use Web3.py in conjunction with Ganache to test your transaction.

* Formulate code to sign and send a transaction by using Web3.py.

* Use Streamlit and Web3.py together to build an application that communicates with the blockchain.

* Test a blockchain web application by using Ganache.

### Instructor Notes

* Ensure that you have your mnemonic phrase ready. We will be using it throughout the class.

* Take some time before class to familiarize yourself with the [BIP-39 online wallet converter](https://iancoleman.io/bip39/) and how to convert your mnemonic into different coins.

---

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [19.3 Lesson Slides](https://docs.google.com/presentation/d/1dvMczEBc7EWOrb5NtrnrnCZ5B1J8koSzXOSilHHlWnM/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this section, you’ll confirm that the class has an understanding of wallets through a quick Q&A.

* **Question:** What is the difference between a hot and a cold wallet?

  * **Answer:** A hot wallet is connected to the internet (e.g., Coinbase, Metamask). A cold wallet is connected to the internet only when attached to your computer. A hot wallet is less secure than a cold wallet.

* **Question:** What are public and private keys?

  * **Answer:**

    * A public key is used to encrypt plaintext to convert it to cipher text. A private key is used by the receiver to decrypt the cipher text in order to read messages or send ether.

    * All users of a blockchain know the public key, but a private key is known only by the account owner.

    * A private key is needed to send ether to other accounts. A public key can be used by all members of the blockchain community to send transactions to a particular user.

Navigate to the [Ganache Download page](https://www.trufflesuite.com/ganache).

Confirm that everyone in the class has downloaded and installed Ganache. Ask the TA(s) to support any students who have installation issues.

---

### 2. Instructor Do: Introduction to Ganache (10 min)

In this section, make sure that the students have downloaded Ganache. Then, check that they understand the purpose of Ganache, its user interface, and why they are learning about it.

Begin by explaining Ganache to the students.

* Ganache is a personal local blockchain with accounts that are preloaded with ether.

* The ether in these accounts has no real value on the Ethereum blockchain, as this blockchain is local only.

* Ganache is a useful tool for testing transactions and smart contracts.

Have the students launch Ganache and select **Quickstart Ethereum**, as shown in the following screenshot.

![Ganache quickstart Ethereum](Images/19-3-ganache_create_workspace-1.png)

* The result is a list of 10 different account addresses with a balance of 100 ETH in each.

   ![Ganache test accounts](Images/19-3-ganache-test-accounts.png)

Demonstrate that clicking an account's key symbol (located at the right side of each account entry) opens a window that reveals the test account's private key as well as the address.

   ![Ganache private key](Images/19-3-ganache-private-key.png)

* Each time we launch Ganache, a new list of accounts with different addresses and keys is created. This fact will become important later.

Point out that the mnemonic seed phrase is in the top left part of the interface.

* This phrase can be added to a `.env` file, which we’ll do later in the lesson, to enable Ganache to run as the provider for transactions.

Be sure that there are no questions before moving forward.

---

### 3. Everyone Do: Using Streamlit with Web3.py (5 min)

**Links:** [Web3.py Documentation](https://web3py.readthedocs.io/en/stable/)

Tell the students to navigate to the Web3.py documentation. Explain that Web3.py will handle the transactions in the application you are building today.

* In most decentralized applications that are built on the blockchain, Web3 is used to interact with smart contracts and read the block data. You will use it to send transactions.

* The web3. eth. Contract objects can help developers interact with smart contracts on the Ethereum blockchain.

* When you create a new contract object, you give it the JSON interface of the respective smart contract, and `web3` will auto-convert all calls into low-level ABI calls over the remote procedure call (RPC).

Slack out the [Web3.py documentation](https://web3py.readthedocs.io/en/stable/contracts.html) to the students. Encourage the students to review this documentation as they learn more about `web3`.

Next, explain that today we will connect `web3` to Streamlit to enable our applications to interact with local blockchains.

Answer any questions before moving on.

---

### 4. Everyone Do: Ethereum and Streamlit (30 min)

In this activity, you will lead students through the process of integrating the account functionality of Ethereum's blockchain with the Streamlit web application.

**Note:** Because this activity involves Streamlit, we will use Python files rather than Jupyter notebooks for the application. The students have been instructed to use Visual Studio Code for these programs.

**Corresponding Activity:** [Ethereum and Streamlit](Activities/01-Evr_Ethereum_and_Streamlit)

**Files:**

* [SAMPLE.env](Activities/01-Evr_Ethereum_and_Streamlit/Unsolved/SAMPLE.env)

* [Streamlit.py](Activities/01-Evr_Ethereum_and_Streamlit/Unsolved/app.py)

* [Ethereum.py](Activities/01-Evr_Ethereum_and_Streamlit/Unsolved/ethereum.py)

* [Solved folder](Activities/01-Evr_Ethereum_and_Streamlit/Solved)

Zip the following folder and slack it out to the students so that they can code along:

* [Starter folder](Activities/01-Evr_Ethereum_and_Streamlit/Unsolved/)

Explain to the students that the focus of this activity is twofold:

1. To automate the Ethereum account functionality that we have learned up to now with the use of Python functions.

2. To integrate those Python functions with a Streamlit web application.

Because Streamlit is involved, the activity will involve Python files rather than Jupyter notebooks. Visual Studio Code will be the IDE used for this and the following activities.

Once the students have the starter folder open in VS Code, have them update the `SAMPLE.env` file with their mnemonic seed phrase from ganache.

Next, open the Python file named `ethereum.py`. Note the imports that are included in the `ethereum.py` file. These should be familiar to the students, as they are the imports associated with loading the variables from the `.env` file.

Explain that, in this `ethereum.py` file, you will create a Python function that does five things:

1. Accesses the `MNEMONIC` variable from the `.env` file.

2. Uses the `mnemonic` variable to create a HD `wallet`.

3. Uses the `wallet` to generate a public/private key pair.

4. Uses the `private` key to create an Ethereum `account`.

5. Returns the `account` from the function.

Write the code that defines the function:

```python
# Create a function called `generate_account` that automates the Ethereum
# account creation process
def generate_account(w3):
```

Ask for a volunteer to provide you with the five lines of code that define the body of the function.

```python
# Access the mnemonic phrase from the `.env` file
mnemonic = os.getenv("MNEMONIC")

# Create Wallet object instance
wallet = Wallet(mnemonic)

# Derive Ethereum private key
private, public = wallet.derive_account("eth")

# Convert private key into an Ethereum account
account = Account.privateKeyToAccount(private)

# Return the account from the function
return account
```

When complete, the entire function should appear as follows:

```python
# Create a function called `generate_account` that automates the Ethereum
# account creation process
def generate_account(w3):

   # Access the mnemonic phrase from the `.env` file
   mnemonic = os.getenv("MNEMONIC")

   # Create Wallet object instance
   wallet = Wallet(mnemonic)

   # Derive Ethereum private key
   private, public = wallet.derive_account("eth")

   # Convert private key into an Ethereum account
   account = Account.privateKeyToAccount(private)

   # Return the account from the function
   return account
```

* By creating the `generate_account` function, we have **automated** the process of creating an Ethereum account from a mnemonic seed phrase.

* With the function created, it’s time to turn our attention to using the power of the automation process in conjunction with the Streamlit web application.

Open the `app.py` Python file, and review the single import for the Streamlit library.

The next step is to import the `generate_account` function from `ethereum.py`.

Pose the following question:

* **Question:** What is the syntax for importing the `generate_account` function from the `ethereum.py` file into the `app.py` file?

  * **Answer:**

   ```python
   from ethereum import generate_account
   ```

  * The functionality associated with the `generate_account` function is now available on the `app.py` page.

Next, we want to create an `account` variable in Streamlit that contains the information generated in the `generate_account` function.

* **Question:** Does anyone know the code for creating an `account` variable on the Streamlit page that will hold the information generated by the `generate_account` function that has just been imported?

  * **Answer:**

   ```python
   # Generate the Ethereum account
   account = generate_account(w3)
   ```

* This code will call the `generate_account` function, create the wallet and account, and return the information to the Streamlit page to be accessed via the `account` variable.

Once the account information has been returned to the Streamlit page, we can display it on the web application.

Run the Streamlit application before adding the address information.

* Navigate to the folder in your terminal and type `streamlit run app.py`.

* The following Streamlit page should open in your browser:

   ![Streamlit without address](Images/streamlit-without-address.png)

Pose the following question:

* **Question:** What is the code to write the account address to the Streamlit application page?

  * **Answer:**

   ```python
   # Write the Ethereum account address to the Streamlit page
   st.write(account.address)
   ```

Navigate back to your browser and refresh the application.

![Streamlit with address](Images/streamlit-with-address.png)

It’s that easy to automate an Ethereum transaction and get the results to display on the Streamlit application webpage!

Ask the students if they have any questions about this activity before proceeding to a similar activity that the students will complete independently.

---

### 5. Students Do: Automating Ethereum (35 min)

In this activity, the students will add functions that automate the process of accessing the balance from the Ganache blockchain as well as sending a signed transaction. They will then incorporate these functions into the Streamlit web application.

**Corresponding Activity:** [Automating Ethereum](Activities/02-Stu_Automating_Ethereum)

**Files:**

* [Instructions](Activities/02-Stu_Automating_Ethereum/README.md)

* [SAMPLE.env](Activities/02-Stu_Automating_Ethereum/Unsolved/SAMPLE.env)

* [app.py](Activities/02-Stu_Automating_Ethereum/Unsolved/app.py)

* [ethereum.py](Activities/02-Stu_Automating_Ethereum/Unsolved/ethereum.py)

Zip the following folder and slack it out to the students:

* [Starter folder](Activities/02-Stu_Automating_Ethereum/Unsolved/)

---

### 6. Instructor Do: Review Automating Ethereum (15 min)

The focus of this review should be on automating the Ethereum processes by creating functions. Try to engage the students as much as possible so that you can check their understanding of the activity.

**Instructor Note:** You will need to add your mnemonic seed phrase to a `.env` file before starting this activity.

**Corresponding Activity:** [Automating Ethereum](Activities/02-Stu_Automating_Ethereum)

**Files:**

* [Starter folder](Activities/02-Stu_Automating_Ethereum/Unsolved/)

* [Instructions](Activities/02-Stu_Automating_Ethereum/README.md)

* [SAMPLE.env](Activities/02-Stu_Automating_Ethereum/Solved/SAMPLE.env)

* [app.py solved file](Activities/02-Stu_Automating_Ethereum/Solved/app.py)

* [ethereum.py solved file](Activities/02-Stu_Automating_Ethereum/Solved/ethereum.py)

Start the review by running the Streamlit application from the `Unsolved` file.

Navigate to the `Unsolved` folder location in the terminal and type `streamlit run app.py`.

If the appropriate information has been added to the `.env` file, the screen should look similar to the following:

![streamlit unsolved](Images/streamlit-unsolved.png)

Confirm that the goal of this activity is to enhance the application by adding the functionality that checks a user's balance and allows them to send an ether transaction.

#### Code the get-balance Function

The next step in the review is to code the `get_balance` function in the `ethereum.py` file.

Ask the students the following question:

* **Question:** At a high level, what are the three steps required to code the `get_balance` function?

  * **Answer:** 1) Using the account address, call the `w3` `get_balance` function to get the balance of the account in wei from Ganache. 2) Convert the wei to ether. 3) Return the ether from the funcion.

Code the following function with the students. Highlight that the function will take in one argument `address` from the Streamlit page. This is the account address that will be used to make the call to the Ganache blockchain.

```python
# Create a function called `get_balance` that calls the Ganache blockchain, converts the wei balance of the account to ether, and returns the value of ether
def get_balance(address):
   """Using an Ethereum account address access the balance of Ether"""
   # Get balance of address in wei
   wei_balance = w3.eth.get_balance(address)

   # Convert wei value to ether
   ether = w3.fromWei(wei_balance, "ether")

   # Return the value in ether
   return ether
```

Now navigate to the `app.py` file and ask the following question:

* **Question:** What needs to be done to make the `get_balance` function available in the `app.py` file?

  * **Answer:** The import statement needs to be adjusted.

   ```python
   # Import the functions from ethereum.py
   from ethereum import generate_account, get_balance
   ```

Next, navigate to the `Ethereum Account Balance` section and create the code that calls the `get_balance` function, passing `account.address` as an argument.

* Note that `account.address` is available from the original call to the `generate_account` function.

```python
# Call the get_balance function and write the account balance to the screen
ether_balance = get_balance(account.address)
st.write(ether_balance)
```

Ask the students if they have any questions about either the `get_balance` function or how it is being called from the Streamlit webpage.

#### Code the `send_transaction` Function

Return to the `ethereum.py` file and work through the process of coding the `send_transaction` function.

* This function is a bit more complicated than either the `generate_account` or `get_balance` functions.

First, create the function. Be sure to highlight the necessary arguments: the `account`, the `receiver` address, and the amount of `ether` that is being sent.

```python
# Create a function called `send_transaction` that creates a raw transaction, signs it, and sends it
def send_transaction(account, receiver, ether):
```

Unlike the `get_balance` function, where just the `account.address` was sent as an argument, explain that the entire `account` is being sent as an argument. Ask the following question:

* **Question:** Can anyone explain why we are sending the entire `account` as an argument rather than just the `account.address`?

  * **Answer:** The account's private key will be required to sign the transaction we are creating. As a result, we will need the entire account object sent to the function.

Next, discuss at a high-level the five steps that we are going to code inside the `send_transaction` function.

1. Set the gas price strategy. Use a medium gas price strategy.

2. Convert the amount of ether to wei.

3. Calculate the gas estimate. For this, you need the receiver address, the sender's address, and the wei value.

4. Construct the raw transaction, which includes the receiver, sender, wei value, gas estimate, gas price, and nonce.

5. Create the signed transaction.

   ```python
      # Send the signed transactions
      return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
   ```

With this code in place, navigate back to the `app.py` file and ask the following question:

* **Question:** What is the first thing we should do on the `app.py` page?

  * **Answer:** Update the import statement to include the `send_transaction` function.

      ```python
      # Import the functions from ethereum.py
      from ethereum import generate_account, get_balance, send_transaction
      ```

Navigate to the `An Ethereum Transaction` section.

The first step is to code the two required input fields: the receiver address and the amount of ether.

* Both of these variables will be used as arguments when the `send_transaction` function is eventually called.

   ```python
   # Create inputs for the receiver address and ether amount
   receiver = st.text_input("Input the receiver address")
   ether = st.number_input("Input the amount of ether")
   ```

Next, create a button that initiates the call to the `send_transaction` function and displays the transaction hash once it’s returned from the function. Here’s the code:

```python
# Create a button that calls the `send_transaction` function and returns the transaction hash
if st.button("Send Transaction"):

   transaction_hash = send_transaction(account, receiver, ether)

   # Display the Etheremum Transaction Hash
   st.text("\n")
   st.text("\n")
   st.markdown("## Ethereum Transaction Hash:")

   st.write(transaction_hash)
```

Save your files, and then navigate to the Streamlit application in your browser and refresh the page. It should now appear as follows:

![Streamlit with input fields](Images/streamlit-with-input-fields.png)

Input a receiver address and an amount of ether, and then click the Send Transaction button. After a few moments, the screen should appear as follows:

![Streamlit with hash](Images/streamlit-with-hash.png)

Ask the students if they have any questions about the process of automating the Ethereum transaction functions and making them available to use in a live web application.

Stress that these are advanced concepts that show just how far they have come in their knowledge of coding and of blockchain. They can now make live calls to the Ethereum blockchain!

Finally, ask the class if they have any questions before you begin discussing the mini-project.

---

### 7. Break (15 min)

---

### 8. Students Do: Cats Mini-Project (45 min)

In this activity, the students will create a Streamlit web application that’s similar to the one that they’ll be asked to create in the homework assignment.

**Corresponding Activity:** [Cats Mini Project]
Activities/03-Stu_Cats_Mini_Project)

**Files:**

* [SAMPLE.env](Activities/03-Stu_Cats_Mini_Project/Unsolved/SAMPLE.env)

* [cat_shop.py](Activities/03-Stu_Cats_Mini_Project/Unsolved/cat_shop.py)

* [crypto_wallet.py](Activities/03-Stu_Cats_Mini_Project/Unsolved/crypto_wallet.py)

* [Instructions](Activities/03-Stu_Cats_Mini_Project/README.md)

Zip the following folder and slack it out to the students so that they can code along:

* [Starter folder](Activities/03-Stu_Cats_Mini_Project/Unsolved/)

---

### 9. Instructor Do: Review Mini Project (20 min)

**Corresponding Activity:** [Adding an Interface with Streamlit](Activities/03-Stu_Cats_Mini_Project)

Ask the students how they feel about the mini project and if they have any questions.

Then, open the `Unsolved` folder for the mini project and begin coding in VS Code.

**Files:**

* [Solved folder](Activities/03-Stu_Cats_Mini_Project/Solved)

**Links:**

* [Streamlit documentation](https://docs.streamlit.io/en/stable/)

* [Web3.py documentation](https://web3py.readthedocs.io/en/stable/)

First, open `crypto_wallet.py`. Explain to the students that the first function generates their wallets. This time they are wrapping this function in another function so that it can be accessed in the other file. The code is as follows:

```python
def generate_account(w3):
   """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
   # Fetch mnemonic from environment variable.
   mnemonic = os.getenv("MNEMONIC")

   # Create Wallet Object
   wallet = Wallet(mnemonic)

   # Derive Ethereum Private Key
   private, public = wallet.derive_account("eth")

   # Convert private key into an Ethereum account
   account = Account.privateKeyToAccount(private)


   return account
```

Next, create a `get_balance` function to obtain the balance from our wallet. Remind the students that this is similar to what they have been doing throughout this unit. Here’s the code:

```python
def get_balance(w3, address):
   """Using an Ethereum account address access the balance of Ether"""
   # Get balance of address in Wei
   wei_balance = w3.eth.get_balance(address)

   # Convert Wei value to ether
   ether = w3.fromWei(wei_balance, "ether")

   # Return the value in ether
   return ether
   ```

Next, open the`cat_shop.py` file. Explain that the starter code imports `dataclass`, which creates structured classes for storing data. These classes hold certain properties and functions to deal specifically with data and allow it to be represented in the code.
Then, import the functions from the other file.

* The objects serve as the database and the name list for retrieving the possible cats that can be purchased.

   ```python
   cat_database = {
      "Jennifurr": ["Jennifurr", 22],
      "Cheddar": ["Cheddar", 151],
      "Meowise": ["Meowise", 31],
   }

   # Create a list of the the cats by first names
   kitties = ["Jennifurr", "Cheddar", "Meowise"]
   ```

* The `for` loop in the `get_cats` function uses `db_list` to return each part of the object, and then displays it using block notation.

   ```python
   for number in range(len(kitties)):
         st.write("Name: ", db_list[number][0])
         st.write("Price in Ether: ", db_list[number][1], "eth")
         st.text(" \n")
   ```

* `st.write` uses Streamlit to add the objects to the user interface. `st.text` can be used to format the text and add an empty line below it.

Next, create headers using `st.markdown`, as the following code shows:

```python
st.markdown("# Kitties")
st.markdown("## Buy a Kitty!")
st.text(" \n")
```

Then, call the functions from `wallet.py` and save them in the `cat` variable. Pass in the names of the cats by using the list from the starter code. Here’s the code:

```python
cat = st.sidebar.selectbox('Select a cat', kitties)
```

Still using `streamlit`, create a header to display cat name and price, as the following code shows:

```python
st.sidebar.markdown("## Cat Name and Price")
```

Create a new variable to identify the cat for purchase by referencing the object by name:

```python
cat = cat_database[cat][0]
```

Create a variable called `cat_price` to retrieve the cat price:

```python
cat_price = cat_database[cat][2]
```

Explain to the class that we are comparing the cat price to the amount of ether we have in our account balance.

```python
if cat_price <= ether:
```

Ask the students if they have any questions about Streamlit, using Streamlit with wallets, or finding the account balance with Web3.py.

Explain to the students how this lesson ties into the homework assignment for this unit.

* The application that you just built is similar to what you’ll be asked to do in the homework assignment. In the assignment, you’ll again use Ganache and Streamlit to build an Ethereum-based application.

Tell the students to pay special attention to the functions they wrote, as they are used frequently in Web3 apps.

Congratulate the students for learning how to use Ganache as a mock blockchain in conjunction with Steamlit and Web3.py.

---

### 11. Instructor Do: Structured Review (35 min)

**Note:** If you are teaching this lesson on a weeknight, save this 35-minute review for the next Saturday class.

Use this entire time to review questions with the students before officially ending class.

Here’s a suggested format:

* Ask the students if there are any activities that they want to review.

* Revisit key activities that are relevant for the homework assignment.

* Allow the students to start the homework assignment, with the TA(s) offering support. The homework assignment is a combination of sections 1 and 3.

Take your time while answering students’ questions. This is a great time to reinforce concepts and clear up any confusion.

---

### End Class

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
