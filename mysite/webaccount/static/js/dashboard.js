$(document).ready(function(){
    $("select#exampleFormControlSelect1").on("change", function(event){
        $(this).parent().parent().submit();
    });
});


    const New_Consultant_Manager_Counts = JSON.parse(document.getElementById('New_Consultant_Manager_Counts').textContent);
    const Confirmed_Consultant_Manager_Counts = JSON.parse(document.getElementById('Confirmed_Consultant_Manager_Counts').textContent);
    const Pending_Consultant_Manager_Counts = JSON.parse(document.getElementById('Pending_Consultant_Manager_Counts').textContent);
    const Completed_Consultant_Manager_Counts = JSON.parse(document.getElementById('Completed_Consultant_Manager_Counts').textContent);
    const Close_Consultant_Manager_Counts = JSON.parse(document.getElementById('Close_Consultant_Manager_Counts').textContent);
    const Rejected_Consultant_Manager_Counts = JSON.parse(document.getElementById('Rejected_Consultant_Manager_Counts').textContent);
    const Declined_Consultant_Manager_Counts = JSON.parse(document.getElementById('Declined_Consultant_Manager_Counts').textContent);

    const accept_pick_up_request_order_counts = JSON.parse(document.getElementById('accept_pick_up_request_order_counts').textContent);
    const reject_pick_up_request_order_counts = JSON.parse(document.getElementById('reject_pick_up_request_order_counts').textContent);
    const on_delivery_pick_up_request_order_counts = JSON.parse(document.getElementById('on_delivery_pick_up_request_order_counts').textContent);
    const receive_pick_up_request_order_counts = JSON.parse(document.getElementById('receive_pick_up_request_order_counts').textContent);
    const failed_pick_up_request_order_counts = JSON.parse(document.getElementById('failed_pick_up_request_order_counts').textContent);
    const pending_pick_up_request_order_counts = JSON.parse(document.getElementById('pending_pick_up_request_order_counts').textContent);

    const   new_client_invoice  =   JSON.parse(document.getElementById('new_client_invoice').textContent);
    const   approved_client_invoice =   JSON.parse(document.getElementById('approved_client_invoice').textContent);
    const   rejected_client_invoice =   JSON.parse(document.getElementById('rejected_client_invoice').textContent);
    const   processed_client_invoice    =   JSON.parse(document.getElementById('processed_client_invoice').textContent);
    const   postponed_client_invoice    =   JSON.parse(document.getElementById('postponed_client_invoice').textContent);

    const   New_Client_Personal_Info_Objects_counts =   JSON.parse(document.getElementById('New_Client_Personal_Info_Objects_counts').textContent);
    const   Active_Client_Personal_Info_Objects_counts  =   JSON.parse(document.getElementById('Active_Client_Personal_Info_Objects_counts').textContent);
    const   Pending_Client_Personal_Info_Objects_counts =   JSON.parse(document.getElementById('Pending_Client_Personal_Info_Objects_counts').textContent);
    const   Completed_Client_Personal_Info_Objects_counts   =   JSON.parse(document.getElementById('Completed_Client_Personal_Info_Objects_counts').textContent);
    const   Disabled_Client_Personal_Info_Objects_counts    =   JSON.parse(document.getElementById('Disabled_Client_Personal_Info_Objects_counts').textContent);

    const  vat_amount  = JSON.parse(document.getElementById("vat_amount").textContent);
    const  book_amount  = JSON.parse(document.getElementById("book_amount").textContent);
    

    const sector_dict = JSON.parse(document.getElementById("sector_dict").textContent);
    const sector_keys= Object.keys(sector_dict);

    // Calculate Percentages of Each Sector Paid Amount
    // console.debug();

    var secotrLabels = [];
    var sector_data = [];
    var backGroundColorsData = [];
    var borderColorsData = [];
    
    // console.debug(sector_dict);
    for(var index = 0; index < sector_keys.length; index++){
        // console.debug(Object.keys(sector_dict)[index]);
        secotrLabels.push([sector_keys[index]]);
        sector_data.push(sector_dict[sector_keys[index]]);
        backGroundColorsData.push("rgb(255, " +  parseInt((Math.random()*(255-0)+0)) +  ", " + parseInt((Math.random()*(255-0)+0)) + ", 0.2)");
        borderColorsData.push("rgb(255, " +  parseInt((Math.random()*(255-0)+0)) +  ", " + parseInt((Math.random()*(255-0)+0)) + ", 1)");
    }

    // console.debug(sector_dict);

    

    // console.debug(escape(sector_objects));

    // Pie Chart # 1
    // Pie Charts Sector Paid Amount 
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: secotrLabels,
            datasets: [{
                label: '# of Votes',
                data: sector_data,
                backgroundColor: backGroundColorsData,
                borderColor: borderColorsData,
                borderWidth: 1
            }]
        },
        options: {
            
        }
    });

    

    // Pie Chart # 2
    var ctx = document.getElementById('myChart2').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['VAT', 'Book Keeping'],
            datasets: [{
                label: '# of Votes',
                data: [vat_amount, book_amount],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            
        }
    });
    


        // Pie Chart # 3
        var ctx = document.getElementById('myChart3').getContext('2d');
        var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['New', 'Active', 'Pending', 'Completed', 'Disbaled'],
            datasets: [{
                label: '# of Votes',
                data: [
                    New_Client_Personal_Info_Objects_counts,
                    Active_Client_Personal_Info_Objects_counts,
                    Pending_Client_Personal_Info_Objects_counts,
                    Completed_Client_Personal_Info_Objects_counts,
                    Disabled_Client_Personal_Info_Objects_counts
                ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            
        }
    });

    
        // Pie Chart # 4
        var ctx = document.getElementById('myChart4').getContext('2d');
        var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['New', 'Approved', 'Rejected', 'Processed', 'Postponed'],
            datasets: [{
                label: '# of Votes',
                data: [
                        new_client_invoice,
                        approved_client_invoice,
                        rejected_client_invoice,
                        processed_client_invoice,
                        postponed_client_invoice
                ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            
        }
    });


        // Pie Chart # 5
        // Pick Up Requests Statistics (By Status) 
        var ctx = document.getElementById('myChart5').getContext('2d');
        var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: [ 'Accepted', 'Rejected', 'On Delivery', 'Recieved', 'Failed', 'Pending'],
            datasets: [{
                label: '# of Votes',
                data: [
                            accept_pick_up_request_order_counts,
                            reject_pick_up_request_order_counts,
                            on_delivery_pick_up_request_order_counts,
                            receive_pick_up_request_order_counts,
                            failed_pick_up_request_order_counts,
                            pending_pick_up_request_order_counts
                ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            
        }
    });

        // Pie Chart # 6
        // Consultation Requests By Status Pie Chart
        var ctx = document.getElementById('myChart6').getContext('2d');
        var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['New', 'Confirmed', 'Pending', 'Completed', 'Close', 'Rejected', "Declined"],
            datasets: [{
                label: '# of Votes',
                data: [New_Consultant_Manager_Counts, Confirmed_Consultant_Manager_Counts, Pending_Consultant_Manager_Counts, Completed_Consultant_Manager_Counts, Close_Consultant_Manager_Counts, Rejected_Consultant_Manager_Counts, Declined_Consultant_Manager_Counts],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 35, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(45, 205, 150, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 35, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 205, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            
        }
    });
