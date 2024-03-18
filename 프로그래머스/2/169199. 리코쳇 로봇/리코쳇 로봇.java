import java.util.*;
class Solution {
    public int solution(String[] board) {
        int answer = -1;
        int r = board.length; 
        int c = board[0].length();
        int[] start = new int[2];
        
        //100 100
        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                if(board[i].charAt(j) == 'R') {
                    start[0] = i;
                    start[1] = j;
                    continue;
                }
            }
        }
        
        boolean[][] visited = new boolean[r][c];
        Queue<Integer[]> q = new LinkedList<>();
        q.offer(new Integer[] {start[0], start[1], 0});
        visited[start[0]][start[1]] = true;
        int[] moveR = {-1,1,0,0};
        int[] moveC = {0,0,-1,1};
        
        while(!q.isEmpty()) {
            
            Integer[] cur = q.poll();
            int curR = cur[0];
            int curC = cur[1];
            int curCnt = cur[2];
            
            if(board[curR].charAt(curC) == 'G') {
                answer = curCnt;
                break;
            }
            
            
            for(int i =0; i<4; i++) {
                int newR = curR+moveR[i];
                int newC = curC+moveC[i];
               
                while(true) {
                    if(newR >= 0 && newR < r && newC >=0 && newC < c) {
                        if(board[newR].charAt(newC) == 'D' ) {
                        	if(!visited[newR-moveR[i]][newC-moveC[i]]) {
	                            q.offer(new Integer[] {newR-moveR[i], newC-moveC[i], curCnt+1});
	                            visited[newR-moveR[i]][newC-moveC[i]] = true;
                        	}
                            break;
                        } else if (((newR ==0 && i == 0) || (newR == r-1 && i == 1) || (newC == 0 && i == 2) || (newC == c-1 && i == 3)) && !visited[newR][newC]) {
                    		q.offer(new Integer[] {newR, newC, curCnt+1});
                            visited[newR][newC] = true;
                            break;
                        } else {
                            newR += moveR[i];
                            newC += moveC[i];
                        }
                    } else {
                        break;
                    }
                }
            }
        }
        return answer;
    }
}