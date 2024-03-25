import java.util.*;
class Solution {
    public int[] solution(String[] wallpaper) {
        ArrayList<Integer> xArr = new ArrayList<>();
        ArrayList<Integer> yArr = new ArrayList<>();
        for(int i=0; i<wallpaper.length; i++) {
        	for(int j=0; j<wallpaper[i].length();j++) {
        		String data = wallpaper[i].charAt(j)+"";
        		if(data.equals("#")) {
        			xArr.add(i);
        			yArr.add(j);
        		}
        	}
        }
        xArr.sort((a,b)->{return a-b;});
        yArr.sort((a,b)->{return a-b;});
        int[] answer = {xArr.get(0),yArr.get(0),xArr.get(xArr.size()-1)+1,yArr.get(yArr.size()-1)+1};
        return answer;
    }
}