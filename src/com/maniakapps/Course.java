package com.maniakapps;

public class Course {
    private String code;
    private int creditHours;
    private String title;

    public Course(String code, int creditHours, String title) {
        this.code = code;
        this.creditHours = creditHours;
        this.title = title;
    }

    @Override
    public String toString() {
        return "Course: " + this.getClass().getName() + code;
    }
}
