package desafioTarget;

import java.util.Scanner;

public class InverteString {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite uma string: ");
        String str = scanner.nextLine();
        scanner.close();

        char[] chars = str.toCharArray();
        int left = 0;
        int right = chars.length - 1;

        while (left < right) {
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }

        String invertedStr = new String(chars);
        System.out.println("String invertida: " + invertedStr);
    }
}
