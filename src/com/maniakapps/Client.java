package com.maniakapps;

public class Client {
    public static void main(String[] args) {
        Shape redCircle = new Circle(100,100, 10, new RedCircle());
        Shape greenCircle = new Circle(100,100, 10, new GreenCircle());
        Triangle triangle = new Triangle(20, 30, 4, 4, new RedTriangle());
        redCircle.draw();
        greenCircle.draw();
        triangle.draw();
    }
}
