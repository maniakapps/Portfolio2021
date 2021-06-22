package com.maniakapps;

public class UserTest {
    public static void main(String[] args){
        Usuario usr =  new Usuario("Angel",1234);
        usr.loguearse("Angel", 2341);
        usr.loguearse("Angel", 1234);
        //usr.contrasena = 2341;
        usr.loguearse("Angel", 2341);
    }
}
