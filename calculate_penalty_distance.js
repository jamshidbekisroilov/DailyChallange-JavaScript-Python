function calculatePenaltyDistance(rounds) {
  return rounds.reduce((sum, n) => sum + Math.max(0, 5 - n), 0) * 150;
}
console.log(calculatePenaltyDistance([4, 4]))


