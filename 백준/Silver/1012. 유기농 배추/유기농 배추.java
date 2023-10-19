import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

import javax.management.Query;

public class Main {
	static int[][] map;
	static int N;
	static int M;
	static int K;
	static HashMap<String, ArrayList<String>> g;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data = br.readLine();
		int T = Integer.parseInt(data);
		for (int t = 0; t < T; t++) {
			String[] data_arr = br.readLine().split(" ");
			N = Integer.parseInt(data_arr[0]);
			M = Integer.parseInt(data_arr[1]);
			K = Integer.parseInt(data_arr[2]);
			map = new int[M][N];
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < N; j++) {
					map[i][j] = 0;
				}
			}

			for (int i = 0; i < K; i++) {
				data_arr = br.readLine().split(" ");
				map[Integer.parseInt(data_arr[1])][Integer.parseInt(data_arr[0])] = 1;
			}

//			for (int[] tt : map) {
//				System.out.println(Arrays.toString(tt));
//			}
//			System.out.println("===============");

			ArrayList<ArrayList<String[]>> input = makeInput();
			
//			for (ArrayList<String[]> road : input) {
//				for (String[] n : road) {
//					System.out.print(n[0] + " " + n[1] + "     ");
//				}
//				System.out.println("");
//			}
			graph(input);
			
//			System.out.println("====graph=====");
//			for (int i = 0; i < M; i++) {
//				for (int j = 0; j < N; j++) {
//					System.out.println(i + "," + j + "    " + g.get(i + "," + j).toString());
//				}
//			}
			
			int cnt=0;
			String V=findV();
//			do {
//				V = findV();
//				bfs(V);
//				cnt++;
////				for(int[] i:map) {
////					System.out.println(V+Arrays.toString(i));
////				}
//			}while(!(V.equals("finish")));
			while(!(V.equals("finish"))){
				bfs(V);
				cnt++;
				V=findV();
			}
			System.out.println(cnt);
		}
	}

	private static ArrayList<ArrayList<String[]>> makeInput() {
		ArrayList<ArrayList<String[]>> flag_result = new ArrayList<ArrayList<String[]>>();
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if ((i + 1) < M) {
					if (map[i][j] == 1 && map[i + 1][j] == 1) {
						ArrayList<String[]> flag = new ArrayList<String[]>();
						String[] first = { i + "", j + "" };
						String[] last = { (i + 1) + "", j + "" };
						flag.add(first);
						flag.add(last);
						flag_result.add(flag);
					}
				}
				if ((j + 1) < N) {
					if (map[i][j] == 1 && map[i][j+ 1] == 1) {
						ArrayList<String[]> flag = new ArrayList<String[]>();
						String[] first = { i + "", j + "" };
						String[] last = { i + "", ( j + 1 ) + "" };
						flag.add(first);
						flag.add(last);
						flag_result.add(flag);
					}
				}
				if(map[i][j] == 1) {
					ArrayList<String[]> flag = new ArrayList<String[]>();
					String[] first = { i + "", j + "" };
					flag.add(first);
					flag.add(first);
					flag_result.add(flag);
				}
			}
		}
		return flag_result;
	}

	static void graph(ArrayList<ArrayList<String[]>> edges) {
		g = new HashMap<String, ArrayList<String>>();

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				g.put(i + "," + j, new ArrayList<String>());
			}
		}
		// System.out.println(gr.get(new String[]{"0","0"}));
		for (ArrayList<String[]> edge : edges) {
			g.get(edge.get(0)[0] + "," + edge.get(0)[1]).add(edge.get(1)[0] + "," + edge.get(1)[1]);
			g.get(edge.get(1)[0] + "," + edge.get(1)[1]).add(edge.get(0)[0] + "," + edge.get(0)[1]);
		}
	}

	static void bfs(String V) {
		boolean[][] visit = new boolean[M][N];
		Queue<String> q = new LinkedList<String>();
		visit[Integer.parseInt(V.split(",")[0])][Integer.parseInt(V.split(",")[1])]=true;
		q.add(V);
		while(!q.isEmpty()) {
			String val =q.poll();
			String flag = val.split(",")[0]+","+val.split(",")[1];
			map[Integer.parseInt(val.split(",")[0])][Integer.parseInt(val.split(",")[1])]=0;
			//System.out.println("test");
			for(String nextVal : g.get(flag)) {
				int y=Integer.parseInt(nextVal.split(",")[0]);
				int x=Integer.parseInt(nextVal.split(",")[1]);
				if(!visit[y][x]) {
					q.add(nextVal);
					visit[y][x] = true;
				}
				
			}
		}
	}
	
	static String findV() {
		String V="finish";
		for(int i=0; i< M;i++) {
			for(int j=0;j<N;j++) {
				if(map[i][j]==1) {
					V=i+","+j;
					return V;
				}
			}
		}
		return V;
	}
}
