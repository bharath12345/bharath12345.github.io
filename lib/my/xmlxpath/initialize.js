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
            createImageGallery: function() {
                var imageItemStore = new ItemFileReadStore({url: "../../lib/my/xmlxpath/images.json"});
                var node = new Gallery({
                    pageSize: 5,
                    imageHeight: 500, imageWidth: 700,
                    style: "height: 500px; width: 700px; margin-left: 200px;"}, "javaxcpumem");

                var itemRequest = {
                    query: {},
                    count: 20
                };
                var itemNameMap = {
                    imageThumbAttr: "thumb",
                    imageLargeAttr: "large"
                };
                node.setDataStore(imageItemStore, itemRequest, itemNameMap);
            }
        });

        return initialize;
    }
);