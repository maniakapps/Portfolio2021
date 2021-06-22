package com.maniakapps;

public class Dividing {
    public static void main(String[] args) {
        System.out.print(divide(1,0));
    }
    public static String divide(int v1, int v2){
        int Ret = 0;
        try {
            Ret = v1/v2;
            String ret = String.valueOf(Ret);
            return ret;
        }catch (Exception e){
            return "Undefined";

        }

    }
}
