````markdown
# ☕ Java Learning Notes

This repository contains my personal notes and code snippets as I learn Java. It's a work in progress, and I'll be updating it regularly with new concepts and examples.

---

<details>
<summary>📚 Arrays</summary>

### 🧠 Arrays - Definition & Basics

Arrays in Java are fundamental data structures for storing collections of elements.

- An **array** is a container that holds a **fixed number of values of a single type**.
- Arrays are **0-indexed**, meaning the first element is at index `0`, the second at `1`, and so on.
- Once an array's size is declared, **it cannot be changed**. You can't add or remove elements once the array is created.

**Types of Arrays:**

- **1D Arrays:** A simple list of elements.
  ```java
  int[] arr = new int[5]; // Declares an array named 'arr' that can hold 5 integers
````

* **2D Arrays (Matrices):** Arrays of arrays, often used to represent tables or grids.

  ```java
  int[][] matrix = new int[3][3]; // A 3x3 matrix
  ```
* **Jagged Arrays (Ragged Arrays):** A special type of 2D array where inner arrays (rows) can have different lengths.

  ```java
  int[][] jagged = { {1, 2}, {3}, {4, 5, 6} }; // Each inner array has a different number of elements
  ```

> Arrays are stored in **contiguous memory locations**, which allows for very efficient **random access** using indices (e.g., `arr[2]`).

---

#### 🔧 `java.util.Arrays` Utility Methods

The `java.util.Arrays` class provides many useful static methods for array manipulation:

* `Arrays.toString(arr)`: Converts a **1D array** to a string representation (e.g., `[1, 2, 3]`).
* `Arrays.deepToString(matrix)`: Converts a **2D or multi-dimensional array** to a string representation (e.g., `[[1, 2], [3, 4]]`).
* `Arrays.sort(arr)`: **Sorts** the array elements in ascending order.
* `Arrays.equals(arr1, arr2)`: Checks if two arrays are **equal** (i.e., same elements in the same order).
* `Arrays.fill(arr, value)`: **Fills** all elements of an array with a specified `value`.

**Example Usage:**

```java
import java.util.Arrays; // Don't forget to import!

int[] arr = {5, 2, 3, 1};
Arrays.sort(arr); // arr is now {1, 2, 3, 5}
System.out.println(Arrays.toString(arr)); // Output: [1, 2, 3, 5]

int[] arr2 = {1, 2, 3, 5};
System.out.println(Arrays.equals(arr, arr2)); // Output: true

int[] numbers = new int[3];
Arrays.fill(numbers, 7);
System.out.println(Arrays.toString(numbers)); // Output: [7, 7, 7]
```

---

#### 📊 2D Array Input

Taking input for a 2D array typically involves nested loops:

```java
import java.util.Scanner; // Required for Scanner

Scanner sc = new Scanner(System.in);
int [][] arr = new int[3][3]; // A 3x3 array

System.out.println("Enter elements for the 3x3 array:");
// Outer loop for rows
for(int i = 0; i < arr.length; i++){ // arr.length gives the number of rows
    // Inner loop for columns
    for(int j = 0; j < arr[i].length; j++){ // arr[i].length gives the number of columns in the current row
        System.out.print("arr[" + i + "][" + j + "]: ");
        arr[i][j] = sc.nextInt();
    }
}
sc.close(); // Close the scanner after use to prevent resource leaks
```

* `arr.length` → number of rows.
* `arr[i].length` → number of columns in row `i` (useful for jagged arrays).

---

#### 🖨️ Ways to Print Multidimensional Arrays

Besides `Arrays.deepToString()`, you can also print 2D arrays using loops:

```java
// Assuming 'arr' is a populated 2D array from the input example

// Method 1: Using Arrays.deepToString() (easiest for debugging)
System.out.println("Using deepToString(): " + Arrays.deepToString(arr));

// Method 2: Iterating through rows and printing each row as a 1D array string
System.out.println("\nIterating row by row:");
for(int row = 0; row < arr.length; row++){
    System.out.println(Arrays.toString(arr[row])); // Prints each row as [element1, element2, ...]
}

