function FeaturesViewModel() {
    self.id = ko.observable();
    self.title = ko.observable();
    self.description = ko.observable();
    self.client = ko.observable();
    self.priority = ko.observable();
    self.target_date = ko.observable();
    self.product_area = ko.observable();
    self.features_response = ko.observable();
    self.id_to_index_map = {};

    self.response = ko.observable();

    apiRequest("/api/features", {}, "GET", self.features_response)

    function apiRequest(url, data, type, resp) {
        $.ajax({
            url: url,
            data: data,
            type: type,
            contentType: "application/json",
            accepts: "application/json",
            success: function (response) {
                resp(response)
                for (i = 0; i < resp().length; i++) {
                    self.id_to_index_map[resp()[i]['id']] = i;
                }
            },
            error: function (error) {
                console.log(error);
            }
        });
    }

    self.saveFeature = function () {
        if (!(self.title() && self.description() && self.client() && self.target_date() && self.product_area())) {
            alert("All input fields are required")
            return;
        } else if (!(self.priority() && Number.parseInt(self.priority()))) {
            alert("Priority requires integer input")
            return;
        }
        validateForm()
        var feature = {
            'id': self.id(),
            'title': self.title(),
            'description': self.description(),
            'client': self.client(),
            'priority': self.priority(),
            'target_date': self.target_date(),
            'product_area': self.product_area()
        }
        self.this = feature
        if (self.id() == null) {
            newFeature(feature)
        } else {
            editFeature(feature)
        }
        $('#featureModal').modal('hide');
    }

    self.newFeature = function (feature) {
        apiRequest("/api/feature/new", JSON.stringify(feature), "POST", response)
        apiRequest("/api/features", {}, "GET", self.features_response)
        self.reset()
    }

    self.editFeature = function (feature) {
        if (hasChanged(feature, self.features_response()[self.id_to_index_map[feature['id']]])) {
            apiRequest("/api/feature/update", JSON.stringify(feature), "PATCH", response)
            apiRequest("/api/features", {}, "GET", self.features_response)
        }
        self.reset()
    }

    self.deleteFeature = function (id) {
        if (confirm("Are you sure you want to delete?") == false)
            return;

        apiRequest("/api/feature/delete", JSON.stringify({
            'id': id
        }), "DELETE", response)
        apiRequest("/api/features", {}, "GET", self.features_response)
    }

    self.hasChanged = function (feature1, feature2) {

        if (feature1['title'] != feature2['title'])
            return true;

        if (feature1['description'] != feature2['description'])
            return true;

        if (feature1['client'] != feature2['client'])
            return true;

        if (feature1['priority'] != feature2['priority'])
            return true;

        if (feature1['target_date'] != feature2['target_date'])
            return true;

        if (feature1['product_area'] != feature2['product_area'])
            return true;

        return false;
    }

    self.reset = function () {
        setUp(null, null, null, null, null, null, null)
    }

    self.setUp = function (id, title, description, client, priority, target_date, product_area) {
        self.id(id)
        self.title(title);
        self.description(description);
        self.client(client);
        self.priority(priority);
        self.target_date(target_date);
        self.product_area(product_area);
    }

    function validateForm() {

    }
}


ko.applyBindings(new FeaturesViewModel());