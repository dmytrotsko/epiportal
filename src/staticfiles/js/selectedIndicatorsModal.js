let checkedIndicatorMembers = [];

function updateSelectedIndicators(
    dataSource,
    indicatorDisplayName,
    indicatorSet,
    indicator
) {
    var selectedIndicatorsList = document.getElementById(
        "selectedIndicatorsList"
    );

    var tr = document.createElement("tr");
    tr.setAttribute("id", `${dataSource}_${indicator}`);
    var indicatorSetName = document.createElement("td");
    indicatorSetName.textContent = indicatorSet;
    tr.appendChild(indicatorSetName);
    var indicatorName = document.createElement("td");
    indicatorName.textContent = indicatorDisplayName;
    tr.appendChild(indicatorName);
    selectedIndicatorsList.appendChild(tr);
}

function addSelectedIndicator(element) {
    if (element.checked) {
        checkedIndicatorMembers.push({
            _endpoint: element.dataset.endpoint,
            data_source: element.dataset.datasource,
            indicator: element.dataset.indicator,
            time_type: element.dataset.timeType,
            indicator_set: element.dataset.indicatorSet,
            display_name: element.dataset.indicatorDisplayname,
            indicator_set_short_name: element.dataset.indicatorSetShortName,
            member_short_name: element.dataset.memberShortName,
        });
        updateSelectedIndicators(
            element.dataset.datasource,
            element.dataset.indicatorDisplayname,
            element.dataset.indicatorSet,
            element.dataset.indicator
        );
    } else {
        checkedIndicatorMembers = checkedIndicatorMembers.filter(
            (indicator) => indicator.indicator !== element.dataset.indicator
        );
        document
            .getElementById(
                `${element.dataset.datasource}_${element.dataset.indicator}`
            )
            .remove();
    }

    //indicatorHandler.indicators = checkedSignalMembers;

    if (checkedIndicatorMembers.length > 0) {
        $("#showSelectedIndicatorsButton").show();
    } else {
        $("#showSelectedIndicatorsButton").hide();
    }
}

const alertPlaceholder = document.getElementById("warning-alert");

const appendAlert = (message, type) => {
    const wrapper = document.createElement("div");
    const alertId = `alert-${Date.now()}`;
    wrapper.innerHTML = [
        `<div id="${alertId}" class="alert alert-${type} alert-dismissible" data-mdb-alert-init role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-mdb-dismiss="alert" aria-label="Close"></button>',
        "</div>",
    ].join("");

    alertPlaceholder.append(wrapper);
    wrapper
        .getElementsByClassName("btn-close")[0]
        .addEventListener("click", () => hideAlert(alertId));
};

var currentMode = 'epivis';

function showNotCoveredGeoWarningMessage(notCoveredSignals, geoValue) {
    var warningMessage = "";
    notCoveredSignals.forEach((signal) => {
        if (currentMode === "epivis") {
            warningMessage += `Indicator ${signal.display_name} is not available for Location ${geoValue} <br>`;
        } else {
            var startDate = document.getElementById("start_date").value;
            var endDate = document.getElementById("end_date").value;
            warningMessage += `Indicator ${signal.display_name} is not available for Location ${geoValue} for the time period from ${startDate} to ${endDate} <br>`;
        }
    });
    appendAlert(warningMessage, "warning");
}

async function checkGeoCoverage(geoType, geoValue) {
    const notCoveredSignals = [];

    try {
        const result = await $.ajax({
            url: "/base/epidata/covidcast/geo_coverage/",
            type: "GET",
            data: {
                geo: `${geoType}:${geoValue}`,
            },
        });

        checkedSignalMembers
            .filter((signal) => signal["_endpoint"] === "covidcast")
            .forEach((signal) => {
                const covered = result["epidata"].some(
                    (e) =>
                        e.source === signal.data_source &&
                        e.signal === signal.signal
                );
                if (!covered) {
                    notCoveredSignals.push(signal);
                }
            });

        return notCoveredSignals;
    } catch (error) {
        console.error("Error fetching geo coverage:", error);
        return notCoveredSignals;
    }
}

$("#geographic_value").on("select2:select", function (e) {
    var geo = e.params.data;
    checkGeoCoverage(geo.geoType, geo.id).then((notCoveredSignals) => {
        if (notCoveredSignals.length > 0) {
            showNotCoveredGeoWarningMessage(notCoveredSignals, geo.text);
        }
    });
});
