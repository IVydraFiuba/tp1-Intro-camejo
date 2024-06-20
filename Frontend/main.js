// La tabla y su configuracion (tambien del tutorial)
let dataTable;
const ConfigDataTable = {
    columnDefs:[
        {className:"centrado",targets:[0,1,2,3,4]}
    ],
    lengthMenu:[10,20,30,40,50],
    pageLength: 10,
    destroy:true,
    language:{
        emptyTable: "No hay insumos cargados",
        lengthMenu: "Mostrar _MENU_ registros por pagina",
        zeroRecords: "Ningun insumo encontrado",
        info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ insumos",
        infoEmpty: "Ningun insumo encontrado",
        infoFiltered: "(filtrados desde _MAX_ insumos totales)",
        search: "Buscar:",
        loadingRecords: "Cargando...",
        paginate:{
            first: "Primero",
            last: "Ultimo",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
}
// Esto es algo del tutorial(la idea es destruir la tabla y volverla a crear para reiniciarla)
let dataTableInicializada = false;

function iniciar_tabla_insumos(){
    if (dataTableInicializada){
        dataTable.destroy();
        }
    fetch("http://localhost:5000/insumos")
            .then((respuesta) => respuesta.json())
            .then(procesar_datos)
            .catch((error) => console.log("ERROR", error))
    };

function procesar_datos(contenido){
    const cuerpo_tabla = document.getElementById("Data_insumos")
    
    function pintar_datos(datos,index,contenido,fila){
        for (let dato of datos){
            const columna = document.createElement("td");
            columna.textContent = contenido[index][dato];
            fila.append(columna)
        }
    }
    let datos = ['Id','Codigo','Descripcion','Presentacion','Rendimiento']
    for (let index = 0; index < contenido.length; index++){
        const fila = document.createElement("tr");
        pintar_datos(datos,index,contenido,fila)
        cuerpo_tabla.append(fila)
    }
    //Inicializo la Datatabla
    dataTable=$("#Tabla_insumos").DataTable(ConfigDataTable);
    dataTableInicializada = true;
}

iniciar_tabla_insumos()  







//Esta parte es la del FORMULARIO

//tengo que cambiar esta funcion
function handle_response(data) {
    if (data.success) {
        location.reload();
    } else {
        alert("Error")
    }
}

function cargar_nuevo_insumo(event){
    event.preventDefault()
    const formData = new FormData(event.target)

    const codigo = formData.get("codigo")
    const descripcion = formData.get("descripcion")
    const presentacion = formData.get("presentacion")
    const rendimiento = formData.get("rendimiento")

    fetch("http://localhost:5000/insumos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            codigo: codigo,
            descripcion: descripcion,
            presentacion: presentacion,
            rendimiento: rendimiento
        })
    })
        .then((respuesta) => respuesta.json())
        .then(handle_response)
        .catch((error) => console.log("ERROR", error))
}
