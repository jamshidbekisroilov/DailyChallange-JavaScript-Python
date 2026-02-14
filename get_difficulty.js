function getDifficulty(track) {
	let sum = 0
	for (let [k, v] of [...track].entries()) {
		if (v === 'S') {
			sum += 0
		} else if (v === 'R' && track[k - 1] === 'L') {
			sum += 15
		} else if (v === 'L' && track[k - 1] === 'R') {
			sum += 15
		} else {
			sum += 5
		}
	}
	if (sum > 200) return 'Hard'
	else if (sum > 100) return 'Medium'
	else if (sum >= 0) return 'Easy'
}
