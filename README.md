# ☕ Java Learning Notes

This repository contains my personal notes and code snippets as I learn Java. It's a work in progress, and I'll be updating it regularly with new concepts and examples.

-----

<details>
<summary>📚 Arrays </summary>

### 🧠 Arrays - Definition & Basics

Arrays in Java are fundamental data structures for storing collections of elements.

  * An **array** is a container that holds a **fixed number of values of a single type**.
  * Arrays are **0-indexed**, meaning the first element is at index `0`, the second at `1`, and so on.
  * Once an array's size is declared, **it cannot be changed**. You can't add or remove elements once the array is created.

**Types of Arrays:**

  * **1D Arrays:** A simple list of elements.
    ```java
    int[] arr = new int[5]; // Declares an array named 'arr' that can hold 5 integers
    ```
  * **2D Arrays (Matrices):** Arrays of arrays, often used to represent tables or grids.
    ```java
    int[][] matrix = new int[3][3]; // A 3x3 matrix
    ```
  * **Jagged Arrays (Ragged Arrays):** A special type of 2D array where inner arrays (rows) can have different lengths.
    ```java
    int[][] jagged = { {1, 2}, {3}, {4, 5, 6} }; // Each inner array has a different number of elements
    ```

> Arrays are stored in **contiguous memory locations**, which allows for very efficient **random access** using indices (e.g., `arr[2]`).

-----

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

-----

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

-----

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

-----

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

-----

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

-----

#### 🆚 Array vs. `ArrayList`

Understanding the differences between `Array` and `ArrayList` is crucial:

| Feature      | `Array`                                                    | `ArrayList`                                                                  |
| :----------- | :--------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Size** | Fixed size; cannot be changed.                             | Dynamic size; can grow or shrink.                                            |
| **Data Type**| Can hold **primitives** (e.g., `int`) and **objects**.     | Can only hold **objects** (use wrappers for primitives).                     |
| **Performance**| Faster for direct element access due to contiguous memory. | Slightly slower for direct access due to object overhead and dynamic resizing.|
| **Manipulation**| Insertions/deletions require shifting elements manually. | Built-in methods make insertions/deletions easier.                           |
| **Package** | Part of basic Java language (`java.lang`).                 | Part of the **Java Collections Framework** (`java.util`).                    |

> **Key Takeaway:** Use `Array` when you know the exact size up front. Use `ArrayList` when you need a resizable collection.

-----

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
System.out.println("Does list contain 30? " + list.contains(30));    // true
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

-----

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

🔧 What Happens When ArrayList Is Full?
When an ArrayList is full (i.e., it reaches its current capacity), and you add one more element using .add(), Java does the following automatically:

✅ Under the Hood:
Creates a new array with a larger capacity (usually 1.5x or 2x the old size).

Copies all elements from the old array into the new one.

Adds the new element to the new array.

The internal elementData reference now points to the new array.

This resizing happens behind the scenes, and you don't have to do anything manually.



> **Important:** You **must** initialize each inner `ArrayList` by calling `new ArrayList<>()` before adding elements.

</details>

-----

<details>
<summary>📜 Strings</summary>

### 📘 String vs. `StringBuilder` vs. `StringBuffer` (Definition)

In Java, there are three common ways to work with sequences of characters:

| Feature         | `String`                                                                  | `StringBuilder`                                                             | `StringBuffer`                                                            |
| :-------------- | :------------------------------------------------------------------------ | :-------------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| **Mutability** | **Immutable** (cannot be changed).                                        | **Mutable** (can be changed).                                               | **Mutable** (can be changed).                                             |
| **Thread-Safety** | N/A (immutable, so inherently safe).                                      | **Not thread-safe**.                                                        | **Thread-safe** (synchronized).                                           |
| **Performance** | Slower for repeated modifications (creates new objects each time).        | **Faster** for single-threaded string modifications.                        | Slower than `StringBuilder` due to synchronization overhead.              |
| **Use Case** | When string content is fixed or rarely changed.                           | When you need efficient string building in a single-threaded context.       | When you need to build strings safely in a multi-threaded context.        |

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

-----

### 📌 Introduction to Strings in Java

  * A **String** is a sequence of characters.
  * Strings in Java are **IMMUTABLE**: once a `String` object is created, its content cannot be changed. Any operation that seems to modify a `String` actually creates a **new `String` object**.
  * All string literal values (e.g., `"hello"`) are stored in a special memory area called the **STRING POOL** (or String Constant Pool) to optimize memory usage.

**Example:**

```java
String name = "Utkarsh"; // "Utkarsh" is stored in the string pool
System.out.println(name); // Output: Utkarsh
```

-----

### 🧠 String Pool and Immutability

Understanding `==` vs. `.equals()` for Strings is vital due to the string pool:

```java
// Example 1: String Literals (from String Pool)
String a = "utkarsh"; // "utkarsh" goes into the pool
String b = "utkarsh"; // 'b' reuses the same pooled "utkarsh" object

System.out.println(a == b);       // true  (same object reference)
System.out.println(a.equals(b)); // true  (same content)

// Example 2: Using 'new String()' (creates objects on the heap)
String c = new String("Utkarsh"); // New object in heap
String d = new String("Utkarsh"); // Another new object in heap

System.out.println(c == d);       // false (different objects)
System.out.println(c.equals(d)); // true  (same content)
```

  * `==` compares **references** (memory addresses).
  * `.equals()` compares the **actual content** of the strings.

-----

### 🔤 String Methods Example - `charAt()`

`charAt(index)` returns the character at the specified index:

```java
String name = "Utkarsh";
// Indices: U(0) t(1) k(2) a(3) r(4) s(5) h(6)
System.out.println(name.charAt(0)); // Output: U
System.out.println(name.charAt(2)); // Output: k
// System.out.println(name.charAt(10)); // Throws StringIndexOutOfBoundsException if index is invalid
```

