// Function to update the modal content
function updateSelectedSignalsModal() {
    var selectedSignals = localStorage.getItem('selectedSignals');
    var signals = selectedSignals ? JSON.parse(selectedSignals) : {};

    var selectedSignalsList = document.getElementById('selectedSignalsList');
    selectedSignalsList.innerHTML = ''; // Clear existing items


    for (const signal in signals) {
        let data = JSON.parse(localStorage.getItem("selectedSignals"))[signal];
        console.log(data);
        var tr = document.createElement('tr');
        var memberName = document.createElement('td');
        memberName.textContent = data['info']['memberName'];
        tr.appendChild(memberName);
        var memberDescription = document.createElement('td');
        memberDescription.textContent = data['info']['memberDescription'];
        tr.appendChild(memberDescription);
        var dataSource = document.createElement('td');
        dataSource.textContent = data['epivis']['params']['data_source'];
        tr.appendChild(dataSource);
        var signalName = document.createElement('td');
        signalName.textContent = data['epivis']['params']['signal'];
        tr.appendChild(signalName);
        var timeType = document.createElement('td');
        timeType.textContent = data['epivis']['params']['time_type'];
        tr.appendChild(timeType);
        var geoType = document.createElement('td');
        geoType.textContent = data['epivis']['params']['geo_type'];
        tr.appendChild(geoType);
        var geoValue = document.createElement('td');
        geoValue.textContent = data['epivis']['params']['geo_value'];
        tr.appendChild(geoValue);
        selectedSignalsList.appendChild(tr);
    }
}

function addSelectedSignals(dataSource, timeType, signalSetEndpoint) {
    let selectedSignals = localStorage.getItem("selectedSignals");
    selectedSignals = selectedSignals ? JSON.parse(selectedSignals) : {};
    var dataSignals = Array.from(document.getElementsByName('selectedSignal'), (signal) => (signal.checked) ? signal : null).filter((el) => el !== null);
    var geographicType = document.getElementById('geographic_type').value;
    // geographicValue is a comma separated string of geographic values. type can be string or integer
    // in case of string, it should be converted to lowercase
    // else it will be treated as integer
    var geographicValue = $('#geographic_value').select2('data').map((el) => (typeof el.id === 'string') ? el.id.toLowerCase() : el.id).join(',');

    if (geographicType === 'Choose...' || geographicValue === '') {
        showWarningAlert("Geographic Type or Geographic Value is not selected.");
        return;
    }

    var geographicValues = geographicValue.split(',');
    dataSignals.forEach((signal) => {
        geographicValues.forEach((geographicValue) => {
            selectedSignals[`${signal.value}_${geographicValue}`] = {
                info: {
                    memberName: signal.getAttribute('data-member-name'),
                    memberDescription: signal.getAttribute('data-member-description'), 
                },
                epivis: {
                color: '#' + (Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0'),
                title: "value",
                params: {
                    _endpoint: signalSetEndpoint,
                    data_source: dataSource,
                    signal: signal.value,
                    time_type: timeType,
                    geo_type: geographicType,
                    geo_value: geographicValue
                }
            }
            };
        });
    });
    localStorage.setItem("selectedSignals", JSON.stringify(selectedSignals));
    updateSelectedSignalsModal();
    $("#showSelectedSignalsButton").show();
}



document.addEventListener('DOMContentLoaded', function() {
    // Call the function to update the modal content when the page loads
    updateSelectedSignalsModal();

});



//for (const signal in JSON.parse(localStorage.getItem("selectedSignals"))) {console.log(JSON.parse(localStorage.getItem("selectedSignals"))[signal])}