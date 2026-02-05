function truncateText(text) {
	if (text.length > 20) {
		return text.slice(0, 17) + '...'
	}
	return text
}
console.log(truncateText('This string should get truncated.'))
