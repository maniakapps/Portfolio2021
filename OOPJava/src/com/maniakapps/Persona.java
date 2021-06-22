package com.maniakapps;

public class Persona {
    private String nombre;
    private int edad;
    private int ID;
    private final static int OJOS = 2;

    public Persona(){
        nombre = "";
        edad = 0;
    }
    Persona(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
    }
    Persona(int ID, String nombre, int edad){
        this(nombre, edad);
        this.ID = ID;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        if (edad>=1) {
            this.edad = edad;
        }else {
            System.out.println("Edad in correcta");
        }
    }

    void speak(){
        System.out.println("Hablando");
    }

    void speak(String mensaje){
        System.out.println("Hablando " + mensaje);
    }
    void run(){
        System.out.println("Correr");
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }
}

