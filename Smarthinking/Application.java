
import java.util.Scanner;

public class Application {

    public static void main(String[] args) {
        String switch_state = null;
        char letter1;
        char letter2;
        int letter3 ;
        Scanner sc = new Scanner((System.in));
        letter1='a';
        while (letter1<= 'z'){
            letter2='a';
            while (letter2<='z'){
                System.out.println(""+ letter1+ "" + letter2 + ".com");
                ++letter2;
            }
            letter3=0;
            while (letter3<=9){
                System.out.println(""+ letter1+ "" + letter3 + ".com");
                ++letter3;
            }
            ++letter1;
        }


}
}