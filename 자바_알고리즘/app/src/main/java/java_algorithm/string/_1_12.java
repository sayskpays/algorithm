package java_algorithm.string;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class _1_12 {

    private static String solution(String in){

        String answer = "";
        List<String> list = new ArrayList<>();
        in = in.replace("#", "1").replace("*", "0");

        int fr = 0;
        int to = 7;

        while(to <= in.length()){

            list.add(in.substring(fr, to));

            fr += 7;
            to += 7;

        }

        for(String ascii : list){
            int decimal = Integer.valueOf(ascii, 2);
            String t = String.valueOf((char)decimal);

            answer += t;
        }

        return answer;
    }
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String inScan = scan.nextLine();

        System.out.println(solution(inScan));
    }
}
