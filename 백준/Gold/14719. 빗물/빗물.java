import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[] arr=Stream.of(br.readLine().split(" ")).mapToInt(i->Integer.parseInt(i)).toArray();
        int[] arr1=Stream.of(br.readLine().split(" ")).mapToInt(i->Integer.parseInt(i)).toArray();
        LinkedList<Integer> arrList1 = new LinkedList<Integer>();
        LinkedList<Integer> arrList2 = new LinkedList<Integer>();
        int maxValue=0;
        int argMax=0;
        int cnt =0;
        for(int i: arr1){
            if(maxValue<i){
                maxValue=i;
                argMax=cnt;
            }
            cnt++;
        }
        for(int i=0; i<arr1.length;i++){
            if(argMax<=i){
                arrList1.add(0,arr1[i]);
            }else{
                arrList2.add(arr1[i]);
            }
        }
        arrList1.removeLast();
        
        int ans = 0;

        int maxValue1 = 0;
        for(int i : arrList1){
            if(i>maxValue1){
                maxValue1=i;
            }else{
                ans+=maxValue1-i;
            }
        }
        maxValue1 = 0;
        for(int i : arrList2){
            if(i>maxValue1){
                maxValue1=i;
            }else{
                ans+=maxValue1-i;
            }
        }
        System.out.println(ans);
    }
}