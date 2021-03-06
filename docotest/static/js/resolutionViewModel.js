define(['knockout', 'jquery', 'jquery.cookie'], function(ko) {
    
    function Resolution(data) {
        this.description = ko.observable(data.description);
        this.id = ko.observable(data.id);
    }

    var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    

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
                //self.resolutions.push(resolution);
                self.resolutions.push(returnedData);
            });
            self.newResolutionText("");
        };
        self.removeResolution = function(resolution){
            $.ajax({url: "/api/resolution/" + resolution.id, 
                    type: 'DELETE',
                    data: resolution,
                    success: function(returnedData) {
                        // This callback is executed if the post was successful     
                        self.resolutions.remove(resolution)
                    }
            });
        };
        self.loadResolutions();
    }

    ko.applyBindings(new resolutionViewModel());
});
