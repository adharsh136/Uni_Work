public class Range extends SetExpression {

    //a private variable that will store the lower bound of the Range(object)
    private int lower_range;
    //a private variable that will store the upper bound of the Range(object)
    private int upper_range;
    
    //Range class that creates a range instance with lower and upper bound values
    public Range(int lower_range,int upper_range){
        this.lower_range = lower_range;
        this.upper_range = upper_range;
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that checks whether the given number(elem) is within the given range
    public boolean contains(int elem){
        if(elem >= lower_range && elem <= upper_range){
            return true;
        }
        else{
        return false;
        }
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that describes/displays a range
    public String describe(){
        return "["+lower_range+".."+upper_range+"]";
    }
}