// Method 3: Nested loops for individual elements (most control)
System.out.println("\nPrinting individual elements:");
for(int i = 0; i < arr.length; i++){
    for(int j = 0; j < arr[i].length; j++){
        System.out.print(arr[i][j] + " ");
    }
    System.out.println(); // New line after each row
}
```

---

#### 📐 Jagged Array Example

A **jagged array** (or ragged array) is an array of arrays where each sub-array can be of a different length.

```java
int[][] array = {
    {1, 2, 3},       // First row has 3 elements
    {4, 5},          // Second row has 2 elements
    {6, 7, 8, 9}     // Third row has 4 elements
};

System.out.println("Printing a jagged array using deepToString():");
System.out.println(Arrays.deepToString(array)); // Output: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

System.out.println("\nIterating and printing jagged array:");
for (int i = 0; i < array.length; i++) {
    for (int j = 0; j < array[i].length; j++) {
        System.out.print(array[i][j] + " ");
    }
    System.out.println(); // New line after each row
}
```

---

#### 🔁 Enhanced For Loop (For-Each Loop)

The enhanced for loop (for-each) provides a simpler way to iterate over arrays and collections:

```java
int[] numbers = {10, 20, 30, 40, 50};

System.out.println("Using enhanced for loop for a 1D array:");
for(int num : numbers){ // For each 'num' in 'numbers'
    System.out.print(num + " ");
}
System.out.println(); // Output: 10 20 30 40 50

// For 2D arrays:
int[][] matrix = {{1, 2}, {3, 4, 5}};

System.out.println("\nUsing enhanced for loop for a 2D array:");
for(int[] row : matrix){ // Each 'row' is a 1D array
    System.out.println(Arrays.toString(row));
}
/* Output:
[1, 2]
[3, 4, 5]
*/
```

---

#### 🆚 Array vs. `ArrayList`

Understanding the differences between `Array` and `ArrayList` is crucial:

| Feature          | `Array`                                                    | `ArrayList`                                                                    |
| ---------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Size**         | Fixed size; cannot be changed.                             | Dynamic size; can grow or shrink.                                              |
| **Data Type**    | Can hold **primitives** (e.g., `int`) and **objects**.     | Can only hold **objects** (use wrappers for primitives).                       |
| **Performance**  | Faster for direct element access due to contiguous memory. | Slightly slower for direct access due to object overhead and dynamic resizing. |
| **Manipulation** | Insertions/deletions require shifting elements manually.   | Built-in methods make insertions/deletions easier.                             |
| **Package**      | Part of basic Java language (`java.lang`).                 | Part of the **Java Collections Framework** (`java.util`).                      |

> **Key Takeaway:** Use `Array` when you know the exact size up front. Use `ArrayList` when you need a resizable collection.

---

#### 📋 `ArrayList` Basics

`ArrayList` is a dynamic array implementation in Java’s Collections Framework:

```java
import java.util.ArrayList;
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
ArrayList<Integer> list = new ArrayList<>(); // Creates an empty ArrayList of Integers

// 1. Adding elements
list.add(10);
list.add(20);
list.add(30);
list.add(40);
list.add(50);
System.out.println("Initial list: " + list); // Output: [10, 20, 30, 40, 50]

// 2. Checking if an element exists - contains()
System.out.println("Does list contain 30? " + list.contains(30));   // true
System.out.println("Does list contain 100? " + list.contains(100)); // false

// 3. Updating an element - set(index, value)
list.set(2, 100); // Replaces the element at index 2 (which was 30) with 100
System.out.println("List after set(2, 100): " + list); // [10, 20, 100, 40, 50]

// 4. Removing an element - remove(index)
list.remove(1); // Removes the element at index 1 (which was 20)
System.out.println("List after remove(1): " + list); // [10, 100, 40, 50]

// 5. Taking input into an ArrayList
System.out.println("Enter 3 integers to add to the list:");
for(int i = 0; i < 3; i++){
    list.add(sc.nextInt()); // Adds user input to the end of the list
}
System.out.println("List after adding user input: " + list);

