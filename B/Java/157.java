import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[][] p = new int[N][K];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < K; j++) {
                p[i][j] = sc.nextInt();
            }
        }
        
        Set<Integer> shopNumber = new HashSet<>();
        
        for (int k = 0; k < K; k++) {
            int minP = 10000;
            int minShop = -1;
            for (int n = 0; n < N; n++) {
                if (p[n][k] < minP) {
                    minP = p[n][k];
                    minShop = n;
                }
            }
            shopNumber.add(minShop);
        }
        
        System.out.println(shopNumber.size());
    }
}
