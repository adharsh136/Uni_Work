public class Singleton extends SetExpression {

    //a private variable that will store the singleton set(object)'s number
    private int number;
    
    //Singleton class constructor that creates a singleton instance 
    public Singleton(int number){
        this.number = number;
    }

    //child class function that overrides the abstract parent class function
    @Override
    //function that checks whether the given number(elem) exists in the singleton set
    public boolean contains(int elem){
        if(elem == number){
            return true;
        }
        else{
        return false;
        }
    }


    //child class function that overrides the abstract parent class function
    @Override
    //funtion that describes/displays a singleton set
    public String describe(){
        return "{"+number+"}";
    }
}