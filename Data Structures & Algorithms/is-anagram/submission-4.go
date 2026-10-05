func isAnagram(s string, t string) bool {

	set := map[rune]int{}

	for _, c := range s {
		set[c] += 1
	}

	for _, c := range t {
		set[c] -= 1
	}

	for _, c := range set {
		if c != 0 {
			return false
		}

	}

	return true


}
