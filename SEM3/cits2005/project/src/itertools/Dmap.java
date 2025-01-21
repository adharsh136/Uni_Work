package itertools;

//Necessary imports
import java.util.NoSuchElementException;
import java.util.function.Function;

//Custom class that is used to implement the logic for TASK(5)
public class Dmap<T, R> implements DoubleEndedIterator<R>{

    //private fields of class Dmap
    private final DoubleEndedIterator<T> dit;
    private final Function<T, R> func;

    //Constructor that will be called when a new Dmap Instance is created
    public Dmap(DoubleEndedIterator<T> dit, Function<T, R> func){
        this.dit = dit;
        this.func = func;
    }

    //Custom hasNext() function that returns a boolean value based on the condition that the iterator has elements to iterate over for the next iteration
    @Override
    public boolean hasNext(){
        return dit.hasNext();
    }

    //Custom next() function that applies a function to the element and returns it(Forward direction)
    @Override
    public R next(){
        if (!hasNext()) throw new NoSuchElementException();
        return func.apply(dit.next());
    }
    //Custom next() function that applies a function to the element and returns it(Reverse direction)
    @Override
    public R reverseNext(){
        if (!hasNext()) throw new NoSuchElementException();
        return func.apply(dit.reverseNext());
    }
}
