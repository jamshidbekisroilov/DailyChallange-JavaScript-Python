function skiJumpMedal(distancePoints, stylePoints, windComp, kPointBonus) {
  let arr = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
  let all = distancePoints + stylePoints + windComp + kPointBonus;
  let index = [...arr.sort().reverse()].findIndex(item => item < all)

  if (index === 0)  return "Gold" 
  else if(index === 1) return "Silver"
  else if(index === 2) return "Bronze"
  else return "No Medal"
}

