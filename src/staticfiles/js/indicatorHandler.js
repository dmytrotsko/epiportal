class IndicatorHandler {
    constructor() {
        this.indicators = {};
    }

    fluviewIndicatorsMapping = {
        wili: "%wILI",
        ili: "%ILI",
    };

    fluSurvRegions = [
        { value: "network_all", label: "Entire Network" },
        { value: "network_eip", label: "EIP Netowrk" },
        { value: "network_ihsp", label: "IHSP Network" },
        { value: "CA", label: "CA" },
        { value: "CO", label: "CO" },
        { value: "CT", label: "CT" },
        { value: "GA", label: "GA" },
        { value: "IA", label: "IA" },
        { value: "ID", label: "ID" },
        { value: "MD", label: "MD" },
        { value: "MI", label: "MI" },
        { value: "MN", label: "MN" },
        { value: "NM", label: "NM" },
        { value: "NY_albany", label: "NY (Albany)" },
        { value: "NY_rochester", label: "NY (Rochester)" },
        { value: "OH", label: "OH" },
        { value: "OK", label: "OK" },
        { value: "OR", label: "OR" },
        { value: "RI", label: "RI" },
        { value: "SD", label: "SD" },
        { value: "TN", label: "TN" },
        { value: "UT", label: "UT" },
    ];

    fluviewRegions = [
        { id: "nat", text: "U.S. National" },
        { id: "hhs1", text: "HHS Region 1" },
        { id: "hhs2", text: "HHS Region 2" },
        { id: "hhs3", text: "HHS Region 3" },
        { id: "hhs4", text: "HHS Region 4" },
        { id: "hhs5", text: "HHS Region 5" },
        { id: "hhs6", text: "HHS Region 6" },
        { id: "hhs7", text: "HHS Region 7" },
        { id: "hhs8", text: "HHS Region 8" },
        { id: "hhs9", text: "HHS Region 9" },
        { id: "hhs10", text: "HHS Region 10" },
        { id: "cen1", text: "Census Region 1" },
        { id: "cen2", text: "Census Region 2" },
        { id: "cen3", text: "Census Region 3" },
        { id: "cen4", text: "Census Region 4" },
        { id: "cen5", text: "Census Region 5" },
        { id: "cen6", text: "Census Region 6" },
        { id: "cen7", text: "Census Region 7" },
        { id: "cen8", text: "Census Region 8" },
        { id: "cen9", text: "Census Region 9" },
        { id: "AK", text: "AK" },
        { id: "AL", text: "AL" },
        { id: "AR", text: "AR" },
        { id: "AZ", text: "AZ" },
        { id: "CA", text: "CA" },
        { id: "CO", text: "CO" },
        { id: "CT", text: "CT" },
        { id: "DC", text: "DC" },
        { id: "DE", text: "DE" },
        { id: "FL", text: "FL" },
        { id: "GA", text: "GA" },
        { id: "HI", text: "HI" },
        { id: "IA", text: "IA" },
        { id: "ID", text: "ID" },
        { id: "IL", text: "IL" },
        { id: "IN", text: "IN" },
        { id: "KS", text: "KS" },
        { id: "KY", text: "KY" },
        { id: "LA", text: "LA" },
        { id: "MA", text: "MA" },
        { id: "MD", text: "MD" },
        { id: "ME", text: "ME" },
        { id: "MI", text: "MI" },
        { id: "MN", text: "MN" },
        { id: "MO", text: "MO" },
        { id: "MS", text: "MS" },
        { id: "MT", text: "MT" },
        { id: "NC", text: "NC" },
        { id: "ND", text: "ND" },
        { id: "NE", text: "NE" },
        { id: "NH", text: "NH" },
        { id: "NJ", text: "NJ" },
        { id: "NM", text: "NM" },
        { id: "NV", text: "NV" },
        { id: "NY", text: "NY" },
        { id: "OH", text: "OH" },
        { id: "OK", text: "OK" },
        { id: "OR", text: "OR" },
        { id: "PA", text: "PA" },
        { id: "RI", text: "RI" },
        { id: "SC", text: "SC" },
        { id: "SD", text: "SD" },
        { id: "TN", text: "TN" },
        { id: "TX", text: "TX" },
        { id: "UT", text: "UT" },
        { id: "VA", text: "VA" },
        { id: "VT", text: "VT" },
        { id: "WA", text: "WA" },
        { id: "WI", text: "WI" },
        { id: "WV", text: "WV" },
        { id: "WY", text: "WY" },
        { id: "ny_minus_jfk", text: "NY (minus NYC)" },
        { id: "as", text: "American Samoa" },
        { id: "mp", text: "Mariana Islands" },
        { id: "gu", text: "Guam" },
        { id: "pr", text: "Puerto Rico" },
        { id: "vi", text: "Virgin Islands" },
        { id: "ord", text: "Chicago" },
        { id: "lax", text: "Los Angeles" },
        { id: "jfk", text: "New York City" },
    ];

    checkForCovidcastIndicators() {
        return this.indicators.some((indicator) => {
            return indicator["_endpoint"] === "covidcast";
        });
    }

    getCovidcastIndicators() {
        var covidcastIndicators = [];
        this.indicators.forEach((indicator) => {
            if (indicator["_endpoint"] === "covidcast") {
                covidcastIndicators.push(indicator);
            }
        });
        return covidcastIndicators;
    }

    getFluviewIndicators() {
        var fluviewIndicators = [];
        this.indicators.forEach((indicator) => {
            if (indicator["_endpoint"] === "fluview") {
                fluviewIndicators.push(indicator);
            }
        });
        return fluviewIndicators;
    }

    getFromToDate(startDate, endDate, timeType) {
        if (timeType === "week") {
            $.ajax({
                url: "get_epiweek/",
                type: "POST",
                async: false,
                data: {
                    csrfmiddlewaretoken: csrf_token,
                    start_date: startDate,
                    end_date: endDate,
                },
                success: function (result) {
                    startDate = result.start_date;
                    endDate = result.end_date;
                },
            });
        }
        return [startDate, endDate];
    }

    sendAsyncAjaxRequest(url, data) {
        var request = $.ajax({
            url: url,
            type: "GET",
            data: data,
        });
        return request;
    }

    showFluviewRegions() {
        var fluviewRegionSelect = `
        <div class="row margin-top-1rem">
            <div class="col-2">
                <label for="fluviewRegions" class="col-form-label">ILINet Location(s):</label>
            </div>
            <div class="col-10">
                <select id="fluviewRegions" name="fluviewRegions" class="form-select" multiple="multiple"></select>
            </div>
        </div>`;
        if ($("#otherEndpointLocations").length) {
            $("#otherEndpointLocations").append(fluviewRegionSelect);
            $("#fluviewRegions").select2({
                placeholder: "Select ILINet Location(s)",
                data: this.fluviewRegions,
                allowClear: true,
                width: "100%",
            });
        }
    }

    plotData() {
        const covidCastGeographicValues =
            $("#geographic_value").select2("data");
        const fluviewRegions = $("#fluviewRegions").select2("data");
        const submitData = {
            indicators: this.indicators,
            covidCastGeographicValues: covidCastGeographicValues,
            fluviewRegions: fluviewRegions,
        };
        const csrftoken = Cookies.get("csrftoken");
        $.ajax({
            url: "epivis/",
            type: "POST",
            async: false,
            dataType: "json",
            contentType: "application/json",
            headers: { "X-CSRFToken": csrftoken },
            data: JSON.stringify(submitData),
        }).done(function (data) {
            window.open(data["epivis_url"], '_blank').focus();
        });
    }

    exportData() {
        var fluviewRegions = $("#fluviewRegions").select2("data");

        var covidCastGeographicValues = Object.groupBy(
            $("#geographic_value").select2("data"),
            ({ geoType }) => [geoType]
        );

        const submitData = {
            start_date: document.getElementById("start_date").value,
            end_date: document.getElementById("end_date").value,
            indicators: this.indicators,
            covidCastGeographicValues: covidCastGeographicValues,
            fluviewRegions: fluviewRegions,
        }
        const csrftoken = Cookies.get("csrftoken");
        $.ajax({
            url: "export/",
            type: "POST",
            async: false,
            dataType: "json",
            contentType: "application/json",
            headers: { "X-CSRFToken": csrftoken },
            data: JSON.stringify(submitData),
        }).done(function (data) {
            $('#modeSubmitResult').html(data["data_export_block"]);
        });
    }

    previewData() {
        $("#loader").show();
        var requests = [];
        var previewExample = [];
        var startDate = document.getElementById("start_date").value;
        var endDate = document.getElementById("end_date").value;

        if (this.checkForCovidcastIndicators()) {
            var geographicValues = $("#geographic_value").select2("data");
            geographicValues = Object.groupBy(
                geographicValues,
                ({ geoType }) => [geoType]
            );
            var geoTypes = Object.keys(geographicValues);
            this.getCovidcastIndicators().forEach((indicator) => {
                const [dateFrom, dateTo] = this.getFromToDate(
                    startDate,
                    endDate,
                    indicator["time_type"]
                );
                var timeValues =
                    indicator["time_type"] === "week"
                        ? `${dateFrom}-${dateTo}`
                        : `${dateFrom}--${dateTo}`;
                geoTypes.forEach((geoType) => {
                    var geoValues = geographicValues[geoType]
                        .map((el) =>
                            typeof el.id === "string"
                                ? el.id.toLowerCase()
                                : el.id
                        )
                        .join(",");
                    var data = {
                        time_type: indicator["time_type"],
                        time_values: timeValues,
                        data_source: indicator["data_source"],
                        signal: indicator["signal"],
                        geo_type: geoType,
                        geo_values: geoValues,
                    };
                    requests.push(
                        this.sendAsyncAjaxRequest("epidata/covidcast/", data)
                    );
                });
            });
        }

        if (this.getFluviewIndicators().length > 0) {
            const [dateFrom, dateTo] = this.getFromToDate(
                startDate,
                endDate,
                "week"
            );
            var fluviewRegions = $("#fluviewRegions")
                .select2("data")
                .map((region) => region.id);
            fluviewRegions = fluviewRegions.join(",");
            var data = {
                regions: fluviewRegions,
                epiweeks: `${dateFrom}-${dateTo}`,
            };

            requests.push(this.sendAsyncAjaxRequest("epidata/fluview/", data));
        }

        $.when.apply($, requests).then((...responses) => {
            if (requests.length === 1) {
                if (responses[0]["epidata"].length != 0) {
                    previewExample.push({
                        epidata: responses[0]["epidata"][0],
                        result: responses["result"],
                        message: responses["message"],
                    });
                } else {
                    previewExample.push(responses[0]);
                }
            } else {
                responses.forEach((response) => {
                    if (response[0]["epidata"].length != 0) {
                        previewExample.push({
                            epidata: response[0]["epidata"][0],
                            result: response[0]["result"],
                            message: response[0]["message"],
                        });
                    } else {
                        previewExample.push(response[0]["epidata"]);
                    }
                });
            }
            $("#loader").hide();
            $("#modeSubmitResult").html(
                JSON.stringify(previewExample, null, 2)
            );
        });
    }
}
