package golang

func twoSum(nums []int, target int) []int {
	mem := make(map[int]int)
	for index, n := range nums {
		mem[n] = index
	}
	for index, n := range nums {
		if buddyIndex, exist := mem[target-n]; exist {
			return []int{index, buddyIndex}
		}
	}
	return []int{}
}
