import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

import javax.management.Query;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data[] = br.readLine().split(" ");
		int N = Integer.parseInt(data[0]);
		int M = Integer.parseInt(data[1]);
		int V = Integer.parseInt(data[2]);
		Integer[][] arr = new Integer[M][2];
		for (int i = 0; i < M; i++) {
			data = br.readLine().split(" ");
			arr[i][0] = Integer.parseInt(data[0]);
			arr[i][1] = Integer.parseInt(data[1]);
		}
		ArrayList<ArrayList<Integer>> g=graph(arr,N);
		for(int i =0; i< g.size();i++) {
			g.get(i).sort((a,b)->{return a-b;});
		}

		String result1 ="";
		boolean[] visit=new boolean[g.size()];
		result1=dfs(g,V,visit,result1);
		System.out.println(result1);
		
		String result=bfs(g,V);
		System.out.println(result);
	}
	static ArrayList<ArrayList<Integer>> graph(Integer[][] edges ,int n){
		ArrayList<ArrayList<Integer>> gr = new ArrayList<ArrayList<Integer>>();
		
		for(int i =0; i<=n;i++) {
			gr.add(new ArrayList<Integer>());
		}
		for(Integer[] edge: edges) {
			gr.get(edge[0]).add(edge[1]);
			gr.get(edge[1]).add(edge[0]);
		}
		return gr;
	}
	static String bfs(ArrayList<ArrayList<Integer>> g, int V) {
		String result="";
		boolean[] visit = new boolean[g.size()];
		Queue<Integer> q = new LinkedList<Integer>();
		visit[V]=true;
		q.add(V);
		while(!q.isEmpty()) {
			int val =q.poll();
			result+=val+" ";
			for(int nextVal : g.get(val)) {
				if(!visit[nextVal]) {
					
					q.add(nextVal);
					visit[nextVal] = true;
				}
			}
		}
		return result;
	}
	static String dfs(ArrayList<ArrayList<Integer>> g, int V,boolean[] visit,String result) {
		visit[V]=true;
		result+= V+" ";
		for(int nextVal:g.get(V)) {
			if(!visit[nextVal]) {
				result=dfs(g,nextVal,visit,result);
			}
		}
		return result;
	}
}