// 6. Accessing elements - get(index)
System.out.println("Elements using get():");
for(int j = 0; j < list.size(); j++){ // list.size() gives the current number of elements
    System.out.println("Element at index " + j + ": " + list.get(j));
}
sc.close();
```

---

#### 🔢 Multi-dimensional `ArrayList` (ArrayList of ArrayLists)

You can create a "2D" `ArrayList` by having an `ArrayList` of `ArrayList`s:

```java
import java.util.ArrayList;
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
// Declare an ArrayList where each element will be an ArrayList of Integers
ArrayList<ArrayList<Integer>> listOfLists = new ArrayList<>();

// Initialize the inner ArrayLists. This is crucial!
// You need to add empty inner ArrayLists before adding elements to them.
for(int i = 0; i < 3; i++){
    listOfLists.add(new ArrayList<Integer>()); // Adds 3 empty inner ArrayLists
}

System.out.println("Enter elements for a 3x3 'matrix':");
for(int i = 0; i < 3; i++){
    for(int j = 0; j < 3; j++){
        System.out.print("Enter element for row " + i + ", col " + j + ": ");
        listOfLists.get(i).add(sc.nextInt());
    }
}
sc.close();
System.out.println("Your 2D ArrayList: " + listOfLists);
/* Example Output:
Enter element for row 0, col 0: 1
...
Your 2D ArrayList: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
*/
```

> **Important:** You **must** initialize each inner `ArrayList` by calling `new ArrayList<>()` before adding elements.

</details>

---

<details>
<summary>📜 Strings</summary>

### 📘 String vs. `StringBuilder` vs. `StringBuffer` (Definition)

In Java, there are three common ways to work with sequences of characters:

| Feature           | `String`                                                           | `StringBuilder`                                                       | `StringBuffer`                                                     |
| ----------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Mutability**    | **Immutable** (cannot be changed).                                 | **Mutable** (can be changed).                                         | **Mutable** (can be changed).                                      |
| **Thread-Safety** | N/A (immutable, so inherently safe).                               | **Not thread-safe**.                                                  | **Thread-safe** (synchronized).                                    |
| **Performance**   | Slower for repeated modifications (creates new objects each time). | **Faster** for single-threaded string modifications.                  | Slower than `StringBuilder` due to synchronization overhead.       |
| **Use Case**      | When string content is fixed or rarely changed.                    | When you need efficient string building in a single-threaded context. | When you need to build strings safely in a multi-threaded context. |

**Example:**

```java
// String (Immutable)
String immutableString = "Hello";
immutableString = immutableString + " World"; 
// Creates a NEW "Hello World" string object; original "Hello" stays unchanged.
System.out.println("Immutable String: " + immutableString); // Hello World

// StringBuilder (Mutable, faster, not thread-safe)
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World"); // Modifies the existing StringBuilder object
System.out.println("StringBuilder: " + sb); // Hello World

// StringBuffer (Mutable, thread-safe, but slower in single-threaded)
StringBuffer sbuf = new StringBuffer("Hello");
sbuf.append(" World"); // Modifies the existing StringBuffer object
System.out.println("StringBuffer: " + sbuf); // Hello World
```

---

### 📌 Introduction to Strings in Java

* A **String** is a sequence of characters.
* Strings in Java are **IMMUTABLE**: once a `String` object is created, its content cannot be changed. Any operation that seems to modify a `String` actually creates a **new `String` object**.
* All string literal values (e.g., `"hello"`) are stored in a special memory area called the **STRING POOL** (or String Constant Pool) to optimize memory usage.

**Example:**

```java
String name = "Utkarsh"; // "Utkarsh" is stored in the string pool
System.out.println(name); // Output: Utkarsh
```

---

### 🧠 String Pool and Immutability

Understanding `==` vs. `.equals()` for Strings is vital due to the string pool:

```java
// Example 1: String Literals (from String Pool)
String a = "utkarsh"; // "utkarsh" goes into the pool
String b = "utkarsh"; // 'b' reuses the same pooled "utkarsh" object

