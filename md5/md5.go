package md5

import (
	"crypto/md5"
	"encoding/hex"
	"io"
	"strconv"
)

func HashToString(key, path string) string {
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, path)
	return hex.EncodeToString(hash.Sum(nil))
}

func HashWithIdxToBytes(key string, num int) []byte {
	numStr := strconv.Itoa(num)
	hash := md5.New()
	io.WriteString(hash, key)
	io.WriteString(hash, numStr)
	return hash.Sum(nil)
}

func HashWithIdxToString(key string, idx int) string {
	hash := HashWithIdxToBytes(key, idx)
	return hex.EncodeToString(hash)
}

func StretchHash(hash string, times int) string {
	for i := 0; i < times; i++ {
		newHash := md5.New()
		io.WriteString(newHash, hash)
		hash = hex.EncodeToString(newHash.Sum(nil))
	}
	return hash
}
