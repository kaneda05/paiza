import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();
        String[] ls = new String[N];
        for (int i = 0; i < N; i++){
            ls[i] = sc.nextLine();
        }

        for (int i = 0; i < N-1; i++){
            char lastChar = ls[i].charAt(ls[i].length()-1);
            char firstChar = ls[i+1].charAt(0);

            if (lastChar == firstChar){
                continue;
            }else{
                System.out.println(lastChar + " " + firstChar);
                return;
            }
        }
        System.out.println("Yes");
    }
}