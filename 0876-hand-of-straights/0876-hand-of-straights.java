class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize != 0) {
            return false;
        }

        Map<Integer, Integer> freq = new HashMap<>();

        for (int card: hand) {
            freq.put(card, freq.getOrDefault(card, 0) + 1);
        }

        Arrays.sort(hand);

        for (int i = 0; i < hand.length; i++) {
            if (freq.get(hand[i]) == 0) {
                continue;
            }

            for (int j = 0; j < groupSize; j++) {
                int currCard = hand[i] + j;
                if (freq.getOrDefault(currCard, 0) == 0) {
                    return false;
                }

                freq.put(currCard, freq.get(currCard) - 1);
            }
        }

        return true;
    }
}