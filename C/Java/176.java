import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++){
            String s = sc.next();
            String t = sc.next();

            char[] sArr = s.toCharArray();
            char[] tArr = t.toCharArray();

            Arrays.sort(sArr);
            Arrays.sort(tArr);

            if (Arrays.equals(sArr, tArr)){
                System.out.println("Yes");
            }else{
                System.out.println("No");
            }
        }
    }
}