// Java code to illustrate clear() method
import java.io.*;
import java.util.*;

public class test {
    public static void main(String[] args)
    {

        // create an empty list with an initial capacity
        List<String> list = new LinkedList<String>();

        // use add() method to initially
        // add elements in the list
        list.add("Geeks");
        list.add("For");
        list.add("Geeks");

        // Remove all elements from the List
       list.removeAll(list);

        // print the List
        System.out.println(list);
    }
}