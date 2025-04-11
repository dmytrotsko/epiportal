const indicatorHandler = new IndicatorHandler();

function initSelect2(elementId, data) {
    $(`#${elementId}`).select2({
        data: data,
        minimumInputLength: 0,
        maximumSelectionLength: 5,
    });
}

let checkedSignalMembers = []

function showWarningAlert(warningMessage, slideUpTime = 2000) {
    $("#warning-alert").html(warningMessage);
    $("#warning-alert").fadeTo(2000, 500).slideUp(slideUpTime, function() {
        $("#warning-alert").slideUp(slideUpTime);
    });
}

async function checkGeoCoverage(geoType, geoValue) {
    const notCoveredSignals = [];
    
    try {
        const result = await $.ajax({
            url: "epidata/covidcast/geo_coverage/",
            type: 'GET',
            data: {
                'geo': `${geoType}:${geoValue}`
            }
        });
        
        checkedSignalMembers.filter(signal => signal["_endpoint"] === "covidcast").forEach(signal => {
            const covered = result["epidata"].some(
                e => (e.source === signal.data_source && e.signal === signal.signal)
            );
            if (!covered) {s
                notCoveredSignals.push(signal);
            }
        });
        
        return notCoveredSignals;
    } catch (error) {
        console.error('Error fetching geo coverage:', error);
        return notCoveredSignals;
    }
}

// Function to update the modal content
function updateSelectedSignals(dataSource, signalDisplayName, signalSet, signal) {
    var selectedSignalsList = document.getElementById('selectedSignalsList');

    var tr = document.createElement('tr');
    tr.setAttribute('id', `${dataSource}_${signal}`);
    var signalSetName = document.createElement('td');
    signalSetName.textContent = signalSet;
    tr.appendChild(signalSetName);
    var signalName = document.createElement('td');
    signalName.textContent = signalDisplayName;
    tr.appendChild(signalName);
    selectedSignalsList.appendChild(tr);
}

function addSelectedSignal(element) {
    if (element.checked) {
        checkedSignalMembers.push({
            _endpoint: element.dataset.endpoint,
            data_source: element.dataset.datasource,
            signal: element.dataset.signal,
            time_type: element.dataset.timeType,
            signal_set: element.dataset.signalSet,
            display_name: element.dataset.signalDisplayname,
            signal_set_short_name: element.dataset.signalSetShortName,
            member_short_name: element.dataset.memberShortName
        });
        updateSelectedSignals(element.dataset.datasource, element.dataset.signalDisplayname, element.dataset.signalSet, element.dataset.signal);
    } else {
        checkedSignalMembers = checkedSignalMembers.filter(signal => signal.signal !== element.dataset.signal);
        document.getElementById(`${element.dataset.datasource}_${element.dataset.signal}`).remove();
    }

    indicatorHandler.indicators = checkedSignalMembers;

    if (checkedSignalMembers.length > 0) {
        $("#showSelectedSignalsButton").show();
    } else {
        $("#showSelectedSignalsButton").hide();
    }
}

$("#showSelectedSignalsButton").click(function() {
    alertPlaceholder.innerHTML = "";
    if (!indicatorHandler.checkForCovidcastIndicators()) {
        $("#geographic_value").prop("disabled", true);
    } else {
        $("#geographic_value").prop("disabled", false);
    }
    $('#geographic_value').select2("data").forEach(geo => {
        checkGeoCoverage(geo.geoType, geo.id).then((notCoveredSignals) => {
            if (notCoveredSignals.length > 0) {
                showNotCoveredGeoWarningMessage(notCoveredSignals, geo.text);
            }
        })
    });
    var otherEndpointLocationsWarning = `<div class="alert alert-info" data-mdb-alert-init role="alert">` +
    `   <div>Please, note that some indicator sets may require to select location(s) that is/are different from location above.<br> `
    nonCovidcastSignalSets = [...new Set(checkedSignalMembers.filter(signal => signal["_endpoint"] != "covidcast").map((signal) => signal["signal_set"]))];
    otherEndpointLocationsWarning += `Different location is required for following signal set(s): ${nonCovidcastSignalSets.join(", ")}`
    otherEndpointLocationsWarning += `</div></div>`
    if (indicatorHandler.getFluviewIndicators().length > 0) {
        $("#differentLocationNote").html(otherEndpointLocationsWarning)
        if (document.getElementsByName("fluviewRegions").length === 0) {
            indicatorHandler.showFluviewRegions();
        }
    }
});

