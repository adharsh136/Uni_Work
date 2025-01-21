/**
 * Represents a barrier within the Domotopia system, such as a gate, window, 
 * or garage door. Barriers can be controlled using various commands such as 
 * "lock", "unlock", "open", or "close", depending on the specific type of 
 * barrier.
 * 
 * <p>Example usage:
 * 
 * <pre>
 *   // Create a new barrier representing the main gate
 *   Barrier gate = new Barrier("gate");
 *   
 *   // Use the barrier in a command (e.g., unlock the gate)
 *   BarrierCommand cmd = new BarrierCommand(
 *       new Location("front-yard"), 
 *       gate, 
 *       BarrierAction.UNLOCK
 *   );
 * </pre>
 * 
 * @see BarrierCommand
 * @see BarrierAction
 * @see Command
 */
public final class Barrier {

  /**
   * The name of the barrier, such as "gate", "window", or "garage-door".
   */
  private final String name;

  /**
   * Constructs a new {@code Barrier} with the specified name. The name 
   * identifies the type or specific instance of the barrier.
   * 
   * @param name The name of the barrier, which must be non-empty.
   */
  public Barrier(String name) {
    this.name = name;
  }

  /**
   * Returns the name of the barrier.
   * 
   * @return The name of the barrier.
   */
  public String getName() {
    return name;
  }
  
  /**
   * Sends instructions to the barrier to lock it.
   * 
   * If the barrier
   * is not of a type that is lockable (e.g. "curtains"), then
   * an UnsupportedOperationException is thrown.
   */
  public void lock() {
    throw new RuntimeException("The lock method is not implemented yet.");
  }

  /**
   * Sends instructions to the barrier to unlock it.
   * 
   * If the barrier
   * is not of a type that is lockable (e.g. "curtains"), then
   * an UnsupportedOperationException is thrown.
   */
  public void unlock() {
	throw new RuntimeException("The unlock method is not implemented yet.");
  }

  /**
   * Sends instructions to the barrier to open it.
   * This method should be implemented to include the actual
   * logic required to open the barrier.
   */
  public void open() {
	throw new RuntimeException("The open method is not implemented yet.");
  }

  /**
   * Sends instructions to the barrier to close it.
   * This method should be implemented to include the actual
   * logic required to close the barrier.
   */
  public void close() {
	throw new RuntimeException("The close method is not implemented yet.");
  }
}