System.out.println(a == b);      // true  (same object reference)
System.out.println(a.equals(b)); // true  (same content)

// Example 2: Using 'new String()' (creates objects on the heap)
String c = new String("Utkarsh"); // New object in heap
String d = new String("Utkarsh"); // Another new object in heap

System.out.println(c == d);      // false (different objects)
System.out.println(c.equals(d)); // true  (same content)
```

* `==` compares **references** (memory addresses).
* `.equals()` compares the **actual content** of the strings.

---

### 🔤 String Methods Example - `charAt()`

`charAt(index)` returns the character at the specified index:

```java
String name = "Utkarsh";
// Indices: U(0) t(1) k(2) a(3) r(4) s(5) h(6)
System.out.println(name.charAt(0)); // Output: U
System.out.println(name.charAt(2)); // Output: k
// System.out.println(name.charAt(10)); // Throws StringIndexOutOfBoundsException if index is invalid
```

---

### 🧱 Wrapper Classes and `toString()`

**Wrapper classes** convert Java’s primitive types into objects (needed for many collections):

* `int` → `Integer`
* `char` → `Character`
* `boolean` → `Boolean`
* `float` → `Float`
* `double` → `Double`
* …and so on.

All wrapper classes have a `.toString()` method that converts their object value into a `String`.

```java
int num = 123;
Integer numObject = num;                   // Autoboxing: int → Integer
String numString = numObject.toString();    // Converts Integer to String
System.out.println(numString);              // Output: "123"

float pi = 3.14f;
String piString = String.valueOf(pi);       // Another way to get a String
System.out.println(piString);               // Output: "3.14"
```

---

### 🖨️ Pretty Printing using `printf`

`System.out.printf()` allows formatted output:

```java
float a = 453.1274f;
// %.2f: format as float with 2 decimal places
System.out.printf("Formatted number: %.2f\n", a); // Output: Formatted number: 453.13

System.out.printf("Pi: %.3f\n", Math.PI);         // Output: Pi: 3.142
System.out.printf("I'm %s and I'm %d years old\n", "Utkarsh", 21); 
// Output: I'm Utkarsh and I'm 21 years old

// Width and alignment:
System.out.printf("Left aligned: %-10sEnd\n", "Hello");  // "Hello     End"
System.out.printf("Right aligned: %10sEnd\n", "World");  // "     WorldEnd"
```

**Common Format Specifiers:**

* `%c` – character
* `%d` – decimal integer
* `%e` – scientific notation
* `%f` – floating-point number
* `%s` – string
* `%n` – newline (platform-independent)

---

### ➕ String Operations & Concatenation

Java handles string concatenation in a specific way, especially when mixing data types:

```java
// Character arithmetic: adds ASCII values
System.out.println('a' + 'b');       // Output: 195 (97 + 98)

// String concatenation: joins strings
System.out.println("a" + "b");       // Output: ab

// Character + integer: converts char to ASCII value, then adds
System.out.println('a' + 3);         // Output: 100
System.out.println((char)('a' + 3)); // Output: d

// String + any type: non-string operand is converted via toString(), then concatenated
System.out.println("a" + 1);         // Output: a1
System.out.println("utkarsh" + new ArrayList<>()); // Output: utkarsh[]

// Complex concatenation:
String ans = 56 + "" + new ArrayList<>();
System.out.println(ans); // Output: 56[]
```

> **Rule of Thumb:** If any operand in a `+` expression is a `String`, the entire expression is evaluated left to right as string concatenation.

---

### 🔁 Loop to Print Alphabets (Inefficient `String` Concatenation)

Using `+` in a loop for many concatenations is inefficient because each iteration creates a new `String`:

```java
String alphabet = ""; // Starts empty
for(int i = 0; i < 26; i++){
    char ch = (char)('a' + i);
    alphabet = alphabet + ch; // ❌ Inefficient: creates a new String each iteration
}
System.out.println(alphabet); // Output: abcdefghijklmnopqrstuvwxyz

