/*
1 - Two Sum
*/

package main

import "fmt"

/*
Runtime
58ms / 5.16%
Memory
3.54MB / 74.76%
*/
func twoSum1(nums []int, target int) []int {
	result := []int{}
outerLoop:
	for i, num1 := range nums {
		rest := target - num1
		for j, num2 := range nums {
			if i != j && num2 == rest {
				result = []int{i, j}
				break outerLoop
			}
		}
	}
	return result
}

/*
Runtime
64ms / 5.16%
Memory
3.54MB / 74.76%
*/
func twoSum2(nums []int, target int) []int {
	for i, num1 := range nums {
		rest := target - num1
		for j, num2 := range nums {
			if i != j && num2 == rest {
				return []int{i, j}
			}
		}
	}
	return nil
}

/*
Resolve by map
Runtime
2ms / 93.28%
Memory
5.51MB / 7.18%
*/
func twoSum3(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		m[num] = i
	}
	for i, num := range nums {
		rest := target - num
		if idx, exist := m[rest]; exist && idx != i {
			return []int{i, idx}
		}
	}
	return nil
}

/*
Resolve by map and one loop
Runtime
6ms / 68.09%
Memory
4.16MB / 58.87%
*/
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		rest := target - num
		if idx, exist := m[rest]; exist && i != idx {
			return []int{idx, i}
		}
		m[num] = i
	}
	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	expected := []int{0, 1}
	result := twoSum(nums, target)
	result_msg := fmt.Sprintf("result: %d", result)
	expected_msg := fmt.Sprintf("expected: %d", expected)
	fmt.Println(result_msg)
	fmt.Println(expected_msg)
}
