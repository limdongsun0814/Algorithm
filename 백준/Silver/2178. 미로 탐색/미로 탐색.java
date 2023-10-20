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
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String data[] = br.readLine().split(" ");
		int N = Integer.parseInt(data[0]);
		int M = Integer.parseInt(data[1]);
		String[][] map = new String[N][M];
		String str = br.readLine();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
								
//				map[i][j] = str.charAt(i * M + j) + "";
				map[i][j] = str.charAt(j) + "";
			}
			str=br.readLine();
		}

		ArrayList<ArrayList<String[]>> input = new ArrayList<ArrayList<String[]>>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if ((i + 1) < N) {
					if (map[i + 1][j].equals("1") && map[i][j].equals("1")) {
						String[] first = new String[2];
						String[] last = new String[2];
						ArrayList<String[]> road = new ArrayList<String[]>();
						first[0] = i + "";
						first[1] = j + "";
						last[0] = (i + 1) + "";
						last[1] = j + "";
						road.add(first);
						road.add(last);
						input.add(road);
					}
				}
				if ((j + 1) < M) {
					if (map[i][j + 1].equals("1") && map[i][j].equals("1")) {
						ArrayList<String[]> road = new ArrayList<String[]>();
						String[] first = { i + "", j + "" };
						String[] last = { i + "", (j + 1) + "" };
						road.add(first);
						road.add(last);
						input.add(road);
					}
				}
			}
		}


		HashMap<String, ArrayList<String>> g = new HashMap<String, ArrayList<String>>();
		g = graph(input, N, M);
		String result = bfs(g, 0 + "," + 0, N, M);
		System.out.println(Integer.parseInt(result.split(",")[2])+1);

	}

	static HashMap<String, ArrayList<String>> graph(ArrayList<ArrayList<String[]>> edges, int N, int M) {
		HashMap<String, ArrayList<String>> gr = new HashMap<String, ArrayList<String>>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				gr.put(i + "," + j, new ArrayList<String>());
			}
		}
		for (ArrayList<String[]> edge : edges) {
			gr.get(edge.get(0)[0] + "," + edge.get(0)[1]).add(edge.get(1)[0] + "," + edge.get(1)[1]);
			gr.get(edge.get(1)[0] + "," + edge.get(1)[1]).add(edge.get(0)[0] + "," + edge.get(0)[1]);
		}
		return gr;
	}

	static String bfs(HashMap<String, ArrayList<String>> g, String V, int N, int M) {
		ArrayList<String> result = new ArrayList<String>();
		boolean[][] visit = new boolean[N][M];
		Queue<String> q = new LinkedList<String>();
		visit[Integer.parseInt(V.split(",")[0])][Integer.parseInt(V.split(",")[1])] = true;
		q.add(V+","+0);
		String size = "";
		//pos y,x,움직인 횟수
		String pos =(N-1)+","+(M-1);
		String val="";
		while (!q.isEmpty()) {
			val = q.poll(); 
			//y,x
			int x=Integer.parseInt(val.split(",")[1]); 
			int y=Integer.parseInt(val.split(",")[0]);  
			int cnt = Integer.parseInt(val.split(",")[2]);
			String flag =y+","+x;
			
			if(flag.equals(pos)) {
				break;
			}
			result.add(val);   
			if((x-1>=0)&&g.get(flag).contains((y)+","+(x-1))&&!visit[y][x-1]) {
				q.add((y)+","+((x-1)+","+(cnt+1)));
				visit[y][x-1]=true;
			}
			if((x+1<M)&&g.get(flag).contains((y)+","+(x+1))&&!visit[y][x+1]) {
				q.add((y)+","+(x+1)+","+(cnt+1));
				visit[y][x+1]=true;
			}
			if((y-1>=0)&&g.get(flag).contains((y-1)+","+(x))&&!visit[y-1][x]) {
				q.add((y-1)+","+(x)+","+(cnt+1));
				visit[y-1][x]=true;
			}
			if((y+1<N)&&g.get(flag).contains((y+1)+","+(x))&&!visit[y+1][x]) {
				q.add((y+1)+","+(x)+","+(cnt+1));
				visit[y+1][x]=true;
			}
		}
		return val;
	}
}
