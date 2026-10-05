func twoSum(nums []int, target int) []int {
    
	set := map[int]int{}

	for i, v := range nums {

		j, ok := set[target-v]

		if ok {
			return []int{j, i}
		}

		set[v] = i
	}

	return []int{}

}
