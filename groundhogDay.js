function groundhogDayPrediction(appearance) {
	if (typeof appearance !== 'boolean') {
		return 'No prediction this year.'
	} else if (appearance) {
		return "Looks like we'll have six more weeks of winter."
	}
	return "It's going to be an early spring."
}
//Demo test
console.log(groundhogDayPrediction('false')) //Output: No prediction this year.
console.log(groundhogDayPrediction(true)) //Output: Looks like we'll have six more weeks of winter.
console.log(groundhogDayPrediction(false)) //Output: It's going to be an early spring.