// Add an event listener to each 'bulk-select' element
let bulkSelectDivs = document.querySelectorAll('.bulk-select');
bulkSelectDivs.forEach(div => {
    div.addEventListener('click', function(event) {
        let form = this.nextElementSibling;
        let showMoreLink = form.querySelector('a');
        let checkboxes = form.querySelectorAll('input[type="checkbox"]');

        if (event.target.checked === true) {
            checkboxes.forEach((checkbox, index) => {
                checkbox.checked = true;
                if (index > 4) {
                    checkbox.parentElement.style.display = checkbox.parentElement.style.display === 'none' ? 'block' : null;
                }
            })
            if (showMoreLink) {
                showMoreLink.innerText = 'Show less...';
            }
        } else if (event.target.checked === false) {
            checkboxes.forEach((checkbox, index) => {
                checkbox.checked = false
                if (index > 4) {
                    checkbox.parentElement.style.display = checkbox.parentElement.style.display === 'block' ? 'none' : null;
                }
            });
            if (showMoreLink) {
                showMoreLink.innerText = 'Show more...';
            }
        }
    });
});

var tableHeight = window.screen.width / 3.4;

function calculate_table_height() {
    var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
    var percent = 60;
    if (h > 1000) {
        percent = 70;
    }
    return (percent * h) / 100;
}


var table = new DataTable('#signalSetsTable', {
    fixedHeader: true,
    searching: false,
    paging: false,
    scrollCollapse: true,
    scrollX: true,
    scrollY: calculate_table_height() + 75,
    info: false,
    fixedColumns: {
        left: 2
    },
    ordering: false,
    mark: true,
    
    language: {
        buttons: {
            colvis: "Toggle Columns"
        }
    }
});
  

new DataTable.Buttons(table, {
    buttons: [
        {
            extend: 'colvis',
            columns: 'th:nth-child(n+3)',
            prefixButtons: ['colvisRestore']
        }
    ]
});
 
table
    .buttons(0, null)
    .container()
    .appendTo("#colvis");


function format (signalSetId, relatedSignals, signalSetDescription) {
    var signals = relatedSignals.filter((signal) => signal.signal_set === signalSetId)
    var disabled, restricted;

    if (signals.length > 0) {
        var data = `<p style="width: 40%;">${signalSetDescription}</p>`
        var tableMarkup = '<table class="table" cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
                    '<thead>'+
                        '<th></th>'+
                        '<th>Indicator Name</th>'+
                        '<th>Indicator API Name</th>'+
                        '<th>Indicator Description</th>'+
                        '<th></th>'+
                    '</thead>'+
                    '<tbody>'
        signals.forEach((signal) => {
            checked = checkedSignalMembers.filter((obj) => obj.data_source == signal.source && obj.signal == signal.name).length;
            var checkboxTitle = ""
            checked = checked ? "checked" : ""
            disabled = signal.endpoint ? "" : "disabled";
            var restricted = signal.restricted != "No";
            if (disabled === "disabled") {
                checkboxTitle = "Visualization functionality for this endpoint is coming soon."
            }
            if (restricted) {
                disabled = "disabled";
                checkboxTitle = "Access to this data source is restricted. Contact delphi-support@andrew.cmu.edu for more information."
            }
            tableMarkup += '<tr>'+
                                `<td><input ${disabled} title="${checkboxTitle}" type="checkbox" name="selectedSignal" onclick="addSelectedSignal(this)" data-signal-displayname='${signal.display_name}' data-endpoint="${signal.endpoint}" data-datasource="${signal.source}" data-signal="${signal.name}" data-time-type="${signal.time_type}" data-signal-set="${signal.signal_set_name}" data-signal-set-short-name="${signal.signal_set_short_name}" data-member-short-name="${signal.member_short_name}" ${checked}></td>`+
                                `<td>${signal.display_name}</td>`+
                                `<td>${signal.member_name}</td>`+
                                `<td>${signal.member_description}</td>`+
                                '<td style="width: 60%"></td>'+
                            '</tr>'
        }) 
        tableMarkup += '</tbody></table>'
        if (disabled === "disabled" || restricted) {
            data += `<div class="alert alert-warning" data-mdb-alert-init role="alert">` +
                    `   <div>This indicator set is available via the <a href="https://cmu-delphi.github.io/delphi-epidata/">Epidata API</a>, and directly via <a href="https://delphi.cmu.edu/epivis/">Epivis</a>, but is not yet available via this interface.</div>` +
                    '</div>'
        }
        data += tableMarkup;
    } else {
        data = "<p>No available indicators yet.</p>"
    }
    return data;
}

