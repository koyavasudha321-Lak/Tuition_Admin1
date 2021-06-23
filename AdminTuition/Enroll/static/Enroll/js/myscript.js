function searchRecords(){
	var input, table, tr, td, filter, i, txtdata;
	input = document.getElementById("myInput");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr= table.getElementsByTagName("tr")
	for(i = 0;i < tr.length;i++){
		td=tr[i].getElementsByTagName("td")[0];
		if(td){
			txtdata = td.textContent || td.innerText;
			if(txtdata.toUpperCase().indexOf(filter) > -1){
				tr[i].style.display="";
			}
			else{
				tr[i].style.display="none";
			}
		}
	}
}

function cleartxt(){
	document.getElementById('myInput').value="";
	document.getElementById("myInput").focus();
}

function msg(){
	alert("Successfully Updated!!!");
}

