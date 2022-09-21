function calcularImc(altura, peso) {   	
    const imc = peso / (altura * altura);
    return imc
}

function tratarClique() {
    const a = parseFloat(document.getElementById("altura").value) / 100;
    const p = parseFloat(document.getElementById("peso").value);

    const imc = calcularImc(a, p)

    if (imc > 25) {
        alert(imc + " Cuidado! Você precisa diminuir seu peso.");
    } else {
        if (imc < 18) {
            alert(imc + " Cuidado! você precisa aumentar seu peso.");
        } else {
            alert(imc + " Parabens você está com o peso ideal");
        }
    }
}

var soma = (a, b) => {
    resultado = a + b
    return resultado
}