package studentstats;

import itertools.DoubleEndedIterator;
import java.util.NoSuchElementException;
import studentapi.*;

/**
 * A (double ended) iterator over student records pulled from the student API.
 *
 * <p>This does not load the whole student list immediately, but rather queries the API ({@link
 * StudentList#getPage}) only as needed.
 */
public class StudentListIterator implements DoubleEndedIterator<Student>{
    // TASK(8): Implement StudentListIterator: Add any fields you require
    private final StudentList list;
    private final int retries;
    private int currentIndex; //To keep track of the current index from head
    private int reverseIndex; //To keep track of the current index from tail
    private int currentPageIndex; //To keep track of the current page number
    private int reverePageIndex; //To keep track of the current page number in reverse direction
    private Student[] currentPage; //To load the appropriate page based on the current page number
    
    /**
     * Construct an iterator over the given {@link StudentList} with the specified retry quota.
     *
     * @param list The API interface.
     * @param retries The number of times to retry a query after getting {@link
     *     QueryTimedOutException} before declaring the API unreachable and throwing an {@link
     *     ApiUnreachableException}.
     */
    public StudentListIterator(StudentList list, int retries){
        // TASK(8): Implement StudentListIterator
        this.list = list;
        this.retries = retries;
        this.currentIndex = 0; //all student records start from 0
        this.reverseIndex = list.getNumStudents()-1; //-1, as the student records start from 0
        this.currentPageIndex = 0; // all pages start from 0
        this.reverePageIndex = list.getNumPages()-1; // from last page 
        this.currentPage = null; //we dont have a page yet
    }

    /**
     * Construct an iterator over the given {@link StudentList} with a default retry quota of 3.
     *
     * @param list The API interface.
     */
    public StudentListIterator(StudentList list){
        // TASK(8): Implement StudentListIterator
        this(list,3); //default retry quota = 3
    }

    private Student[] getPage(int pageIndex) throws ApiUnreachableException {
        int count = 0; //to keep track of the attempts
        while (count < retries) { 
            try {
                return list.getPage(pageIndex);
            } catch (QueryTimedOutException e) { //when Time out occurs, attempt is over, hence increment
                count++;
            }
        }
        throw new ApiUnreachableException(); //when page is not loaded withtin the allowed retires/attempts, it is unreachable
    }

    @Override
    public boolean hasNext(){
        // TASK(8): Implement StudentListIterator

        //I think I am stuck here(handling lesser records than page size ), using print statetment to understand whats going on:
        //System.out.println(currentPageIndex+" "+reverseIndex+" "+currentIndex+" "+list.getNumStudents()+" "+list.getNumPages()+" "+list.getPageSize());
        // currentPageIndex == list.getNumPages() - 1 (last page) && (currentIndex+1) % list.getPageSize() == list.getNumStudents() % list.getPageSize(); ??
        
        // Check if there are more elements in the current page
        if (currentIndex < list.getNumStudents()) {
            return true;
        }
        //return false if not
        return false;
    }

    @Override
    public Student next(){
        // TASK(8): Implement StudentListIterator

        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        if (currentIndex % list.getPageSize() == 0 || currentPage == null) { // this block is executed only when a page has been seen fully.(to the end of page)          
            currentPageIndex = currentIndex / list.getPageSize(); //move to next page
            currentPage = getPage(currentPageIndex); //load the next page
        }

        return currentPage[currentIndex++ % list.getPageSize()]; //return the element and move the pointer/index(currentIndex) to next element
    }

    @Override
    public Student reverseNext(){
        // TASK(8): Implement StudentListIterator
        if (reverseIndex <= 0) {
            throw new NoSuchElementException();
        }
        if (reverseIndex % list.getPageSize() == 0 || currentPage == null) { //this block is executed only when a page has been seen fully in reverse direction. (back to top of page)
            reverePageIndex = reverseIndex / list.getPageSize(); //move to previous page
            currentPage = getPage(reverePageIndex); //load the previous page
        }

        return currentPage[reverseIndex-- % list.getPageSize()]; //return the element and move the pointer/indec(reverseIndex) to previous element
    }
}
