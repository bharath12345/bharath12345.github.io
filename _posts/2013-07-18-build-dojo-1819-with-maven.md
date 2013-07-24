---
layout: post
title: "Build Dojo 1.8/1.9 with Maven"
category: posts
published: false
---

I have been a Dojo user for many years now. I use many JavaScript libraries (jQuery, backbone, bootstrap, d3, highsoft) but Dojo is what I really love. I would not embark on any "professional" development work without being armed with Dojo. But I rest my opinions and comparisons for a different blog. Here the context is to "build" Dojo. After all every professional project should do a build of their JS - compilers like Closure can find bugs, obfuscate and finally make execution faster.

I still am mainly a Java programmer (the enterprise products I have built are predominantly in Java… my time split between Java/JavaScript may be 65/35). I am used to Maven as my primary build tool. So maven is what I shall use.

Folks who have not tried to build Dojo should probably start-off by reading these two articles -
* [Creating Builds](http://dojotoolkit.org/documentation/tutorials/1.9/build/) from Dojo documentation
* [Creating custom dojo builds in maven](http://www.mahieu.org/?p=3) 

The last article is very good but slightly dated. And here is what I propose to add to it -
1. Use dojo v1.9 (v1.8 and v1.7 with AMD should also work well)
2. I use WebStorm as my JavaScript IDE. It has excellent contextual support which includes Dojo. However it requires dojo to be at a constant referencable path from where it could index. Once the indexes are built, typing a "." after an object should show up the list of method and variable belonging to that object. This is extremely useful for fast development
3. Dojo builds are slow. A typical build from source download to unzip to transform can take anywhere between 5 to 15 minutes. This can be painful and needs to be made faster

Now, here is the how…

### Step 1: Installing Dojo in Maven Repository and Unpack Task
This is no different from the Step 1 & 2 in Mahieu blog. The unzipped sources are placed in src/main/js of my maven hierarchy. I dont do any renaming of this directory.

### Step 2: Build Dojo
For this, I use antrun plugin

    <plugin>
    	<artifactId>maven-antrun-plugin</artifactId>
    	<executions>
    		<execution>
    			<id>AppsOne dojo ${dojo.version} Custom Build</id>
        		<phase>compile</phase>
        		<configuration>
        			<tasks>
        				<parallel>
            				<java classname="org.mozilla.javascript.tools.shell.Main"
                  		fork="true" maxmemory="512m" failonerror="false"
                  		classpath="${shrinksafe-dir}/js.jar${path.separator}${closure-dir}/compiler.jar${path.separator}${shrinksafe-dir}/shrinksafe.jar">
 	                			<arg value="${js-dir}/dojo/dojo.js"/>
    	            			<arg value="baseUrl=${js-dir}/dojo"/>
                    			<arg value="load=build"/>
                    			<arg line="--profile ${basedir}/dashboard.profile.js"/>
                    			<arg value="--release"/>
               				</java>
            			</parallel>
         			</tasks>
         		</configuration>
         		<goals>
         			<goal>run</goal>
         		</goals>
    		</execution>
    	</executions>
    </plugin>



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