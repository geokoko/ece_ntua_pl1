package ex2.moves;
import java.util.*;

class Cell implements Comparable<Cell> {
    int x, y, cost;
    Cell parent;

    Cell(int x, int y, int cost, Cell parent) {
        this.x = x;
        this.y = y;
        this.cost = cost;
        this.parent = parent;
    }

    @Override
    public int compareTo(Cell o) {
        return this.cost - o.cost;
    }
}

public class Moves {
    private static final int[] dRow = {-1, 1, 0, 0, -1, -1, 1, 1};
    private static final int[] dCol = {0, 0, -1, 1, -1, 1, -1, 1};

    public static boolean out_of_bounds (int x, int y, int n) {
        if (x < 0 || x >= n || y < 0 || y >= n) {
            return true;
        }
        return false;
    }
    
    public static void shortest_path(int[][] grid, int n) {
        PriorityQueue<Cell> frontier = new PriorityQueue<>();
        boolean visited[][] = new boolean[n][n];

        frontier.add(new Cell(0, 0, grid[0][0], null));

        while (!frontier.isEmpty()) {
            Cell current = frontier.poll();
            visited[current.x][current.y] = true;

            for (int i = 0; i < 8; i++) {
                int newRow = current.x + dRow[i];
                int newCol = current.y + dCol[i];

                if (!out_of_bounds(newRow, newCol, n) && !visited[newRow][newCol]) {
                    frontier.add(new Cell(newRow, newCol, current.cost + grid[newRow][newCol], current));
                }
            }
        }
    }
}
