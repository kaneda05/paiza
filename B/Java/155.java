import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int H = sc.nextInt();
        int W = sc.nextInt();
        int N = sc.nextInt();
        sc.nextLine();

        String[][] stamps = new String[N][H];
        for (int k = 0; k < N; k++){
            for (int i = 0; i < H; i++){
                stamps[k][i] = sc.nextLine();
            }
        }

        int R = sc.nextInt();
        int C = sc.nextInt();
        int [][] B = new int[R][C];
        for (int i = 0; i < R; i++){
            for (int j = 0; j < C; j++){
                B[i][j] = sc.nextInt() - 1;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < R; i++){
            for (int subrow = 0; subrow < H; subrow++){
                for (int j = 0; j < C; j++){
                    sb.append(stamps[B[i][j][subrow]]);
                }
                sb.append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}