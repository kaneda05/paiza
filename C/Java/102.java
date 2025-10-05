import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int M = sc.nextInt();
        Set<Integer> A = new HashSet<>();
        for (int i = 0; i < M; i++) A.add(sc.nextInt());


        int N = sc.nextInt();
        Set<Integer> B = new HashSet<>();
        for (int i = 0; i < N; i++) B.add(sc.nextInt());

        String[] date = new String[32];
        Arrays.fill(date, "x");
        boolean flag = true;

        for (int i = 1; i < 32; i++){
            boolean inA = A.contains(i);
            boolean inB = B.contains(i);

            if (inA && inB){
                if (flag){
                    date[i] = "A";
                    flag = false;
                }else{
                    date[i] = "B";
                    flag = true;
                }
            }else if (inA){
                date[i] = "A";
            }else if (inB){
                date[i] = "B";
            }
        }

        for (int i = 1; i < 32; i++){
            System.out.println(date[i]);
        }
    }
}