
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
	static int[][] map = new int[100][100];
	static boolean[] visit;
	static int N; // 컴퓨터의 수
	static int M;
	static int result = 0;
	static HashMap<Integer,ArrayList<Integer>> graph;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] data_arr = br.readLine().split(" ");
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		N = Integer.parseInt(data_arr[0]);
		M = Integer.parseInt(data_arr[1]);
		make_graph(br);
		ArrayList<Integer> final_arr = new ArrayList<Integer>();
		int max = 0;
		visit = new boolean[N + 1];
		for(int i  : graph.keySet()) {
			int result = bfs(i, visit);
			if (max < result) {
				final_arr.clear();
				final_arr.add(i);
				max = result;
			} else if (max == result) {
				final_arr.add(i);
			}
			visit = new boolean[N + 1];
		}
		

		for (int i : final_arr) {
			bw.write(i + " ");
		}
		bw.flush();
	}

	static void make_graph(BufferedReader br) throws IOException {
		graph = new HashMap<Integer,ArrayList<Integer>>();

		for (int i = 0; i < M; i++) {
			String[] data_arr = br.readLine().split(" ");
			if(graph.get(Integer.parseInt(data_arr[1]))==null) {
				graph.put(Integer.parseInt(data_arr[1]), new ArrayList<Integer>());
			}
			graph.get(Integer.parseInt(data_arr[1])).add(Integer.parseInt(data_arr[0]));
		}
	}

	static int bfs(int V, boolean[] visit) {
		Queue<Integer> q = new LinkedList<Integer>();
		int result = 0;
		q.add(V );
		visit[V] = true;
		while (!q.isEmpty()) {
			int data = q.poll();
			result++;
			if(graph.get(data)==null) {continue;}
			for (int nextdata : graph.get(data)) {
				if (!visit[nextdata]) {
					visit[nextdata] = true;
					q.add(nextdata);
				}
			}
		}
		return result;
	}
}
