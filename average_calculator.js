let nums = [13, 20, 17, 25]
let datapoints = nums.length
let sum = 0
nums.forEach(num => (sum += num))
let non_roundResultNum = sum / datapoints
let roundedResultNum = Math.ceil(non_roundResultNum)
console.log(
  `The average number out of all the numbers in the list is: ${roundedResultNum}`
)

// console.log(
//   `The average number out of all the numbers is: ${non_roundResultNum}`
// )

// Calculates average number out of the array called nums