-----

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
Integer numObject = num;             // Autoboxing: int → Integer
String numString = numObject.toString();   // Converts Integer to String
System.out.println(numString);             // Output: "123"

float pi = 3.14f;
String piString = String.valueOf(pi);      // Another way to get a String
System.out.println(piString);              // Output: "3.14"
```

-----

### 🖨️ Pretty Printing using `printf`

`System.out.printf()` allows formatted output:

```java
float a = 453.1274f;
// %.2f: format as float with 2 decimal places
System.out.printf("Formatted number: %.2f\n", a); // Output: Formatted number: 453.13

System.out.printf("Pi: %.3f\n", Math.PI);          // Output: Pi: 3.142
System.out.printf("I'm %s and I'm %d years old\n", "Utkarsh", 21);
// Output: I'm Utkarsh and I'm 21 years old

// Width and alignment:
System.out.printf("Left aligned: %-10sEnd\n", "Hello");   // "Hello      End"
System.out.printf("Right aligned: %10sEnd\n", "World");  // "     WorldEnd"
```

**Common Format Specifiers:**

  * `%c` – character
  * `%d` – decimal integer
  * `%e` – scientific notation
  * `%f` – floating-point number
  * `%s` – string
  * `%n` – newline (platform-independent)

-----

### ➕ String Operations & Concatenation

Java handles string concatenation in a specific way, especially when mixing data types:

```java
// Character arithmetic: adds ASCII values
System.out.println('a' + 'b');        // Output: 195 (97 + 98)

// String concatenation: joins strings
System.out.println("a" + "b");        // Output: ab

// Character + integer: converts char to ASCII value, then adds
System.out.println('a' + 3);          // Output: 100
System.out.println((char)('a' + 3)); // Output: d

// String + any type: non-string operand is converted via toString(), then concatenated
System.out.println("a" + 1);          // Output: a1
System.out.println("utkarsh" + new ArrayList<>()); // Output: utkarsh[]

// Complex concatenation:
String ans = 56 + "" + new ArrayList<>();
System.out.println(ans); // Output: 56[]
```

> **Rule of Thumb:** If any operand in a `+` expression is a `String`, the entire expression is evaluated left to right as string concatenation.

-----

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

-----

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

-----

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
System.out.println("indexOf('t'): " + name.indexOf('t'));        // e.g. 3
System.out.println("indexOf(\"KAN\"): " + name.indexOf("KAN")); // e.g. 11

// 5. trim() / strip(): Remove whitespace
String spaced = "    hello    \n\t";
System.out.println("Original: '" + spaced + "'");
System.out.println("After trim(): '" + spaced.trim() + "'");    // 'hello'
System.out.println("After strip(): '" + spaced.strip() + "'"); // 'hello'

// 6. compareTo(String): Lexicographic comparison
System.out.println("\"apple\".compareTo(\"banana\"): " + "apple".compareTo("banana")); // negative
System.out.println("\"banana\".compareTo(\"apple\"): " + "banana".compareTo("apple")); // positive
System.out.println("\"hello\".compareTo(\"hello\"): " + "hello".compareTo("hello"));    // zero

// 7. substring(start, end): Extract a portion (end is exclusive)
System.out.println("\"hello\".substring(1, 4): " + "hello".substring(1, 4)); // "ell"
System.out.println("\"hello\".substring(2): " + "hello".substring(2));        // "llo"

// 8. replace(oldChar, newChar) / replace(oldStr, newStr)
System.out.println("\"apple\".replace('p', 'b'): " + "apple".replace('p', 'b'));            // "abble"
System.out.println("\"hello world\".replace(\"world\", \"java\"): " + "hello world".replace("world", "java")); // "hello java"

// 9. contains(String): Check for substring
System.out.println("\"hello world\".contains(\"world\"): " + "hello world".contains("world")); // true
System.out.println("\"hello world\".contains(\"mars\"): " + "hello world".contains("mars"));    // false

// 10. split(delimiter): Split by delimiter into an array
String[] parts = commaSeparated.split(",");
System.out.println("Split by comma: " + Arrays.toString(parts)); // [one, two, three, four]

// 11. matches(regex): Check if matches a regular expression
System.out.println("\"abc123\".matches(\"[a-z]+\\\\d+\"): " + numbers.matches("[a-z]+\\d+")); // true
System.out.println("\"123abc\".matches(\"[a-z]+\\\\d+\"): " + "123abc".matches("[a-z]+\\d+")); // false
```

</details>

-----

<details>
<summary>
 🔗 Linked Lists
</summary>

-----

## 1\. Singly Linked List ➡️

A singly linked list is a linear data structure where each element (called a node) points to the next node in the sequence. It maintains a `head` (first node) and a `tail` (last node) for efficient operations at both ends.

### Core Concepts 💡

  \* **Node:** The fundamental building block of a linked list. Each node typically contains:
      \* `value`: The data stored in the node.
      \* `next`: A reference (or pointer) to the next node in the sequence. The last node's `next` reference is `null`.
  \* **Head:** A reference to the first node of the list.
  \* **Tail:** A reference to the last node of the list.
  \* **Size:** An integer tracking the number of nodes in the list.

### `LinkedList.java` Implementation 💻

