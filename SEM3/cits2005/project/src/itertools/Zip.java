package itertools;

//Necessary imports
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.function.BiFunction;

//Custom class that is used to implement the logic for TASK(6)
public class Zip<T, U, R> implements Iterator<R>{
    
    //private fields of class Zip
    private final Iterator<T> lit;
    private final Iterator<U> rit;
    private final BiFunction<T, U, R> bfunc;

    //Constructor that will be called when a new Zip Instance is created
    public Zip(Iterator<T> lit, Iterator<U> rit, BiFunction<T, U, R> bfunc){
        this.lit = lit;
        this.rit = rit;
        this.bfunc = bfunc;
    }

    //Custom hasNext() function that returns a boolean value based on the condition both the iterators have elements to iterate over for the next iteration
    @Override
    public boolean hasNext(){
        return lit.hasNext() && rit.hasNext();
    }

    //Custom next() function that applies a function to the corresponding elements of left and right iterators and returns the result
    @Override
    public R next(){
       if(!hasNext()) throw new NoSuchElementException();
       return bfunc.apply(lit.next(), rit.next());
    }
}
