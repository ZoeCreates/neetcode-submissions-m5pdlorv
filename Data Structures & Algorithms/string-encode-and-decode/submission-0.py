class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        # ['5', '#', 'Hello', '5', '#', 'World']
        return "".join(res)
        # ['5#hello5#world']

        '''

你可能会问：“为什么不直接用一个字符串变量，每次用 `+` 号往后加呢？” 比如写成这样：

```python
# 看起来更直观，但性能很差的写法：
res = ""
for s in strs:
    res += str(len(s)) + "#" + s
return res

```

在 Python 中，**字符串是不可变的（Immutable）**。这意味着：

* 每次你执行 `res += ...` 时，Python **不能**直接在原来的字符串后面续写。
* 它必须在内存里**重新开辟一块大空间**，把旧的 `res` 复制过去，再把新的内容贴在后面，然后把旧的销毁。

如果输入有 10,000 个单词，使用 `+=` 就会导致 Python 在内存里反复申请空间、复制、销毁 10,000 次，这会变得**极其缓慢**（时间复杂度会退化到 $O(N^2)$）。

**而使用 `list` + `join` 的聪明之处在于：**

1. `res = []` 创建的是一个列表，列表在 Python 中是**可变的**。往列表里 `append` 元素非常快，不需要每次都重新复制整段内存。
2. 最后的 `"".join(res)` 是一次性绝招：Python 会先算好最终字符串的总长度，**只在内存里开辟一次空间**，把列表里的所有碎片依次填进去。

> **大白话总结**：
> 先用列表 `[]` 把碎片收集起来，最后用 `join` **一次性打包成字符串**。这是 Python 中拼接大量字符串的**标准标准高效写法（Best Practice）**。

        '''


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 

        ['5#hello5#world']
        while i < len(s):
            j = i 
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j 
        return res


