public class Empty extends SetExpression {

    //Empty class constructor with no parameters
    public Empty(){
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that checks whether the given number(elem) is in the empty set (always false as empty sets do not contain any numbers)
    public boolean contains(int elem){
        return false;
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that describes/displays an empty set
    public String describe(){
        return "{}";
    }
}