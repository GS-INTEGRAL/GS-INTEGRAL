secundariaSelect.addEventListener("change", function () {
    const obraId = obraSelect.value;
    const secundariaId = this.value;

    fetch("/get_estancias", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ obra_id: obraId, obra_secundaria: secundariaId }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            estanciaSelect.innerHTML = '<option value="">Seleccione...</option>';
            data.forEach((option) => {
                estanciaSelect.innerHTML += `<option value="${option[0]}">${option[1]}</option>`;
            });
        })
        .catch((error) => {
            console.error("Error al obtener estancias:", error);
        });
});
