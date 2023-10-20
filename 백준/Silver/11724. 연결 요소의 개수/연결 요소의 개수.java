
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visit;
	static ArrayList<Integer> arr_bfs=new ArrayList<Integer>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data[] = br.readLine().split(" ");
		int N = Integer.parseInt(data[0]);
		int M = Integer.parseInt(data[1]);
		
		Integer[][] arr = new Integer[M][2];
		for (int i = 0; i < M; i++) {
			data = br.readLine().split(" ");
			arr[i][0] = Integer.parseInt(data[0]);
			arr[i][1] = Integer.parseInt(data[1]);
		}
		graph(arr,N);
		
		
		visit=new boolean[N+1];
		int cnt=0;
		for(int i=1;i<=N;i++) {
			if(!arr_bfs.contains(i)) {
				bfs(i);
				cnt++;
			}
		}
		System.out.println(cnt);
	}
	static void graph(Integer[][] edges ,int n){
		graph = new ArrayList<ArrayList<Integer>>();
		
		for(int i =0; i<=n;i++) {
			graph.add(new ArrayList<Integer>());
		}
		for(Integer[] edge: edges) {
			graph.get(edge[0]).add(edge[1]);
			graph.get(edge[1]).add(edge[0]);
		}
	}
	
	
	static void bfs(int V) {
		Queue<Integer> q = new LinkedList<Integer>();
		visit[V]=true;
		q.add(V);
		while(!q.isEmpty()) {
			Integer val =q.poll();
			arr_bfs.add(val);
			for(Integer nextVal : graph.get(val)) {
				if(!visit[nextVal]) {
					q.add(nextVal);
					visit[nextVal] = true;
				}
			}
		}
		
	}
	
}
