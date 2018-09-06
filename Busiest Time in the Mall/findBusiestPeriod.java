import java.io.*;
import java.util.*;

class Solution {
	
  static int findBusiestPeriod(int[][] data) {
    int n = data.length;
    int growth = 0;
    int maxGrowth = 0;
    int maxPeriod = 0;
    
    for(int i = 0; i < n; i++){
      if(data[i][2] == 1)
        growth += data[i][1];
      else if(data[i][2] == 0)
        growth -= data[i][0];
      
      if(i < n - 1 && data[i][0] == data[i + 1][0]) 
        continue;
        
      if(growth > maxGrowth){
        maxGrowth = growth;
        maxPeriod = data[i][0];
      }
      
    }
    return maxPeriod;
      
  }

  public static void main(String[] args) {

  }

}