func lengthOfLongestSubstring(s string) int {
	longest := ""
	for i, _ := range s {
		found := make(map[string]int)
		sub := ""
		for _, c := range s[i:] {
			d := string(c)
			if found[d] == 1 {
				break
			}
			found[d] += 1
			sub += d
		}
		if len(sub) > len(longest) {
			longest = sub
		}
	}
	return len(longest)
}