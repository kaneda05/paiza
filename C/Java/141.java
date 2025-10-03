import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextLine();
        List<String> A = new ArrayList<>();
        for (int i = 0; i < N; i++){
            A.add(sc.nextLine());
        }

        Map<String, Integer> c = new HashMap<>();
        for (String s : A){
            c.put(s, c.getOrDefault(s, 0) + 1);
        }

        int ans = -1;
        String name = "";
        for (Map.Entry<String, Integer> entry : c.entrySet()){
            if (ans < entry.getValue()){
                ans = entry.getValue();
                name = entry.getKey();
            }
        }

        System.out.println(name);
    }
}