import java.io.*;

public class Main {

   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int num = Integer.parseInt(br.readLine());
      int[] grape = new int[num+1];
      int[][] dp = new int[num+1][2]; //[][0] => 비연속, [][1] 연속
      for (int i = 1; i <= num; i++) {
         grape[i] = Integer.parseInt(br.readLine());
      }
      
      if(num == 1) {
         System.out.println(grape[1]);
         return;
      }else if(num == 2) {
         System.out.println(grape[1]+grape[2]);
         return;
      } else {
         dp[1][0] = grape[1];
         dp[2][0] = grape[2];
         dp[2][1] = grape[1] + grape[2];   
         for (int i = 3; i <= num; i++) {            
        	 dp[i][1] = grape[i] + dp[i-1][0];
        	 dp[i][0] =  Math.max( Math.max(dp[i-2][0] + grape[i], dp[i-1][1]),dp[i-2][1] + grape[i]);
         }
         System.out.println(Math.max(dp[num][1], dp[num][0]));
      }
   }
}