package util

func Abs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}

func ManhattanDistance(x1, y1, x2, y2 int) int {
	i := Abs(x1 - x2)
	j := Abs(y1 - y2)
	return i + j
}