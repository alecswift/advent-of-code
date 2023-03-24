package arrayOps

import (
	"testing"
	"reflect"
)

func TestRotateRightThree(t *testing.T) {
	input := []string{"a", "b", "c", "d"}
	expected := []string{"b", "c", "d", "a"}
	output := Rotate(input, 3, 1)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", input, expected)
	}
}

func TestRotateLeftTwo(t *testing.T) {
	input := []string{"a", "b", "c", "d", "e"}
	expected := []string{"c", "d", "e", "a", "b"}
	output := Rotate(input, 2, -1)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", input, expected)
	}
}

func TestReverseFromPosOneToPosThree(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "d", "c", "b", "e"}
	ReverseFrom(output, 1, 3)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseFromFullArray(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"e", "d", "c", "b", "a"}
	ReverseFrom(output, 0, 4)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}

func TestReverseFrom(t *testing.T) {
	output := []string{"a", "b", "c", "d", "e"}
	expected := []string{"a", "e", "d", "c", "b"}
	ReverseFrom(output, 1, 4)

	if !reflect.DeepEqual(output, expected) {
		t.Errorf("got %v want %v", output, expected)
	}
}