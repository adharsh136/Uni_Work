package itertools;

//Necessary imports
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.function.Predicate;

//Custom class that is used to implement the logic for TASK(3)
public class Filter<T> implements Iterator<T> {

    //private fields of class Filter
    private final Iterator<T> it;
    private final Predicate<T> pred;
    private T nextElem; //to store the index so that the iteration can continue from the correct index, when elements are skipped.
    private boolean hasNextElem; //to store a boolean value, if there is or is not an element for the next iteration.

    //Constructor that will be called when a new Filter Instance is created
    public Filter(Iterator<T> it, Predicate<T> pred){
        this.it = it;
        this.pred = pred;
        this.nextElem = null;
        this.hasNextElem = true;
        goToNext();
    }

    //Custom function that skips the element that does not meet the filter(condition)
    private void goToNext() {
        hasNextElem = false;
        while(it.hasNext()){
            T elem = it.next();
            if(pred.test(elem)){
                nextElem = elem;
                hasNextElem = true;
                break;
            }
        }
    }

    //Custom hasNext() function that returns a boolean value based on the goToNext() return value/result
    @Override
    public boolean hasNext(){
        return hasNextElem;
    }
    
    //Custom next() function that returns only elements that pass the filter(condition)
    @Override
    public T next(){
        if(!hasNext()) throw new NoSuchElementException();
        T result = nextElem;
        goToNext();
        return result;
    }
}
