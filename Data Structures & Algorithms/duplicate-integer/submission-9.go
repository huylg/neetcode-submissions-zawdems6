func hasDuplicate(nums []int) bool {
    	mySet := map[int]struct{}{}

	for _, value := range nums {

		_, contain := mySet[value]

		if contain {
			return true
		}

		mySet[value] = struct{}{}
	}

	return false


}
