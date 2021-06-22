package com.maniakapps;

public class RedTriangle implements DrawAPI{

    @Override
    public void drawCircle(int radius, int x, int y) {

    }

    @Override
    public void drawTriangle(int width, int height, int x, int y) {
    System.out.println(""+  width + " " + height);
    }
}
