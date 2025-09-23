import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Set<Integer> x_set = new HashSet<>();
        
        for (int i=0; i<N; i++){
            int x = sc.nextInt();
            if (x <= N){
                x_set.add(x);
            }
        }

        System.out.println(N - x_set.size());
    }
}