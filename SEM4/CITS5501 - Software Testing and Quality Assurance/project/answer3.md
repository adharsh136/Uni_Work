### Question 3

#### 1. **Reasoning behind my choice of Test Cases**

The test cases developed in *Question 2* comprehensively test both **valid and invalid** forms of the Domolect 2.0 language. Justification for the test cases I have chosen, and classification of each of them:

**Valid Test Cases**:

* Test **basic** commands: For instance, test: `living-room set air-conditioner to 275 K` without any temperature or time conditions to check that the core functionality from Domolect 1.7 is still working and assert that the options are indeed optional.

* Test command with **"when"** condition For example, test: `living-room set air-conditioner to 275 K when current-temperature less-than 300 K` - this will add a condition related to temperature.

* Test the command using an **"until"** condition. For instance, test: `living-room turn oven on until 08: 00 pm`. This will bring in time conditions.

* Test **"when" and "until"** condition: `living-room set electric-blanket to 400 K when current-temperature greater than 295 K until 10:00 pm`. This tests whether the system accepts both kinds of conditions in the right order.

These tests cover the basic functionality of the **Domolect 2.0** language, and test that valid commands are accepted.

**Invalid Cases:**

* Test **invalid sequencing** of the optional conditions. Test cases like: `living-room set thermostat to 300 K until 10:00 pm when current-temperature greater-than 295 K` ensure that the "when" condition must always come after the "until" condition.

* Tests for **invalid comparators**: Test cases like: `living-room set air-conditioner to 275 K when current-temperature more-than 300 K` will help validate that only valid comparators such as "less-than", "greater-than", or "equal-to" will be accepted.

* **Missing Comparators or Incomplete Conditions**: Test cases like: `missing living-room set oven to 300 K when current-temperature 295 K`, `missing living-room set oven to 300 K when greater than 295 K`; it should check whether a good format with subject-comparator is present.

* Test for **invalid formatting of temperature or time**: Test cases like: `living-room set oven to 300 K when current-temperature greater-than K` OR `living-room turn lamp on until 25:10 pm`, which enforces temperature being followed by "K" and time in proper format (hh:mm am/pm).

* Test **incomplete commands**: Test cases like: `living-room set oven to 290 K when` or `living-room turn lamp on until`, verifying that the system refuses incomplete commands which do not finish specifying the condition.

These tests will test the **boundaries of validity**, since **Domolect 2.0** should parse valid commands and reject incomplete ones.

---

#### 2. **Production coverage**

The above test cases have **production coverage** for the following reasons:

* They **cover all the valid scenarios** possible for "when" and "until" conditions.

* They also cover wide range of **error conditions**, which will test the rejection of incomplete / invalid commands.

* Test cases also include **edge cases** like invalid times, temperatures or missing comparators to see how gracefully the system handles such commands.

This test suite covers production quite well as it has test cases for the new features of Domolect 2.0, temperature and time-based conditions, covering both valid and invalid use cases.

---

#### 3. **Semantic Constraints Not Covered by the Grammar**

There are two major cases of **semantic constraints** which are not fully captured by the grammar itself, that will be important to test before deploying **Domolect 2.0** in a production system. These include:

* **Device Capacity Logic**: Grammar itself does not check whether conditions set in command are semantically appropriate to the device. For instance, the following command is syntactically valid yet semantically impossible: `living-room set air-conditioner to 275 K when current-temperature greater-than 1000 K`, as 1000 K is well beyond any practical temperature range over which an air conditioner could conceivably hope to operate. This may cause unexpected system behaviour or even device malfunction. A proper system should ensure that the "when" conditions be within a realistic operational range for the device. For instance, a ridiculous trigger such as turning on the air conditioner when temperature soars beyond extreme values like 1000 K should not be allowed.

* **Time-related logic**: Grammar allows time-specific conditions such as "until," but such grammar does not guarantee if the time provided makes sense or not. For example, take the command: `living-room turn lamp on until 08:00 pm`
at `07:59 pm`, it would run just once a minute and might be quite different from what was expected. Besides, the grammar will also allow for invalid times like `25:10 pm` or `03:79 pm`, which, though syntactically correct, would be semantically meaningless. A proper system should check not only the correctness of time formats but ensure that the times specified make logical sense.
