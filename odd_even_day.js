function oddOrEvenDay(timestamp) {
	const date = new Date(timestamp)
	const day = date.getUTCDate()

	return day % 2 == 0 ? 'even' : 'odd'
}
//Demo test !!! UTC time zonasi uchun
console.log(oddOrEvenDay(1769472000000))
console.log(oddOrEvenDay(1769444440000))
