fetch("http://localhost:5000/Inicio/usuarios")
            .then((respuesta) => respuesta.json())
            .then(procesar_datos)
            .catch((error) => console.log("ERROR", error))

function procesar_datos(contenido){
    console.log(contenido)
}




function handle_response(data) {
    if (data.success) {
        let respuesta = confirm("Quires empezar la partida con el?")
        if (respuesta) {
            alert("Iniciando...")
        }
    } else {
        alert("Error al crear el personaje ")
    }
}
function cargar_nuevo_personaje(event){
    event.preventDefault()
    const DataFormulario = new FormData(event.target)

    const Nom_usuario = DataFormulario.get("nom_usuario")
    const Nom_mercado = DataFormulario.get("nom_mercado")

    fetch("http://localhost:5000/Inicio", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nom_usuario: Nom_usuario,
            nom_mercado: Nom_mercado
        })
    })
        .then((respuesta) => respuesta.json())
        .then(handle_response)
        .catch((error) => console.log("ERROR", error))
}