import java.util.Scanner;

public class round_2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n1 = sc.nextInt();
        printPalindromePattern(n1);
    }

    public static void printPalindromePattern(int n) {
	    System.out.println("*");
        for (int i = 1; i <4; i++) {
            System.out.print("* ");
            for (int j = 1; j < i; j++) {
                System.out.print(j + " ");
            }
            for (int j = i; j > 0; j--) {
                System.out.print(j + " ");
            }
            System.out.println("*");
        }

        for (int i = 3 - 1; i > 0; i--) {
            System.out.print("* ");
            for (int j = 1; j < i; j++) {
                System.out.print(j + " ");
            }
            for (int j = i; j > 0; j--) {
                System.out.print(j + " ");
            }
            System.out.println("*");
        }
		System.out.println("*");
    }
}