// Plot/Export/Preview data block

var currentMode = 'epivis';


function handleModeChange(mode) {
    $('#modeSubmitResult').html('');

    var choose_dates = document.getElementsByName('choose_date');

    if (mode === 'epivis') {
        currentMode = 'epivis';
        choose_dates.forEach((el) => {
            el.style.display = 'none';
        });
        $('#modeSubmitResult').html('');
    } else if (mode === 'export') {
        currentMode = 'export';
        choose_dates.forEach((el) => {
            el.style.display = 'flex';
        });
        $('#modeSubmitResult').html('');
    } else {
        currentMode = 'preview';
        choose_dates.forEach((el) => {
            el.style.display = 'flex';
        });
    }
    document.getElementsByName("modes").forEach((el) => {
        if (currentMode === el.value) {
            el.checked = true;
        }
    });
}

function hideAlert(alertId) {
    const alert = document.getElementById(alertId);
    if (alert) {
        alert.remove();
    }
}



const alertPlaceholder = document.getElementById('warning-alert')
const appendAlert = (message, type) => {
    const wrapper = document.createElement('div')
    const alertId = `alert-${Date.now()}`;
    wrapper.innerHTML = [
      `<div id="${alertId}" class="alert alert-${type} alert-dismissible" data-mdb-alert-init role="alert">`,
      `   <div>${message}</div>`,
      '   <button type="button" class="btn-close" data-mdb-dismiss="alert" aria-label="Close"></button>',
      '</div>'
    ].join('')
  
    alertPlaceholder.append(wrapper)
    wrapper.getElementsByClassName('btn-close')[0].addEventListener('click', () => hideAlert(alertId))
  }

function showNotCoveredGeoWarningMessage(notCoveredSignals, geoValue) {
    var warningMessage = "";
    notCoveredSignals.forEach(signal => {
        if (currentMode === 'epivis') {
            warningMessage += `Indicator ${signal.display_name} is not available for Location ${geoValue} <br>`
        } else {
            var startDate = document.getElementById("start_date").value;
            var endDate = document.getElementById("end_date").value;
            warningMessage += `Indicator ${signal.display_name} is not available for Location ${geoValue} for the time period from ${startDate} to ${endDate} <br>` 
        }
    })
    appendAlert(warningMessage, "warning")
}

$('#geographic_value').on('select2:select', function (e) {
    var geo = e.params.data;
    checkGeoCoverage(geo.geoType, geo.id).then((notCoveredSignals) => {
        if (notCoveredSignals.length > 0) {
            showNotCoveredGeoWarningMessage(notCoveredSignals, geo.text);
        }
    }
    );
});


function submitMode(event) {
    event.preventDefault();
    var geographicValues = $('#geographic_value').select2('data');
    if (indicatorHandler.checkForCovidcastIndicators()) {
        if (geographicValues.length === 0) {
            appendAlert("Please select at least one geographic location", "warning")
            return;
        }
    }

    if (currentMode === 'epivis') {
        indicatorHandler.plotData();
    } else if (currentMode === 'export') {
        indicatorHandler.exportData();
    } else {
        indicatorHandler.previewData();
    }
}

const isPlural = num => Math.abs(num) !== 1;
const simplePlural = word => `${word}s`;
const pluralize = (num, word, plural = simplePlural) =>
  isPlural(num) ? plural(word) : word;