```java
package learningJava;

class LinkedList {
    private Node head;
    private Node tail;
    private int size;

    // Node class definition (private inner class)
    class Node {
        private int value; // Data stored in the node
        private Node next; // Reference to the next node

        // Constructor for a node with only value
        public Node(int val) {
            this.value = val;
        }

        // Constructor for a node with value and next node reference
        public Node(int val, Node next) {
            this.value = val;
            this.next = next;
        }
    }

    // Constructor for LinkedList
    public LinkedList() {
        this.size = 0; // Initialize size to 0 for an empty list
    }

    /**
     * Returns the current size of the linked list.
     * Time Complexity: O(1)
     */
    public int getSize() {
        return size;
    }

    /**
     * Inserts a new node with the given value at the beginning of the list.
     *
     * Steps:
     * 1. Create a new Node with the provided value.
     * 2. Set the `next` of the new node to the current `head`.
     * 3. Update the `head` to point to the new node.
     * 4. If the list was empty (tail was null), set `tail` to `head`.
     * 5. Increment the `size`.
     *
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     */
    public void insertFirst(int val) {
        Node node = new Node(val); // Create new node
        node.next = head;          // New node's next points to old head
        head = node;               // Head now points to the new node

        if (tail == null) { // If list was empty, new node is also the tail
            tail = head;
        }
        size += 1; // Increment size
    }

    /**
     * Inserts a new node with the given value at the end of the list.
     *
     * Steps:
     * 1. If the list is empty, call `insertFirst` to handle it.
     * 2. Create a new Node with the provided value.
     * 3. Set the `next` of the current `tail` to the new node.
     * 4. Update the `tail` to point to the new node.
     * 5. Increment the `size`.
     *
     * Time Complexity: O(1) (because we have a tail pointer)
     * Space Complexity: O(1)
     */
    public void insertLast(int val) {
        if (tail == null) { // If the list is empty, inserting last is same as inserting first
            insertFirst(val);
            return;
        }
        Node node = new Node(val); // Create new node
        tail.next = node;          // Current tail's next points to new node
        tail = node;               // Tail now points to the new node
        size++;                    // Increment size
    }

    /**
     * Inserts a new node with the given value at a specific index.
     *
     * Steps:
     * 1. Handle edge cases: if index is 0, call `insertFirst`; if index is `size`, call `insertLast`.
     * 2. Traverse to the node *before* the target index.
     * 3. Create a new Node, linking its `next` to the node that was originally at the target index.
     * 4. Update the `next` of the previous node to point to the new node.
     * 5. Increment the `size`.
     *
     * Time Complexity: O(index) in the worst case (O(N) for insertion near end).
     * Space Complexity: O(1)
     */
    public void insert(int val, int index) {
        if (index == 0) { // Inserting at the beginning
            insertFirst(val);
            return;
        }
        if (index == size) { // Inserting at the end
            insertLast(val);
            return;
        }
        if (index < 0 || index > size) { // Invalid index check
            System.err.println("Error: Index out of bounds for insertion.");
            return;
        }

        Node temp = head; // Start from head
        // Traverse to the node *before* the insertion point
        for (int i = 1; i < index; i++) {
            temp = temp.next;
        }

        // Create new node, its next points to what temp.next was
        Node node = new Node(val, temp.next);
        temp.next = node; // temp's next now points to the new node
        size++;            // Increment size
    }

    /**
     * Public wrapper method for recursive insertion.
     * Initiates the recursive process by calling the private helper method with the current head.
     * Time Complexity: O(index)
     * Space Complexity: O(index) due to recursion stack
     */
    public void insertRec(int val, int index) {
        // The head might change during recursive insertion at index 0,
        // so we update the head with the result of the recursive call.
        head = insertRec(val, index, head);
    }

    /**
     * Private recursive helper method to insert a node at a given index.
     *
     * Base Case:
     * If `index` is 0, it means we've reached the position to insert. Create a new node,
     * link its `next` to the current `node` (which will be the node originally at `index`),
     * increment size, and return the new node.
     *
     * Recursive Step:
     * Recursively call `insertRec` for the `node.next` with `index-1`.
     * The result of this recursive call (the modified sub-list starting from `node.next`)
     * is assigned back to `node.next`. This effectively links the current node
     * to the rest of the list after the insertion.
     *
     * @param val The value to insert.
     * @param index The target index for insertion.
     * @param node The current node being processed in the recursion.
     * @return The head of the (potentially modified) sub-list.
     */
    private Node insertRec(int val, int index, Node node) {
        if (index == 0) { // Base case: reached the insertion point
            Node temp = new Node(val, node); // Create new node, linking it to the current node
            size++; // Increment size
            return temp; // Return the new node as the head of this sub-list
        }

        // Recursive step: go to the next node, decrementing the index
        node.next = insertRec(val, index - 1, node.next);
        return node; // Return the current node (its 'next' might have been updated)
    }

    /**
     * Deletes the first node in the list.
     *
     * Steps:
     * 1. Store the value of the `head` node.
     * 2. Update `head` to point to `head.next`.
     * 3. If the list becomes empty after deletion, update `tail` to `null`.
     * 4. Decrement the `size`.
     * 5. Return the deleted value.
     *
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     */
    public int deleteFirst() {
        if (head == null) {
            throw new IllegalStateException("Cannot delete from an empty list.");
        }
        int val = head.value; // Store value of node to be deleted
        head = head.next;      // Move head to the next node
        if (head == null) {    // If list becomes empty, tail should also be null
            tail = null;
        }
        size--;                // Decrement size
        return val;            // Return deleted value
    }

    /**
     * Helper method to get the node at a specific index.
     * Used internally for deletion operations.
     *
     * Steps:
     * 1. Start from the `head`.
     * 2. Traverse `index` times, moving `node` to `node.next` in each step.
     * 3. Return the node at the specified index.
     *
     * Time Complexity: O(index)
     * Space Complexity: O(1)
     */
    public Node getNode(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds.");
        }
        Node node = head; // Start from head
        for (int i = 0; i < index; i++) { // Traverse to the desired index
            node = node.next;
        }
        return node; // Return the node
    }

    /**
     * Deletes the last node in the list.
     *
     * Steps:
     * 1. Handle edge case: if size is 0 or 1, call `deleteFirst`.
     * 2. Get the second-to-last node using `getNode(size-2)`.
     * 3. Store the value of the current `tail`.
     * 4. Update `tail` to the `secondLast` node.
     * 5. Set `tail.next` to `null` to detach the old last node.
     * 6. Decrement `size`.
     * 7. Return the deleted value.
     *
     * Time Complexity: O(N) because `getNode(size-2)` requires traversal.
     * Space Complexity: O(1)
     */
    public int deletelast() {
        if (size <= 1) { // If 0 or 1 element, delete first handles it
            return deleteFirst();
        }

        Node secondLast = getNode(size - 2); // Get the node before the current tail
        int val = tail.value;                 // Store value of tail
        tail = secondLast;                    // Update tail to secondLast
        tail.next = null;                     // Detach the old last node
        size--;                               // Decrement size
        return val;                           // Return deleted value
    }

    /**
     * Deletes the node at a specific index.
     *
     * Steps:
     * 1. Handle edge cases: if index is 0, call `deleteFirst`; if index is `size-1`, call `deleteLast`.
     * 2. Get the node *before* the target index using `getNode(index-1)`.
     * 3. Store the value of the node to be deleted (`node.next.value`).
     * 4. Update `node.next` to skip the target node (`node.next.next`), effectively removing it.
     * 5. Decrement `size`.
     * 6. Return the deleted value.
     *
     * Time Complexity: O(index) in the worst case (O(N) for deletion near end).
     * Space Complexity: O(1)
     */
    public int delete(int index) {
        if (index == 0) { // Delete first node
            return deleteFirst();
        }
        if (index == size - 1) { // Delete last node
            return deletelast();
        }
        if (index < 0 || index >= size) { // Invalid index check
            throw new IndexOutOfBoundsException("Index out of bounds for deletion.");
        }

        Node prevNode = getNode(index - 1); // Get the node just before the one to be deleted
        int val = prevNode.next.value;       // Store the value of the node to be deleted
        prevNode.next = prevNode.next.next;  // Bypass the node to be deleted
        size--;                              // Decrement size
        return val;                          // Return deleted value
    }

    /**
     * Finds and returns the Node object containing the specified value.
     *
     * Steps:
     * 1. Start traversal from the `head`.
     * 2. Iterate through the list until the end (`temp != null`).
     * 3. If the `value` of the current node matches the target `value`, return the node.
     * 4. If the end of the list is reached without finding the value, return `null`.
     *
     * Time Complexity: O(N) in the worst case (value not found or at the end).
     * Space Complexity: O(1)
     */
    public Node find(int value) {
        Node temp = head; // Start from head
        while (temp != null) { // Iterate until end of list
            if (temp.value == value) { // Check if current node's value matches
                return temp; // Return the node if found
            }
            temp = temp.next; // Move to the next node
        }
        return null; // Value not found
    }

    /**
     * Displays all elements of the linked list in sequence.
     *
     * Steps:
     * 1. Start traversal from the `head`.
     * 2. Print the value of the current node and " -> ".
     * 3. Move to the next node until `temp` becomes `null`.
     * 4. Print "end" to signify the end of the list.
     *
     * Time Complexity: O(N) (iterates through all N nodes).
     * Space Complexity: O(1)
     */
    public void display() {
        Node temp = head; // Start from head
        while (temp != null) { // Iterate until end of list
            System.out.print(temp.value + " -> ");
            temp = temp.next; // Move to next node
        }
        System.out.println("end"); // Mark the end of the list
    }
}
```

