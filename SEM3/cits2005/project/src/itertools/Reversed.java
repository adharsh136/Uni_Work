package itertools;

//Necessary imports
import java.util.Iterator;
import java.util.NoSuchElementException;

//Custom class that is used to implement the logic for TASK(2)
public class Reversed<T> implements Iterator<T> {

    //private field of class Reversed
    private final DoubleEndedIterator<T> dit;

    //Constructor that will be called when a new Reversed Instance is created
    public Reversed(DoubleEndedIterator<T> dit){
        this.dit = dit;
    }
    
    //Custom hasNext() function that returns a boolean value based on the condition that the iterator has elements to iterate over for the next iteration
    @Override
    public boolean hasNext(){
        return dit.hasNext();
    }

    //Custom nest() function that returns the previous element
    @Override
    public T next(){
        if(!hasNext()) throw new NoSuchElementException();
        return dit.reverseNext();
    }
}
