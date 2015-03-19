define(['knockout'], function(ko) {
    
    function Resolution(data) {
        this.description = ko.observable(data.description);
    }

    

    return function resolutionViewModel() { 
        var self = this;
        //self.resolutions = ko.observableArray(ResolutionData);
        self.resolutions = ko.observableArray([]);
        self.newResolutionText = ko.observable();

        self.loadResolutions = function () {
            $.getJSON('/api/resolution/', function (data) {
                self.resolutions(data.results)
            }
            );
        }

        self.addResolution = function(resolution) {
            self.resolutions.push(new Resolution({ description: this.newResolutionText() }));
            self.newResolutionText("");
        };
        self.removeResolution = function(resolution){
            self.resolutions.remove(resolution)
        };
        self.loadResolutions();
    }

    ko.applyBindings(new resolutionViewModel());
});
