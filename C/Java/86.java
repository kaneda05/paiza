import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String name = sc.next();
        String vowels = "aiueoAIUEO";
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < name.length(); i++){
            char c = neame.charAt(i);
            if (vowels.indexOf(c) == -1){
                ans.append(c);
            }
        }
        System.out.println(ans.toStoring());
    }
}