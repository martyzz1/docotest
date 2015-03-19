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
            });
        }

        self.addResolution = function(resolution) {
            resolution = new Resolution({ description: this.newResolutionText() });
            var jsonData = ko.toJSON(resolution);

            $.post("/api/resolution/", resolution, function(returnedData) {
                // This callback is executed if the post was successful     
                self.resolutions.push(resolution);
            });
            self.newResolutionText("");
        };
        self.removeResolution = function(resolution){
            self.resolutions.remove(resolution)
        };
        self.loadResolutions();
    }

    ko.applyBindings(new resolutionViewModel());
});