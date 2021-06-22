package com.maniakapps;

public class Triangle extends Shape {
    private int x, y, width, height;

    public Triangle(int width, int height, int x, int y, DrawAPI drawAPI) {
        super(drawAPI);
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    Triangle(DrawAPI drawAPI) {
        super(drawAPI);
    }

    public void draw() {
        drawAPI.drawTriangle(width,height, x, y);
    }
}
