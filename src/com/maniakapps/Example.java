package com.maniakapps;

import java.util.Scanner;

public class Example {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name: ");
        String name = sc.nextLine();
        String greeting = greet(name);
        System.out.println(greeting);
    }

    public  static String greet(String name){
        return "Hello " + name + " welcome to Smarthinking";
    }
}
