import java.util.Scanner;

public class Palindrome {
    public static boolean isPalindrome(String s){
        if(s.length() == 0 || s.length() == 1) return true;
        if(s.charAt(0) == s.charAt(s.length()-1)) return isPalindrome(s.substring(1, s.length()-1));
        return false;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(isPalindrome(s));

        sc.close();
    }
}