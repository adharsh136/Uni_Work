package itertools;

//Necessary imports
import java.util.Iterator;
import java.util.function.BiFunction;

//Custom class that is used to implement the logic for TASK(7)
public class Reduce<T, R>{
    
    //private fields of class Reduce
    private final Iterator<T> it;
    private final R initialVal;
    private final BiFunction<R, T, R> bfunc;

    //Constructor that will be called when a new Reduce Instance is created
    public Reduce(Iterator<T> it, R initialVal, BiFunction<R, T, R> bfunc){
        this.it = it;
        this.initialVal = initialVal;
        this.bfunc = bfunc;
    }
    
    //Custom reduce function that applies the function to the elements of the iterator(one by one), starting from an initial value, reducing them to a single value.
    public R reduction(){
        R result = initialVal;
        while(it.hasNext()){
            result = bfunc.apply(result, it.next());
        }
        return result;
    }
}
