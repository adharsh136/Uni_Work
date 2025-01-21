public class Complement extends SetExpression {

    //a private SetExpression instance that will hold a reference to any of the child class instance
    private SetExpression expression;
    
    //Complement class constructor that creates a complement instance 
    public Complement(SetExpression expression){
        this.expression = expression;
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that checks whether the given number(elem) is not present in the complement of the given set(returns true if so)
    public boolean contains(int elem){
        if(expression.contains(elem)){
            return false;
        }
        else{
        return true;
        }
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that describes/displays complement of a set
    public String describe(){
        return "~"+expression.describe();
    }
}