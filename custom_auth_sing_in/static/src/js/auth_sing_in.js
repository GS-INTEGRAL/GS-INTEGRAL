document.addEventListener('DOMContentLoaded', function() {
    var obraId = document.getElementById('obra_id');
    var obraSecundaria = document.getElementById('obra_secundaria');
    var estanciaId = document.getElementById('estancia_id');

    function toggleObraSecundaria() {
        if (obraId.value === 'maristas') {
            obraSecundaria.parentElement.style.display = 'block';
        } else {
            obraSecundaria.parentElement.style.display = 'none';
            estanciaId.parentElement.style.display = 'none';
            obraSecundaria.value = '';
            estanciaId.value = '';
        }
    }

    function toggleEstanciaId() {
        if (obraSecundaria.value) {
            estanciaId.parentElement.style.display = 'block';
        } else {
            estanciaId.parentElement.style.display = 'none';
            estanciaId.value = '';
        }
    }

    obraId.addEventListener('change', toggleObraSecundaria);
    obraSecundaria.addEventListener('change', toggleEstanciaId);

    // Inicializar el estado de los campos
    toggleObraSecundaria();
    toggleEstanciaId();
});
