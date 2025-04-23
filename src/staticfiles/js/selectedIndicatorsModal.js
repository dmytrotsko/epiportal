let checkedIndicatorMembers = []

function updateSelectedIndicators(dataSource, indicatorDisplayName, indicatorSet, indicator) {
    var selectedIndicatorsList = document.getElementById('selectedIndicatorsList');

    var tr = document.createElement('tr');
    tr.setAttribute('id', `${dataSource}_${indicator}`);
    var indicatorSetName = document.createElement('td');
    indicatorSetName.textContent = indicatorSet;
    tr.appendChild(indicatorSetName);
    var indicatorName = document.createElement('td');
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
            member_short_name: element.dataset.memberShortName
        });
        updateSelectedIndicators(element.dataset.datasource, element.dataset.indicatorDisplayname, element.dataset.indicatorSet, element.dataset.indicator);
    } else {
        checkedIndicatorMembers = checkedIndicatorMembers.filter(indicator => indicator.indicator !== element.dataset.indicator);
        document.getElementById(`${element.dataset.datasource}_${element.dataset.indicator}`).remove();
    }

    //indicatorHandler.indicators = checkedSignalMembers;

    if (checkedIndicatorMembers.length > 0) {
        $("#showSelectedIndicatorsButton").show();
    } else {
        $("#showSelectedIndicatorsButton").hide();
    }
}