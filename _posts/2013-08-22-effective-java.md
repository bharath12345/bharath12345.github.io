---
layout: post
title: "Effective Java"
category: posts
tags: []
categories: []
published: false
tweetfb: true
disqus: true
---

### Creating and Destorying Objects
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Consider static factory methods instead of constructors</td>
        <td>Similar to flyweight. valueof/of/getInstance/newInstance/getType/newType</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider a builder when faced with many constructor parameters</td>
        <td>Telescoping constructors are hard to read and write. Inconsistent state partway through the construction</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Enforce the singleton property with a private constructor or an enum type</td>
        <td>All instance fields should be transient. Provide a readResolve() method else serialization/deserialization can lead to new objects</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Enforce noninstantiability with a private constructor</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid creating unnecessary objects</td>
        <td>A statement like this in a for loop can lead to huge number of unnecessary objects getting created -
        <code>String s = new String("stringette");</code>
        The improved version is simply the following:
        <code>String s = "stringette";</code>
        This version uses a single String instance, rather than creating a new one each time it is executed. Furthermore, it is guaranteed that the object will be reused by any other code running in the same virtual machine that happens to con- tain the same string literal
        The static factory method <code>Boolean.valueOf(String)</code> is almost always preferable to the constructor <code>Boolean(String)</code>
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Eliminate obsolete object references</td>
        <td>Is there a memory leak in this program?

        <code>
        // Can you spot the "memory leak"?
           public class Stack {
               private Object[] elements;
               private int size = 0;
               private static final int DEFAULT_INITIAL_CAPACITY = 16;
               public Stack() {
                   elements = new Object[DEFAULT_INITIAL_CAPACITY];
        }
               public void push(Object e) {
                   ensureCapacity();
                   elements[size++] = e;
        }
               public Object pop() {
                   if (size == 0)
                       throw new EmptyStackException();
                   return elements[--size];
        }
               /**
                * Ensure space for at least one more element, roughly
                * doubling the capacity each time the array needs to grow.
                */
               private void ensureCapacity() {
                   if (elements.length == size)
                       elements = Arrays.copyOf(elements, 2 * size + 1);
        } }
        </code>

        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid finalizers</td>
        <td>What is a finalizer? Is it always called by the GC? Is there a performance penalty to using finalizer? Why?</td>
        <td></td>
    </tr>
</table>

### The Java methods common to all objects
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Obey the general contract when overriding equals()</td>
        <td>When do you override equals()? When a class has a notion of logical equality that differs from mere object identity, and a superclass has not already overridden equals to implement the desired behavior.
        What are the main rules that you would follow to implement equals()?
        1. Use == to check for same reference
        2. Use instanceof to check if the agrument is of the correct type
        3. Match all significant fields of the two objects
        4. Symmetric? Transivitve? Consistent?
        5. override hashCode()
        6. </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Always override hashCode() when you override equals()</td>
        <td>
        1. Iftwoobjectsareequalaccordingtotheequals(Object)method,thencall- ing the hashCode method on each of the two objects must produce the same integer result.
            2. Itisnotrequiredthatiftwoobjectsareunequalaccordingtotheequals(Ob- ject) method, then calling the hashCode method on each of the two objects must produce distinct integer results. However, the programmer should be aware that producing distinct integer results for unequal objects may improve the performance of hash tables.
            3. How will you compute the hashCode()? Do not be tempted to exclude significant parts of an object from the hash code computation to improve performance</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Always override toString()</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Override clone() judiciously</td>
        <td>
        1. Does Cloneable interface have a clone() method? Why not?
        Because the Java Object's clone() method (which is protected) is supposed to be used
        2. How does Java Object's clone() method work?
        If a class implements Cloneable, Object’s clone method returns a field-by-field copy of the object; otherwise it throws CloneNotSupportedException
        3. What are the 3 rules for implementing Cloneable?
            a. x.clone() != x
            b. x.clone().getClass() == x.getClass()
            c. x.clone().equals(x)
        4. How to clone properly?
        All classes that implement Cloneable should override clone with a public method whose return type is the class itself. This method should first call super.clone and then fix any fields that need to be fixed. Typically, this means copying any mutable objects that comprise the internal “deep structure” of the object being cloned, and replacing the clone’s references to these objects with ref- erences to the copies. While these internal copies can generally be made by call- ing clone recursively, this is not always the best approach. If the class contains only primitive fields or references to immutable objects, then it is probably the case that no fields need to be fixed.
        5. How come interfaces like Cloneable and Serializable have no methods? Why do they exist at all then? How does JVM use them?
        The UID and custom readers/writers are accessed via reflection.
        Serializable serves as a marker to the JRE/JVM, which may take action(s) based on its presence.
        http://en.wikipedia.org/wiki/Marker_interface_pattern
        An example of the application of marker interfaces from the Java programming language is the Serializable interface. A class implements this interface to indicate that its non-transient data members can be written to an ObjectOutputStream. The ObjectOutputStream private method writeObject() contains a series of instanceof tests to determine writeability, one of which looks for the Serializable interface. If any of these tests fails, the method throws a NotSerializableException.
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider implementing Comparable</td>
        <td>
        1. What is the use of the Comparable interface?
        Helps in sorting when there is a natural order among the objects
        2. Whats the difference between interfaces like Comparable and those like Cloneable/Serializable?</td>
        <td></td>
    </tr>
