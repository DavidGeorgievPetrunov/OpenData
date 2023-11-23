async function mostrarDatos() {
    const myApiUrl = "https://opendatadavidpetrunov.onrender.com/autobuses";
    var elemento = document.getElementById("ResultadoMostrarDatos");
    var select = document.getElementById("comunidades").value;

    elemento.innerHTML="Calculando"

    const json = {
        comunidad: select,
    }

    console.log("Comunidad Autónoma seleccionada:", select);

    const response = await fetch(myApiUrl+"/aaaa",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(json),
    });

    const data = await response.json();
    console.log(data)

    elemento.innerHTML=JSON.stringify(data);
}

async function compararDatosTotal(){
    const myApiUrl = "https://opendatadavidpetrunov.onrender.com/autobuses";

    var elemento = document.getElementById("ResultadoCompararTotalyPais") 
    var select = document.getElementById("comunidades").value;
    var select2 = document.getElementById("pais").value

    elemento.innerHTML = "Calculando"

    const json = {
        comunidad: select,
        pais: select2,
    }

    console.log("Comunidad Autónoma y pais seleccionados:", select, select2);

    const response = await fetch(myApiUrl+"/bbbb",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(json),
    });

    const data = await response.json();
    console.log(data)
    console.log(elemento);
    elemento.innerHTML = data;

}

async function mostrarArea(){

    const myApiUrl = "https://opendatadavidpetrunov.onrender.com/autobuses";

    var elemento = document.getElementById("ResultadosAreaPais") 
    var select = document.getElementById("comunidades").value;

    elemento.innerHTML = "Calculando"

    console.log(select)

    const json = {
        comunidad: select,
    }

    const response = await fetch(myApiUrl+"/cccc",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(json),
    });

    const data = await response.json();
    console.log(data)
    elemento.innerHTML = JSON.stringify(data);
}

async function mostrarPoblacionE(){
    const myApiUrl = "https://opendatadavidpetrunov.onrender.com/autobuses";
    var elemento = document.getElementById("ResultadosAreaPaisMayor");
    var select = document.getElementById("comunidades").value;

    elemento.innerHTML="Calculando"

    console.log(select)

    const json = {
        comunidad: select,
    }

    console.log("Comunidad Autónoma seleccionada:", select);

    const response = await fetch(myApiUrl+"/dddd",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(json),
    });

    const data = await response.json();
    console.log(data)

    elemento.innerHTML=JSON.stringify(data);
}