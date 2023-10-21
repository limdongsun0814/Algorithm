
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int[][] map=new int[100][100];
	static boolean[] visit;
	static int N;
	static int result = 0;
	static HashMap<Integer, ArrayList<Integer>> graph;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		visit=new boolean[N+1];
		make_graph(br);
		HashMap<Integer,Integer> result=bfs(1,visit);
		int cnt =0;
		for(int i=0;i<=N;i++) {
			if(result.get(i)==null) {
				cnt++;
			}
		}
		System.out.println(N-cnt);
	}
	
	static void make_graph(BufferedReader br) throws IOException {
		graph = new HashMap<Integer, ArrayList<Integer>>();
		int line = Integer.parseInt(br.readLine());
		for(int i=0;i<N+1;i++) {
			graph.put(i, new ArrayList<Integer>());
		}
		for(int i=0;i<line;i++) {
			String[] data_arr=br.readLine().split(" ");
			graph.get(Integer.parseInt(data_arr[0])).add(Integer.parseInt(data_arr[1]));
			graph.get(Integer.parseInt(data_arr[1])).add(Integer.parseInt(data_arr[0]));
		}
	}
	static HashMap<Integer,Integer> bfs(int V,boolean[] visit) {
		Queue<String> q = new LinkedList<String>();
		HashMap<Integer,Integer> result = new HashMap<Integer,Integer>();
		q.add(V+","+1);
		visit[V]=true;
		while (!q.isEmpty()) {
			String data = q.poll();
			result.put(Integer.parseInt(data.split(",")[0]), Integer.parseInt(data.split(",")[1]));
			Integer val = Integer.parseInt(data.split(",")[0]);
			for(int nextdata : graph.get(val)) {
				if(!visit[nextdata]) {
					visit[nextdata]=true;
					q.add(nextdata+","+val);
				}
			}
		}
		return result;
	}
}
