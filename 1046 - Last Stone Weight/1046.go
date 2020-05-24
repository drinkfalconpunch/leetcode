func lastStoneWeight(stones []int) int {
	for {
		if len(stones) == 0 {
			return 0
		}
		if len(stones) == 1 {
			return stones[0]
		}
		max_weight := maxSlice(stones)
		stones = removeFromSlice(stones, max_weight)
		max_weight2 := maxSlice(stones)
		stones = removeFromSlice(stones, max_weight2)
		if max_weight != max_weight2 {
			diff := max_weight - max_weight2
			if diff < 0 {
				diff = -diff
			}
			stones = append(stones, diff)
		}
	}
}

func maxSlice(slice []int) int {
	max_value := 0
	if len(slice) == 0 {
		return max_value
	}
	for _, v := range slice {
		if v > max_value {
			max_value = v
		}
	}
	return max_value
}

func minSlice(slice []int) int {
	min_value := 0
	if len(slice) == 0 {
		return min_value
	}
	for _, v := range slice {
		if v < min_value {
			min_value = v
		}
	}
	return min_value
}

func removeFromSlice(slice []int, value int) []int {
	for i, v := range slice {
		if v == value {
			if i == len(slice)-1 {
				return slice[:i]
			}
			println(slice[i+1:])
			return append(slice[:i], slice[i+1:]...)
		}
	}
	return slice
}