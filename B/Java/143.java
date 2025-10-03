import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        List<List<Interger>> winners = new ArraryList<>();
        for (int i = 0; i <= N; i++){
            winners.add(new ArraryList<>());
        }

        for (int i = 0; i < M; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();

            winners.get(x).add(y);

            if (!winners.get(y).isEmpty()){
                winners.get(x).addAll(winners.get(y));
            }

            siners.get(y).clear();
        }

        int [] counts = new int[N+1];
        for (int i = 1; i <= N; i++){
            counts[i] = winners.get(i).size();
        }

        int maxwinner = 0;
        for (int i = 0; i <= N; i++){
            maxwinner = Math.max(maxwinner, counts[i]);
        }

        for (int i = 0; i <= N; i++){
            if (counts[i] == maxwinner){
                System.out.println(i);
            }
        }
    }
}