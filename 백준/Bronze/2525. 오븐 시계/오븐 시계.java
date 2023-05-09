import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] line = bf.readLine().split(" ");
        int A = Integer.parseInt(line[0]);
        int B = Integer.parseInt(line[1]);
        int C = Integer.parseInt(bf.readLine());

        int count = (B + C) / 60;


        if (count != 0) {
            B = (B + C) - (60 * count);
            A = A + count;
        } else {
            B += C;
        }

        if (A >= 24) {
            A = A - 24;
        }

        System.out.println(A + " " + B);

    }
}
