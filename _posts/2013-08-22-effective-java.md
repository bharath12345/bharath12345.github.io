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
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider a builder when faced with many constructor parameters</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Enforce the singleton property with a private constructor or an enum type</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Enforce noninstantiability with a private constructor</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid creating unnecessary objects</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Eliminate obsolete object references</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Avoid finalizers</td>
        <td></td>
        <td></td>
    </tr>
</table>

### The java methods common to all objects
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Obey the general contract when overriding equals()</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Always override hashCode() when you override equals()</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Always override toString()</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Override clone() judiciously</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Consider implementing Comparable</td>
        <td></td>
        <td></td>
    </tr>
</table>

### Classes and Interfaces
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Minimize the accessibility of classes and members</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>In public classes, use public classes not public fields</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Minimize mutability</td>
        <td></td>
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
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use interfaces only to define types</td>
        <td></td>
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
        <td></td>
        <td></td>
    </tr>
</table>

### Generics
<table class="table table-bordered table-striped table-condensed bs-docs-grid">
    <tr class="tablerow"">
        <td>Dont use raw types in new code</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Eliminate unchecked warnings</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Prefer lists to arrays</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor generic types</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Favor generic methods</td>
        <td></td>
        <td></td>
    </tr>
    <tr class="tablerow"">
        <td>Use bounded wildcards to increase API flexibility</td>
        <td></td>
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
