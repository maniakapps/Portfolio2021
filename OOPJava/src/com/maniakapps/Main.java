package com.maniakapps;

public class Main {

    public static void main(String[] args) {
	// Class obj = new Class(arguments);
        /*Persona persona1 = new Persona();
        persona1.setNombre("Angel");
        persona1.setEdad(22);
        System.out.println(persona1.getNombre() + " " + persona1.getEdad());
        System.out.println("Numero de ojos: " + Persona.OJOS);
        System.out.println(persona1.OJOS);
        Persona.OJOS = persona1.OJOS + 1;
        Persona persona2 = new Persona();
        persona1.setNombre("Andy");
        persona1.setEdad(23);
        persona1.speak();
        persona1.speak("Angel");
         */

        Persona p2 = new Persona("Angel", 22);
        System.out.println(p2.getNombre() + " " + p2.getEdad());
        Persona p3 = new Persona(34, "Angel", 22);
        System.out.println(p3.getID()+ " " + p3.getNombre() + " " + p3.getEdad());
    }
}
