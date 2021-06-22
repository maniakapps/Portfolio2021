package com.maniakapps;

import static jdk.nashorn.internal.runtime.regexp.joni.constants.AsmConstants.RANGE;

class cfg
{


    private static final int UPPER_BOUND = 26;
    private static String str;
    private static String key;

    static String getky(String plain, String key){
        String result = "";
        char ch[];
        int add1;
        int p = 0;
        for(int i = 0; i < plain.length(); i++){
                result = String.valueOf(plain.charAt(i) + key.charAt(p++));
                if(p >= key.length()){
                    p = 0;
                    p++;
                    add1 = Integer.parseInt(result);
                    while(add1 > UPPER_BOUND){
                        add1 -= RANGE;
                    }
                }
        }
        return result;
    }

    /**
     * @param str
     * @param key
     * @return
     */
    // This function generates the key in
// a cyclic manner until it's length isi'nt
// equal to the length of original text
    private static String generateKey(String str, String key)
    {
        cfg.str = str;
        cfg.key = key;
        int x = str.length();

        StringBuilder keyBuilder = new StringBuilder(key);
        for (int i = 0;  ; i++)
        {
            if (x == i)
                i = 0;
            if (keyBuilder.length() == str.length())
                break;
            keyBuilder.append(keyBuilder.charAt(i));
        }
        key = keyBuilder.toString();
        return key;
    }

    // This function returns the encrypted text
// generated with the help of the key
    private static String cipherText(String str, String key)
    {
        StringBuilder cipher_text= new StringBuilder();

        for (int i = 0; i < str.length(); i++)
        {
            // converting in range 0-25
            int x = (str.charAt(i) + key.charAt(i)) %26;

            // convert into alphabets(ASCII)
            x += 'A';

            cipher_text.append((char) (x));
        }
        return cipher_text.toString();
    }

    // This function decrypts the encrypted text
// and returns the original text
    private static String originalText(String cipher_text, String key)
    {
        StringBuilder orig_text= new StringBuilder();

        for (int i = 0 ; i < cipher_text.length() &&
                i < key.length(); i++)
        {
            // converting in range 0-25
            int x = (cipher_text.charAt(i) -
                    key.charAt(i) + 26) %26 ;

            // convert into alphabets(ASCII)
            x += 'A';
            orig_text.append((char) (x));
        }
        return orig_text.toString();
    }

    // Driver code
    public static void main(String[] args)
    {
        String str = "MANIAK";
        String keyword = "hey";

        String key = generateKey(str, keyword);
        System.out.println(key);
        String cipher_text = cipherText(str, key);

        System.out.println("Ciphertext : "
                + cipher_text + "\n");

        System.out.println("Original/Decrypted Text : "
                + originalText(cipher_text, key));
    }
}
