requirejs.config( {
    "shim": {
        "jquery.cookie"  : ["jquery"]
    }
} );



require(['knockout', 'resolutionViewModel', 'jquery', 'jquery.cookie', 'domReady!'], function(ko, resolutionViewModel) {
        ko.applyBindings(new resolutionViewModel());
    });
