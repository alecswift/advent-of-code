package md5

import (
	"crypto/md5"
	"io"
	"strconv"
)

func HashWithIdxToBytes(key string, num int) []byte {
	numStr := strconv.Itoa(num)
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, numStr)
	return hash.Sum(nil)
}