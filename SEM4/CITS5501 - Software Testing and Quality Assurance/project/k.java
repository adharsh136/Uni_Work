import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Test class for the LightingCommand constructor.
 */
public class LightingCommandTest {

    /**
     * Test ID: T1 (Question 7)
     * Test case for valid ON state with a valid location.
     * Ensures that an exception is thrown when the light is turned on,
     * as the method is not implemented yet.
     */
    @Test
    public void testValidOnStateWithValidLocation() {
        // Arrange
        Location location = new Location("living-room");
        LightSource lightSource = new LightSource("lamp");

        // Act
        LightingCommand command = new LightingCommand(location, lightSource, State.ON);
        
        // Assert: Expecting a RuntimeException since the turnOn method is not implemented
        assertThrows(RuntimeException.class, command::execute, "The turnOn method should throw a RuntimeException as it is not implemented.");
    }

    /**
     * Test ID: T2 (Question 7)
     * Test case for valid OFF state with a null location.
     * Ensures that an exception is thrown when the light is turned off,
     * as the method is not implemented yet.
     */
    @Test
    public void testValidOffStateWithNullLocation() {
        // Arrange
        Location location = null;
        LightSource lightSource = new LightSource("lamp");

        // Act
        LightingCommand command = new LightingCommand(location, lightSource, State.OFF);
        
        // Assert: Expecting a RuntimeException since the turnOff method is not implemented
        assertThrows(RuntimeException.class, command::execute, "The turnOff method should throw a RuntimeException as it is not implemented.");
    }

    /**
     * Test ID: T3 (Question 7)
     * Test case for invalid null state with a valid location.
     * Ensures that the constructor throws an IllegalArgumentException when the state is null.
     */
    @Test
    public void testInvalidNullStateWithValidLocation() {
        // Arrange
        Location location = new Location("bedroom");
        LightSource lightSource = new LightSource("lamp");

        // Act & Assert: The constructor should throw an IllegalArgumentException for null state
        assertThrows(IllegalArgumentException.class, () -> {
            new LightingCommand(location, lightSource, null);
        }, "The constructor should throw an exception for null state.");
    }
}
