/**
 * Created with JetBrains WebStorm.
 * User: bharadwaj
 * Date: 02/09/13
 * Time: 2:08 PM
 * To change this template use File | Settings | File Templates.
 */

module.exports = function(grunt) {

    grunt.initConfig({
        uglify: {
            mycommon: {
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
        /*copy: {
            bootstrap: {
                files: [
                    {expand: true, cwd: 'components/bootstrap/img/', src: ['**'], dest: 'assets/img/'}
                ]
            }
        },*/
        exec: {
            build: {
                cmd: 'jekyll build'
            },
            serve: {
                cmd: 'jekyll serve --watch'
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-exec');

    grunt.registerTask('default', [ 'uglify', /*'copy',*/ 'exec:serve' ]);

};