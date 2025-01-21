### Question 5

#### **Preconditions**

Conditions that must be considered and adhered to **before** the constructor call are called preconditions. This will ensure the creation of  a valid `LightingCommand` object. The following are preconditions that I identified for the constructor of the`LightingCommand` class:

1. **Location:**

    * The first parameter, `location` is optional, meaning, if specified it should be an instance of the type `Location` (e.g, `living-room`,`bedroom`, etc.) or can be `null`

    * Specifying location could mean that there are multiple light sources in the premises and the user only wants to control one of them present in a particular room / area, otherwise causing all light sources to shine or go off.

2. **Light source:**

    * The second parameter, `lightSource` is not optional, meaning cannot be `null` and has to be an instance of the type `LightSource` (e.g., `lamp`, `bulb`, etc.)

    * Specifying a light source helps identify the light source and only that light light source. Passing a `null` or an instance of a different type would not help identifying the light source and will break the preconditions.

3. **State:**

    * The third parameter, `state` is also not optional, so it cannot be `null` and it has to be an instance of the `State` enum (`ON` or `OFF`).

    * Specifying state would allow control over the state light source and the state of a light source cannot be `null`. Similar to `lightsource` precondition, a `null` or instance of a different type being passed as the third parameter to the constructor would fail the preconditions.

---

#### **Postconditions**

Postconditions are conditions that must hold true **after** the constructor has successfully executed and the object has been created.

1. **`LightingCommand` Object Created Successfully**:
   * After the constructor is called, a valid `LightingCommand` object is created with the specified `lightSource` and `state`. The command is ready to be executed and will control the correct light source.

   * If the constructor is called with `location: living-room`, `lightSource: lamp`, and `state: ON`, then a valid `LightingCommand` object will be created to turn the lamp on in the living room.

2. **Correct Association of Light Source and State**:
   * The command object will store the `lightSource` and `state`, which can be accessed later via the `getLightSource()` and `getState()` methods.

   * After creation, calling `getLightSource()` will return the correct light source (e.g., lamp), and calling `getState()` will return the desired state (e.g., `ON`).

3. **Error-Free Creation**:
   * If all preconditions are satisfied (valid `lightSource`, valid `state`), no exceptions or errors should be thrown during object creation.

   * If valid inputs are provided, the constructor will execute without throwing any exceptions.
