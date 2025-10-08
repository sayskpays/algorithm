package java_algorithm.string;

import java.util.Scanner;

public class _1_11 {
    // 내 풀이 (실패)
    /*
    * i + 1 < inCharList.length => index
    *
    * */
    private static String solution(String in){

        String answer = "";
        char[] inCharList = in.toCharArray();

        int cnt = 1;

        for(int i=0; i< inCharList.length; i++){

            if (i + 1 < inCharList.length && inCharList[i] == inCharList[i+1]){
                cnt++;
            }else{
                answer += String.valueOf(inCharList[i]);
                if(cnt > 1) answer += String.valueOf(cnt);
                cnt = 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String param = scan.nextLine().toUpperCase();

        System.out.println(solution(param));

    }
}
