import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] line = bf.readLine().split(" ");
        int H = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int minute = 45;

        int minusMinute = M - minute;

        if (minusMinute < 0) {
            minusMinute += 60;
            H -= 1;
        }
        if (H < 0) {
            H += 24;
        }

        System.out.println(H + " " + minusMinute);
        
    }
}