### `LL.java` (Main Driver for Singly Linked List) 🚀

```java
package learningJava;

public class LL {

    public static void main(String[] args) {

        // Notes on Singly Linked Lists:
        // - Non-contiguous memory allocation: Nodes can be anywhere in memory.
        // - Singly linked: Each node points only to the next one.
        // - Uses 'head' and 'tail' pointers for efficient start/end operations.
        // - Structure: (head)a -> b -> c -> d(tail) -> null
        // - Cannot directly access an element by index (requires traversal from head).

        LinkedList list = new LinkedList();

        // Demonstrating insertFirst
        list.insertFirst(3); // List: 3 -> end
        list.insertFirst(4); // List: 4 -> 3 -> end
        list.insertFirst(5); // List: 5 -> 4 -> 3 -> end

        // Demonstrating insertLast
        list.insertLast(2);  // List: 5 -> 4 -> 3 -> 2 -> end
        list.insertLast(1);  // List: 5 -> 4 -> 3 -> 2 -> 1 -> end

        System.out.print("Initial list: ");
        list.display(); // Expected: 5 -> 4 -> 3 -> 2 -> 1 -> end
        System.out.println("Size: " + list.getSize()); // Expected: 5

        // Demonstrating insert at specific index
        System.out.print("Insert 99 at index 3: ");
        list.insert(99, 3); // List: 5 -> 4 -> 3 -> 99 -> 2 -> 1 -> end
        list.display();
        System.out.println("Size: " + list.getSize()); // Expected: 6

        // Demonstrating deleteFirst
        System.out.print("Delete first: ");
        int deletedVal1 = list.deleteFirst(); // Deletes 5. List: 4 -> 3 -> 99 -> 2 -> 1 -> end
        System.out.println("Deleted value: " + deletedVal1);
        list.display();
        System.out.println("Size: " + list.getSize()); // Expected: 5

        // Demonstrating deleteLast
        System.out.print("Delete last: ");
        int deletedVal2 = list.deletelast(); // Deletes 1. List: 4 -> 3 -> 99 -> 2 -> end
        System.out.println("Deleted value: " + deletedVal2);
        list.display();
        System.out.println("Size: " + list.getSize()); // Expected: 4

        // Demonstrating delete at specific index
        System.out.print("Delete at index 2 (value 99): ");
        int deletedVal3 = list.delete(2); // Deletes 99. List: 4 -> 3 -> 2 -> end
        System.out.println("Deleted value: " + deletedVal3);
        list.display();
        System.out.println("Size: " + list.getSize()); // Expected: 3

        // Demonstrating recursive insert
        System.out.print("List before recursive insert: ");
        list.display();
        System.out.print("Insert 999 at index 1 recursively: ");
        list.insertRec(999, 1); // List: 4 -> 999 -> 3 -> 2 -> end
        list.display();
        System.out.println("Size: " + list.getSize()); // Expected: 4

        // Demonstrating find
        System.out.print("Find node with value 999: ");
        LinkedList.Node foundNode = list.find(999);
        if (foundNode != null) {
            System.out.println("Found node with value: " + foundNode.value);
        } else {
            System.out.println("Node not found.");
        }

        System.out.print("Find node with value 1000: ");
        foundNode = list.find(1000);
        if (foundNode != null) {
            System.out.println("Found node with value: " + foundNode.value);
        } else {
            System.out.println("Node not found.");
        }
    }
}
```

