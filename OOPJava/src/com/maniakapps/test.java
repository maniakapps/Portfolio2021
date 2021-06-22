package com.maniakapps;

import java.util.Scanner;

public class test {
    public static void main(String[] args){
        int[] arr = new int[5];
        Scanner scanner =  new Scanner(System.in);
        for (int i = 0 ; i < 5; i++)
            arr[i] = scanner.nextInt();
        System.out.println(multiply(arr, 4));
    }
    static int multiply(int x[], int count){
        if(count<0)
            return 1;
        return x[count] * multiply(x, --count);
    }

}