// Creates 26 intermediate String objects, which is wasteful.
```

---

### 📦 `StringBuilder` – Efficient String Operations

For repeated string modifications in a single-threaded context, use `StringBuilder`:

```java
StringBuilder series = new StringBuilder(); // Create one StringBuilder

for(int i = 0; i < 26; i++){
    series.append((char)('a' + i)); // Appends to the existing object
}
System.out.println(series); // Output: abcdefghijklmnopqrstuvwxyz

// Convert back to String if needed:
String finalResult = series.toString();
System.out.println("Final String: " + finalResult);
```

> **Benefits:** `StringBuilder` is **mutable**, so it avoids creating many temporary `String` objects, making it much faster for loops.

---

### 🧰 Useful String Methods

Java’s `String` class provides many built-in methods:

```java
import java.util.Arrays; // Required for Arrays.toString()

String name = "  Utkarsh KANwal  ";
String phrase = "hello world java";
String numbers = "abc123";
String commaSeparated = "one,two,three,four";

// 1. toCharArray(): Converts string to a character array
System.out.println("toCharArray(): " + Arrays.toString(name.toCharArray()));
// Output: [ ,  , U, t, k, a, r, s, h,  , K, A, N, w, a, l,  ,  ]

// 2. getBytes(): Converts string to a byte array (default encoding, e.g., UTF-8)
System.out.println("getBytes(): " + Arrays.toString(name.getBytes()));

// 3. toLowerCase() & toUpperCase(): Change case
System.out.println("toLowerCase(): " + name.toLowerCase()); // "  utkarsh kanwal  "
System.out.println("toUpperCase(): " + name.toUpperCase()); // "  UTKARSH KANWAL  "

// 4. indexOf(char) / indexOf(String): Find occurrences
System.out.println("indexOf('t'): " + name.indexOf('t'));       // e.g. 3
System.out.println("indexOf(\"KAN\"): " + name.indexOf("KAN")); // e.g. 11

// 5. trim() / strip(): Remove whitespace
String spaced = "   hello   \n\t";
System.out.println("Original: '" + spaced + "'");
System.out.println("After trim(): '" + spaced.trim() + "'");   // 'hello'
System.out.println("After strip(): '" + spaced.strip() + "'"); // 'hello'

// 6. compareTo(String): Lexicographic comparison
System.out.println("\"apple\".compareTo(\"banana\"): " + "apple".compareTo("banana")); // negative
System.out.println("\"banana\".compareTo(\"apple\"): " + "banana".compareTo("apple")); // positive
System.out.println("\"hello\".compareTo(\"hello\"): " + "hello".compareTo("hello"));   // zero

// 7. substring(start, end): Extract a portion (end is exclusive)
System.out.println("\"hello\".substring(1, 4): " + "hello".substring(1, 4)); // "ell"
System.out.println("\"hello\".substring(2): " + "hello".substring(2));       // "llo"

// 8. replace(oldChar, newChar) / replace(oldStr, newStr)
System.out.println("\"apple\".replace('p', 'b'): " + "apple".replace('p', 'b'));         // "abble"
System.out.println("\"hello world\".replace(\"world\", \"java\"): " + "hello world".replace("world", "java")); // "hello java"

// 9. contains(String): Check for substring
System.out.println("\"hello world\".contains(\"world\"): " + "hello world".contains("world")); // true
System.out.println("\"hello world\".contains(\"mars\"): " + "hello world".contains("mars"));   // false

// 10. split(delimiter): Split by delimiter into an array
String[] parts = commaSeparated.split(",");
System.out.println("Split by comma: " + Arrays.toString(parts)); // [one, two, three, four]

// 11. matches(regex): Check if matches a regular expression
System.out.println("\"abc123\".matches(\"[a-z]+\\\\d+\"): " + numbers.matches("[a-z]+\\d+")); // true
System.out.println("\"123abc\".matches(\"[a-z]+\\\\d+\"): " + "123abc".matches("[a-z]+\\d+")); // false
```

</details>
```
