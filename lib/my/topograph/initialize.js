/**
 * Created with JetBrains WebStorm.
 * User: bharadwaj
 * Date: 29/08/13
 * Time: 12:23 PM
 * To change this template use File | Settings | File Templates.
 */

define(["dojo/_base/declare", "dijit/layout/ContentPane", "dijit/layout/BorderContainer", "dijit/TitlePane"],

    function (declare, ContentPane, BorderContainer, TitlePane) {

        var Initialize = declare("Initialize", null, {

            getContentPane: function(region, splitter, style, name, id) {
                /*return new ContentPane({
                    region:region,
                    splitter:splitter,
                    style: style
                });*/

                return new TitlePane({
                    region:region,
                    splitter:splitter,
                    style:style,
                    content:"<div id='" + id + "' style='width: 100%; height: 100%;'></div>",
                    title:name,
                    toggleable:false
                });
            },

            getBorderContainer: function() {
                return new BorderContainer({
                    design:"sidebar",
                    liveSplitters:false,
                    persist:true,
                    gutters:false,
                    style: "width: 100%; height: 100%;"
                });
            },

            addCPstartBC: function(bc, cpList, paneToPlace) {
                for(var i=0; i< cpList.length; i++) {
                    bc.addChild(cpList[i]);
                }
                bc.placeAt(paneToPlace);
                bc.startup();
                bc.resize();
            },

            initialize: function() {
                var bc = this.getBorderContainer();
                var cpList = [];
                cpList.push(this.getContentPane("left",false,"height:100%;width:50%", "D3 Graph", "D3AppGraph"));
                cpList.push(this.getContentPane("center",false, "", "jsPlumb Graph", "JsPlumbAppGraph"));
                this.addCPstartBC(bc, cpList, dojo.byId("graphs"));
            }

        });

        return Initialize;
    }
);
