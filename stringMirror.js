function mirror(str) {
	return str + str.split('').reverse().join('')
}
//Demo test
console.log(mirror('shamol')) //Output: shamollomahs