### Time and Space Complexity Summary (Singly Linked List) ⏱️

| Operation        | Average Time Complexity | Worst Case Time Complexity | Space Complexity | Notes                                        |
| :--------------- | :---------------------- | :------------------------- | :--------------- | :------------------------------------------- |
| `insertFirst`    | O(1)                    | O(1)                       | O(1)             | Requires updating `head` and potentially `tail` |
| `insertLast`     | O(1)                    | O(1)                       | O(1)             | Requires `tail` pointer                      |
| `insert(val, idx)` | O(idx)                  | O(N)                       | O(1)             | Traversal to `idx-1`                         |
| `insertRec(val, idx)` | O(idx)                  | O(N)                       | O(idx)           | Recursive call stack                         |
| `deleteFirst`    | O(1)                    | O(1)                       | O(1)             | Requires updating `head` and potentially `tail` |
| `deletelast`     | O(N)                    | O(N)                       | O(1)             | Traversal to `size-2` to find new `tail`     |
| `delete(idx)`    | O(idx)                  | O(N)                       | O(1)             | Traversal to `idx-1`                         |
| `find(value)`    | O(N)                    | O(N)                       | O(1)             | Traversal of entire list in worst case       |
| `getNode(idx)`   | O(idx)                  | O(N)                       | O(1)             | Traversal to `idx`                           |
| `display`        | O(N)                    | O(N)                       | O(1)             | Traversal of entire list                     |
| `getSize`        | O(1)                    | O(1)                       | O(1)             | Direct access to `size` variable             |

-----

## 2\. Circular Linked List 🔄

A circular linked list is a variation of a singly linked list where the last node points back to the first node (`head`), forming a circle. This eliminates the `null` termination found in standard singly linked lists.

### Core Concepts 💡

  \* **Node:** Similar to a singly linked list node (`value`, `next`).
  \* **Head:** Reference to the first node.
  \* **Tail:** Reference to the last node. In a circular linked list, `tail.next` points to `head`.

### `CircularLinkedList.java` Implementation 💻

```java
package learningJava;

class CircularLinkedList {
    Node head; // Reference to the first node
    Node tail; // Reference to the last node

    // Node class definition (private inner class)
    class Node {
        int val;  // Data stored in the node
        Node next; // Reference to the next node

        // Constructor for a node with only value
        public Node(int val) {
            this.val = val;
        }

        // Constructor for a node with value and next node reference
        public Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    // Constructor for CircularLinkedList
    public CircularLinkedList() {
        this.head = null; // Initially empty list
        this.tail = null; // Initially empty list
    }

    /**
     * Inserts a new node with the given value into the circular linked list.
     * New nodes are typically inserted at the end for simplicity in circular lists.
     *
     * Steps:
     * 1. Create a new Node with the provided value.
     * 2. If the list is empty:
     * a. Set `head` and `tail` to the new node.
     * b. Make the new node point to itself (`node.next = node`) to form a circle.
     * (Note: The current implementation makes `node.next = head; tail.next = node;` in general case
     * and relies on `tail = head` for the first element. This is slightly different and requires
     * that `head` and `tail` point to the same node, and that node's `next` points to itself for a single element.)
     * 3. If the list is not empty:
     * a. Set the `next` of the new node to the current `head` (to connect it to the beginning).
     * b. Set the `next` of the current `tail` to the new node (to link the new node at the end).
     * c. Update `tail` to point to the new node.
     *
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     */
    public void insert(int val) {
        Node node = new Node(val); // Create new node

        if (head == null) { // If the list is empty
            head = node;     // New node is both head and tail
            tail = head;
            node.next = head; // In a single-node circular list, it points to itself
            return;
        }

        node.next = head; // New node's next points to the current head
        tail.next = node; // Current tail's next points to the new node
        tail = node;      // Update tail to the new node
    }

    /**
     * Displays all elements of the circular linked list.
     *
     * Steps:
     * 1. Handle empty list case.
     * 2. Start traversal from `head`.
     * 3. Use a `do-while` loop because even if there's only one node, it needs to be printed,
     * and `temp` will initially be `head`. The loop continues until `temp` points back to `head`.
     * 4. Print the value of the current node and " -> ".
     * 5. Move to the next node (`temp = temp.next`).
     * 6. Print "⟳" to signify the circular nature.
     *
     * Time Complexity: O(N)
     * Space Complexity: O(1)
     */
    public void display() {
        Node temp = head; // Start from head
        if (temp == null) { // Handle empty list
            System.out.println("empty");
            return;
        }
        do { // Use do-while to ensure at least one element is printed if list is not empty
            System.out.print(temp.val + " -> ");
            temp = temp.next; // Move to next node
        } while (temp != head); // Continue until we loop back to head
        System.out.println("⟳"); // Indicate circularity
    }

    /**
     * Deletes the first occurrence of a node with the given value from the circular linked list.
     *
     * Steps:
     * 1. Handle empty list case.
     * 2. If the head node itself needs to be deleted:
     * a. If it's the only node (`head == tail`), set `head` and `tail` to `null`.
     * b. Otherwise, move `head` to `head.next` and update `tail.next` to the new `head`.
     * 3. For other nodes:
     * a. Traverse using a `do-while` loop, keeping track of the current node (`node`) and the next node (`n`).
     * b. If `n.val` matches the target `value`:
     * i. Bypass `n` by setting `node.next = n.next`.
     * ii. If `n` was the `tail`, update `tail` to `node`.
     * iii. Break the loop (as only the first occurrence is deleted).
     * c. Move `node` to `node.next`.
     * 4. The loop condition `node != head` handles wrapping around the circle.
     *
     * Time Complexity: O(N) (in worst case, needs to traverse entire list)
     * Space Complexity: O(1)
     */
    public void delete(int value) {
        Node node = head; // Start from head
        if (node == null) { // Empty list, nothing to delete
            return;
        }


        // Case 1: Deleting the head node
        if (node.val == value) {
            if (head == tail) { // Only one node in the list
                head = null;
                tail = null;
            } else { // Multiple nodes, head needs to be updated
                head = head.next;   // Move head to the next node
                tail.next = head;   // Tail's next must point to the new head
            }
            return; // Deletion complete
        }

        // Case 2: Deleting a node other than the head
        do {
            Node n = node.next; // n is the potential node to be deleted
            if (n.val == value) {
                node.next = n.next; // Bypass n, linking current node to n's next
                if (n == tail) { // If the deleted node was the tail, update tail
                    tail = node; // Current node becomes the new tail
                }
                return; // Deletion complete for the first occurrence
            }
            node = node.next; // Move to the next node
        } while (node != head); // Continue until we wrap around to the head
    }
}
```

