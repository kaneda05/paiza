import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        
        int minTime = Integer.MAX_VALUE;
        int maxTime = Integer.MIN_VALUE;

        for (int i = 0; i < N; i++){
            int s = sc.nextInt();
            int f = sc.nextInt();
            int t = sc.nextInt();
            int dayLength = s + f + (24 - t);
        

            minTime = Math.min(minTime, dayLength);
            maxTime = Math.max(maxTime, dayLength);
        }
    }

    System.out.println(minTime);
    System.out.println(maxTime);
}