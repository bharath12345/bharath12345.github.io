/**
 * Created with JetBrains WebStorm.
 * User: bharadwaj
 * Date: 28/06/14
 * Time: 11:02 AM
 * To change this template use File | Settings | File Templates.
 */
define(["dojo/_base/declare", "dojox/image/Gallery", "dojo/data/ItemFileReadStore"],
    /** @lends module:initialize */
        function (declare, Gallery, ItemFileReadStore) {

        var initialize = declare("initialize", null, {

            createGallery: function(name, jsonFile) {
                var imageItemStore = new ItemFileReadStore({url: "../../lib/my/xmlxpath/" + jsonFile});
                var node = new Gallery({
                    pageSize: 5,
                    imageHeight: 500, imageWidth: 700,
                    style: "height: 500px; width: 700px; margin-left: 200px;"}, name);

                var itemRequest = {
                    query: {},
                    count: 20
                };
                var itemNameMap = {
                    imageThumbAttr: "thumb",
                    imageLargeAttr: "large"
                };
                node.setDataStore(imageItemStore, itemRequest, itemNameMap);
            },

            createImageGallery: function() {
                this.createGallery("javaxcpumem", "javaxcpumem.json");
                this.createGallery("javaxgc", "javaxgc.json");

                this.createGallery("saxoncpumem", "saxoncpumem.json");
                this.createGallery("saxongc", "saxongc.json");

                this.createGallery("scalacpumem", "scalacpumem.json");
                this.createGallery("scalagc", "scalagc.json");

                this.createGallery("vtdcpumem", "vtdcpumem.json");
                this.createGallery("vtdgc", "vtdgc.json");
            }
        });

        return initialize;
    }
);