## 18.2 Lesson Plan: Build a Shared Record-Keeping System

### Overview

In this lesson, students will build a simple blockchain—a basic, digital, shared record-keeping system—in Python by using industry-standard libraries. Each block will consist of a single record, or transaction. They’ll learn new techniques to verify the data in each block, and chain the blocks together.

Today's class will introduce students to the fundamental cryptographic techniques used throughout blockchain and internet technologies.

The goal of this lesson is for students to understand and apply basic cryptographic concepts to real-world scenarios, as well as to arbitrary data.

---

### Class Objectives

By the end of the class, students will be able to:

* Describe what cryptography is and how it’s used to secure a blockchain.

* Explain how cryptography is used to convert data into a hash code.

* Use Python to define a `Block` class data structure that includes attributes and methods.

* Understand the role that hash codes play in securing the integrity of record data on the blockchain.

* Use hash codes to link blocks together in order to create a blockchain.

---

### Instructor Notes

* A lot of material is covered in this lesson. Focus on making sure that students understand the basics of the Python class structure used to build both the `Block` and `PyChain` data classes.

* If running short on time, the “Students Do” activities in the second half of the class can be changed to Everyone Do activities, where you live code and students follow along.

---

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 18.2 Slides](https://docs.google.com/presentation/d/1y7CEMy4FU14Wt9guHiMhDgp0UaYhaJd2NcwhVl5LgJQ/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome to Class (10 min)

Welcome students to class.

Build excitement for today’s lesson by telling them they’ll build their very own blockchain from scratch by using Python and a couple of related libraries.

Recap that, in the previous lesson, students were introduced to the concept of blockchain, as well as the concepts of trust and value as they relate to financial transactions. The concept of trust is central to blockchain. Cover the following talking points related to trust and blockchain:

* For any financial system, there are malicious hackers who hope to target unsuspecting users.

* According to a [recent study by Verizon](https://enterprise.verizon.com/resources/reports/dbir/), 70% of all the data breaches in the world in 2020 were financially motivated. And 43% of the breaches targeted vulnerabilities in web applications, which is more than double the reported amount from the previous year. This highlights the problem of securing online financial systems.

* To combat malicious hackers and keep data secure, blockchain systems combine clever mathematical concepts, called **cryptography**, with a collection of formalized data that’s known as a **block**.

* The blocks then link together to form a chain of trust, or integrity, which is known as a blockchain.

* This blockchain data structure is unique, because the data that’s written to it becomes instantly verifiable by design. This means that if someone changes or tampers with the data in the ledger, the users of the ledger will know about it.

Explain the focus of today’s lesson:
 
* Today's lesson will focus on building a basic, digital, shared record-keeping system—a simple blockchain-based application—in Python by using industry-standard libraries. The blockchain will incorporate techniques to verify the data in each record, or block, and to securely chain the blocks together.

* The Python library Streamlit will be used to create a user-friendly web application for the blockchain app. This webpage will simplify the process of adding and storing data in the shared record-keeping system.

Briefly review the blockchain fundamentals introduced in the previous lesson, using a question-and-answer format:

**Question:** What are the five key features of a blockchain?

  * **Answer:** The five key features of a blockchain are:

    1. **Decentralization:** A blockchain is decentralized because all the users can simultaneously edit the blockchain. Every user always has direct access to the blockchain, and no central authority monitors the user transactions.

    2. **A distributed architecture:** First, many computers in various locations store identical copies of the same ledger. Second, these computers communicate with each other to arrive at particular decisions, like the validity of a new block in the chain.

    3. **Trust:** The technology is designed so that users can trust that the blockchain accurately records all its data and prevents tampering with that data. Without this trust, no one would use a blockchain for a transaction.

    4. **Record keeping:** In a blockchain, each block represents a transaction, and the chain links these transactions over time.

    5. **Transparency:** Anyone can review the history of the transactions in a blockchain. This doesn’t mean that anyone can review all the data that the transactions contain—the data itself might be private or sensitive. Rather, it means that users can verify the existence of the transactions—specifically, who added data to the chain and when.

**Question:** What is the difference between a permissioned and a permissionless blockchain?

  * **Answer:** A **permissioned** blockchain has a trusted, third-party arbiter or central authority that makes decisions, like a government, well-respected institution, CEO, or Board of Directors. A **permissionless** blockchain doesn’t have a central authority to instill trust. Instead, trust is placed in the blockchain standards, or rules of conduct, which include incentives for users to act appropriately.

Answer any questions before moving on to the next section.

---

### 2. Instructor Do: Shared Accounting with Digital Ledgers (15 min)

**Corresponding Activity**: [Blockchain Block DataClass](Activities/01-Ins_Blockchain_Block_DataClass)

In this activity, you will introduce the concept of a data class in Python. You will also build a Block DataClass for the PyChain blockchain.

Use the starter file to live code the demonstration for students.

**Files:**

[Starter file](Activities/01-Ins_Blockchain_Block_DataClass/Unsolved/block.py)

[Solution file](Activities/01-Ins_Blockchain_Block_DataClass/Solved/block.py)

Review that, at its most fundamental level, a blockchain is a record-keeping system.

* A blockchain is a type of shared record-keeping system that seeks to maintain trust through the use of a distributed ledger.

* A shared record-keeping system must be able to store records, or data. And for users to trust the system, it must store data in a way that’s secure.

Tell students that this lesson will explore how both records are stored, and how they are kept secure.

#### Storing Digital Records

Explain that, like a typical accounting system, or ledger, a blockchain is a shared record-keeping system that will take in and retain user data.

* In a ledger, represented as either a Pandas DataFrame or SQL table, each row represents a new entry in the ledger. Similarly, in a ledger that a blockchain represents, each block represents a new entry in the ledger.

* A **block** is the most fundamental data structure of the blockchain. It’s essentially a container that holds data.

* In a blockchain, new entries can be added only to the end of the ledger. That is, a new block can be added only to the end of the chain.

* Different blockchains store different types of data records inside their blocks. However, almost every chain can store transaction data. (An example is sending cryptocurrency from one account to another.)

* In today’s class, we’ll create a data structure for blocks that can store data records. To do this, we’ll need to create a Python data container called a **data class**.

#### Defining a Blockchain Block with a Python Data Class

Explain that a **class** offers a way to define a custom data structure in Python.

* The class can store multiple variables, known as **attributes** when they exist in a class.

* Python has a special type of class, called a **data class** that can be used to define and store data.

* Think of a Python data class as a blueprint for a data container. It defines the structure and provides hints about the types of data that belong in it. This is called **typing**.

Open the [starter file](Activities/01-Ins_Blockchain_Block_DataClass/Unsolved/block.py) and present the code to create the Block class for students.

#### Define the Data Class

First, import the "dataclass" library from Python, as the following code shows:

  ```python
  # Imports
  from dataclasses import dataclass
  ```

Explain that, to use a data class in Python, the data names and types that belong to the class must first be defined.

* This tells Python what kind of data is expected to be stored in the data class.

Define a special data class named `Block` that can hold a string in its `data` attribute, as the following code shows:

  ```python
  # Creating the Block data class
  @dataclass
  class Block:
      data: str
  ```

Examine the code line by line.

* First, the `@dataclass` line uses special Python syntax to indicate that it’s a decorator. A **decorator** is a modifier that adds or extends the functionality of the object—in this case, the `Block` class—without modifying its structure. Decorators are usually called before the definition of the function being decorated.

* The `@dataclass` decorator is used to make structured classes that specialize in storing data.

Have a TA slack out the link to [Data Classes](https://docs.python.org/3/library/dataclasses.html) and [Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/) in the Python documentation.

Continue reviewing the code:

* `class Block:` is used to define the `Block` class. This resembles the syntax for defining functions. In this case, Python is used to create a class named `Block`. Remember that the preceding decorator tells Python that this particular class is a data class.

* The indented code inside the class defines the attributes and types that need to be included in the data class.

* In this example, only one data attribute is defined, named `data`.

* The `data` attribute is defined with a data type of `str`, or string. This means that the `data` attribute can store information as text.

* We can add as many attribute names and corresponding data types to the `Block` class as needed for the program.

* The available data types are the same as those associated with Python: string (`str`), integer (`int`), floating point numbers (`float`), and boolean (`bool`) values. There are also data types like `Any` and `List`, which we’ll explore later.

Pose the following question to students: How would the block of data we just created  appear in a system if multiple users wanted to add data?

* The key takeaway is that there is currently no way to know which user added what information to the block of data.

Explain to students that **metadata** is data that provides information about other data. It can be used to provide the user information that we’re looking for.

* **Metadata**, data that describes or provides information about other data—such as the creator of the block and the time of creation—must be added to the block.

* Metadata helps read and identify the data in the shared record-keeping system. By adding this information, the integrity and clarity of the record is improved.

#### Add Metadata to the Block

Add two attributes to the `dataclass` block structure named `creator_id` and `timestamp`, as the following code shows:

  ```python
  # Imports
  from dataclasses import dataclass
  from datetime import datetime

  # Creating the Block data class
  @dataclass
  class Block:
      data: str
      creator_id: int
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
  ```

**Important** It is best to use .py files for these activities. If you run this code in a notebook they might notice that the timestamp of new blocks does not get updated. This is because the Data Class library defines variables when the code for the class is run, not when the class is instantiated (which is the default behavior for regular Python classes). This means the timestamp is only updated when redefining the class, not when creating new instances of the class. This isn't a problem using streamlit, as the entire code is executed with each block addition, producing a unique timestamp each time. If similar code is executed in a notebook, then unique timestamps can be produced by either running all the code in one cell or by defining the timestamp as: `timestamp: datetime = field(default_factory=datetime.now)`.

* By adding this metadata, now anyone will know who created the block and when they created it.

* The attribute `creator_id` is added with a data type of integer (`int`). As a reminder, an integer is zero or a positive or negative whole number without a fractional part (decimal).

* The `timestamp` attribute is defined with a data type of string (`str`), meaning that it will hold the data associated with the timestamp as text.

* A **default value** for the timestamp will be automatically supplied. The default value will be used if no data is supplied for that attribute. In this case, we use the current time as the default value for the timestamp by importing the "datetime" Python library and using it to create a `datetime` object. 

Next, we make the block more versatile by changing the type of the `data` attribute to `Any`.

  ```python
  # Imports
  from dataclasses import dataclass
  from datetime import datetime
  from typing import Any

  # Creating the Block data class
  @dataclass
  class Block:
      data: Any
      creator_id: int
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
  ```

* To use the `Any` type, it must be imported from the typing module.

* This will allow for a wide range of inputs in addition to strings, including lists, dictionaries, and even other data classes.

Tell students that, now that the `Block` class is created, it’s time to use it!

#### Add Data to the Block

Explain that, to use a data class, it needs to be created in memory.

* This is like calling a function in Python. The name of the data class is provided (`Block`, in this case) and data is assigned to the `Block` attributes. Python then creates and stores that block of data in memory.

* Using a data class like this is called creating an **instance** of the data class.

* This is like drawing a blueprint for a house (defining the data class) and then using the blueprint to build the house with real materials (creating an instance of the data class).

Have a TA slack out the link to [Classes](https://docs.python.org/3/tutorial/classes.html) in the Python documentation for further reading.

Create a new block and pass it some data to store. For this example, the data that the block will store is the `“My First Block!”` string.

Define the `data` attribute as the `“My First Block!”` string and the `creator_id` attribute as the (arbitrarily selected) integer 42, as the following code shows:

  ```python
  # Creating a new block
  new_block = Block(data="My First Block!", creator_id=42)

  # Print the new block
  print(new_block)
  ```

Navigate to a terminal instance and run the `block.py` file for the students.

The result of printing the current value of `new_block` should appear similar to the following:

  ```text
  Block(data='My First Block!', creator_id=42, timestamp='18:54:16')
  ```

Point out the following to the students:

* We didn’t need to supply a value for the `timestamp` because we already set up the attribute to use a default value.

* The time is displayed as UTC time, not the timezone that is local to where the program is being run. In this way, all of the times associated with each new block will be recorded relative to one another.

Before moving on, ask the students if they have any questions on either the creation of the `Block` class, or how an instance of the `Block` class is created.

Explain that the next step is to make the block of data easier to use in a distributed way.

* Remember that a blockchain is a distributed ledger. So, for a real-life blockchain, hundreds or even millions of users might add blocks of data to the same chain.

* One way to make the blockchain more user-friendly is to build an interface that displays both the existing blocks of the chain and any newly created blocks directly in a web browser.

* This is where Streamlit comes into play! Streamlit provides all the form components and table elements that are needed in order to display our blockchain data on a webpage. Therefore, it’s possible to build an interactive web application to make it easier for people to interact with the blockchain.

Tell students that in the next activity, they’ll use a Python data class to define a basic blockchain block, and then use Streamlit to add data to it.

---

### 3. Student Do: Build a Blockchain Block (15 min)

**Corresponding Activity** [Build a Blockchain Block](Activities/02-Stu_Build_a_Blockchain_Block)

In this activity, students will build a Streamlit application that accepts user input and then stores that input in a `Block` data class.

> **Important:** Remind students that Streamlit doesn’t work with Jupyter notebooks (`.ipynb` files). For this activity—as well as any future activities in which they build Streamlit applications—we recommend working in Visual Studio Code.

Slack out the following files to students so that they can complete the activity.

**Files:**

[Instructions](Activities/02-Stu_Build_a_Blockchain_Block/README.md)

[Starter file](Activities/02-Stu_Build_a_Blockchain_Block/Unsolved/app.py)

---

### 4. Instructor Do: Review Build a Blockchain Block (10 min)

**Corresponding Activity** [Build a Blockchain Block](Activities/02-Stu_Build_a_Blockchain_Block)

Review the activity solution code.

As Python classes are new to students, be sure to focus on the creation of the `Block` class, including the concepts of the decorator and the attributes.

Even though this is new information for students, encourage them to share their code snippets as you work through the solution.

> **Note:** Feel free to use the following video to guide your review:
[Build a Blockchain Block Solution Walkthrough](https://fast.wistia.net/embed/iframe/vxl11j118g)

**Files:**

[Instructions](Activities/02-Stu_Build_a_Blockchain_Block/README.md)

[Starter file](Activities/02-Stu_Build_a_Blockchain_Block/Unsolved/app.py)

[Solution file](Activities/02-Stu_Build_a_Blockchain_Block/Solved/app.py)

Begin by reviewing the creation of the `Block` dataclass. Here’s the code:

```python
  # Define a class `Block` and add the `@dataclass` decorator.
  @dataclass
  class Block:

      # Define an attribute named `data` with a type of `Any`.
      data: Any

      # Define an attribute named `creator_id` with a type of `int`.
      creator_id: int

      # Define an attribute name `timestamp` with a type of `str`.
      # Use the following code to set the value:
      # `datetime.utcnow().strftime("%H:%M:%S")`
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
  ```

* `@dataclass` is a decorator that informs Python about what is to come, in this case, a dataclass named `Block`.

* The `data` attribute will contain the record information that is to be stored in the `Block` instance.

* The attributes `creator_id` and `timestamp` act as metadata, providing additional information about the instance of the `Block`.

* The `timestamp` is set to default to the current time that the record is created. The time is recorded in UTC format, not the local timezone of the record creator.

Next, create the Streamlit component that holds the data that will eventually be recorded in the block, by using the following code.

* The Streamlit [`text_input` component](https://docs.streamlit.io/en/stable/api.html?highlight=text_input#streamlit.text_input) allows a user to add single lines of text information.

* Compare this to the [`text_area` component](https://docs.streamlit.io/en/stable/api.html?highlight=text_input#streamlit.text_area), which allows for multi-line inputs.

  ```python
  # Referencing the Streamlit library, use the `text_input` function and pass the
  # parameter "Block Data".
  input_data = st.text_input("Block Data")
  ```

Next, create a button that will trigger the action for storing and displaying the `Block` information. Here’s the code:

  ```python
  # Create a Streamlit `button`, and pass the “Add Block” parameter to it.
  if st.button("Add Block"):

      # Create an instance of the `Block` data class called `new_block`
      # Use the user input from Step 2 for the `data` attribute
      # Use the integer 42 for the `creator_id`
      new_block = Block(data=input_data, creator_id=42)

      # Use the `st.write` function to display the new block.
      st.write(new_block)
  ```

* The Streamlit [`button`] begins with an if statement, allowing the function to remain inactive until the button is pushed on the user interface.

* The instance of the `Block` that is created will contain the data that was input by the users and a creator_id, which is hard-coded as the number 42.

* It’s also possible to create a Streamlit input field for this data attribute using the Streamlit [`number_input`](https://docs.streamlit.io/en/stable/api.html?highlight=text_input#streamlit.number_input) component.

* Finally, the Streamlit [`write` function](https://docs.streamlit.io/en/stable/api.html?highlight=write#streamlit.write) is called to display the new block on the application webpage.

Navigate to the terminal instance and run the file, inputting data into the text input field (for example,Test Block 1).

A page similar to the following should appear:

![Streamlit page with block instance](Images/streamlit-page-with-block.png)

* The resulting `Block` instance contains all of the attributes detailed when the `Block` class was created.

Congratulate students for creating their first blockchain block by using only Python and a couple of libraries.

Ask students if they have any questions about creating the `Block` instance before moving on.

---

### 5. Instructor Do: Improving Data Integrity with Hashing (10 min)

**Corresponding Activity** [Intro to Hashlib](Activities/03-Ins_Intro_to_Hashlib)

In this section, you will introduce students to the concept of hashing, especially as it relates to securing the data contained in a block.

**Files:**

[Starter file](Activities/03-Ins_Intro_to_Hashlib/Unsolved/hash.py)

[Solution file](Activities/03-Ins_Intro_to_Hashlib/Solved/hash.py)

Explain that, for the instance of the `Block` class we just created, it’s easy to verify that no one else has changed the data—we simply check the information in the `data` attribute.

* We can determine if someone has changed the string simply by looking at it. However, imagine a block with a data attribute that contains an entire novel.

* Manually validating all of that data would take a lot of time and energy! In these cases, we need a better approach. This is where hashing comes in.

* **Hashing** is a cryptography technique that takes a piece of input data and then outputs a fixed-length, mathematical representation of that data—the data hash.

* A **hash** hides the input and gives you an output that represents the data.

* Hashing functions have three key properties:

  1. When given a piece of unique data, a hashing function **always returns the same unique hash** for that piece of data. In other words, the same input will always return the same output.

  2. Hashing functions return **fixed-length** hashes. That is, all hashes returned by the same function have the same length.

  3. Hashing functions are always **one-way** functions—you can’t determine the input (the original piece of data) by analyzing the output (the hash).

Navigate to the following image in the slide deck:

![An illustration depicts input turning into a long number, or the hash. But, the hash can’t then turn into the piece of input.](Images/hashing-example.png)

Explain the image using these talking points:

* A hash is like a fingerprint for a piece of data. If you change even a little bit of the input data (say, one word in the  novel we mentioned earlier), you’ll get a completely different hash.

* Hashing functions are one-way functions. The data is translated via the hashing function into the hash code. It’s not possible to translate a hash code back into the original pieces of data. This makes hashing especially useful for securing private data, such as financial or medical records.

Explain that hashing is a fundamental component of a blockchain.

* We can verify whether the data in a block has changed by checking the hash for the block. This is because the same input data always returns the same hash, and even slightly different input data returns a completely different hash.

Tell students we’ll add a hashing function to the `Block` class instance. But before doing so, let’s explore how data is hashed by using Python.

* Some industry-standard hashing functions are available in a Python library named hashlib.

Navigate to the [starter file](Activities/03-Ins_Intro_to_Hashlib/Unsolved/hash.py) to demonstrate the hashlib library.

#### Use hashlib

First, import the hashlib library by using the following code:

  ```python
  # Imports
  import hashlib
  ```

* The hashlib library provides access to various hashing functions.

* The `sha256` function is a common hashing function for validating the integrity of a file.

Access the `sha256` function from hashlib by creating an instance of the function named `sha`, as shown in the following code:

  ```python
  # Create an instance of the sha256 hashing function
  sha = hashlib.sha256()
  ```

* The `sha` instance of the `sha256` hashing function can be used to encode any piece of input data as a fixed-length output.

* This `sha256` function returns hashes that are 64 characters long.

* Later, the `sha256` function will be used to encode the data in instances of the `Block` data class.

#### Encode the Data with a Hashing Function

Explain that encoding data is a two-step process.

* The first step is to convert the text strings of our data into a standard format that the hashlib library can use.

* The second step is to hash  the converted, or encoded data.

Explain that the Python `encode` function encodes a text string and converts the text into a standard format, as shown in the following code:

  ```python
  # Create the data input to be hashed
  my_data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a nisi et nunc sollicitudin laoreet in sed neque. Proin convallis varius odio, id euismod justo tristique at. Cras at ultricies nisi, sed vulputate ante. Praesent faucibus odio in tortor tincidunt tincidunt. Vivamus interdum, tortor ac semper laoreet, nisl nibh tincidunt ante, vitae iaculis arcu sapien quis turpis. Nunc in ullamcorper enim. Sed in est egestas, pulvinar orci in, laoreet nisl."

  # Encode the data using the encode function
  encoded_data = my_data.encode()
  ```

* A new variable named `my_data` is defined and assigned to a string of text (specifically, a whole paragraph). In this case, lorem ipsum text is used to simulate data.

* The `encode` function is included with Python, which is why it can be used without first having to reference it in a library.

* The `encode` function is used to convert the data from human-readable language to computer-readable language.

* The encoded data can now be passed to the hashing function in order to get a hash.

Next, use the `update` function to pass the encoded data to the hashing function, as shown in the following code.

  ```python
  # Update the encoded data
  sha.update(encoded_data)
  ```

* The `update` function converts the encoded data into a bytes-like object, or data that can be used for various operations that work with binary data.

Finally, return a hash from the `sha` object via the `hexdigest` function, as shown in the following code:

  ```python
  # Print the hash code resulting from the hexdigest function
  print(sha.hexdigest())
  ```

* The hash code resulting from the `hexdigest` function is a string object that contains only hexadecimal digits—the numbers 0–9 and the capital letters A–F—from the data passed to the `update` function.

Run this code for students, highlighting the unique hash that is returned as the output.

  ```text
  99d76fef961c38bfe8bc8fb2e80e99b0638cf5420d1d0ff7ef5027551fc52b53
  ```

* Confirm that the output is 64 characters long.

* This is how we hash a piece of data into a unique data fingerprint!

Explain that the data fingerprint and its hash can be used to verify that the data hasn’t changed.

* If the same hash code is returned for hashed data, it verifies that the input data has not been altered. Remember, the same input will always result in the same output when the same hashing function is used.

Recap the hashing process for the students:

1. Create a new `sha` object by using the hashlib library.

2. Encode the text string with the Python `encode` function.

3. Update the `sha` object with the encoded data.

4. Return the unique hash (the fingerprint) of the data via the `hexdigest` function.

Ask students if they have any questions about using the hashlib `sha256` hash function to convert data into a unique 64-character string.

Tell students that in the next activity, they’ll practice what they’ve learned so far: the `Block` class, Streamlit, and hashing.

### 6. Student Do: Hashing with Hashlib (15 min)

**Corresponding Activity** [Hashing with Hashlib](Activities/04-Stu_Hashing_with_Hashlib)

In this activity, students will use the hashlib library and Streamlit to build an application that can hash any text input.

Have a TA slack out the following files to the students:

**Files:**

[Instructions](Activities/04-Stu_Hashing_with_Hashlib/README.md)

[Starter file](Activities/04-Stu_Hashing_with_Hashlib/Unsolved/app.py)

---

### 7. Instructor Do: Review Hashing with Hashlib (10 min)

**Corresponding Activity** [Hashing with Hashlib](Activities/04-Stu_Hashing_with_Hashlib)

In this review, focus on how to incorporate the hashlib library, as well as the hash code that results from applying `sha256` to the original text.

As you review, encourage students to share their solutions. Live code the snippets that students do not volunteer.

> **Note:** Feel free to use the following video to guide your review:
>
> [Hashing with Hashlib Solution Walkthrough](https://fast.wistia.net/embed/iframe/j3e149n4th)

**Files:**

[Instructions](Activities/04-Stu_Hashing_with_Hashlib/README.md)

[Starter file](Activities/04-Stu_Hashing_with_Hashlib/Unsolved/app.py)

[Solution file](Activities/04-Stu_Hashing_with_Hashlib/Solved/app.py)

Open the starter file. Point out that the hashlib and Streamlit libraries have already been imported.

  ```python
  # Imports
  import hashlib
  import streamlit as st
  ```

Next, review the code for creating the function that hashes an input value:

  ```python
  # Define a function called `hash_data` that takes in a parameter called `data`
  def hash_data(data):

      # Call an instance of hashlib's `sha256` function
      sha = hashlib.sha256()

      # Use the `encode` function to encode the string version of the data that
      # was passed in as a parameter to the function
      encoded_data = str(data).encode()

      # Call the hashing instance and the `update` function. Pass it the encoded
      # data as a parameter
      sha.update(encoded_data)

      # Return the unique hash of the data using the `hexdigest` function
      return sha.hexdigest()
  ```

* First, declare a variable `sha` that calls the hashlib library and the `sha256` function.

* The data being hashed must first be encoded. This converts the data from human-readable language to computer-readable language.

* Once the data is encoded, the `sha.update` function is called to create the unique, 64-character hash code.

* Finally, the `sha.hexdigest` function is called to return the hash.

Next, use the Streamlit [`text_area` component](https://docs.streamlit.io/en/stable/api.html?highlight=text_input#streamlit.text_area) to create a space in the application to input text from the user. In order to do this, the Streamlit data must first be converted into a string, and then encoded:

  ```python
  # Add a Streamlit `text_area` component to accept data from the user
  # Be sure to convert the input data to a string
  # Use the `encode` function to encode the input data
  input_data = str(st.text_area("Enter Data")).encode()
  ```

To compare the length of the original input text to the length of the output hash, write the length of the input text to the screen, using the following code:

  ```python
  # Use the Streamlit `write` function to display the length (`len`) of the input
  # data back to the user
  st.write(f"Input Length: {len(input_data)}")
  ```

* This will show that the length of the input text does not influence the length of the resulting hash.

Now, create the Streamlit button that calls the `hash_data` function and, using the input text, returns both an `input_hash` value and the length of the hash. This is shown in the following code:

  ```python
  # Add a Streamlit `button` named “Hash Text”
  if st.button("Hash Text"):

      # Generate a hash of the user input using the `hash_data` function
      input_hash = hash_data(input_data)

      # Use the Streamlit `write` function to display the unique hash of the data
      st.write(f"Output Hash (fingerprint): {input_hash}")

      # Use the Streamlit `write` function to display the length of the output hash.
      st.write(f"Output Length: {len(input_hash)}")
  ```

Finally, navigate to a terminal instance and run the Streamlit application.

Use one of the lorem ipsum sites to get the text:

* [Lorem Ipsum](https://www.lipsum.com/)

* [Bacon Ipsum](https://baconipsum.com/)

* [Cupcake Ipsum](http://www.cupcakeipsum.com/)

After entering the text into the text-input area, click the Hash Text button. Point out  the values for the length of the text as well as the hash code and hash length.

Change one letter in the text and rerun the application. Show the students that the hash code is completely different.

Add a new paragraph to the text already present. Again, show that the hash code is completely different. Also, despite the change in the length of the input text, the hash code is still 64 characters in length.

Ask students if they have any questions about the hashlib library or the `sha256` function.

Recap the activity by asking students the following questions. Ask for volunteers to share their answers.

**Question:** When we hash data with the `sha256` function, how many characters is the resulting hash?

  * **Answer:** The fixed length of data hashed with the `sha256` function is 64 characters.

**Question:** Is it possible to determine the original data from the related hash code?

  * **Answer:** No. One of the primary features of hashing is that it is only one way. You cannot determine the original data from the hash code.

**Question:** Will similar data entries result in similar hash codes?

  * **Answer:** No. Even a minor change in data will result in a completely unique and different hash code.

**Question:** Why must data be encoded before it can be hashed?

  * **Answer:** Encoding data converts it from a human-readable form into computer-readable form so that it can be hashed.

---

### 8. Break (15 min)

---

### 9. Instructor Do: Add Hashing to the Block Data Class (15 min)

**Corresponding Activity** [Adding a Method to a Class](Activities/05-Ins_Adding_a_Method_to_a_Class)

This section will introduce students to the concept of adding methods to a data class.

Focus on getting students to understand the concept of `self`, which is key to successfully working with methods inside a data class.

**Files:**

[Starter file](Activities/05-Ins_Adding_a_Method_to_a_Class/Unsolved/method.py)

[Solution code](Activities/05-Ins_Adding_a_Method_to_a_Class/Solved/method.py)

Welcome the class back from the break.

Recap that hashing is a simple but powerful tool for validating data—that is, for verifying that no one has tampered with the data.

* Data is validated by comparing hash values. Because of a hash value's unique fingerprint, changing even the smallest data element will result in completely different hash codes.

Explain that the integrity of each block is an essential aspect of a blockchain.

* In order for users to validate the integrity of the data, there needs to be a function that can hash each block and return its unique fingerprint.

* In this part of the lesson, students will apply their new hashing skills in order to create a hashing function that returns a unique fingerprint of the data in each `Block` instance

Explain that a data class can contain functions.

* These functions can perform actions on the data attributes of that class.

* Functions that are defined inside a class are called **methods**.

Open the [starter file](Activities/05-Ins_Adding_a_Method_to_a_Class/Unsolved/method.py) and add a `Counter` dataclass to the existing code base.

Tell students that the data in this file should look familiar—it’s the code to create and test the `Block` class.

Run the code in the terminal to show the output, which should look like the following:

  ```text
  Block(data='test', creator_id=0, timestamp='16:49:11')
  ```

#### Add a Method to a Data Class

First, create a new data class called `Counter`. This class should be created below all of the code associated with the `Block` class.

* The `Counter` class should include a data attribute named `count`, which has a type of `int` and a default value of 0, as the following code shows:

  ```python
  # Create a data class called Counter
  @dataclass
  class Counter:
      count: int = 0
  ```

* The `Counter` data class will be used to record a count—for example, the number of cars that drive by an office window.

* The data attribute defined in the `Counter` class is named `count`, and it’s assigned a data type of integer `int`.  The `count` attribute is assigned a starting value of 0.

Explain that the next step is to find a way to increase the count—for example, when a new car drives by.

* Classes can perform actions via custom internal functions, which, as mentioned earlier, are often called methods.

* Methods perform an action, like increasing the value of the `count` variable.

* The method associated with `Counter` will be called `update_count`, as shown in the following code:

  ```python
  # Create the data class called Counter
  # Include a method called update_count
  @dataclass
  class Counter:
      count: int = 0
      def update_count(self):
          self.count = self.count + 1
  ```

Explain a key aspect of methods: they can pass a built-in parameter named **self**.

* The `self` parameter gives the method access to all the values, or attributes, inside the class.

* Any data or function ("method") can be accessed from the `Counter` class by using the `self` parameter. Here, the `update_count` method can use and update the count data by using `self.count`.

* `self.count` is set equal to `self.count + 1`. This increments the count in the class instance each time that the `update_count` method is called.

#### Test the Counter Class

Instantiate a new instance of the `Counter` class.

* The class `Counter` is called and set equal to a variable called `new_counter`, as shown in the following code:

  ```python
  # Create a new instance of Counter
  new_counter = Counter()
  ```

Next, call the `update_count` method twice to update the count to 2:

  ```python
  # Update the count by calling update_count
  new_counter.update_count()
  new_counter.update_count()

  # Print the updated value of count
  print("The current count is: ", new_counter.count)
  ```

* The count of this `Counter` instance is accessed by calling `new_counter.count`.

Run the code in the terminal, confirming that the current count is 2:

  ```text
  The current count is: 2
  ```

Change the value of the `count` variable to `2` and rerun the code. The output changes:

  ```text
  The current count is: 4
  ```

* Classes are useful because developers can use them to wrap their required values and functions in usable data structures that are easily expanded to include additional attributes and methods.

The next step is to apply the concept of methods in order to add a hashing function to the `Block` class.

#### Create a Hashing Function for the Block Class

The following code shows the current `Block` class:

  ```python
  # Imports
  from dataclasses import dataclass
  from datetime import datetime
  from typing import Any
  import hashlib

  # The Block class
  @dataclass
  class Block:
      data: Any
      creator_id: int
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
  ```

Inside the `Block` class and below the `timestamp` attribute, define a new method named `hash_block`.

* This method uses the `self` parameter to access each data attribute defined in the `Block` class, hashes the values in those attributes, and then returns all the resulting hashes. This is shown in the following code:

  ```python
  # Create a method called hash_block
  def hash_block(self):
      sha = hashlib.sha256()

      # Turn the block data into an encoded string
      data = str(self.data).encode()
      sha.update(data)

      # Turn the block creator_id into an encoded string
      creator_id = str(self.creator_id).encode()
      sha.update(creator_id)

      # Turn the block timestamp into an encoded string
      timestamp = str(self.timestamp).encode()
      sha.update(timestamp)

      return sha.hexdigest()
  ```

Break down what’s happening in this code for the students.

* First, the `sha` variable  is defined as our hash function, `sha256`, as the following line shows:

  ```python
  sha = hashlib.sha256()
  ```

* The next step is to encode the string value of each of the blockchain attributes: `data`, `creator_id`, and `timestamp`:

  * The `self` parameter is used to access and encode each of these attributes in the `Block` class.

  * The data type of `self.data` is `Any`, and the `creator_id` is `int`.

  * The Python `str` function is used to convert those attributes into strings before encoding the strings into a standard format.

  ```python
  data = str(self.data).encode()
  creator_id = str(self.creator_id).encode()
  timestamp = str(self.timestamp).encode()
  ```

* Next, the attributes are hashed by using the `sha.update` function.

  ```python
  sha.update(data)
  sha.update(creator_id)
  sha.update(timestamp)
  ```

* Finally, the updated information of all the data attributes is combined into a single hash by using the `hexdigest` function.

  ```python
  return sha.hexdigest()
  ```

Here’s the complete code of the `Block` data class with the addition of the  new `hash_block` method:

  ```python
  # The Block class including a hash_block method
  @dataclass
  class Block:
      data: Any
      creator_id: int
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

      def hash_block(self):
          sha = hashlib.sha256()

          data = str(self.data).encode()
          sha.update(data)

          creator_id = str(self.creator_id).encode()
          sha.update(data)

          timestamp = str(self.timestamp).encode()
          sha.update(timestamp)

          return sha.hexdigest()
  ```

Explain that just a few more lines of code are needed to test the `hash_block` functionality.

* The code for creating the next "Block" is in place. The `data` being passed is "test", and the `creator_id` is "0".

* The new block's hash is created by calling the `hash_block` method, which results in a single hash code for the entire block.

* Finally, rather than printing the `new_block`, the code is updated to print the `block_hash`.

The code associated with these talking points is as follows:

  ```python
  # Create a new block instance using some test data
  new_block = Block(data="test", creator_id=0)

  # Calculate the block hash using the new method
  block_hash = new_block.hash_block()

  #  block's hash
  print(block_hash)
  ```

The resulting output from running the code should look similar to the following hash:

  ```text
  '41d7255780adf0b3b9431e778af5c1de96fc368412df4759775bffa2b5e849aa'
  ```

Remind students that when a block defaults to the current timestamp, no two hashes will match, regardless of whether the other input elements match.

Ask the students if they have any questions about how an instance of a new `Block` is converted into a single hash code using the `hash_block` method.

Pose the following question as a review:

**Question:** What does the `self` keyword provide access to inside of a class?

  * **Answer:** The `self` keyword allows methods written inside of a class to access the attributes (and even other methods) defined in that same class.

Tell students that in the next activity, they’ll practice adding the `hash_block` functionality to a `Block` class and its Streamlit web interface.

---

### 10. Student Do: Hashing a Block (15 min)

**Corresponding Activity** [Hashing a Block](Activities/06-Stu_Hashing_a_Block)

In this activity, students will create a Streamlit application that can create a new block of data and display the hash for that block.

Have a TA slack out the following files to the students:

**Files:**

[Instructions](Activities/06-Stu_Hashing_a_Block/README.md)

[Starter file](Activities/06-Stu_Hashing_a_Block/Unsolved/app.py)

---

### 11. Instructor Do: Review Hashing a Block (10 min)

**Corresponding Activity** [Hashing a Block](Activities/06-Stu_Hashing_a_Block)

In this review, focus on how the `hash_block` function is created, especially the use of the `self` keyword.

As you review, encourage students to share their solutions. Live code the snippets that students do not volunteer.

> **Note:** Feel free to use the following video to guide your review:
>
> [Hashing a Block Solution](https://fast.wistia.net/embed/iframe/hmocp6c1ht)

**Files:**

[Instructions](Activities/06-Stu_Hashing_a_Block/README.md)

[Starter file](Activities/06-Stu_Hashing_a_Block/Unsolved/app.py)

[Solution file](Activities/06-Stu_Hashing_a_Block/Solved/app.py)

Open the starter file and review the libraries that have already been imported, as well as the `Block` data class:

  ```python
  import streamlit as st
  from dataclasses import dataclass
  from typing import Any, List
  from datetime import datetime
  import hashlib

  @dataclass
  class Block:
      data: Any
      creator_id: int
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")
  ```

#### Add the hash_block Function

The first step of the activity is to add a function named `hash_block`. This function includes an instance of the `sha256` hashing function, and it will encode and hash the `data`,  `creator_id`, and `timestamp` attributes. The function should return the resulting hashes in a `hexdigest` format.

As you review the code, engage the students with the following questions:

**Question:** What is another name for a function located inside a Python class?

  * **Answer:** A function located inside a Python class is also called a **method**.

**Question:** What does the `self` keyword provide access to?

  * **Answer:** The `self` keyword enables access to the attributes and methods defined inside the Python class.

  ```python
  @dataclass
  class Block:
      data: Any
      creator_id: int
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

      # Add a new function called `hash_block`
      def hash_block(self):

          # Add an instance of the `sha256` hashing function
          sha = hashlib.sha256()

          # Encode the Block's data attribute
          data = str(self.data).encode()
          # Update the encoded data using the hashing function
          sha.update(data)

          # Encode the Blocks's creator_id attribute
          creator_id = str(self.creator_id).encode()
          # Update the encoded creator_id using the hashing function
          sha.update(creator_id)

          # Encode the Block's timestamp attribute
          timestamp = str(self.timestamp).encode()
          # Update the encoded timestamp using the hashing function
          sha.update(timestamp)

          # Return the hashes of all the Block class attributes
          return sha.hexdigest()
  ```

#### Code the Streamlit Button

In the next section of this review, code the action portion of a Streamlit button. Review the following:

* Call the `hash_block` method on the `new_block` that is defined inside the button. This method call is set equal to the variable `block_hash`.

* The `st.write` component allows us to display the hash code returned from the `hash_block` function to the application page.

* These steps are captured in the following code:

  ```python
  if st.button("Add Block"):
      new_block = Block(data=input_data, creator_id=42)
      st.write(new_block)

      # Call the `hash_block` function on the `new_block` to create a `block_hash`
      block_hash = new_block.hash_block()

      # Use `st.write` to display the `block_hash` to the page.
      st.write(f"The block's hash is: {block_hash}")
  ```

Ask the students if they have any questions about the process of hashing data or returning the result.

Congratulate them on completing another activity and expanding their blockchain skill set.

Review what we've done so far: the code we’ve written takes in data and creates a hashed block, which are two key steps in creating a blockchain.

Explain that the next step in building a blockchain is to link the individual blocks being created into a chain.

---

### 12. Instructor Do: Chaining Blocks (15 min)

**Corresponding Activity** [A Chain of Blocks](Activities/07-Ins_A_Chain_of_Blocks)

In this activity, you will build a PyChain dataclass that completes the blockchain.

**Files:**

[Starter file](Activities/07-Ins_A_Chain_of_Blocks/Unsolved/chain.py)

[Solution file](Activities/07-Ins_A_Chain_of_Blocks/Solved/chain.py)

Introduce the concept that a blockchain is a series (or a chain) of data containers (or blocks).

* There’s data in each block, and the order in which these blocks are added to the chain often matters.

* For example, consider a blockchain that holds records of financial transactions. The order in which these transactions occur has importance; for instance, you might need to transfer money into an account before you can use that account to make a purchase.

* Blockchain uses hashing to maintain not only the integrity of the data but also the order of the data over time.

* The software program that underlies the blockchain hashes the data when creating the block, as well as links the blocks to each other. When the software creates a new block, it links the new block to the previous block.

* It does this by adding the hash of the previous block to the data of the new block. The hash of the previous block becomes part of the data in the new block.

Navigate to the following image in the slide deck to illustrate the link between hashes.

![An illustration depicts a chain of three blocks, each of which includes its own hash and the hash of the previous block.](Images/blocks-chained-by-hash-codes.png)

* The purpose of linking blocks by hash code is that if someone changes the data in the previous block, the new block will know. This is because the hash of the previous block will change, and the new block already knows what that hash should be.

* This continual linking of block to block via the hashes is how the “chain” part of a blockchain works. The chaining process means that the hash of a new block depends on the integrity of all the previous blocks.

Present the following example:

* Let’s say that we have a blockchain of 10 blocks. Someone changes the data in Block 5, which also changes the hash of Block 5. Because the data in each block includes the hash of the previous block, the data in Block 6 includes the original hash of Block 5. When the hash of Block 5 changes, the hash of Block 6 becomes invalid. This, in turn, invalidates the hash of Block 7, and so on throughout the chain. So, if a malicious hacker tries to change either the data in any block or the sequence of the blocks, the rest of the chain becomes invalid.

Sum up the chaining process:

* The chaining process allows all users of the blockchain to validate the records in the chain over time.

* Users can thus trust the integrity and order of the data in the chain.

* This capability of blockchain—maintaining data integrity without a central authority—is one of the most exciting innovations of this technology.

Explain to students that now we’ll implement a chain of blocks for our Python blockchain.

Open the [starter file](Activities/07-Ins_A_Chain_of_Blocks/Unsolved/chain.py) for this activity and review the code.

* The code should look familiar—it’s the `Block` data class, including the `hash_block` functionality from the prior demonstration.

  ```python
  # Imports
  from dataclasses import dataclass
  from datetime import datetime
  from typing import Any
  import hashlib

  # Creating a dataclass called Block
  @dataclass
  class Block:
      data: Any
      creator_id: int
      prev_hash: str = "0"
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

      def hash_block(self):
          sha = hashlib.sha256()

          data = str(self.data).encode()
          sha.update(data)

          timestamp = str(self.timestamp).encode()
          sha.update(timestamp)

          prev_hash = str(self.prev_hash).encode()
          sha.update(prev_hash)

          return sha.hexdigest()


  # Create a new block instance using some test data
  new_block = Block(data="test", creator_id=0)

  # Calculate the block hash using the new method
  block_hash = new_block.hash_block()

  # Print the block's hash
  print(block_hash)
  ```

#### Create a Chain of Blocks

Explain that the process of creating a chain of blocks begins with creating a new data class to hold the blocks.

Below the `Block` class, create the code for a custom `PyChain` data class. The name of this custom data class will be `PyChain`, as the following code shows:

  ```python
  # Creating a data class called PyChain
  @dataclass
  class PyChain:
  ```

Next, define one attribute named `chain` in the `PyChain` class.

* This `chain` attribute is where all the blocks in the blockchain will be stored.

  ```python
  # Creating a data class called PyChain
  @dataclass
  class PyChain:
      chain:
  ```

Explain that in order to create the `chain` attribute, we need to use the `List` type.

* The data type specified for this `chain` attribute is slightly more complex than those that we've used so far.

* A container needs to be specified that can store all the instances of the `Block` data class in the chain. To do this, we first import the `List` type from the typing module, as shown in the following code.

  ```python
  # Imports
  from typing import List
  ```

Inside the `PyChain` data class, set the type for `chain` as `List[Block]`.

* To accommodate the list of blocks, define a  `List` type that itself contains `Block` types, as the following code shows.

  ```python
  # Creating a data class called PyChain
  @dataclass
  class PyChain:
      chain: List[Block]
  ```

Finally, add a method to `PyChain` that can add a new block to the chain.

* The name of this new method is `add_block`. This method accepts a new block and appends it to the existing chain:

  ```python
  def add_block(self, block):
      self.chain += [block]
  ```

* The final `PyChain` class now has one new attribute, named `chain`, to store our blocks.

* It also now has a method, named `add_block`, that can add new blocks to the chain. This is shown in the following code.

  ```python
  # Creating a data class called PyChain
  @dataclass
  class PyChain:
      chain: List[Block]

      def add_block(self, block):
          self.chain += [block]
  ```

Test the code for students by creating an instance of the `PyChain` data class.

* To mimic how a real blockchain works, the new chain is initialized with a starting block, which is called a **Genesis block**.

* The Genesis block provides a starting point for every new block to work from.

  ```python
  # Initiating a new chain with the Genesis block
  pychain = PyChain([Block(data="Genesis", creator_id=0)])

  print(pychain)
  ```

Run the code as written. It should return something similar to the following output:

  ```text
  PyChain(chain=[
      Block(data='Genesis', creator_id=0, prev_hash=0, timestamp='23:17:19')
  ])
  ```

* The output shows that the chain now contains one block, the Genesis block.

* It also shows the metadata of the Genesis block.

Explain that we now have a data class that can store blocks of data! The next step is to write the code that will link new blocks of data to the chain.

#### Link Blocks to the Chain

Explain that, each time that a new block is added, it must be linked to the chain with the hash of the previous block. The basic process for linking blocks is as follows:

1. Select the last block in the chain.

2. Calculate the hash of the last block in the chain.

3. Create a new block that includes a data attribute named `prev_hash`, and use this attribute to store the hash of the last block.

4. Update the chain with the new block.

Explain that the goal in writing a functioning blockchain is to code each of these steps, starting with selecting the last block in the chain.

#### Select the Last Block in the Chain

Explain that selecting the last block in the chain is important, because the hash of this last block becomes information added to the next block in the chain.

* Use the index position of -1 to select the last block.

* The last block is assigned to a variable named `prev_block`, as the following code shows:

  ```python
  # Access the last block in the chain
  prev_block = pychain.chain[-1]
  ```

#### Calculate the Hash of the Last Block

Next, calculate the hash of this block. Assign this hash to a variable named `prev_block_hash`, as the following code shows:

  ```python
  # Calculate the hash for the last block in the chain
  prev_block_hash = prev_block.hash_block()
  ```

* Now that we have the hash of the last block, we can create a new block and store this hash in one of its data attributes.

* Doing this creates a cryptographic link to the previous block. If the data in the previous block ever changes, the hash stored in this new block will no longer match.

#### Create a New Block that Includes a Data Attribute Named prev_hash

Store the hash of the last block as an attribute in the `Block` data class.

* To store the hash of the last block as an attribute in the new block, add the `prev_hash` attribute to the `Block` data class. This attribute has a string data type and an initial value of 0, as the following code shows:

  ```python
  # Add an attribute called prev_hash to the Block class
  prev_hash: str = "0"
  ```

#### Update the Chain with the New Block

Now, the final step of linking a new block to the chain is to encode the hash of the previous block, and then update the hash, as shown in the following code:

  ```python
  # Encode and update the hash of the previous block
  prev_hash = str(self.prev_hash).encode()
  sha.update(prev_hash)
  ```

* The `prev_hash` attribute should now be included as part of the information contained in the new `Block`.

* To correctly add the `prev_hash` attribute to the new Block, it must be encoded and hashed like the `data` and `timestamp` attributes.

Explain that this code essentially hashes the old hash. That is, the old hash is encoded and then added to the data that will be hashed for the new block.

The following code defines the `Block` data class which nows includes hashing the `prev_hash` attribute, along with all the other attributes of the block, and returns an overall new hash:

  ```python
  # Creating a data class called Block
  @dataclass
  class Block:
      data: Any
      creator_id: int
      prev_hash: str = "0"
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

      def hash_block(self):
          sha = hashlib.sha256()

          data = str(self.data).encode()
          sha.update(data)

          timestamp = str(self.timestamp).encode()
          sha.update(timestamp)

          prev_hash = str(self.prev_hash).encode()
          sha.update(prev_hash)

          return sha.hexdigest()
  ```

The code for the full PyChain blockchain should appear as follows:

  ```python
  # Imports
  from dataclasses import dataclass
  from datetime import datetime
  from typing import Any
  import hashlib
  from typing import List

  # Creating a dataclass called Block
  @dataclass
  class Block:
      data: Any
      creator_id: int
      prev_hash: str = "0"
      timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

      def hash_block(self):
          sha = hashlib.sha256()

          data = str(self.data).encode()
          sha.update(data)

          timestamp = str(self.timestamp).encode()
          sha.update(timestamp)

          prev_hash = str(self.prev_hash).encode()
          sha.update(prev_hash)

          return sha.hexdigest()


  # Creating a data class called PyChain
  @dataclass
  class PyChain:
      chain: List[Block]

      def add_block(self, block):
          self.chain += [block]

  # Initiating a new chain with the Genesis block
  pychain = PyChain([Block(data="Genesis", creator_id=0)])

  print(pychain)

  # Access the last blocka in the chain
  prev_block = pychain.chain[-1]

  # Calculate the hash for the last block in the chain
  prev_block_hash = prev_block.hash_block()
  ```

Explain to students that, at this point, the code has been completed for both the `Block` and `PyChain` classes. Now it’s time to test the PyChain functionality. To do this, we’ll create a new block and add it to the chain.

#### Test the PyChain

First, create a new instance of the `Block` class, as shown in the following code.

  ```python
  # Create a new instance of the Block class
  new_block = Block(data="new_block", creator_id=42, prev_hash=prev_block_hash)
  ```

Explain that, to add a new block to the chain, use the `add_block` method of the `PyChain` class. Here’s the code:

  ```python
  # Add the new block to the chain
  pychain.add_block(new_block)
  print(pychain)
  ```

Run the code to confirm that the `prev_hash` value is added to the `new_block` information.

* The output shows that we now have the Genesis block and the new block stored inside the chain:

  ```text
  PyChain(chain=[
      Block(data='Genesis', creator_id=0, prev_hash=0, timestamp='23:17:16'),
      Block(data='new_block', creator_id=42, prev_hash='88499086683fb6766a7792147d52108af9515c73a67e0fd2e24d6853f20b65ac', timestamp='23:17:16')])
  ```

* The blockchain works! The data in the new block includes the hash of the Genesis block, so these blocks are now linked.

* We also need to test our code in the Streamlit application. But first, we need to add one piece of Streamlit code to make our PyChain application work as expected.

#### Code a Blockchain with Streamlit

Start by explaining that a Streamlit application reruns all its code any time that an on-screen Streamlit component is used to change or update the data.

* Previously, we only tested one block of code at a time, so this didn’t matter. Because we only ever added the Genesis block, it was never deleted when a second block was created.

* With the addition of the `PyChain` data class, the application now needs to remember the data that an instance of our `PyChain` data class contains.

* This is accomplished by adding a [**cache decorator**](https://docs.streamlit.io/en/stable/caching.html). The cache decorator saves the property values—in this case, the Genesis instance of the `Block` class—in the memory of the Streamlit application during the time that the webpage is open.

Have a TA slack out the following block of code to the students:

  ```python
  @st.cache(allow_output_mutation=True)
  def setup():
      return PyChain([Block(data="Genesis", creator_id=0)])

  pychain = setup()
  ```

Explain that this code ensures that Streamlit will remember the data in the blockchain.

Ask students if they have any questions about the `PyChain` data class and how the `prev_hash` value is used to link together blocks of data in the chain.

---

### 13. Student Do: Blockchain Application (15 min)

**Corresponding Activity** [Blockchain Application](Activities/08-Stu_Blockchain_Application)

In this activity, students will enhance a Streamlit application that generates new blocks of user data and adds the blocks to a Python blockchain.

> **Notes:**
>
> If you’re running short on class time, complete the activity as a code-along, encouraging as much student participation as possible.

Have a TA slack out the following files to the students:

**Files:**

[Instructions](Activities/08-Stu_Blockchain_Application/README.md)

[Starter file](Activities/08-Stu_Blockchain_Application/Unsolved/app.py)

---

### 14. Instructor Do: Review Blockchain Application (10 min)

**Corresponding Activity** [Blockchain Application](Activities/08-Stu_Blockchain_Application)

In this review, focus on the role of the `prev_hash` values in linking the block in the `PyChain`. Also, address the role of the `cache decorator` in ensuring that the Genesis block stays persistent when a second block is added to the chain.

> **Note:** Feel free to use the following video to guide your review:
>
> [Blockchain Application Solution Walkthrough](https://fast.wistia.net/embed/iframe/im8f2l6vaq)

**Files:**

[Instructions](Activities/08-Stu_Blockchain_Application/README.md)

[Starter file](Activities/08-Stu_Blockchain_Application/Unsolved/app.py)

[Solution file](Activities/08-Stu_Blockchain_Application/Solved/app.py)

First, review the code for both the `Block` and `PyChain` data classes, which is provided in the starter file:

  ```python
  # Imports
  import streamlit as st
  import datetime as datetime
  from dataclasses import dataclass
  from typing import Any, List
  import pandas as pd
  import datetime as datetime
  import hashlib

  ################################################################################
  # Creates the Block and PyChain data classes


  @dataclass
  class Block:
      data: Any
      creator_id: int
      prev_hash: str = "0"
      timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

      def hash_block(self):
          sha = hashlib.sha256()

          data = str(self.data).encode()
          sha.update(data)

          creator_id = str(self.creator_id).encode()
          sha.update(creator_id)

          timestamp = str(self.timestamp).encode()
          sha.update(timestamp)

          prev_hash = str(self.prev_hash).encode()
          sha.update(prev_hash)

          return sha.hexdigest()

  # Create the data class PyChain


  @dataclass
  class PyChain:
      chain: List[Block]

      def add_block(self, block):
          self.chain += [block]
  ```

Next, review the code for the Streamlit application that is also included in the `app.py` file.

This review should include a discussion about the cache decorator, which is used to maintain the existence of each block as long as the application window is kept open.

Also, address the `setup` function. Although the function is new, the code contained within the `setup` function should be familiar.

* The `setup` function is used to initialize the instance of the `PyChain` data class with the Genesis block.

* This instance of the `PyChain` data class will be established with the variable `pychain`. This variable will be used to access the blockchain throughout the application. The code is as follows:

  ```python
  @st.cache(allow_output_mutation=True)
  def setup():
      print("Initializing Chain")
      return PyChain([Block(data="Genesis", creator_id=0)])


  pychain = setup()
  ```

The activity asks students to create the code for the "Add Block" button, which is as follows:

  ```python
  if st.button("Add Block"):

      # Select the previous block in the chain
      prev_block = pychain.chain[-1]

      # Hash the previous block in the chain
      prev_block_hash = prev_block.hash_block()

      # Create a new block in the chain
      new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)

      # Add the new block to the chain
      pychain.add_block(new_block)

  ```

* The first time through, the `prev_block` will be the `Genesis` block. The `Genesis` block will be hashed by the `hash_block` method from the `Block` class.

* The value for the `prev_block_hash` will then become an input value for the creation of the next `new_block`.

* The `new_block` is added to the chain by calling the `add_block` method from the `PyChain` class.

Finally, review the code to post the `PyChain` blockchain (ledger) to the application page:

  ```python
  st.markdown("## PyChain Ledger")

  # Create a Pandas DataFrame to display the `PyChain` ledger
  pychain_df = pd.DataFrame(pychain.chain)

  # Use the Streamlit `write` function to display the `PyChain` DataFrame
  st.write(pychain_df)
  ```

* The `pd.DataFrame` function is called to create the chain (`pychain.chain`) as a Pandas DataFrame.

* Remember, the variable `pychain` is associated with the instance of the `PyChain` class that was defined when the `setup` function was called. The variable `chain` is the data attribute associated with the `PyChain` class.

* The DataFrame is written to the page using `st.write`.

Test the code by running the application from a terminal instance. Point out that the `prev_hash` attribute is part of each new block.

Congratulate students on completing this activity, and acknowledge that this class covered a lot of blockchain information. Offer a few words of encouragement and motivation. For example:

* Students should be proud of everything they’ve accomplished so far. They have built a functioning blockchain from scratch, using only Python and a couple of supporting libraries.

* This is only the beginning of students’ blockchain journey. In the next class, we’ll continue to build the `PyChain` ledger, incorporating additional processes for verifying information on the chain.

Before ending class and releasing students for office hours, ask them if they have any questions about what we covered in today’s class, such as data classes, decorators, attributes, methods, hashing, or chaining blocks

---

### End Class

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
