async function fetchData() {
  const response = await fetch('/user');
  const data = await response.json();
  return data;
}

let changeCheckboxes = function()
{
    var og = document.getElementById('checkAll');
    var cbs = document.getElementsByName('checkxD');
    console.log(cbs);
    cbs.forEach(cb => {
	cb.checked = og.checked;
	cb.dispatchEvent(new Event('change'));
    });
}

let tableData = document.getElementById("table");
fetchData().then(data => {
    //console.log(data);
    fields = Object.keys(data[0]);

    
    //set header of table

    let table = `
<div class='row bg-primary text-white' style="padding: 10px;">
<div class='col-sm-4'><h3>Gestion de <b>Usuarios</b></h3></div>
<div class='col-sm-8 text-end'>
<button class='btn btn-success' style="border-radius:4px;" data-toggle='modal'>
<i class='material-icons' style="vertical-align:middle;">add_circle</i>
<span style="vertical-align:middle;">Agregar</span>
</button>
<button class='btn btn-danger' data-toggle='modal' style="border-radius:4px;">
<i class='material-icons' style="vertical-align:middle;">remove_circle</i>
<span style="vertical-align:middle;">Eliminar Usuario</span>
</button>
</div>
</div>
<div class="row">

<table class="table table-hover table-bordered" id = "myTable">
  <thead class="table-primary">
    <tr>`;
    table += `<th class="text-center"><input type="checkbox" id="checkAll" class="form-check-input"></input></th>`
    table += "<th scope='col' class='text-center'>#</th>";
     for(i=0;i<fields.length;i++)
	 table += `<th scope="col" class="text-center">${fields[i]}</th>`;
    table += `<th class='text-center'>Accion</th>`;
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
	table += `<td class="text-center"><input type="checkbox" name="checkxD" class="form-check-input"></input></td>`
	table += `<td class="text-center">${i}</td>`;
	for(j=0;j<values.length;j++)
	{
	    table += `<td class="text-center">${values[j]}</td>`;
	}
	table += `
<td class="text-center">
<a data-bs-toggle="modal" href="#modalEdit">
<i class='material-icons' data-bs-toggle='tooltip' title="Editar" data-bs-placement="top" style="color:#FFC107;">create</i>
</a>
<a data-bs-toggle="modal" href="#modalDelete">
<i class='material-icons' data-bs-toggle='tooltip' title="Eliminar" data-bs-placement="left" style="color:#F44336;">delete</i>
</a>
</td>

`;
	
	table += `</tr>`;
    }
    //close off table
    table +=
	`</tbody>
  </table>
<div class="text-hint">Mostrando <b>${data.length}</b> de <b>${data.length}</b> resultados</div>
</div>
`

    ;

    tableData.innerHTML = table;
    document.querySelector('#checkAll')
	.addEventListener('change', changeCheckboxes);
});


