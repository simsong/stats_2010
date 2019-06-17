google.charts.load('current', {callback: generateChartParameters, packages: ['corechart', 'line']});

// Convert UNIX timestamps to a JavaScript date object
function converted_UNIX_Time(UNIX_timestamp){
    return new Date(UNIX_timestamp * 1000);
}

// Generates the parameters to be used by the chart. 
// Data is related to columbs and will be used to add data from API. Options is related to formatting
function generateChartParameters(){
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'time');
    data.addColumn('number', 'Licenses\n available');
    
    var options = {
        title: 'Gurobi Licenses Available',
        hAxis: {
            title: 'Time'
        },
        vAxis: {
            title: 'Licenses Available',
            format:'0'
        },
        explorer: {
            axis: 'horizontal',
            keepInBounds: true,
            maxZoomIn: 4.0
        }
    };

    getDataFromAPI(data, options);
}

// Get the data from the API and then graph 
function getDataFromAPI(data,options){
    fetch("/cgi-bin/get_stats.cgi?seconds=3600")
        .then(function(response){
            return response.json();
        })
        .then(function(result){
            var hostNameList = result.sysload.hostName
            var timeList  = result.sysload.time_t
            var min1_List = result.sysload.min1
        
            // Temporarily i will just be graphing a single host
            var hostName = hostNameList[0]

            var rows = timeList.map(function(time, i){
                if(hostNameList[i] == hostName)
                    return [converted_UNIX_Time(time), min1_List[i]]
            });
	    
            drawChart(rows, data, options);
        });   
}

// Draws the chart. Handles failure
function drawChart(rows, data, options) {
    data.addRows(rows);
    // Put the chart in the DIV
    var chart = new google.visualization.LineChart(document.getElementById('gurobi_chart'));
    chart.draw(data, options);
}

// Wire up the buttons to change the amount seen
// This requires a new database fetch