### `CLL.java` (Main Driver for Circular Linked List) 🚀

```java
package learningJava;

public class CLL {
    public static void main(String[] args) {
        CircularLinkedList cll = new CircularLinkedList();

        // Inserting elements
        cll.insert(5); // List: 5 -> ⟳
        cll.insert(4); // List: 4 -> 5 -> ⟳
        cll.insert(3); // List: 3 -> 4 -> 5 -> ⟳
        cll.insert(2); // List: 2 -> 3 -> 4 -> 5 -> ⟳

        System.out.print("Initial CLL: ");
        cll.display(); // Expected: 2 -> 3 -> 4 -> 5 -> ⟳

        // Deleting element '3' (middle)
        System.out.print("Deleting 3: ");
        cll.delete(3);
        cll.display(); // Expected: 2 -> 4 -> 5 -> ⟳

        // Deleting element '5' (tail)
        System.out.print("Deleting 5 (tail): ");
        cll.delete(5);
        cll.display(); // Expected: 2 -> 4 -> ⟳

        // Deleting element '2' (head)
        System.out.print("Deleting 2 (head): ");
        cll.delete(2);
        cll.display(); // Expected: 4 -> ⟳

        // Deleting the last remaining element '4'
        System.out.print("Deleting 4 (last element): ");
        cll.delete(4);
        cll.display(); // Expected: empty
    }
}
```

### Time and Space Complexity Summary (Circular Linked List) ⏱️

| Operation        | Average Time Complexity | Worst Case Time Complexity | Space Complexity | Notes                                                              |
| :--------------- | :---------------------- | :------------------------- | :--------------- | :----------------------------------------------------------------- |
| `insert`         | O(1)                    | O(1)                       | O(1)             | Inserts at the end by updating `tail.next` and `tail`              |
| `display`        | O(N)                    | O(N)                       | O(1)             | Traverses all N nodes using `do-while`                             |
| `delete(value)`  | O(N)                    | O(N)                       | O(1)             | Requires traversal to find the node or its predecessor             |

-----

## 3\. Doubly Linked List ↔️

A doubly linked list is a linear data structure where each node contains a data element and two pointers: one to the next node in the sequence (`next`) and one to the previous node (`prev`). This bidirectional linking allows for traversal in both forward and backward directions.

### Core Concepts 💡

  \* **Node:** The fundamental building block. Each node typically contains:
      \* `value`: The data stored in the node.
      \* `next`: A reference to the next node.
      \* `prev`: A reference to the previous node. The first node's `prev` reference is `null`. The last node's `next` reference is `null`.
  \* **Head:** A reference to the first node of the list.

### `DoublyLinkedList.java` Implementation 💻

