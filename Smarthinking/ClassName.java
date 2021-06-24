
/**
 * Write a description of class code here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.io.*;
import java.util.Scanner;

// The Stack ADT -- linked list implementation

interface LLStack {
    public void push (int item);

    public int pop();

    public int size();

    public boolean empty();

    public int ontop();
}
class Node {
    private int data;
    private Node next;

    public Node () {
        this(0, null);
    }

    public Node (int d) {
        data = d;
    }

    public Node (int d, Node n) {
        data = d;
        next = n;
    }

    public void setData (int newData) {
        data = newData;
    }

    public void setNext (Node newNext) {
        next = newNext;
    }

    public int getData () {
        return data;
    }

    public Node getNext () {
        return next;
    }

    public void displayNode () {
        System.out.print (data);
    }
}

class LLStackADT implements LLStack {
    private Node top;
    private int size;

    public LLStackADT () {
        top = null;
        size = 0;
    }

    public boolean empty () {
        return (top == null);
    }

    public void push (int number) {
        Node newNode = new Node ();
        newNode.setData(number);
        newNode.setNext(top);
        top = newNode;
        size++;
    }

    public int pop () {
        int i;
        i = top.getData();
        top = top.getNext();
        size--;
        return i;
    }

    public int ontop () {
        int i = pop();
        push(i);
        return i;
    }

    public int size () {
        return size;
    }

}

interface LLQueue {
    public void enqueue (int item);

    public int dequeue();

    public int size();

    public boolean empty();

    public int front();
}
class QNode {
    private int data;
    private Node next;

    public QNode () {
        this(0, null);
    }

    public QNode (int d) {
        data = d;
    }

    public QNode (int d, Node n) {
        data = d;
        next = n;
    }

    public void setData (int newData) {
        data = newData;
    }

    public void setNext (Node newNext) {
        next = newNext;
    }

    public int getData () {
        return data;
    }

    public Node getNext () {
        return next;
    }

    public void displayNode () {
        System.out.print (data);
    }
}

class LLQueueADT implements LLQueue {

    private int size;
    private Node front;
    private Node rear;

    public LLQueueADT () {
        size = 0;
        front = null;
        rear = null;
    }

    public boolean empty () {
        return (size == 0);
    }

    public void enqueue (int number) {
        Node newNode = new Node ();
        newNode.setData(number);
        newNode.setNext(null);
        if (this.empty())
            front = newNode;
        else
            rear.setNext(newNode);
        rear = newNode;
        size++;
    }

    public int dequeue () {
        int i;
        i = front.getData();
        front = front.getNext();
        size--;
        if (this.empty())
            rear = null;
        return i;
    }

    public int front () {
        return front.getData();
    }

    public int size () {
        return size;
    }
}

public class ClassName {

    public static void main (String[] args) throws IOException {

        Scanner scan = new Scanner (System.in);

        LLStackADT stack = new LLStackADT();
        LLQueueADT queue = new LLQueueADT();

        int i = 2;

        for (int j = 1; j <= 10; j++) {
            stack.push(i);
            System.out.println (stack.ontop() + " is the top element.");
            i = i + 2;
        }

        i = 2;
        for (int j = 1; j <= 10; j++) {
            queue.enqueue(i);
            System.out.println (queue.front() + " is the front element.");
            i = i + 2;
        }

        System.out.println ("The current stack contains " + stack.size() +
                " elements.");
        System.out.println ("The current queue contains " + queue.size() +
                " elements.");

        while (!stack.empty())
            System.out.println (stack.pop() + " is removed from the stack.");
        while (!queue.empty())
            System.out.println (queue.dequeue() + " is dequeued from the queue.");

        if (stack.empty())
            System.out.println ("The stack is empty.");
        else
            System.out.println ("There are more elements on the stack.");
        if (queue.empty())
            System.out.println ("The queue is empty.");
        else
            System.out.println ("There are more elements on the queue.");

    //class LLQueueAppl {

    //create instance of Scanner class
    Scanner sc = new Scanner(System.in);

    System.out.println("Enter a postfix expression: ");

    //read an expression
    String s = sc.nextLine();

    //evalute expression
    //double x = evaluation(s);

    //print the result
    //System.out.println(s + " = " + x);

    //close Scanner
    sc.close();

}
}

// The Queue ADT -- linked list implementation




