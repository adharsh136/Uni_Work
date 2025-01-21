import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for the LightingCommand constructor.
 * LightSource parameter is always set to "lamp".
 * The test cases test all the partions of characteristics location and state,
 * and some combinations of the two(mentioned below).
 * Test cases:
 * T1: Test with a valid state (ON) and a valid location ("living-room") parameters.
 * T2: Test with a valid state (OFF) and a valid location (null) parameters.
 * T3: Test with a invalid state (null) and a valid location ("bedroom") parameters.
 */
public class LightingCommandTest {

    /**
     * Test ID: T1 (Question 7)
     * Test case for valid ON state with a valid location.
     * Ensures that the light is turned on when both the location and state are valid.
     */
    @Test
    public void testValidOnStateWithValidLocation() {
        //Arrange
        Location location = new Location("living-room");
        LightSource lightSource = new LightSource("lamp");
        State state = State.ON;

        //Act
        LightingCommand command = new LightingCommand(location, lightSource, state);
        command.execute();

        //Assert
        //Expecting a RuntimeException since the turnOn method is not implemented
        assertThrows(RuntimeException.class, command::execute, "The turnOn method should throw a RuntimeException as it is not implemented.");
        //Expecting location equality
        assertEquals(location, command.getLocation());
        //Expecting state equality
        assertEquals(state, command.getState());
    }

    /**
     * Test ID: T2 (Question 7)
     * Test case for valid OFF state with a null location.
     * Ensures that the light is turned off when the state is valid, but location is null.
     */
    @Test
    public void testValidOffStateWithNullLocation() {
        //Arrange
        Location location = null;
        LightSource lightSource = new LightSource("lamp");
        State state = State.OFF;

        //Act
        LightingCommand command = new LightingCommand(location, lightSource, state);
        command.execute();

        //Assert
        //Expecting a RuntimeException since the turnOff method is not implemented
        assertThrows(RuntimeException.class, command::execute, "The turnOff method should throw a RuntimeException as it is not implemented.");
        //Expecting null
        assertNull(command.getLocation());
        //Expecting state equality
        assertEquals(state, command.getState());
    }

    /**
     * Test ID: T3 (Question 7)
     * Test case for invalid null state with a valid location.
     * Ensures that the constructor throws an IllegalArgumentException when the state is null.
     */
    @Test
    public void testInvalidNullStateWithValidLocation() {
        //Arrange
        Location location = new Location("bedroom");
        LightSource lightSource = new LightSource("lamp");
        State state = null;

        //Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            new LightingCommand(location, lightSource, state);
        }, "The constructor should throw an exception for null state.");
    }
}