```java
package learningJava;

class DoublyLinkedList {

    Node head; // Reference to the first node of the list

    // Node class definition (private inner class)
    class Node {
        int val;  // Data stored in the node
        Node next; // Reference to the next node
        Node prev; // Reference to the previous node

        // Constructor for a node with only value (typically for first node)
        public Node(int val) {
            this.val = val;
        }

        // Constructor for a node with value, next, and previous node references
        public Node(int val, Node next, Node prev) {
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }

    /**
     * Inserts a new node with the given value at the beginning of the list.
     *
     * Steps:
     * 1. Create a new Node.
     * 2. Set the `next` of the new node to the current `head`.
     * 3. Set the `prev` of the new node to `null` (it's the new first node).
     * 4. If the list was not empty (`head != null`), update the `prev` of the *old* `head` to the new node.
     * 5. Update `head` to point to the new node.
     *
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     */
    public void insertFirst(int val) {
        Node node = new Node(val); // Create new node
        node.next = head;          // New node's next points to current head
        node.prev = null;          // New node's prev is null (it's the new first)
        if (head != null) {        // If list was not empty, old head's prev points to new node
            head.prev = node;
        }
        head = node;               // Head now points to the new node
    }

    /**
     * Inserts a new node with the given value at the end of the list.
     *
     * Steps:
     * 1. Handle empty list case: if `head` is `null`, call `insertFirst`.
     * 2. Traverse to the last node.
     * 3. Create a new Node, linking its `next` to `null` and its `prev` to the old last node.
     * 4. Update the `next` of the old last node to point to the new node.
     *
     * Time Complexity: O(N) (requires traversal to the end)
     * Space Complexity: O(1)
     */
    public void insertLast(int val) {
        if (head == null) { // If list is empty, insert first
            insertFirst(val);
            return;
        }
        Node temp = head; // Start from head
        while (temp.next != null) { // Traverse to the last node
            temp = temp.next;
        }
        // Create new node: value, next (null), prev (temp - the old last node)
        temp.next = new Node(val, null, temp);
    }

    /**
     * Inserts a new node with the given value at a specific index.
     *
     * Steps:
     * 1. Handle edge case: if `index` is 0, call `insertFirst`.
     * 2. Traverse to the node *before* the target index.
     * 3. Create a new Node, linking its `next` to `temp.next` and its `prev` to `temp`.
     * 4. Update `temp.next` to point to the new node.
     * 5. If the new node is not the last node (`new_node.next != null`), update `new_node.next.prev`
     * to point back to the new node.
     *
     * Time Complexity: O(index) in the worst case (O(N) for insertion near end).
     * Space Complexity: O(1)
     */
    public void insert(int index, int value) {
        if (index == 0) { // Inserting at the beginning
            insertFirst(value);
            return;
        }
        // If inserting at the end, it is handled by the loop below implicitly,
        // as temp.next will be null, and new Node's next will be null.
        // The displayReverse method would need a 'tail' pointer or
        // a traversal to the end to start. For this specific 'insert' method,
        // it behaves correctly even for `index == size`.

        Node temp = head; // Start from head
        // Traverse to the node *before* the insertion point (index-1)
        for (int i = 0; i < index - 1; i++) {
            if (temp == null) { // Handle index out of bounds if list is shorter than index
                System.err.println("Error: Index out of bounds for insertion.");
                return;
            }
            temp = temp.next;
        }

        // Check if temp is null (e.g., trying to insert at index 5 in a list of size 2)
        if (temp == null) {
             System.err.println("Error: Index out of bounds for insertion.");
             return;
        }

        // Create the new node: value, temp.next (old next node), temp (previous node)
        Node newNode = new Node(value, temp.next, temp);
        temp.next = newNode; // Link previous node to new node

        // If the new node is not the last node, update the 'prev' of the node after it
        if (newNode.next != null) {
            newNode.next.prev = newNode;
        }
    }

    /**
     * Finds and returns the Node object containing the specified value.
     *
     * Steps:
     * 1. Start traversal from the `head`.
     * 2. Iterate through the list until the end (`temp != null`).
     * 3. If the `value` of the current node matches the target `value`, return the node.
     * 4. If the end of the list is reached without finding the value, return `null`.
     *
     * Time Complexity: O(N)
     * Space Complexity: O(1)
     */
    public Node find(int value) {
        Node temp = head; // Start from head
        while (temp != null) { // Iterate until end of list
            if (temp.val == value) { // Check if current node's value matches
                return temp; // Return the node if found
            }
            temp = temp.next; // Move to the next node
        }
        return null; // Value not found
    }

    /**
     * Deletes the first node in the list.
     *
     * Steps:
     * 1. Store the value of the `head` node.
     * 2. Update `head` to point to `head.next`.
     * 3. If the new `head` is not `null`, update its `prev` pointer to `null`.
     * 4. Return the deleted value.
     *
     * Time Complexity: O(1)
     * Space Complexity: O(1)
     */
    public int deleteFirst() {
        if (head == null) {
            throw new IllegalStateException("Cannot delete from an empty list.");
        }
        int val = head.val; // Store value of node to be deleted
        head = head.next;      // Move head to the next node
        if (head != null) {    // If list is not empty, new head's prev should be null
            head.prev = null;
        }
        return val;            // Return deleted value
    }

    /**
     * Deletes the last node in the list.
     *
     * Steps:
     * 1. Handle edge case: if `head` is `null` or `head.next` is `null` (only one node), call `deleteFirst`.
     * 2. Traverse to the last node.
     * 3. Store the value of the last node.
     * 4. Set the `next` of the second-to-last node (`temp.prev.next`) to `null`.
     * 5. Return the deleted value.
     *
     * Time Complexity: O(N) (requires traversal to the end)
     * Space Complexity: O(1)
     */
    public int deleteLast() {
        if (head == null || head.next == null) { // Empty or single-node list
            return deleteFirst();
        }
        Node temp = head;
        while (temp.next != null) { // Traverse to the last node
            temp = temp.next;
        }
        int val = temp.val; // Value of the last node
        temp.prev.next = null; // Detach the last node
        return val;
    }

    /**
     * Deletes the node at a specific index.
     *
     * Steps:
     * 1. Handle edge cases: if `index` is 0, call `deleteFirst`; if `index` corresponds to the last node, call `deleteLast`.
     * 2. Traverse to the node at the target `index`.
     * 3. Store its value.
     * 4. Bypass the node by linking its previous node's `next` to its next node, and its next node's `prev` to its previous node.
     *
     * Time Complexity: O(index) (requires traversal to the index)
     * Space Complexity: O(1)
     */
    public int delete(int index) {
        if (index == 0) {
            return deleteFirst();
        }
        // Note: For deleteLast, you might want to call it explicitly if index == size - 1,
        // but the general deletion logic below would also handle it if temp.next becomes null.

        Node temp = head;
        for (int i = 0; i < index; i++) { // Traverse to the node to be deleted
            if (temp == null) {
                throw new IndexOutOfBoundsException("Index out of bounds for deletion.");
            }
            temp = temp.next;
        }

        if (temp == null) { // This means index was out of bounds
            throw new IndexOutOfBoundsException("Index out of bounds for deletion.");
        }

        int val = temp.val;

        // Link prev node's next to current node's next
        temp.prev.next = temp.next;
        // If not deleting the last node, link next node's prev to current node's prev
        if (temp.next != null) {
            temp.next.prev = temp.prev;
        }
        return val;
    }

    /**
     * Displays all elements of the doubly linked list from head to tail.
     *
     * Steps:
     * 1. Start traversal from the `head`.
     * 2. Print the value of the current node and " <-> ".
     * 3. Move to the next node until `temp` becomes `null`.
     * 4. Print "END" to signify the end of the list.
     *
     * Time Complexity: O(N)
     * Space Complexity: O(1)
     */
    public void display() {
        Node temp = head; // Start from head
        while (temp != null) { // Iterate until end of list
            System.out.print(temp.val + " <-> ");
            temp = temp.next; // Move to next node
        }
        System.out.println("END"); // Mark the end of the list
    }

    /**
     * Displays all elements of the doubly linked list from tail to head (reverse order).
     *
     * Steps:
     * 1. Find the last node by traversing from `head`.
     * 2. Start traversal from the last node, moving backward using `prev` pointer.
     * 3. Print the value of the current node and " <-> ".
     * 4. Continue until `temp` becomes `null`.
     * 5. Print "START" to signify the beginning of the list.
     *
     * Time Complexity: O(N) (to find tail + N to traverse back)
     * Space Complexity: O(1)
     */
    public void displayReverse() {
        Node temp = head; // Start from head
        if (temp == null) {
            System.out.println("empty");
            return;
        }
        while (temp.next != null) { // Traverse to the last node
            temp = temp.next;
        }
        // Now temp is at the tail
        while (temp != null) { // Traverse backwards
            System.out.print(temp.val + " <-> ");
            temp = temp.prev; // Move to previous node
        }
        System.out.println("START"); // Mark the start of the list
    }
}
```

