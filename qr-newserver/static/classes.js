async function fetchData() {
  const response = await fetch('/class');
  const data = await response.json();
  return data;
}
let tableData = document.getElementById("table");
fetchData().then(data => {
    //console.log(data);
    fields = Object.keys(data[0]);

    
    //set header of table

    let table = `
<table class="table table-striped table-hover table-bordered" id = "myTable">
  <thead class="table-dark">
    <tr>`;
    table += "<th scope='col' class='text-center'>#</th>";
     for(i=0;i<fields.length;i++)
	 table += `<th scope="col" class="text-center">${fields[i]}</th>`;
    table += `
        </tr>
  </thead>
  <tbody>
  `;
    //create//append rows
    for(i = 0; i < data.length; i++){
	let row = data[i];
	table += 
	    `<tr>`;
	values = Object.values(row);
	table += `<td class="text-center">${i}</td>`;
	for(j=0;j<values.length;j++)
	{
	    table += `<td class="text-center">${values[j]}</td>`;
	}
	table += `</tr>`;
    }
    //close off table
    table +=
	`</tbody>
  </table>`
    ;

    tableData.innerHTML = table;

});
