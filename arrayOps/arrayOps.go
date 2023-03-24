package arrayOps

func Rotate(seq []string, steps, direction int) []string {
	/* 
	rotate an array a given number of steps in the specified direction
	1 = right, -1 = left
	*/
	length := len(seq)
	if direction == 1 {
		for ;0 < steps; steps-- {
			seq = append(seq[length - 1:], seq[0:length - 1]...)
		}
	} else {
		for ;0 < steps; steps-- {
			seq = append(seq[1: length], seq[0])
		}
	}
	return seq
}

func ReverseFrom(seq []string, start, end int) {
	/*
	Reverse the given sequence from position start to position end
	*/
	for ; start <= end; start, end = start + 1, end - 1 {
		seq[start], seq[end] = seq[end], seq[start]
	}
}