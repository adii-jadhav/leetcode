class Solution {

    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a1, a2) -> Integer.compare(a1[0], a2[0]));

        int arrows = 1;
        int[] lastProcessed = points[0];

        for (final int[] point : points) {
            // no interaction
            if (lastProcessed[1] < point[0]) {
                lastProcessed = point;
                arrows++;
            } else {
                lastProcessed[0] = Math.max(lastProcessed[0], point[0]);
                lastProcessed[1] = Math.min(lastProcessed[1], point[1]);
            }
        }

        return arrows;
    }
}