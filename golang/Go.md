# Golang

官网：[Downloads - The Go Programming Language (google.cn)](https://golang.google.cn/dl/)


## 基础

### channel
无缓冲：读写是同步进行，没有对接人的话会一直阻塞着
有缓冲：有数据时读不会阻塞；未满时写数据不会阻塞



注意点:
1) 大多数时候，读写要在不同 goroutine，尤其是无缓冲 channel





## 最佳实践

### error
1. 对于将错误作为返回值的话,不需要带上stacktrace,若是作为异常的话,就最好是带上
2. 对于调用第三方库返回的error,最好使用wrap之后再进行上抛, 或者使用withWrap
3. 推荐使用第三方包:/pkg/errors,  打印堆栈信息需要使用指定方式: %+v
4. 


**所以尽量只把 error 用作异常情况，而不是一种返回值。**


