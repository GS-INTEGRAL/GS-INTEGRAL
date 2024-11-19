document.addEventListener("DOMContentLoaded", function () {
    const obraSelect = document.getElementById("obra_id");
    const secundariaSelect = document.getElementById("obra_secundaria");
    const estanciaSelect = document.getElementById("estancia_id");

    obraSelect.addEventListener("change", function () {
        const obraId = this.value;

        // Actualizar obra secundaria
        if (obraId === "maristas") {
            secundariaSelect.innerHTML = `
                <option value="fuensanta">Fuensanta</option>
                <option value="merced">Merced</option>`;
            secundariaSelect.disabled = false;
        } else {
            secundariaSelect.innerHTML = '<option value="">Seleccione...</option>';
            secundariaSelect.disabled = true;
            estanciaSelect.innerHTML = '<option value="">Seleccione...</option>';
        }
    });

    secundariaSelect.addEventListener("change", function () {
        const obraId = obraSelect.value;
        const secundariaId = this.value;

        // Llamar a backend para actualizar estancias
        fetch("/get_estancias", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ obra_id: obraId, obra_secundaria: secundariaId }),
        })
            .then((response) => response.json())
            .then((data) => {
                estanciaSelect.innerHTML = '<option value="">Seleccione...</option>';
                data.forEach((option) => {
                    estanciaSelect.innerHTML += `<option value="${option[0]}">${option[1]}</option>`;
                });
            });
    });
});
