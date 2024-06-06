var isNStraightHand = function(hand, groupSize) {
  if (hand.length % groupSize !== 0) {
    return false;
  }

  const countMap = new Map();

  // Count the occurrences of each card
  for (const card of hand) {
    countMap.set(card, (countMap.get(card) || 0) + 1);
  }

  // Sort the cards in ascending order
  hand.sort((a, b) => a - b);

  for (const card of hand) {
    if (countMap.get(card) === 0) {
      // Skip cards that have been used in previous groups
      continue;
    }

    // Check if we can form a group of consecutive cards
    for (let i = 0; i < groupSize; i++) {
      const currCard = card + i;

      if (countMap.get(currCard) === undefined || countMap.get(currCard) === 0) {
        // If any card in the group is missing, return false
        return false;
      }

      // Reduce the count of the current card in the map
      countMap.set(currCard, countMap.get(currCard) - 1);
    }
  }

  return true;
}