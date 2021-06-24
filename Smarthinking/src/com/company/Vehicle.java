package com.company;

public class Vehicle {
    private String make;
    private String color;
    private int year;
    private String model;



    public void printDetails() {
        System.out.println("Manufacturer: " + make);
        System.out.println("Color: " + color);
        System.out.println("Year: " + year);
        System.out.println("Model: " + model);
    }

}