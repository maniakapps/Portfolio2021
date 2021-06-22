package com.maniakapps;

public class Usuario {
    private String usuario;
    private int contrasena;

    Usuario(String userName, int password){
        usuario = userName;
        contrasena = password;
    }

    public void loguearse(String usuario, int contrasena){
        if(this.usuario.toLowerCase().equals(usuario.toLowerCase()) && this.contrasena == contrasena){
            System.out.println("Iniciaste sesión");
        }else {
            System.out.println("No se pudo acceder");
        }
    }
}
