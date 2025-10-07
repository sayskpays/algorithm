package java_algorithm.string;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class _1_10 {

    private static List<Integer> solution(String[] in) {

        List<Integer> answer = new ArrayList<>();
        char[] charList = in[0].toCharArray();

        int p = 1001;
        for (int i = 0; i < charList.length; i++) {
            if (String.valueOf(charList[i]).equals(in[1])) {
                answer.add(0);
                p = 1001;
            } else {
                answer.add(p);
                p++;
            }
        }

        for (int j = charList.length - 1; j >= 0; j--) {
            if (String.valueOf(charList[j]).equals(in[1])) {
                p = 1001;
            } else {
                answer.set(j, Math.min(answer.get(j), p));
                p++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String[] inScan = scan.nextLine().split(" ");

        System.out.println(solution(inScan));

    }
}
