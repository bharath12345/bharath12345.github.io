/**
 * Created with JetBrains WebStorm.
 * User: bharadwaj
 * Date: 28/08/13
 * Time: 2:29 PM
 * To change this template use File | Settings | File Templates.
 */

define(["dojo/_base/declare", "dojo/i18n", "dojo/i18n!dashboard/views/topology/nls/topology", "dashboard/logger/Logger",
    "dojox/layout/GridContainer", "dijit/TitlePane", "dijit/layout/ContentPane", "dojo/request/xhr", "dojo/_base/lang",
    "dashboard/helper/Helper", "dashboard/helper/Scheduler", "dashboard/views/topology/TopologyForm"],

    function (declare, i18n, i18nString, Logger, GridContainer, TitlePane, ContentPane, xhr, lang, Helper, Scheduler, TopologyForm) {

        dashboard.classnames.ConnectionStatus = "dashboard.topology.forms.SampleTopologyForm.ConnectionStatus";

        var ConnectionStatus = declare(dashboard.classnames.ConnectionStatus, null, {

            create:function (data, input) {

            }
        });

        ConnectionStatus.LOG = Logger.addTimer(new Logger(dashboard.classnames.ConnectionStatus));

        /*
         *
         *
         */

        dashboard.classnames.NodeStatus = "dashboard.topology.forms.SampleTopologyForm.NodeStatus";

        var NodeStatus = declare(dashboard.classnames.NodeStatus, null, {

            create:function (data, input) {

            }
        });

        NodeStatus.LOG = Logger.addTimer(new Logger(dashboard.classnames.NodeStatus));

        /*
         *
         *
         */

        dashboard.classnames.RenderConnectivity = "dashboard.topology.forms.SampleTopologyForm.RenderConnectivity";

        var RenderConnectivity = declare(dashboard.classnames.RenderConnectivity, null, {

            constructor:function () {
                jsPlumb.importDefaults({
                    // default drag options
                    DragOptions:{ cursor:'pointer', zIndex:2000 },

                    // default to blue at one end and green at the other
                    EndpointStyles:[
                        { fillStyle:'#225588' },
                        { fillStyle:'#558822' }
                    ],

                    // blue endpoints 7 px; green endpoints 11.
                    Endpoints:[
                        [ "Dot", {radius:3} ],
                        [ "Dot", { radius:3 } ]
                    ],

                    // the overlays to decorate each connection with.  note that the label overlay uses a function to generate the label text; in this
                    // case it returns the 'labelText' member that we set on each connection in the 'init' method below.
                    ConnectionOverlays:[
                        [ "Arrow", { location:0.9, foldback:0.5, width:6 } ],
                        [ "Label", {
                            location:0.1,
                            id:"label",
                            cssClass:"aLabel"
                        }]
                    ]
                });
            },

            create:function (data, input) {
                var nodeName = input.netBankingConnectivityVO.name;
                var sourceType = input.netBankingConnectivityVO.sourceType;
                var dstType = input.netBankingConnectivityVO.dstType;
                var connections = input.netBankingConnectivityVO.connections;

                var lhsDivName = data.id + "_" + data.name + RenderNodes.ENDPOINT_SUFFIX;
                for (var i = 0; i < connections.length; i++) {
                    var rhsDivName = dstType + "_" + connections[i] + RenderNodes.ENDPOINT_SUFFIX;
                    console.log("lhs div name = " + lhsDivName + " rhs div name = " + rhsDivName);

                    // create Endpoint on LHS and RHS node
                    var srcUuid = RenderConnectivity.FROM + data.name + RenderConnectivity.TO + connections[i];
                    var dstUuid = RenderConnectivity.FROM + connections[i] + RenderConnectivity.TO + data.name;
                    console.log("src uuid = " + srcUuid + " dst uuid = " + dstUuid);

                    var sourceEP = jsPlumb.addEndpoint(lhsDivName,
                        RenderConnectivity.sourceEndpoint,
                        {
                            uuid:srcUuid,
                            container:dashboard.dom.CpCenterInnerTop.domNode,
                            anchor:"RightMiddle"
                        });


                    var dstEP = jsPlumb.addEndpoint(rhsDivName,
                        RenderConnectivity.targetEndpoint,
                        {
                            uuid:dstUuid,
                            container:dashboard.dom.CpCenterInnerTop.domNode,
                            anchor:"LeftMiddle"
                        });

                    // create connection link
                    jsPlumb.connect({ source:sourceEP, target:dstEP, container:dashboard.dom.CpCenterInnerTop.domNode });

                    // get and set the status of the connection link
                    var viewMeta = {
                        id:"", // uuid of the link?
                        name:"" // uuid of the link?

                    };

                    xhr("topology/ConnectionStatus.action", {
                        handleAs:"json",
                        method:"POST",
                        query:viewMeta,
                        headers:Helper.JSON_HEADER
                    }).then(lang.hitch(this, this.renderConnectivityStatus));

                }
            },

            renderConnectivityStatus:function (input) {
                var data = Helper.parseInput(input);
                new ConnectionStatus().create(data, input);
            }
        });

        RenderConnectivity.LOG = Logger.addTimer(new Logger(dashboard.classnames.RenderConnectivity));
        RenderConnectivity.FROM = "FROM_";
        RenderConnectivity.TO = "_TO_";


        // this is the paint style for the connecting lines..
        RenderConnectivity.connectorPaintStyle = {
            lineWidth:1,
            strokeStyle:"#deea18",
            joinstyle:"round",
            outlineColor:"#EAEDEF",
            outlineWidth:1
        };

        // .. and this is the hover style.
        RenderConnectivity.connectorHoverStyle = {
            lineWidth:2,
            strokeStyle:"#2e2aF8"
        };

        // the definition of source endpoints (the small blue ones)
        RenderConnectivity.sourceEndpoint = {
            endpoint:"Dot",
            paintStyle:{ fillStyle:"#225588", radius:3 },
            isSource:true,
            connector:[ "Straight", { stub:[40, 60], gap:10 } ],
            connectorStyle:RenderConnectivity.connectorPaintStyle,
            hoverPaintStyle:RenderConnectivity.connectorHoverStyle,
            connectorHoverStyle:RenderConnectivity.connectorHoverStyle,
            dragOptions:{},
            overlays:[
                [ "Label", {
                    location:[0.5, 1.5],
                    label:"",
                    cssClass:"endpointSourceLabel"
                } ]
            ]
        };

        RenderConnectivity.targetEndpoint = {
            endpoint:"Dot",
            paintStyle:{ fillStyle:"#558822", radius:3 },
            hoverPaintStyle:RenderConnectivity.connectorHoverStyle,
            maxConnections:-1,
            dropOptions:{ hoverClass:"hover", activeClass:"active" },
            isTarget:true,
            overlays:[
                [ "Label", { location:[0.5, -0.5], label:"", cssClass:"endpointTargetLabel" } ]
            ]
        };

        /*
         *
         *
         */

        dashboard.classnames.RenderNodes = "dashboard.topology.forms.SampleTopologyForm.RenderNodes";

        var RenderNodes = declare(dashboard.classnames.RenderNodes, null, {

            getSvgIcon:function (src, width, height) {
                var svgIcon = dojo.create("img");
                svgIcon.src = src;
                //svgIcon.type = "image/svg+xml";
                svgIcon.height = width;
                svgIcon.width = height;
                return svgIcon;
            },

            createEndpoint:function (endPointsArray, endPointType, width, height) {
                var styleString = "width: " + width + "; height: " + height + ";";
                for (var i = 0; i < endPointsArray.length; i++) {
                    var divCol = dojo.byId(endPointType + RenderNodes.ROW_SUFFIX);
                    var node = dojo.create("div");
                    node.id = endPointType + "_" + endPointsArray[i] + RenderNodes.ENDPOINT_SUFFIX;
                    node.className = "topoIconContainer";
                    node.style.cssText = styleString;
                    divCol.appendChild(node);
                    //var endpoint = jsPlumb.addEndpoint(endPointName);
                    //TOPOLOGY.NODEMAP[endPointName] = endpoint;

                    var imgW = 50, imgH = 50;
                    switch (endPointType) {
                        case RenderNodes.TYPE.WEBSERVER:
                            var svgIcon = this.getSvgIcon("./images/topology/osa_server_web.svg", imgW, imgH);
                            node.appendChild(svgIcon);
                            break;

                        case RenderNodes.TYPE.APPSERVER:
                            var svgIcon = this.getSvgIcon("./images/topology/osa_server_application.svg", imgW, imgH);
                            node.appendChild(svgIcon);
                            break;

                        case RenderNodes.TYPE.DATABASES:
                            var svgIcon = this.getSvgIcon("./images/topology/osa_database.svg", imgW, imgH);
                            node.appendChild(svgIcon);
                            break;

                        case RenderNodes.TYPE.MESSAGEQ:
                            var svgIcon = this.getSvgIcon("./images/topology/Messaging_Queue.svg", imgW, imgH);
                            node.appendChild(svgIcon);
                            break;

                        case RenderNodes.TYPE.TCPENDPOINTS:
                            var svgIcon = this.getSvgIcon("./images/topology/osa_ics_drive.svg", imgW, imgH);
                            node.appendChild(svgIcon);
                            break;

                        default:
                            console.log("unknown end point type = " + endPointType);
                            return;
                    }
                }
            },

            createColumnPanes:function (names, width, height) {
                console.log("in createColumnPanes = " + (names.length) + " w = " + width + " h = " + height);
                try {
                    var styleString = "width: " + (width / (names.length)) + "; height: " + height + ";";

                    var titlePanes = [];
                    for (var i = 0; i < names.length; i++) {
                        console.log("new pane for = " + names[i]);
                        var titlePane = new TitlePane({
                            splitter:false,
                            style:styleString,
                            content:"<div id='" + names[i] + RenderNodes.COLUMN_SUFFIX + "' style='width: 100%; height: 100%;'></div>",
                            title:names[i],
                            toggleable:false
                        });
                        titlePanes[i] = titlePane;
                    }

                    var gridContainer = new GridContainer({nbZones:names.length, isAutoOrganized:true,
                        style:"width: 100%; height: 100%;"});
                    dashboard.dom.CpCenterInnerTop.addChild(gridContainer);
                    gridContainer.disableDnd();

                    var j = 0, k = 0;
                    for (var i = 0; i < names.length; i++) {
                        j = (i % (names.length));
                        k = parseInt(i / (names.length));
                        gridContainer.addChild(titlePanes[i], j, k);
                    }
                    gridContainer.startup();
                    gridContainer.resize();

                    this.removeMargins(gridContainer);

                } catch (e) {
                    console.log("exception = " + e);
                }
                //return titlePanes;
            },

            removeMargins:function (gridContainer) {
                var innerPane = dojo.query(".dijitTitlePaneContentInner", gridContainer.domNode);
                //console.log("inner len = " + innerPane.length);
                for (var i = 0; i < innerPane.length; i++) {
                    innerPane[i].style.padding = 0;
                }

                var head = dojo.query(".dijitTitlePaneTitle", gridContainer.domNode)
                for (var i = 0; i < head.length; i++) {
                    head[i].style.padding = 0;
                    head[i].style.minHeight = 0;
                }

                var headFocus = dojo.query(".dijitTitlePaneTitleFocus", gridContainer.domNode)
                for (var i = 0; i < headFocus.length; i++) {
                    headFocus[i].style.margin = 0;
                    headFocus[i].style.padding = 0;
                }
            },

            createInnerPanes:function (layers, name, width, height) {
                try {
                    var hl = height / layers.length;
                    var styleString = "width: " + width + "; height: " + hl + ";";

                    var innerPanes = [];
                    for (var i = 0; i < layers.length; i++) {
                        var innerPane = new TitlePane({
                            splitter:false,
                            style:styleString,
                            content:"<div id='" + layers[i] + RenderNodes.ROW_SUFFIX + "' style='" + styleString + "'></div>",
                            title:layers[i],
                            toggleable:false
                        });
                        innerPanes[i] = innerPane;
                    }

                    var gridContainer = new GridContainer({nbZones:1, isAutoOrganized:true}, dojo.byId(name + RenderNodes.COLUMN_SUFFIX));
                    gridContainer.disableDnd();

                    for (var i = 0; i < layers.length; i++) {
                        gridContainer.addChild(innerPanes[i], 1, i);
                    }
                    gridContainer.startup();
                    gridContainer.resize();
                    this.removeMargins(gridContainer);

                } catch (e) {
                    console.log("exception inner page = " + e);
                }
                return innerPanes;
            },

            create:function (data, input) {

                var nbLayers = input.netBankingLayersVO.layers;

                var layerTypes = [];
                for (var i = 0; i < nbLayers.length; i++) {
                    layerTypes.push(nbLayers[i].layertype);
                }
                this.createColumnPanes(layerTypes, data.dimensions.width, data.dimensions.height);

                var colWidth = data.dimensions.width / layerTypes.length;
                var divW = 60, divH = 60;
                for (var i = 0; i < nbLayers.length; i++) {
                    console.log("layer type = " + layerTypes[i]);

                    var layer = nbLayers[i].layer;
                    console.log("layer length = " + layer.length);
                    var layerNames = [];
                    for (var j = 0; j < layer.length; j++) {
                        console.log("layer inner name = " + layer[j].name);
                        layerNames.push(layer[j].name);
                    }
                    this.createInnerPanes(layerNames, layerTypes[i], colWidth, data.dimensions.height);
                    for (var j = 0; j < layer.length; j++) {
                        this.createEndpoint(layer[j].value, layer[j].name, divW, divH);
                    }

                    // start drawing the connections ONLY after ALL nodes are rendered
                    for (var j = 0; j < layer.length; j++) {
                        // by this point all nodes have been created
                        // the next job is to draw connections
                        // drawing connections has 2 tasks - create endpoints and then create a connection - all using jsPlumb
                        // query connections for all nodes and start drawing
                        // problem 1 -
                        // if you query links for node A and find a link A --> B, then later querying links for B
                        // will give us a B --> A which has to be ignored??
                        // problem 2 - placement of endpoints on the node

                        for (var k = 0; k < layer[j].value.length; k++) {
                            var viewMeta = {
                                id:layer[j].name, // this will be something like WebServers
                                name:layer[j].value[k] // this will be something like FLXRET_IHS1

                            };

                            xhr("topology/Connections.action", {
                                handleAs:"json",
                                method:"POST",
                                query:viewMeta,
                                headers:Helper.JSON_HEADER
                            }).then(lang.hitch(this, this.createConnectivity));

                        }
                    }

                    // start putting in the node Status ONLY after ALL connection requests are despatched
                    for (var j = 0; j < layer.length; j++) {
                        for (var k = 0; k < layer[j].value.length; k++) {
                            // get the STATUS of the nodes
                            var viewMeta = {
                                id:layer[j].value[k], // this will be something like FLXRET_IHS1
                                name:layer[j].value[k] // this will be something like FLXRET_IHS1

                            };
                            xhr("topology/NodeStatus.action", {
                                handleAs:"json",
                                method:"POST",
                                query:viewMeta,
                                headers:Helper.JSON_HEADER
                            }).then(lang.hitch(this, this.renderNodeStatus));

                        }
                    }
                }

                var innerPane = dojo.query(".dijitTitlePaneContentOuter", dashboard.dom.CpCenterInnerTop.domNode);
                for (var i = 0; i < innerPane.length; i++) {
                    innerPane[i].style.border = 0;
                }

                var gridText = dojo.query(".dijitTitlePaneTextNode", dashboard.dom.CpCenterInnerTop.domNode);
                for (var i = 0; i < gridText.length; i++) {
                    gridText[i].style.display = "block";
                    gridText[i].style.textAlign = "center";
                }
            },

            createConnectivity:function (input) {
                var data = Helper.parseInput(input);
                new RenderConnectivity().create(data, input);
            },

            renderNodeStatus:function (input) {
                var data = Helper.parseInput(input);
                new NodeStatus().create(data, input);
            }
        });

        RenderNodes.LOG = Logger.addTimer(new Logger(dashboard.classnames.RenderNodes));

        RenderNodes.TYPE = {};
        RenderNodes.TYPE.WEBSERVER = "WebServers";
        RenderNodes.TYPE.APPSERVER = "AppServers";
        RenderNodes.TYPE.DATABASES = "Databases";
        RenderNodes.TYPE.MESSAGEQ = "MessageQueues";
        RenderNodes.TYPE.TCPENDPOINTS = "TcpEndpoints";

        RenderNodes.COLUMN_SUFFIX = "_col";
        RenderNodes.ROW_SUFFIX = "_row";
        RenderNodes.ENDPOINT_SUFFIX = "_endpoint";


        /*
         *
         *
         */

        dashboard.classnames.SampleTopologyForm = "dashboard.topology.forms.SampleTopologyForm";

        var SampleTopologyForm = declare(dashboard.classnames.SampleTopologyForm, TopologyForm, {

            title: i18nString.SAMPLE_TOPOLOGY,
            inAnalysisPane: false,

            createToolbarButtons: function() {

            },

            startup:function () {
                this.inherited(arguments);
            },

            launch: function() {
                var width = this.domNode.parentNode.offsetWidth - 20;
                var height = this.domNode.offsetHeight;
                console.log("view port width = " + width + " height = " + height);

                var viewMeta = {
                    dimensions:[width, height]
                };

                xhr("topology/Nodes.action", {
                    handleAs:"json",
                    method:"POST",
                    query:viewMeta,
                    headers:Helper.JSON_HEADER
                }).then(lang.hitch(this, this.createNodeLayout));


                dashboard.dom.STANDBY.hide();
            },

            createNodeLayout:function (input) {
                var data = Helper.parseInput(input);
                new RenderNodes().create(data, input);
            }


        });

        // static variables of this class
        SampleTopologyForm.LOG = Logger.addTimer(new Logger(dashboard.classnames.SampleTopologyForm));

        return SampleTopologyForm;
    });