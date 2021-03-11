

​	**Cheetsheet:*

- Sort lists by keys:

- - ```python
    student_tuples = [('john', 'A', 15),('jane', 'B', 12), ('dave', 'B', 10),]
    x = sorted(student_tuples, key=lambda student: student[2],reverse = True) 
    ```

- Sort dictionary by keys

- - ```python
    y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    ```

- 步长：

- - ```python
    d = [x for x in range(10)]
    e = d[:8:2]
    ```

- 字符串格式化

- - ```python
    'Print {1} {0} {1}'.format("hello", "world") 
    
    'Print world hello world'
    ```

* 将字符转为列表

  * ```python
    sorted(str(123123))
    
    ['1', '1', '2', '2', '3', '3']
    ```

* 将**sorted和set**结合起来使用以得到一个**由序列中的唯一元素构成的有序列表**

  - ```python
    sorted(str(123123))
    
    ['1', '1', '2', '2', '3', '3']
    ```

* zip：**同时迭代多个序列**

  ```{python}
  seq1 = ['chao', 'qing', 'wq']
  seq2 = ['qin', 'wang', 'qc']
  for i , (a,b) in enumerate(zip(seq1, seq2)):
    print('%d: %s %s' % (i, a, b))
  
  0: chao qin
  1: qing wang
  2: wq qc
  ```

* 按逆序迭代序列中的元素

  * ```python
    [x for x in reversed([1, 2, 5, 3, -1])]
    
    [-1, 3, 5, 2, 1]
    ```

* Convert list to str

  ```python
  ' '.join([str(elem) for elem in s]) 
  ```

* 判断是否为回文

* ```python
  def test(input_text):
      if len(list(input_text)) <= 1:
          return True
      else:
          if list(input_text)[0] != list(input_text)[-1]:
              return False
          else:
              return test(' '.join([str(elem) for elem in list(['a', 's', 'd'])[1:-1]]))
  ```

* 逆序打印

* ```python
  def test(input_text):
      if input_text == []:
          return input_text
      else:
          return input_text[-1:] + test(input_text[:-1])
  ```

  