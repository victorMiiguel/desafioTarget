package desafioTarget;

import java.util.Scanner;

public class Fibonacci {
    public static boolean isFibonacci(int n) {
        int a = 0, b = 1;
        while (b < n) {
            int temp = b;
            b = a + b;
            a = temp;
        }
        return (b == n);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um numero: ");
        int num = scanner.nextInt();
        scanner.close();

        if (isFibonacci(num)) {
            System.out.println(num + " pertence a sequencia de Fibonacci.");
        } else {
            System.out.println(num + " nao pertence a sequencia de Fibonacci.");
        }
    }
}
