//Question 1 : Gas Station
import java.util.*;
public class Solution {
    public int canCompleteCircuit(final int[] A, final int[] B) {
        List<Integer> gasList = new ArrayList<>();
        List<Integer> costList = new ArrayList<>();
        
        for (int gas : A) {
            gasList.add(gas);
        }
        
        for (int cost : B) {
            costList.add(cost);
        }
        
        int start = 0;
        int totalGas = 0;
        int tank = 0;
        
        for (int i = 0; i < gasList.size(); i++) {
            int gasDiff = gasList.get(i) - costList.get(i);
            totalGas += gasDiff;
            tank += gasDiff;
        
        // If tank becomes negative, update start to the next station    
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        
        // If total gas is greater than or equal to 0, return the start index
        if (totalGas >= 0) {
            return start;
        }
        
        // Otherwise, return -1 as the tour cannot be completed
        return -1;
    }
}
