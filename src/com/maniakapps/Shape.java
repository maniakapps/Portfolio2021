package com.maniakapps;

public abstract class Shape {
    DrawAPI drawAPI;

    Shape(DrawAPI drawAPI){

        this.drawAPI = drawAPI;
    }
    public abstract void draw();
}
