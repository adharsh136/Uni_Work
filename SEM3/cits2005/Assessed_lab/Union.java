public class Union extends SetExpression {

    //a private SetExpression instance that will hold a reference to any of the child class instance
    private SetExpression left_expression;
    //a private SetExpression instance that will hold a reference to any of the child class instance
    private SetExpression right_expression;
    
    //Union class constructor that creates two union instances(left set and right set)
    public Union(SetExpression left_expression, SetExpression right_expression){
        this.left_expression = left_expression;
        this.right_expression = right_expression;
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that checks whether the given number(elem) is in the union of the two given sets
    public boolean contains(int elem){
        if(left_expression.contains(elem) || right_expression.contains(elem)){
            return true;
        }
        else{
        return false;
        }
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that describes/displays the union of two sets
    public String describe(){
        return "("+left_expression.describe()+" U "+right_expression.describe()+")";
    }
}