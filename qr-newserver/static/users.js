async function fetchData() {
    const response = await fetch('/user');
    console.log(response);
    if(response.redirected)
    {
	window.location.href = "/";
	return;
    }
    const data = await response.json();
    return data;
}

async function fetchPk()
{
    const response = await fetch('/pk?name=usuarios');
    const data = await response.json();
    return data;
}

let modalEditContent = document.getElementById("modalEditContent");
let modalCreateContent = document.getElementById("modalCreateContent");
let fields;
let data;
let pk;

let deleteSelected = function()
{
    let cbs = document.getElementsByName("checkxD");
    let pksToRemove = [];
    for(i=0;i<cbs.length;i++)
	if(cbs[i].checked) pksToRemove.push(data[i][pk]);
    if(!pksToRemove.length) return;
    console.log(cbs);
    console.log(pksToRemove);
    $("#btnConfirmDelete").unbind('click');
    $("#btnConfirmDelete").click(() => {
	content = {"pk": pksToRemove};
	console.log(content);
	deleteRecord(content);
    });
    $("#modalDelete").modal('toggle');
}

let updateFetch = function ()
{
    let tableData = document.getElementById("table");
    fetchData().then(temp => {
	data = temp;
	//console.log(data);
	fields = Object.keys(data[0]);
	let cont = 0;
	//set header of table
	let table = `
<div class='row bg-primary text-white' style="padding: 10px;">
<div class='col-sm-4'><h3>Gestion de <b>Usuarios</b></h3></div>
<div class='col-sm-8 text-end'>
<button class='btn btn-success' style="border-radius:4px;" onclick="openModalCreate()">
<i class='material-icons' style="vertical-align:middle;">add_circle</i>
<span style="vertical-align:middle;">Agregar</span>
</button>
<button class='btn btn-danger' onclick="deleteSelected()" data-toggle='modal' style="border-radius:4px;">
<i class='material-icons' style="vertical-align:middle;">remove_circle</i>
<span style="vertical-align:middle;">Eliminar Usuario(s)</span>
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
	    if(row[pk] == null) continue;
	    cont++;
	    table += 
		`<tr>`;
	    values = Object.values(row);
	    table += `<td class="text-center"><input type="checkbox" name="checkxD" class="form-check-input"></input></td>`
	    table += `<td class="text-center">${i}</td>`;
	    for(j=0;j<values.length;j++)
		table += `<td class="text-center">${values[j]}</td>`;
	    table += `
<td class="text-center">
<a href="javascript:openModalEdit(${i})">
<i class='material-icons' data-bs-toggle='tooltip' title="Editar" data-bs-placement="top" style="color:#FFC107;">create</i>
</a>
<a href="javascript:openModalDelete(${i})">
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
<div class="text-hint">Mostrando <b>${cont}</b> de <b>${cont}</b> resultados</div>
</div>
`
	;

	tableData.innerHTML = table;
	document.querySelector('#checkAll')
	    .addEventListener('change', changeCheckboxes);
	updateModalEdit();
	updateModalCreate();
    }).catch(error => {
	//console.log("error catcheado");
    });
}

fetchPk().then(temp => {
    pk = temp["pk"];
    console.log(pk);
    updateFetch();
});

let editRecord = function(content)
{
    fetch("/user", {
	method: "POST",
	headers: {'Content-Type': 'application/json'},
	body: JSON.stringify(content)
    }).then(res => {
	res.json().then(res => {
	    console.log("Request complete! response:", res);
	    if(res["success"] === 1){
		updateFetch(); $("#modalEdit").modal('toggle');}
	    
	});
    });   
}

let createRecord = function(content)
{
    fetch("/user", {
	method: "POST",
	headers: {'Content-Type': 'application/json'},
	body: JSON.stringify(content)
    }).then(res => {
	res.json().then(res => {
	    console.log("Request complete! response:", res);
	    if(res["success"] === 1){
		updateFetch(); $("#modalCreate").modal('toggle');}
	    
	});
    });       
}
    

let deleteRecord = function(content)
{
    fetch("/user/delete", {
	method: "POST",
	headers: {'Content-Type': 'application/json'},
	body: JSON.stringify(content)
    }).then(res => {
	res.json().then(res => {
	    console.log("Request complete! response:", res);
	    if(res["success"] === 1){
		updateFetch(); $("#modalDelete").modal('toggle');}
	    
	});
    });       
}

let openModalEdit = function(id)
{
    fields.forEach(field => {
	$(`[id='${field}']`).val(data[id][`${field}`]);
	//$(`#${field}`).val(data[id][`${field}`]);
    });

    $("#btnConfirmEdit").unbind('click');
    $("#btnConfirmEdit").on('click', () => {
	content = {};
	fields.forEach(field => {
	    content[field] = $(`#${field}`).val();
	});
	content["pk"] = data[id][pk];
	console.log(content);
	editRecord(content);
    });

    $("#modalEdit").modal('toggle');
}

let openModalCreate = function()
{
    $("#btnConfirmCreate").unbind('click');
    $("#btnConfirmCreate").on('click', () => {
	content = {};
	fields.forEach(field => {
	    content[field] = $(`#create${field}`).val();
	});
	content["pk"] = content[pk];
	content["create"] = 1;
	console.log(content);
	createRecord(content);
    });

    $("#modalCreate").modal('toggle');
}

let openModalDelete = function(id)
{
    console.log(data);
    console.log(id);
    $("#btnConfirmDelete").unbind('click');
    $("#btnConfirmDelete").click(() => {
	content = {"pk": data[id][pk]};
	console.log(content);
	deleteRecord(content);
    });

    $("#modalDelete").modal('toggle');
}

let updateModalEdit = function()
{
    if(!fields) return;
    let content = "<form>";
    fields.forEach(field =>
	{
	    content += `
<label for="${field}">${field}</label>
<input type="text" class="form-control" id="${field}" placeholder="">
		`;
	});
    content += "</form>";
    modalEditContent.innerHTML = content;
}

let updateModalCreate = function()
{
    if(!fields) return;
    let content = "<form>";
    fields.forEach(field =>
	{
	    content += `
<label for="${field}">${field}</label>
<input type="text" class="form-control" id="create${field}" placeholder="">
		`;
	});
    content += "</form>";
    modalCreateContent.innerHTML = content;    
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




