package itertools;

//Necessary imports
import java.util.Iterator;
import java.util.NoSuchElementException;

//Custom class that is used to implement the logic for TASK(1)
public class Take<T> implements Iterator<T> {
    
    //private fields of class Take
    private final Iterator<T> it;
    private int leftout;

    //Constructor that will be called when a new Take Instance is created
    public Take(Iterator<T> it, int count){
        this.it = it;
        this.leftout = count;
    }

    //Custom hasNext() function that returns a boolean value based on the condition that the iterator has elements to iterate over for the next iteration
    //and leftout variable is greater than zero
    @Override
    public boolean hasNext(){
        return leftout > 0 && it.hasNext();
    }

    //Custom next() function that returns the next element, decreasing the number of elements left to consume(leftout)
    @Override
    public T next(){
        if(!hasNext()) throw new NoSuchElementException();
        leftout--;
        return it.next();
    }
}
