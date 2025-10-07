package java_algorithm.string;

import java.util.Scanner;

public class _1_9 {

    private static int soulution(String in) {

        int answer = 0;

        char[] inCharArray = in.toCharArray();

        for (char a : inCharArray) {
            if (a >= 48 && a <= 57) {
                answer = answer * 10 + (a - 48);
            }
        }

        return answer;
    }

    private static int soulutionString(String in) {
        String answer = "";

        char[] inCharArray = in.toCharArray();

        for (char a : inCharArray) {
            if (Character.isDigit(a)) {
                answer += a;
            }
        }

        return Integer.parseInt(answer);
    }


    public static void main(String[] args) {


        Scanner scan = new Scanner(System.in);

        String scanList = scan.nextLine();

        System.out.println(soulutionString(scanList));

    }

}
