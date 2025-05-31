
````markdown
# ☕ Java Learning Notes

This repository contains my personal notes and code snippets as I learn Java. It's a work in progress, and I'll be updating it regularly with new concepts and examples.

---

<details>
<summary>📚 <strong>Arrays</strong></summary>

### 🧠 Arrays - Definition & Basics

Arrays in Java are fundamental data structures for storing collections of elements.

- An **array** is a container that holds a **fixed number of values of a single type**.
- Arrays are **0-indexed**.
- Once created, **you cannot change the size** of an array.

#### ✅ Types of Arrays

- **1D Arrays:**
  ```java
  int[] arr = new int[5];
  ```

- **2D Arrays (Matrices):**
  ```java
  int[][] matrix = new int[3][3];
  ```

- **Jagged Arrays:**
  ```java
  int[][] jagged = { {1, 2}, {3}, {4, 5, 6} };
  ```

> Arrays use **contiguous memory**, allowing fast access with indices.

---

### 🔧 `java.util.Arrays` Utility Methods

The `Arrays` class provides helpful methods for array manipulation:

```java
import java.util.Arrays;

int[] arr = {5, 2, 3, 1};
Arrays.sort(arr);
System.out.println(Arrays.toString(arr)); // [1, 2, 3, 5]

int[] arr2 = {1, 2, 3, 5};
System.out.println(Arrays.equals(arr, arr2)); // true

int[] numbers = new int[3];
Arrays.fill(numbers, 7);
System.out.println(Arrays.toString(numbers)); // [7, 7, 7]
```

#### Common Methods

- `Arrays.toString(arr)`
- `Arrays.deepToString(matrix)`
- `Arrays.sort(arr)`
- `Arrays.equals(arr1, arr2)`
- `Arrays.fill(arr, value)`

---

### 📊 2D Array Input (Scanner)

```java
Scanner sc = new Scanner(System.in);
int[][] arr = new int[3][3];

for (int i = 0; i < arr.length; i++) {
    for (int j = 0; j < arr[i].length; j++) {
        arr[i][j] = sc.nextInt();
    }
}
sc.close();
```

---

### 🖨️ Printing 2D Arrays

```java
System.out.println(Arrays.deepToString(arr));

for (int[] row : arr) {
    System.out.println(Arrays.toString(row));
}

for (int i = 0; i < arr.length; i++) {
    for (int j = 0; j < arr[i].length; j++) {
        System.out.print(arr[i][j] + " ");
    }
    System.out.println();
}
```

---

### 📐 Jagged Array Example

```java
int[][] jagged = {
    {1, 2, 3},
    {4, 5},
    {6, 7, 8, 9}
};

System.out.println(Arrays.deepToString(jagged));

for (int[] row : jagged) {
    for (int val : row) {
        System.out.print(val + " ");
    }
    System.out.println();
}
```

---

### 🔁 Enhanced For Loop (For-Each)

```java
int[] numbers = {10, 20, 30};

for (int num : numbers) {
    System.out.print(num + " ");
}

int[][] matrix = {{1, 2}, {3, 4, 5}};
for (int[] row : matrix) {
    System.out.println(Arrays.toString(row));
}
```

---

### 🆚 Array vs. ArrayList

| Feature        | Array                            | ArrayList                              |
|----------------|----------------------------------|-----------------------------------------|
| Size           | Fixed                            | Dynamic                                 |
| Data Types     | Primitives and Objects           | Objects only (use wrapper classes)      |
| Performance    | Faster (contiguous memory)       | Slower (dynamic resizing)               |
| Manipulation   | Manual                           | Easier with built-in methods            |
| Package        | `java.lang`                      | `java.util` (Collections Framework)     |

</details>

---

<details>
<summary>📋 <strong>ArrayList</strong></summary>

### 🔰 Basics

```java
ArrayList<Integer> list = new ArrayList<>();

list.add(10);
list.set(0, 100);
list.remove(0);
list.contains(50);
list.get(0);
```

### 🧾 Full Example

```java
Scanner sc = new Scanner(System.in);
ArrayList<Integer> list = new ArrayList<>();

list.add(10); list.add(20); list.add(30);
System.out.println(list); // [10, 20, 30]

System.out.println(list.contains(20)); // true

list.set(1, 99);
list.remove(0);

for (int i = 0; i < 3; i++) {
    list.add(sc.nextInt());
}
System.out.println(list);
sc.close();
```

---

### 🔢 2D ArrayList (ArrayList of ArrayLists)

```java
ArrayList<ArrayList<Integer>> list = new ArrayList<>();

for (int i = 0; i < 3; i++) {
    list.add(new ArrayList<>());
}

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        list.get(i).add(sc.nextInt());
    }
}
```

> You must **initialize inner lists** before adding elements.

</details>

---

<details>
<summary>📜 <strong>Strings</strong></summary>

### 📘 String vs. StringBuilder vs. StringBuffer

| Feature        | String         | StringBuilder     | StringBuffer        |
|----------------|----------------|-------------------|---------------------|
| Mutability     | Immutable      | Mutable           | Mutable             |
| Thread-Safety  | Safe (by immutability) | Not Thread-Safe | Thread-Safe (synchronized) |
| Performance    | Slow for edits | Fast              | Slower (sync overhead) |

---

### 📌 String Pool and `.equals()` vs `==`

```java
String a = "utkarsh";
String b = "utkarsh";
System.out.println(a == b);       // true
System.out.println(a.equals(b));  // true

String c = new String("utkarsh");
String d = new String("utkarsh");
System.out.println(c == d);       // false
System.out.println(c.equals(d));  // true
```

---

### 🔤 `charAt()` Example

```java
String name = "Utkarsh";
System.out.println(name.charAt(0)); // U
```

---

### 🧱 Wrapper Classes

```java
int num = 123;
Integer boxed = num;
String str = boxed.toString();

float pi = 3.14f;
String s = String.valueOf(pi);
```

---

### 🖨️ Pretty Printing with `printf`

```java
System.out.printf("Pi: %.2f\n", Math.PI);
System.out.printf("Name: %-10s Age: %d\n", "Utkarsh", 21);
```

| Format | Meaning                    |
|--------|----------------------------|
| `%d`   | Integer                    |
| `%f`   | Float                      |
| `%s`   | String                     |
| `%n`   | Newline (platform-safe)    |

---

### ➕ String Concatenation & Arithmetic

```java
System.out.println('a' + 'b');          // 195
System.out.println("a" + "b");          // ab
System.out.println("a" + 1);            // a1
System.out.println((char)('a' + 3));    // d
System.out.println("utkarsh" + new ArrayList<>()); // utkarsh[]
```

</details>
````

---
