### Question 7:

Steps that I used to apply **ISP** to the `LightingCommand` constructor, starting with identifying the characteristics of its inputs.

---

### Step 1: Identifying Characteristics of the `LightingCommand` Constructor

The `LightingCommand` constructor takes three parameters:

1. **Location**: This parameter represents the physical location of the light (e.g., "living-room", "kitchen"). It can either be a specific location (represented as a `Location` object) or it can be `null` if the location is not necessary (e.g., if there's only one light to control and no ambiguity).

2. **Light Source**: This represents the actual light device that the command controls, such as a lamp, a neon light, or a bulb. It is an object of the `LightSource` class and must not be `null` since the command cannot operate without a specific light source.

3. **State**: The `State` parameter is an enumerated value (`ON` or `OFF`) that determines whether the light should be turned on or off. This parameter tells the `LightingCommand` what action to perform.

---

### Step 2: Define Partitions for Each Characteristic

#### **Characteristic 1: Location**

For the `Location` parameter, we can define two main partitions:

- **Partition 1**: The location is **null**. This is a valid case where the command doesn’t need a specific location because there’s no ambiguity (e.g., there’s only one light to control).
- **Partition 2**: The location is a valid `Location` object (e.g., `new Location("living-room")`). In this case, the command is tied to a specific room or area.

#### **Characteristic 2: Light Source**

For the `lightSource` parameter, we define two partitions:

- **Partition 1**: The light source is a valid `LightSource` object, such as a lamp or bulb. This is required for the command to work as expected.
- **Partition 2**: The light source is **null**, which is an invalid case. The command cannot operate without specifying which light source it is controlling.

#### **Characteristic 3: State of the Light Source**

The possible partitions for the `State` parameter are:

- **Partition 1: `State.ON`**: This represents the command to turn the light on.
- **Partition 2: `State.OFF`**: This represents the command to turn the light off.
- **Partition 3: `null`**: This is an invalid case where the state is not provided. The constructor should handle this case by throwing an appropriate exception.

---

### Step 3: Define Test Cases Combining **State** and **Location**

The following test cases will test the `Location` and `State` parameters of the constructor for the `LightCommand` class keeping `LightSource` constant (`lamp`).

### Test Case 1: Valid ON State with a Valid Location

- **Test ID**: T1
- **Description**: This test checks if the `LightingCommand` successfully turns on the light when both the `Location` and `State` are valid.
- **Input Values**:
  - **Location**: `new Location("living-room")` (a valid location)
  - **LightSource**: `new LightSource("lamp")` (a valid light source)
  - **State**: `State.ON` (we want to turn the light on)
- **Expected Outcome**: The command should execute successfully, and the light source should be turned on in the specified location.
- **Fixtures**: We create a valid `Location`, `LightSource`, and use the `State.ON` value.
- **Assertions**: We verify that the `LightSource.turnOn()` method is called when the `execute()` method is invoked.

---

### Test Case 2: Valid OFF State with a Null Location

- **Test ID**: T2
- **Description**: This test checks if the `LightingCommand` can successfully turn off the light when the `Location` is `null` but the `State` is valid.
- **Input Values**:
  - **Location**: `null` (no location is provided)
  - **LightSource**: `new LightSource("lamp")` (a valid light source)
  - **State**: `State.OFF` (we want to turn the light off)
- **Expected Outcome**: The command should execute successfully, and the light source should be turned off. Since the location is `null`, the system should default to the single available light source.
- **Fixtures**: We create a `null` `Location` and a valid `LightSource`, using the `State.OFF` value.
- **Assertions**: We verify that the `LightSource.turnOff()` method is called during execution.

---

### Test Case 3: Invalid Null State with a Valid Location

- **Test ID**: T3
- **Description**: This test checks if the `LightingCommand` throws an exception when the `State` is `null`, even if the `Location` is valid.
- **Input Values**:
  - **Location**: `new Location("bedroom")` (a valid location)
  - **LightSource**: `new LightSource("lamp")` (a valid light source)
  - **State**: `null` (this is an invalid state)
- **Expected Outcome**: The constructor should throw an `IllegalArgumentException` because the `State` is `null`.
- **Fixtures**: We create a valid `Location` and `LightSource`, but pass `null` for the `State`.
- **Assertions**: We check that an `IllegalArgumentException` is thrown, indicating that the `State` must not be `null`.

---

### Test Case 4: Valid ON State with a Null Location

- **Test ID**: T4
- **Description**: This test checks if the `LightingCommand` can turn the light on when the `Location` is `null` but the `State` is valid.
- **Input Values**:
  - **Location**: `null` (no location is specified)
  - **LightSource**: `new LightSource("lamp")` (a valid light source)
  - **State**: `State.ON` (we want to turn the light on)
- **Expected Outcome**: The command should execute successfully, and the light source should turn on. The system should handle the `null` location appropriately by defaulting to a single light source.
- **Fixtures**: We create a `null` `Location`, a valid `LightSource`, and use the `State.ON` value.
- **Assertions**: We verify that the `LightSource.turnOn()` method is called.

---

### Test Case 5: Invalid Null State with a Null Location

- **Test ID**: T5
- **Description**: This test checks if the `LightingCommand` throws an exception when both the `State` and the `Location` are `null`.
- **Input Values**:
  - **Location**: `null`
  - **LightSource**: `new LightSource("lamp")` (a valid light source)
  - **State**: `null` (this is an invalid state)
- **Expected Outcome**: The constructor should throw an `IllegalArgumentException` because the `State` is `null`, regardless of the `Location` being `null`.
- **Fixtures**: We create a `null` `Location`, a valid `LightSource`, and pass `null` for the `State`.
- **Assertions**: We verify that an `IllegalArgumentException` is thrown due to the invalid `null` `State`.

---

### Step 4: Conclusion

By using **Input Space Partitioning**, the **Location** and **State** characteristics were combined to create test cases that cover valid and invalid combinations. These tests ensure that the `LightingCommand` constructor handles different conditions correctly, including `null` states and locations, and verifies the expected behaviour when turning the light on or off.