### `DLL.java` (Main Driver for Doubly Linked List) 🚀

```java
package learningJava;

public class DLL {
    public static void main(String[] args) {
        DoublyLinkedList list = new DoublyLinkedList();

        // Inserting elements
        list.insertFirst(3); // List: 3 <-> END
        list.insertFirst(2); // List: 2 <-> 3 <-> END
        list.insertFirst(1); // List: 1 <-> 2 <-> 3 <-> END

        System.out.print("Initial DLL (forward): ");
        list.display(); // Expected: 1 <-> 2 <-> 3 <-> END

        System.out.print("Initial DLL (reverse): ");
        list.displayReverse(); // Expected: 3 <-> 2 <-> 1 <-> START

        list.insertLast(4); // List: 1 <-> 2 <-> 3 <-> 4 <-> END
        list.insertLast(5); // List: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> END
        System.out.print("DLL after insertLast: ");
        list.display(); // Expected: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> END

        System.out.print("DLL after insertLast (reverse): ");
        list.displayReverse(); // Expected: 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> START

        list.insert(2, 99); // Insert 99 at index 2 (0-indexed)
        System.out.print("DLL after insert 99 at index 2: ");
        list.display(); // Expected: 1 <-> 2 <-> 99 <-> 3 <-> 4 <-> 5 <-> END
        System.out.print("DLL after insert 99 at index 2 (reverse): ");
        list.displayReverse(); // Expected: 5 <-> 4 <-> 3 <-> 99 <-> 2 <-> 1 <-> START

        // Test find method
        DoublyLinkedList.Node found = list.find(99);
        if (found != null) {
            System.out.println("Found 99: " + found.val); // Expected: Found 99: 99
        }
        found = list.find(100);
        if (found == null) {
            System.out.println("100 not found as expected."); // Expected: 100 not found as expected.
        }

        // Test deletion
        System.out.println("Deleted first: " + list.deleteFirst()); // Deletes 1
        System.out.print("DLL after deleteFirst: ");
        list.display(); // Expected: 2 <-> 99 <-> 3 <-> 4 <-> 5 <-> END

        System.out.println("Deleted last: " + list.deleteLast()); // Deletes 5
        System.out.print("DLL after deleteLast: ");
        list.display(); // Expected: 2 <-> 99 <-> 3 <-> 4 <-> END

        System.out.println("Deleted at index 1 (value 99): " + list.delete(1)); // Deletes 99
        System.out.print("DLL after delete at index 1: ");
        list.display(); // Expected: 2 <-> 3 <-> 4 <-> END
    }
}
```

### Time and Space Complexity Summary (Doubly Linked List) ⏱️

| Operation        | Average Time Complexity | Worst Case Time Complexity | Space Complexity | Notes                                                              |
| :--------------- | :---------------------- | :------------------------- | :--------------- | :----------------------------------------------------------------- |
| `insertFirst`    | O(1)                    | O(1)                       | O(1)             | Direct `head` manipulation                                         |
| `insertLast`     | O(N)                    | O(N)                       | O(1)             | Requires traversal to find the last node (unless `tail` is kept)   |
| `insert(idx, val)` | O(idx)                  | O(N)                       | O(1)             | Traversal to `idx-1`                                             |
| `find(value)`    | O(N)                    | O(N)                       | O(1)             | Traversal of entire list in worst case                           |
| `deleteFirst`    | O(1)                    | O(1)                       | O(1)             | Direct `head` manipulation                                         |
| `deleteLast`     | O(N)                    | O(N)                       | O(1)             | Traversal to find the second-to-last node (unless `tail` is kept) |
| `delete(idx)`    | O(idx)                  | O(N)                       | O(1)             | Traversal to `idx`                                               |
| `display`        | O(N)                    | O(N)                       | O(1)             | Traversal of entire list                                         |
| `displayReverse` | O(N)                    | O(N)                       | O(1)             | Traversal to find tail, then traversal back                       |

</details>


-----

<details>
 <summary>
  📚 Stacks & Queues
 </summary>
</details>

-----

<details>
 <summary>
  🗺️ HashMaps & HashSets
 </summary>
</details>

-----

<details>
 <summary>
  🔎 Searching & Sorting
 </summary>
</details>

-----


