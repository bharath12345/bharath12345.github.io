/**
 * Created with JetBrains WebStorm.
 * User: bharadwaj
 * Date: 28/08/13
 * Time: 10:02 AM
 * To change this template use File | Settings | File Templates.
 */

define(["dojo/_base/declare"],

    function (declare) {

        var Common = declare("common", null, {});

        Common.AdjustDivHeight = function() {
            var leftCol = document.getElementsByClassName("left");
            var rightCol = document.getElementsByClassName("right");
            var firstCol = document.getElementsByClassName("first");
            console.log("num of elements = " + leftCol.length);
            for(var i=0;i<leftCol.length;i++) {
                //console.log("setting right height to = " + leftCol[i].clientHeight);
                rightCol[i].style.height = leftCol[i].clientHeight+2+"px";
                if(firstCol[i]!=null) {
                    firstCol[i].style.height = leftCol[i].clientHeight+2+"px";
                }
            }
        };

        Common.GenerateTOC = function(startLevel, depth) {
            var entryBlock = jQuery("#entryBlock");
            var container = jQuery("<div id='tocBlock'></div>");
            entryBlock.append(container);

            var heading = 'Table of Contents';
            container.append('<span class="tocHeading">' + heading + '</span>');

            var div = jQuery("<ul id='toc' style='padding-left: 10px'></ul>");
            container.append(div);

            div.tableOfContents(document.body, {startLevel: startLevel, depth: depth});
        };

        return Common;
    }
);