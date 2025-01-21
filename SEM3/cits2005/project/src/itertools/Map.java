package itertools;

//Necessary imports
import java.util.Iterator;
import java.util.function.Function;
import java.util.NoSuchElementException;

//Custom class that is used to implement the logic for TASK(4)
public class Map<T, R> implements Iterator<R>{
    
    //private fields of class Map
    private final Iterator<T> it;
    private final Function<T, R> func;
    
    //Constructor that will be called when a new Map Instance is created
    public Map(Iterator<T> it, Function<T, R> func){
        this.it = it;
        this.func = func;
    }

    //Custom hasNext() function that returns a boolean value based on the condition that the iterator has elements to iterate over for the next iteration
    @Override
    public boolean hasNext(){
        return it.hasNext();
    }

    //Custom next() function that applies a function to the element and returns it
    @Override
    public R next(){
        if(!hasNext()) throw new NoSuchElementException();
        return func.apply(it.next());
    }
}