</table>

### Classes and Interfaces
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Minimize the accessibility of classes and members</td>
        <td>What is package-private? How do you implement?
        The member is accessible from any class in the package where it is declared. Technically known as default access, this is the access lev- el you get if no access modifier is specified.</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>In public classes, use public classes not public fields</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Minimize mutability</td>
        <td>
1. Is it good or bad to minimize mutability? why?
     If objects are immutable they are automatically thread-safe and no synchronization or locking is required
2. How would you make an object immutable?
    a. No mutators - no setters
    b. Class cant be extended - class should be marked final
    c. Make all fields final
    d. Make all fields private
    e. Ensure exclusive access to any mutable components
    f. getters should return a new instance of the object
</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor composition over inheritance</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Design and document for inheritance or else prohibit it</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer interfaces to abstract classes</td>
        <td>Why are interfaces better than abstract classes?
        1. Existing classes can be easily retrofitted to implement a new interface
        2. Interfaces are ideal for defining mixins
        3. Interfaces allow the construction of nonhierarchical type frameworks.
        4. Interfaces enable safe, powerful functionality enhancements
        5. combine the virtues of interfaces and abstract classes by providing an abstract skeletal implementation class to go with each nontrivial interface that you export</td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use interfaces only to define types</td>
        <td>1. Is 'constants' in an interface a good programming pattern?
        No. </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer class hierarchies to tagged classes</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use function objects to represent strategies</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor static member classes over nonstatic</td>
        <td>
1. What are the 4 kinds of nested classes?
    a. static member classes
    b. nonstatic member classes
    c. anonymous classes
    d. local classes

2. When will you make a nested class static?
If an instance of a nested class can exist in isolation from an instance of its enclosing class, then the nested class must be a static member class: it is impossible to create an instance of a nonstatic member class without an enclosing instance. If you declare a member class that does not require access to an enclosing instance, always put the static modifier in its declaration

3. Why would one prefer static classes?
The association between a nonstatic member class instance and its enclosing instance is established when the former is created; it cannot be modified thereafter. Storing this reference costs time and space, and can result in the enclosing instance being retained when it would otherwise be eligible for garbage collection
        </td>
        <td></td>
    </tr>
</table>

### Generics
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Dont use raw types in new code</td>
        <td>1. What is the problem with doing <code>private final Collection stamps = ... ;</code>
        Loss of compile time type safety
        2. Is List<String>.class legal? What will it give me?
        It is not legal
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Eliminate unchecked warnings</td>
        <td>
1. How do you eliminate a unchecked warning?
        suppress the warning with an @SuppressWarnings("unchecked") annotation.
        </td>
        <td>Always use the Suppress- Warnings annotation on the smallest scope possible.</td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer lists to arrays</td>
        <td>
