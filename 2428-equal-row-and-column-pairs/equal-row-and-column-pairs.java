class Solution {
    public int equalPairs(int[][] grid) {
        Map<String, Integer> rowMap = new HashMap<>();
        int count = 0;

        for(int[] row : grid){
            String key = Arrays.toString(row);
            rowMap.put(key, rowMap.getOrDefault(key, 0) + 1);
        }

        for(int col = 0; col < grid[0].length; col++){
            int[] column = new int[grid.length];
            for(int row = 0; row < grid.length; row++){
                column[row] = grid[row][col];
            }
            String key = Arrays.toString(column);
            count += rowMap.getOrDefault(key, 0);
        }
        return count;
    }
}