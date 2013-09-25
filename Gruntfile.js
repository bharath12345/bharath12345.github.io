/**
 * Created with JetBrains WebStorm.
 * User: bharadwaj
 * Date: 02/09/13
 * Time: 2:08 PM
 * To change this template use File | Settings | File Templates.
 */

module.exports = function(grunt) {

    grunt.initConfig({
        clean : {
            htmlmins: {
                src: ["_layouts/about.html", "_layouts/layout.html", "!_includes/*.max.html"]
            },
            common: {
                src: [ "lib/my/*.min.js", "lib/my/*.min.css"]
            },
            topograph: {
                src: [ "lib/my/topograph/*.min.js", "lib/my/topograph/*.min.css"]
            }
        },
        uglify: {
            common: {
                files: {
                    'lib/my/common.min.js': 'lib/my/common.js'
                }
            },
            topograph: {
                files: {
                    'lib/my/topograph/initialize.min.js': 'lib/my/topograph/initialize.js',
                    'lib/my/topograph/d3AppGraph.min.js': 'lib/my/topograph/d3AppGraph.js',
                    'lib/my/topograph/jsPlumbAppGraph.min.js': 'lib/my/topograph/jsPlumbAppGraph.js'
                }
            }
        },
        cssmin: {
            common: {
                expand: true,
                cwd: 'lib/my/',
                src: ['*.css', '!*.min.css'],
                dest: 'lib/my/',
                ext: '.min.css'
            },
            topograph: {
                expand: true,
                cwd: 'lib/my/topograph/',
                src: ['*.css', '!*.min.css'],
                dest: 'lib/my/topograph/',
                ext: '.min.css'
            }
        },
        htmlmin: {
            dist: {
                options: {
                    removeComments: true,
                    collapseWhitespace: true,
                    collapseBooleanAttributes: true,
                    removeAttributeQuotes: true
                },
                files: {
                    '_layouts/layout.html'          : '_layouts/layout.max.html',
                    '_layouts/about.html'           : '_layouts/about.max.html',
                    '_includes/analytics.html'      : '_includes/analytics.max.html',
                    '_includes/css.html'            : '_includes/css.max.html',
                    '_includes/disqus.html'         : '_includes/disqus.max.html',
                    '_includes/facebook.html'       : '_includes/facebook.max.html',
                    '_includes/fb-sdk.html'         : '_includes/fb-sdk.max.html',
                    '_includes/footer.html'         : '_includes/footer.max.html',
                    '_includes/gauges.html'         : '_includes/gauges.max.html',
                    '_includes/google-analytics.html': '_includes/google-analytics.max.html',
                    '_includes/javascripts.html'    : '_includes/javascripts.max.html',
                    '_includes/meta.html'           : '_includes/meta.max.html',
                    '_includes/postpagescripts.html': '_includes/postpagescripts.max.html',
                    '_includes/topmost-nav.html'    : '_includes/topmost-nav.max.html',
                    '_includes/twitter.html'        : '_includes/twitter.max.html'
                }
            }
        },
        jsdoc : {
            dist : {
                src: [
                    'lib/my/common.js',
                    'lib/my/topograph/initialize.js',
                    'lib/my/topograph/d3AppGraph.js',
                    'lib/my/topograph/jsPlumbAppGraph.js'
                ],
                options: {
                    destination: 'docs'
                }
            }
        },
        exec: {
            build: {
                cmd: 'jekyll build'
            },
            serve: {
                cmd: 'jekyll serve --watch'
            }
        }
    });

    /*
     loadNpmTasks
     */
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-htmlmin');
    grunt.loadNpmTasks('grunt-exec');
    grunt.loadNpmTasks('grunt-jsdoc');

    /*
     registerTask
     */
    grunt.registerTask('default', [ 'clean', 'uglify', 'cssmin', 'htmlmin', /*'jsdoc',*/ 'exec:serve' ]);


};