
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static PriorityQueue<Integer> result = new PriorityQueue<Integer>(Collections.reverseOrder());
	static BufferedReader br;
	static int n;
//	static HashMap<Integer, ArrayList<Integer>> arr = new HashMap<Integer, ArrayList<Integer>>();
	static HashMap<Integer, HashMap<Integer, Integer>> graph = new HashMap<Integer, HashMap<Integer, Integer>>();

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		makeGraph();
		dfs(1,0,result);
		for(Integer key : graph.keySet()) {
			dfsInit(key, 0, true);
		}
		System.out.println(result.peek());
	}

	static void makeGraph() throws IOException {
		while (br.ready()) {
			String data[] = br.readLine().split(" ");
			int s = Integer.parseInt(data[0]);
			int e = Integer.parseInt(data[1]);
			int d = Integer.parseInt(data[2]);
			if (graph.get(s) == null) {
				graph.put(s, new HashMap<Integer, Integer>());
			}
			graph.get(s).put(e, d);
		}
	}

	static void dfsInit(int V, int d, boolean quarter) {
		if (graph.get(V).size() > 1 && quarter) {
			quarter = false;
		}
		if (!quarter) {
			ArrayList<Integer> flag = new ArrayList<Integer>();
			for (int nextVal : graph.get(V).keySet()) {
//				System.out.println(nextVal);
				int dInit = graph.get(V).get(nextVal);
				PriorityQueue<Integer> arrFlag = new PriorityQueue<Integer>(Collections.reverseOrder());
				dfs(nextVal, dInit,arrFlag/* ,quarter */);
//				System.out.println("=====");
//				System.out.println(arrFlag);
				flag.add(arrFlag.peek());
			}
			flag.sort((a, b) -> {
				return b - a;
			});
//			System.out.println("********************************");
//			System.out.println(flag.get(0)+flag.get(1));
			result.add(flag.get(0)+flag.get(1));
//			System.out.println("********************************");
		}
	}

	static void dfs(int V, int d,PriorityQueue<Integer> arr2/* ,boolean quarter */) {
//		System.out.println("d:  "+d);
		int flag = d;
		if (graph.get(V) != null) {
//			System.out.println("size"+graph.get(V).keySet().size());
			for (int val : graph.get(V).keySet()) {
//				System.out.println("graph.get(V).get(val)"+graph.get(V).get(val)+"  "+d+":"+flag);
//				d += graph.get(V).get(val);
				int flag2 = graph.get(V).get(val)+flag;
				dfs(val, flag2,arr2);
			}
		}else {
			arr2.add(flag);
//			System.out.println("sadsad "+flag+","+arr2);
		}
	}
}
