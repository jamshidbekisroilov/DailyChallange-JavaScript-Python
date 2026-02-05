function countChange(change) {
	return `$${(change.reduce((sum, n) => sum + n, 0) / 100).toFixed(2)}`
}
console.log(countChange([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]))
