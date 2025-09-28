import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] A = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                A[i][j] = sc.nextInt();
            }
        }

        int X = sc.nextInt();
        int[][] route = new int[X][2];
        for (int i = 0; i < X; i++) {
            route[i][0] = sc.nextInt();
            route[i][1] = sc.nextInt();
        }

        int curLine = 1, curStation = 1;
        int totalCost = 0;

        for (int i = 0; i < X; i++) {
            int Ri = route[i][0] - 1;  // 0-index化
            int Si = route[i][1] - 1;
            totalCost += Math.abs(A[Ri][Si] - A[Ri][curStation - 1]);
            curLine = Ri + 1;
            curStation = Si + 1;
        }

        System.out.println(totalCost);
    }
}
