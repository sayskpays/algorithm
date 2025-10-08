package java_algorithm.string;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class _1_12 {

    /* 내 풀이(정답)
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
    */
    public static String solution(int n, String s){
        String answer="";
        for(int i=0; i<n; i++){
            String tmp=s.substring(0, 7).replace('#', '1').replace('*', '0');
            int num=Integer.parseInt(tmp, 2);
            answer+=(char)num;
            s=s.substring(7);
        }
        return answer;
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String inScan = scan.nextLine();

        System.out.println(solution(inScan));
    }
}