1. If Sub is a subtype of Super, then is the array Sub[] a subtype of Super[]?
Yes. Arrays are covariant. Lists are invariant
2. So which one is better? And why?
Lists are better. Arrays are reified. This means that arrays know and enforce their element types at runtime. Generics, by contrast, are implemented by erasure. This means that they enforce their type constraints only at compile time and discard (or erase) their element type information at runtime.
3. Test question -
This code fragment is legal but fails at runtime! -
                  <code>Object[] objectArray = new Long[1];
                  objectArray[0] = "I don't fit in"; // Throws ArrayStoreException
                  </code>
                  But this one wont compile at all! -
                  <code>List<Object> ol = new ArrayList<Long>(); // Incompatible types ol.add("I don't fit in");
                  </code>
4. Are these legal?
<code>new List<E>[]
new List<String>[]
new E[]</code>
No. It is illegal to create an array of a generic type, a parameterized type, or a type parameter. Types such as E, List<E>, and List<String> are technically known as non-reifiable types. Intuitively speaking, a non-reifiable type is one whose runtime representation contains less information than its compile-time representation.
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor generic types</td>
        <td>Which of these is better and why?
        <code>public class Stack {
                private Object[] elements;
                public void push(Object e) {
                }
                public Object pop() {
                }
             }
        </code>
        or
        <code>public class Stack<E> {
                private E[] elements;
                public void push(E e) {
                }
                public E pop() {
                }
              }
        </code>
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor generic methods</td>
        <td>Which of these is better and why?
        <code>public static Set union(Set s1, Set s2)</code>
        or
        <code>public static <E> Set<E> union(Set<E> s1, Set<E> s2)</code>
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use bounded wildcards to increase API flexibility</td>
        <td>What is the PECS rule or Get-and-Put principle?
        Bounded wildcards can be of two types -
        <code>X<? extends E></code>
        or
        <code>Y<? super E></code>
        PECS stands for producer-extends, consumer-super.
        In other words, if a parameterized type represents a T producer, use <? extends T>; if it represents a T consumer, use <? super T>.
        </td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider typesafe heterogenous containers</td>
        <td></td>
        <td></td>
    </tr>
</table>

### Enums and Annotations
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Use enums instead of int constants</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use instance fields instead of ordinals</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use EnumSet instead of bit fields</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use EnumMap instead of ordinal indexing</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Emulate extensible enums with interfaces</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer annotations to naming patterns</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consistently use the Override annotation</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use marker interfaces to define types</td>
        <td></td>
        <td></td>
    </tr>
</table>

### Methods
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Check parameters for validity</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Make defensive copies when needed</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Design method signatures carefully</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use overloading judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use varargs judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Return empty arrays or collections, not nulls</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Write doc comments for all exposed API comments</td>
        <td></td>
        <td></td>
    </tr>
</table>

### General Programming
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Minimize the scope of local variables</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer foreach loops to traditional for loops</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Know and use the libraries</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid float and double if exact answers are required</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer primitives to boxed primitives</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid strings when other types are more appropriate</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Beware the performance of string concatenation</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Refer to objects by their interfaces</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer interfaces to reflection</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use native methods judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Optimize judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Adhere to generally accepted naming conventions</td>
        <td></td>
        <td></td>
    </tr>
</table>

### Exceptions
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Use exceptions only for exceptional conditions</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use checked exceptions for recoverable conditions and runtime exceptions for programming errors</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid unnecessary use of checked exceptions</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor the use of standard exceptions</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Throw exceptions appropriate to the abstraction</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Document all exceptions thrown by each method</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Include failure-capture information in detail messages</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Strive for failure atomicity</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Dont ignore exceptions</td>
        <td></td>
        <td></td>
    </tr>
</table>

### Concurrency
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Synchronize access to shared mutable data</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid excessive synchronization</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer executors and tasks to threads</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer concurrency utilities to wait and notify</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Document thread safety</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use lazy initialization judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Dont depend on the thread scheduler</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid thread groups</td>
        <td></td>
        <td></td>
    </tr>
</table>

### Serialization
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Implement serializable judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider using a custom serialized form</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Write readObject methods defensively</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>For instance control prefer enum types than readResolve</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider serialization proxies instead of serialized instances</td>
        <td></td>
        <td></td>
    </tr>
</table>


### Conclusion