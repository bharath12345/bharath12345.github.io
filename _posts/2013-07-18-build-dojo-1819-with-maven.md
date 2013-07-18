---
layout: post
title: "Build Dojo 1.8/1.9 with Maven"
category: posts
published: false
---

I have been a Dojo user for many years now. But I still am mainly a Java programmer (the enterprise products I have built are predominantly in Java… my time split between Java/JavaScript may be 65/35 or so!). And thus I am used to Maven as my primary build tool. Not that I am complaining - I love all things Dojo, Maven, JavaScript and Java!!

Folks who have not tried to build Dojo ever should probably start-off by reading these two articles -
* [Creating Builds](http://dojotoolkit.org/documentation/tutorials/1.9/build/) from Dojo documentation
* [Creating custom dojo builds in maven](http://www.mahieu.org/?p=3) (this uses dojo v1.3 while I shall use v1.9. v1.8 should work as well)

Readers can refer to this [pom.xml](https://github.com/bharath12345/uiDashboard/blob/master/uiJS/pom.xml) from one of my projects on GitHub. It has 2 profiles -
1. Full Build: Unarchives the Dojo 'source' bundle. Builds Dojo. Packages user written JS. And builds a WAR
2. Faster build: Assumes the presence of unarchived dojo bundle in the source tree. Since dojo ZIP download from maven repository can be slow (dojo source is upwards of 35MB in size) and unzip even slower, the "-DskipFullBuild" is an optimization for developers

In this article I quickly describe only the full build. Reading and understanding the faster build profile should be fairly straightforward after reading this.

# Step 1: Clean Existing Dojo source Artifacts

In a fresh build, the dojo source zip is downloaded from a local maven repository and uncompressed. I move the uncompressed dojo directories {dojo, dijit, dojoX, util} from the unarchived position in 'target' to under src/main/js. This is done for two reasons - (a) It enables the faster build which I have mentioned above. Also note that 'target' directory is always removed during a build (b) It helps referencing JavaScript classes from my WebStorm IDE

I use many dojo related projects in my code - for example dgrid, gridX and their dependencies. These are also placed in 'src/main/js' but are not removed in the clean phase. The clean task therefore looks like this -

    <plugin>
        <artifactId>maven-clean-plugin</artifactId>
        <version>2.5</version>
        <executions>
            <execution>
                <id>clean-resources</id>
                <phase>clean</phase>
                <goals>
                    <goal>clean</goal>
                </goals>
                <configuration>
                    <excludeDefaultDirectories>true</excludeDefaultDirectories>
                    <filesets>
                        <fileset>
                            <directory>${js-dir}</directory>
                            <includes>
                                <include>dijit</include>
                                <include>dojo</include>
                                <include>dojox</include>
                                <include>util</include>
                                <include>${dojo.source.basename}</include>
                            </includes>
                            <followSymlinks>false</followSymlinks>
                        </fileset>
                    </filesets>
                </configuration>
            </execution>
            <execution>
                <id>clean-js</id>
                <phase>prepare-package</phase>
                <goals>
                    <goal>clean</goal>
                </goals>
                <configuration>
                    <excludeDefaultDirectories>true</excludeDefaultDirectories>
                    <filesets>
                        <fileset>
                            <directory>${release-dir}/dashboard</directory>
                            <includes>
                                <include>**/*uncompressed.js</include>
                            </includes>
                            <followSymlinks>true</followSymlinks>
                        </fileset>
                        <!-- MANY MORE SIMILAR ONES -->
                     </filesets>
                </configuration>
            </execution>
        </executions>
    </plugin>